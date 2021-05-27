#include "TFile.h"
#include "TH1.h"
#include "TMath.h"
#include "TLorentzVector.h"

#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "TPRegexp.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
#include "Geometry/CommonDetUnit/interface/GluedGeomDet.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "DataFormats/TrackerRecHit2D/interface/BaseTrackerRecHit.h"
#include "DataFormats/TrackerRecHit2D/interface/OmniClusterRef.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2D.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "RecoLocalTracker/SiStripClusterizer/interface/SiStripClusterInfo.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "tracking_resolution/interface/BrenoTrackingResolution.h"
// -----------------------------
// constructors and destructor
// -----------------------------
BrenoTrackingResolution::BrenoTrackingResolution(const edm::ParameterSet& ps):
  parameters_(ps),
  moduleName_(parameters_.getUntrackedParameter<std::string>("moduleName", "BrenoTrackingResolution")),
  folderName_(parameters_.getUntrackedParameter<std::string>("folderName", "TrackRefitting")),
  hitsRemain(parameters_.getUntrackedParameter<std::string>("hitsRemainInput", "3")),
  minTracksEta(parameters_.getUntrackedParameter<double>("minTracksEtaInput", 0.0)),
  maxTracksEta(parameters_.getUntrackedParameter<double>("maxTracksEtaInput", 2.2)),
  minTracksPt(parameters_.getUntrackedParameter<double>("minTracksPtInput", 15.0)),
  maxTracksPt(parameters_.getUntrackedParameter<double>("maxTracksPtInput", 99999.9)),
  lowPtRegion(parameters_.getUntrackedParameter<double>("lowPtRegionInput", 15.0)),
  medPtRegion(parameters_.getUntrackedParameter<double>("medPtRegionInput", 30.0)),
  higPtRegion(parameters_.getUntrackedParameter<double>("higPtRegionInput", 100.0)),
  muonsTag(parameters_.getUntrackedParameter<edm::InputTag>("muonsInputTag", edm::InputTag("muons", "", "RECO"))),
  pfcandsTag(parameters_.getUntrackedParameter<edm::InputTag>("pfcandsInputTag", edm::InputTag("particleFlow", "", "RECO"))),
  tracksTag(parameters_.getUntrackedParameter<edm::InputTag>("tracksInputTag", edm::InputTag("rCluster4", "", "HITREMOVER"))),
  tracksRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("tracksRerecoInputTag", edm::InputTag("generalTracks", "", "reRECO"))),
  muonsToken(consumes<std::vector<reco::Muon>>(muonsTag)),
  pfcandsToken(consumes<std::vector<reco::PFCandidate>>(pfcandsTag)),
  tracksToken(consumes<std::vector<reco::Track>>(tracksTag)),
  tracksRerecoToken(consumes<std::vector<reco::Track>>(tracksRerecoTag))
{

  trackPtAllPt_ = nullptr;
  trackPtLowPt_ = nullptr;
  trackPtMedPt_ = nullptr;
  trackPtHigPt_ = nullptr;

  trackChi2ndofAllPt_ = nullptr;
  trackChi2ndofLowPt_ = nullptr;
  trackChi2ndofMedPt_ = nullptr;
  trackChi2ndofHigPt_ = nullptr;

  trackDzAllPt_ = nullptr;
  trackDzLowPt_ = nullptr;
  trackDzMedPt_ = nullptr;
  trackDzHigPt_ = nullptr;

  trackDxyAllPt_ = nullptr;
  trackDxyLowPt_ = nullptr;
  trackDxyMedPt_ = nullptr;
  trackDxyHigPt_ = nullptr;

}

void BrenoTrackingResolution::bookHistograms(DQMStore::IBooker &iBook, edm::Run const& iRun, edm::EventSetup const& iSetup) {

  std::string currentFolder = folderName_+"/" ;
  iBook.setCurrentFolder(currentFolder);

  trackPixelLayers_ = iBook.book1D("trackPixelLayers"+hitsRemain+"l", "Pixel layers with measurement - "+hitsRemain+" layers",11,-0.5,10.5);
  trackTrackerLayers_ = iBook.book1D("trackTrackerLayers"+hitsRemain+"l", "Tracker layers with measurement - "+hitsRemain+" layers",11,-0.5,10.5);

  trackPtAllPt_ = iBook.book1D("trackPt"+hitsRemain+"lAllPt", "Track p_{T} - "+hitsRemain+" layers",40,0.0,2.0);
  trackPtLowPt_ = iBook.book1D("trackPt"+hitsRemain+"lLowPt", "Track p_{T} - "+hitsRemain+" layers",40,0.0,2.0);
  trackPtMedPt_ = iBook.book1D("trackPt"+hitsRemain+"lMedPt", "Track p_{T} - "+hitsRemain+" layers",40,0.0,2.0);
  trackPtHigPt_ = iBook.book1D("trackPt"+hitsRemain+"lHigPt", "Track p_{T} - "+hitsRemain+" layers",40,0.0,2.0);

  trackChi2ndofAllPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lAllPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofLowPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lLowPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofMedPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lMedPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofHigPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lHigPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);

