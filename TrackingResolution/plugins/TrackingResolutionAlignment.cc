#include "TFile.h"
#include "TH1.h"
#include "TMath.h"
#include "TLorentzVector.h"

#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <vector>

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
#include "TrackingResolution/TrackingResolution/interface/TrackingResolutionAlignment.h"
// -----------------------------
// constructors and destructor
// -----------------------------
TrackingResolutionAlignment::TrackingResolutionAlignment(const edm::ParameterSet& ps):
  parameters_(ps),
  moduleName_(parameters_.getUntrackedParameter<std::string>("moduleName", "TrackingResolutionAlignment")),
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
  tracksTag(parameters_.getUntrackedParameter<edm::InputTag>("tracksInputTag", edm::InputTag("generalTracks", "", "RECO"))),
  primVertexTag(parameters_.getUntrackedParameter<edm::InputTag>("primVertexInputTag", edm::InputTag("offlinePrimaryVertices", "", "RECO"))),
  tracksRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("tracksRerecoInputTag", edm::InputTag("HitFilteredTracks", "", "DQM"))),
  tracksToken(consumes<std::vector<reco::Track>>(tracksTag)),
  primVertexToken(consumes<std::vector<reco::Vertex>>(primVertexTag)),
  tracksRerecoToken(consumes<std::vector<reco::Track>>(tracksRerecoTag))
{

  trackPtAllPt_ = nullptr;
  trackChi2ndofAllPt_ = nullptr;

  trackPixelLayers_ = nullptr;
  trackTrackerLayers_ = nullptr;

  trackEfficiencyCalc_ = nullptr;

}

void TrackingResolutionAlignment::bookHistograms(DQMStore::IBooker &iBook, edm::Run const& iRun, edm::EventSetup const& iSetup) {

  std::string currentFolder = folderName_+"/" ;
  iBook.setCurrentFolder(currentFolder);

  trackPixelLayers_ = iBook.book1D("trackPixelLayers"+hitsRemain+"l", "Pixel layers with measurement - "+hitsRemain+" layers",11,-0.5,10.5);
  trackTrackerLayers_ = iBook.book1D("trackTrackerLayers"+hitsRemain+"l", "Tracker layers with measurement - "+hitsRemain+" layers",11,-0.5,10.5);

  trackPtAllPt_ = iBook.book1D("trackPt"+hitsRemain+"lAllPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);
  trackChi2ndofAllPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lAllPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);

  trackEfficiencyCalc_ = iBook.book1D("trackEfficiencyCalc"+hitsRemain+"l", "Number of shortened matched and full tracks - "+hitsRemain+" layers",3,-0.5,2.5);

}
void TrackingResolutionAlignment::analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) {

  //std::cout << "Started the analyzer" << std::endl;

  edm::Handle< std::vector<reco::Track> > tracks;
  edm::Handle< std::vector<reco::Vertex> > vertices;
  edm::Handle< std::vector<reco::Track> > tracks_rereco;

  iEvent.getByToken(tracksToken, tracks);
  iEvent.getByToken(primVertexToken, vertices);
  iEvent.getByToken(tracksRerecoToken, tracks_rereco);

  const reco::Vertex vertex = vertices->at(0);

  //int hitsRemain_int = stoi(hitsRemain);
  int numTracks = 0;
  int numRerecoTracks = 0;
  int numRerecoMatchedTracks = 0;

  for (std::vector<reco::Track>::const_iterator track = tracks->begin(); track != tracks->end(); ++track) {

    //std::cout << "Started loop on generalTracks" << std::endl;

    reco::HitPattern hp = track->hitPattern();
    if(int(int(hp.numberOfValidHits()) - int(hp.numberOfAllHits(reco::HitPattern::TRACK_HITS))) != 0) {break;}

    Double_t dxy = (track->dxy(vertex.position()));
    Double_t dz = (track->dz(vertex.position()));
    TLorentzVector tvec;
    tvec.SetPtEtaPhiM(track->pt(),track->eta(),track->phi(),0.0);

    if(hp.trackerLayersWithMeasurement() > minNumberOfLayers){

      //std::cout << "Tracks with more trackerLayersWithMeasurement than minNumberOfLayers" << std::endl;

      if(abs(dxy) < maxDxy){

        //std::cout << "Tracks with dxy smaller than maxDxy" << std::endl;

        if(abs(dz) < maxDz){

          //std::cout << "Tracks with dz smaller than maxDz" << std::endl;

          if(abs(track->eta())>maxTracksEta or track->pt()<minTracksPt) break;

          //std::cout << "Tracks inside eta region and with pt higher than minDz" << std::endl;

          ++numTracks;

          for (std::vector<reco::Track>::const_iterator track_rereco = tracks_rereco->begin(); track_rereco != tracks_rereco->end(); ++track_rereco) {

            ++numRerecoTracks;

            //std::cout << "Started loop on reRECO tracks" << std::endl;

            TLorentzVector trerecovec;
            trerecovec.SetPtEtaPhiM(track_rereco->pt(),track_rereco->eta(),track_rereco->phi(),0.0);
            double deltaR = tvec.DeltaR(trerecovec);
            if(deltaR < maxDr){

              ++numRerecoMatchedTracks;

              if(track_rereco->pt()>=minTracksPt && track_rereco->pt()<=maxTracksPt && abs(track_rereco->eta())>=minTracksEta && abs(track_rereco->eta())<=maxTracksEta){

                int track_trackerLayersWithMeasurement = track_rereco->hitPattern().trackerLayersWithMeasurement();
                int track_pixelLayersWithMeasurement = track_rereco->hitPattern().pixelLayersWithMeasurement();

                trackPixelLayers_->Fill(track_pixelLayersWithMeasurement);
                trackTrackerLayers_->Fill(track_trackerLayersWithMeasurement);

                trackPtAllPt_->Fill(1.0*track_rereco->pt()/track->pt());

                double track_chi2perNdof = 0.0;

                if(track_rereco->ndof()>0) track_chi2perNdof = 1.0*track_rereco->chi2()/track_rereco->ndof();

                trackChi2ndofAllPt_->Fill(track_chi2perNdof);

              }

            }

          }

          if(numRerecoTracks > 0) trackEfficiencyCalc_->Fill(1.0);
          if(numRerecoMatchedTracks > 0) trackEfficiencyCalc_->Fill(2.0);

        }

      }

    }

  }

  if(numTracks > 0) trackEfficiencyCalc_->Fill(0.0);

  //std::cout << "##################### END OF EVENT #####################" << std::endl;

}
// Define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackingResolutionAlignment);
