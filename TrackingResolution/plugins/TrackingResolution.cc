#include "TFile.h"
#include "TH1.h"
#include "TMath.h"
#include "TLorentzVector.h"

#include <iostream>
#include <string>

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
#include "TrackingResolution/TrackingResolution/interface/TrackingResolution.h"
// -----------------------------
// constructors and destructor
// -----------------------------
TrackingResolution::TrackingResolution(const edm::ParameterSet& ps):
  parameters_(ps),
  moduleName_(parameters_.getUntrackedParameter<std::string>("moduleName", "TrackingResolution")),
  folderName_(parameters_.getUntrackedParameter<std::string>("folderName", "TrackRefitting")),
  hitsRemain(parameters_.getUntrackedParameter<std::string>("hitsRemainInput", "3")),
  minTracksEta(parameters_.getUntrackedParameter<double>("minTracksEtaInput", 0.0)),
  maxTracksEta(parameters_.getUntrackedParameter<double>("maxTracksEtaInput", 2.2)),
  minTracksPt(parameters_.getUntrackedParameter<double>("minTracksPtInput", 15.0)),
  maxTracksPt(parameters_.getUntrackedParameter<double>("maxTracksPtInput", 99999.9)),
  lowPtRegion(parameters_.getUntrackedParameter<double>("lowPtRegionInput", 15.0)),
  medPtRegion(parameters_.getUntrackedParameter<double>("medPtRegionInput", 30.0)),
  higPtRegion(parameters_.getUntrackedParameter<double>("higPtRegionInput", 100.0)),
  maxDxy(parameters_.getUntrackedParameter<double>("maxDxyInput", 0.2)),
  maxDz(parameters_.getUntrackedParameter<double>("maxDzInput", 0.1)),
  maxDr(parameters_.getUntrackedParameter<double>("maxDrInput", 0.01)),
  minNumberOfLayers(parameters_.getUntrackedParameter<int>("minNumberOfLayersInput", 10)),
  muonsTag(parameters_.getUntrackedParameter<edm::InputTag>("muonsInputTag", edm::InputTag("muons", "", "RECO"))),
  tracksTag(parameters_.getUntrackedParameter<edm::InputTag>("tracksInputTag", edm::InputTag("rCluster4", "", "HITREMOVER"))),
  primVertexTag(parameters_.getUntrackedParameter<edm::InputTag>("primVertexInputTag", edm::InputTag("offlinePrimaryVertices", "", "RECO"))),
  tracksRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("tracksRerecoInputTag", edm::InputTag("generalTracks", "", "reRECO"))),
  muonsToken(consumes<std::vector<reco::Muon>>(muonsTag)),
  tracksToken(consumes<std::vector<reco::Track>>(tracksTag)),
  primVertexToken(consumes<std::vector<reco::Vertex>>(primVertexTag)),
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

}