//  trackDzAllPt_ = iBook.book1D("trackDz"+hitsRemain+"lAllPt", "Track d_{z} - "+hitsRemain+" layers",40,-10.0,10.0);
//  trackDzLowPt_ = iBook.book1D("trackDz"+hitsRemain+"lLowPt", "Track d_{z} - "+hitsRemain+" layers",40,-10.0,10.0);
//  trackDzMedPt_ = iBook.book1D("trackDz"+hitsRemain+"lMedPt", "Track d_{z} - "+hitsRemain+" layers",40,-10.0,10.0);
//  trackDzHigPt_ = iBook.book1D("trackDz"+hitsRemain+"lHigPt", "Track d_{z} - "+hitsRemain+" layers",40,-10.0,10.0);

  muontrackDxyAllPt_ = iBook.book1D("muontrackDxy"+hitsRemain+"lAllPt", "Track d_{xy} - "+hitsRemain+" layers",100,-0.1,0.1);

//  trackDxyAllPt_ = iBook.book1D("trackDxy"+hitsRemain+"lAllPt", "Track d_{xy} - "+hitsRemain+" layers",100,-0.1,0.1);
//  trackDxyLowPt_ = iBook.book1D("trackDxy"+hitsRemain+"lLowPt", "Track d_{xy} - "+hitsRemain+" layers",100,-0.1,0.1);
//  trackDxyMedPt_ = iBook.book1D("trackDxy"+hitsRemain+"lMedPt", "Track d_{xy} - "+hitsRemain+" layers",100,-0.1,0.1);
//  trackDxyHigPt_ = iBook.book1D("trackDxy"+hitsRemain+"lHigPt", "Track d_{xy} - "+hitsRemain+" layers",100,-0.1,0.1);

  trackDzAllPt_ = iBook.book1D("trackDz"+hitsRemain+"lAllPt", "Track d_{z} - "+hitsRemain+" layers",40,0.0,2.0);
  trackDzLowPt_ = iBook.book1D("trackDz"+hitsRemain+"lLowPt", "Track d_{z} - "+hitsRemain+" layers",40,0.0,2.0);
  trackDzMedPt_ = iBook.book1D("trackDz"+hitsRemain+"lMedPt", "Track d_{z} - "+hitsRemain+" layers",40,0.0,2.0);
  trackDzHigPt_ = iBook.book1D("trackDz"+hitsRemain+"lHigPt", "Track d_{z} - "+hitsRemain+" layers",40,0.0,2.0);

  trackDxyAllPt_ = iBook.book1D("trackDxy"+hitsRemain+"lAllPt", "Track d_{xy} - "+hitsRemain+" layers",40,0.0,2.0);
  trackDxyLowPt_ = iBook.book1D("trackDxy"+hitsRemain+"lLowPt", "Track d_{xy} - "+hitsRemain+" layers",40,0.0,2.0);
  trackDxyMedPt_ = iBook.book1D("trackDxy"+hitsRemain+"lMedPt", "Track d_{xy} - "+hitsRemain+" layers",40,0.0,2.0);
  trackDxyHigPt_ = iBook.book1D("trackDxy"+hitsRemain+"lHigPt", "Track d_{xy} - "+hitsRemain+" layers",40,0.0,2.0);

}
void BrenoTrackingResolution::analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) {

  edm::Handle< std::vector<reco::Muon> > muons;
  edm::Handle< std::vector<reco::PFCandidate> > pfcands;
  edm::Handle< std::vector<reco::Track> > tracks;
  edm::Handle< std::vector<reco::Track> > tracks_rereco;

  iEvent.getByToken(muonsToken, muons);
  iEvent.getByToken(pfcandsToken, pfcands);
  iEvent.getByToken(tracksToken, tracks);
  iEvent.getByToken(tracksRerecoToken, tracks_rereco);

  for (std::vector<reco::Muon>::const_iterator muon = muons->begin(); muon != muons->end(); ++muon) {

    TLorentzVector mvec;
    mvec.SetPtEtaPhiM(muon->pt(),muon->eta(),muon->phi(),muon->mass());

    double summed_pt = 0.0;
    for (std::vector<reco::PFCandidate>::const_iterator pfcand = pfcands->begin(); pfcand != pfcands->end(); ++pfcand) {
      TLorentzVector pfvec;
      pfvec.SetPtEtaPhiM(pfcand->pt(), pfcand->eta(), pfcand->phi(), pfcand->mass());
      if(pfvec.DeltaR(mvec)>0.02 and pfvec.DeltaR(mvec)<0.3){
        summed_pt += pfcand->pt();
      }
    }
    if(summed_pt/muon->pt()>0.2) continue;

    for (std::vector<reco::Track>::const_iterator track = tracks->begin(); track != tracks->end(); ++track) {

      TLorentzVector tvec;
      tvec.SetPtEtaPhiM(track->pt(),track->eta(),track->phi(),0.0);
      if(tvec.DeltaR(mvec)<0.01){

        if(track->hitPattern().trackerLayersWithMeasurement() > 10){

//          if(abs(track->dxy()) < 0.2){

//            if(abs(track->dz()) < 0.1){

              if(abs(track->eta())>maxTracksEta or track->pt()<minTracksPt) break;

              for (std::vector<reco::Track>::const_iterator track_rereco = tracks_rereco->begin(); track_rereco != tracks_rereco->end(); ++track_rereco) {

                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(track_rereco->pt(),track_rereco->eta(),track_rereco->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                if(deltaR < 0.01){

                  if(track_rereco->pt()>=minTracksPt && track_rereco->pt()<=maxTracksPt && abs(track_rereco->eta())>=minTracksEta && abs(track_rereco->eta())<=maxTracksEta){

                    int track_trackerLayersWithMeasurement = track_rereco->hitPattern().trackerLayersWithMeasurement();
                    int track_pixelLayersWithMeasurement = track_rereco->hitPattern().pixelLayersWithMeasurement();

                    trackPixelLayers_->Fill(track_pixelLayersWithMeasurement);
                    trackTrackerLayers_->Fill(track_trackerLayersWithMeasurement);

                    trackPtAllPt_->Fill(1.0*track_rereco->pt()/track->pt());
//                    trackDzAllPt_->Fill(track_rereco->dz());
//                    trackDxyAllPt_->Fill(track_rereco->dxy());
//                    muontrackDxyAllPt_->Fill(track->dxy());
                    trackDzAllPt_->Fill(1.0*track_rereco->dz()/track->dz());
                    trackDxyAllPt_->Fill(1.0*track_rereco->dxy()/track->dxy());

                    if(track->pt()>=lowPtRegion && track->pt()<medPtRegion){

                      trackPtLowPt_->Fill(1.0*track_rereco->pt()/track->pt());
//                      trackDzLowPt_->Fill(track_rereco->dz());
//                      trackDxyLowPt_->Fill(track_rereco->dxy());
                      trackDzLowPt_->Fill(1.0*track_rereco->dz()/track->dz());
                      trackDxyLowPt_->Fill(1.0*track_rereco->dxy()/track->dxy());

                    }

                    if(track->pt()>=medPtRegion && track->pt()<higPtRegion){

                      trackPtMedPt_->Fill(1.0*track_rereco->pt()/track->pt());
//                      trackDzMedPt_->Fill(track_rereco->dz());
//                      trackDxyMedPt_->Fill(track_rereco->dxy());
                      trackDzMedPt_->Fill(1.0*track_rereco->dz()/track->dz());
                      trackDxyMedPt_->Fill(1.0*track_rereco->dxy()/track->dxy());

                    }

                    if(track->pt()>=higPtRegion){

                      trackPtHigPt_->Fill(1.0*track_rereco->pt()/track->pt());
//                      trackDzHigPt_->Fill(track_rereco->dz());
//                      trackDxyHigPt_->Fill(track_rereco->dxy());
                      trackDzHigPt_->Fill(1.0*track_rereco->dz()/track->dz());
                      trackDxyHigPt_->Fill(1.0*track_rereco->dxy()/track->dxy());

                    }

                    double track_chi2perNdof = 0.0;

                    if(track_rereco->ndof()>0) track_chi2perNdof = 1.0*track_rereco->chi2()/track_rereco->ndof();

                    trackChi2ndofAllPt_->Fill(track_chi2perNdof);

                    if(track->pt()>=lowPtRegion && track->pt()<medPtRegion){

                      trackChi2ndofLowPt_->Fill(track_chi2perNdof);

                    }

                    if(track->pt()>=medPtRegion && track->pt()<higPtRegion){

                      trackChi2ndofMedPt_->Fill(track_chi2perNdof);

                    }

                    if(track->pt()>=higPtRegion){

                      trackChi2ndofHigPt_->Fill(track_chi2perNdof);

                    }
                    
                  }

                }

              }

//            }

//          }

        }

      }

    }

  }

}
void BrenoTrackingResolution::endLuminosityBlock(edm::LuminosityBlock const& lumiBlock, edm::EventSetup const& eSetup){}
// Define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(BrenoTrackingResolution);