void TrackingResolution::bookHistograms(DQMStore::IBooker &iBook, edm::Run const& iRun, edm::EventSetup const& iSetup) {

  std::string currentFolder = folderName_+"/" ;
  iBook.setCurrentFolder(currentFolder);

  trackPixelLayers_ = iBook.book1D("trackPixelLayers"+hitsRemain+"l", "Pixel layers with measurement - "+hitsRemain+" layers",11,-0.5,10.5);
  trackTrackerLayers_ = iBook.book1D("trackTrackerLayers"+hitsRemain+"l", "Tracker layers with measurement - "+hitsRemain+" layers",11,-0.5,10.5);

  trackPtAllPt_ = iBook.book1D("trackPt"+hitsRemain+"lAllPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);
  trackPtLowPt_ = iBook.book1D("trackPt"+hitsRemain+"lLowPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);
  trackPtMedPt_ = iBook.book1D("trackPt"+hitsRemain+"lMedPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);
  trackPtHigPt_ = iBook.book1D("trackPt"+hitsRemain+"lHigPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);

  trackChi2ndofAllPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lAllPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofLowPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lLowPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofMedPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lMedPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofHigPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lHigPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);

  trackEfficiencyCalc_ = iBook.book1D("trackEfficiencyCalc"+hitsRemain+"l", "Number of shortened matched and full tracks - "+hitsRemain+" layers",4,-0.5,3.5);

}
void TrackingResolution::analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) {

  edm::Handle< std::vector<reco::Muon> > muons;
  edm::Handle< std::vector<reco::Track> > tracks;
  edm::Handle< std::vector<reco::Vertex> > vertices; 
  edm::Handle< std::vector<reco::Track> > tracks_rereco;

  iEvent.getByToken(muonsToken, muons);
  iEvent.getByToken(tracksToken, tracks);
  iEvent.getByToken(primVertexToken, vertices);
  iEvent.getByToken(tracksRerecoToken, tracks_rereco);

  const reco::Vertex vertex = vertices->at(0);

  for (std::vector<reco::Track>::const_iterator track = tracks->begin(); track != tracks->end(); ++track) {
    trackEfficiencyCalc_->Fill(0.0);
  }

  for (std::vector<reco::Muon>::const_iterator muon = muons->begin(); muon != muons->end(); ++muon) {

    TLorentzVector mvec;
    mvec.SetPtEtaPhiM(muon->pt(),muon->eta(),muon->phi(),muon->mass());

    for (std::vector<reco::Track>::const_iterator track = tracks->begin(); track != tracks->end(); ++track) {

      Double_t dxy = (track->dxy(vertex.position()));
      Double_t dz = (track->dz(vertex.position()));
      TLorentzVector tvec;
      tvec.SetPtEtaPhiM(track->pt(),track->eta(),track->phi(),0.0);
      if(tvec.DeltaR(mvec)<maxDr){

        if(track->hitPattern().trackerLayersWithMeasurement() > minNumberOfLayers){

          if(abs(dxy) < maxDxy){

            if(abs(dz) < maxDz){

              if(abs(track->eta())>maxTracksEta or track->pt()<minTracksPt) break;

              for (std::vector<reco::Track>::const_iterator track_rereco = tracks_rereco->begin(); track_rereco != tracks_rereco->end(); ++track_rereco) {

                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(track_rereco->pt(),track_rereco->eta(),track_rereco->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                if(deltaR < maxDr){

                  if(track_rereco->pt()>=minTracksPt && track_rereco->pt()<=maxTracksPt && abs(track_rereco->eta())>=minTracksEta && abs(track_rereco->eta())<=maxTracksEta){

                    int track_trackerLayersWithMeasurement = track_rereco->hitPattern().trackerLayersWithMeasurement();
                    int track_pixelLayersWithMeasurement = track_rereco->hitPattern().pixelLayersWithMeasurement();

                    trackPixelLayers_->Fill(track_pixelLayersWithMeasurement);
                    trackTrackerLayers_->Fill(track_trackerLayersWithMeasurement);

                    trackEfficiencyCalc_->Fill(3.0);

                    trackPtAllPt_->Fill(1.0*track_rereco->pt()/track->pt());

                    if(track->pt()>=lowPtRegion && track->pt()<medPtRegion){

                      trackPtLowPt_->Fill(1.0*track_rereco->pt()/track->pt());

                    }

                    if(track->pt()>=medPtRegion && track->pt()<higPtRegion){

                      trackPtMedPt_->Fill(1.0*track_rereco->pt()/track->pt());

                    }

                    if(track->pt()>=higPtRegion){

                      trackPtHigPt_->Fill(1.0*track_rereco->pt()/track->pt());

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

            }

          }

        }

      }

    }

  }

}
//void TrackingResolution::endLuminosityBlock(edm::LuminosityBlock const& lumiBlock, edm::EventSetup const& eSetup){}
// Define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackingResolution);
