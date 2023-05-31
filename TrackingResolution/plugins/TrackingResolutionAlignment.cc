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
TrackingResolutionAlignment::TrackingResolutionAlignment(const edm::ParameterSet &ps) : parameters_(ps),
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
                                                                                        tracksTag(parameters_.getUntrackedParameter<edm::InputTag>("tracksInputTag", edm::InputTag("generalTracks", "", "DQM"))),
                                                                                        primVertexTag(parameters_.getUntrackedParameter<edm::InputTag>("primVertexInputTag", edm::InputTag("offlinePrimaryVertices", "", "DQM"))),
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

void TrackingResolutionAlignment::bookHistograms(DQMStore::IBooker &iBook, edm::Run const &iRun, edm::EventSetup const &iSetup)
{

  std::string currentFolder = folderName_ + "/";
  iBook.setCurrentFolder(currentFolder);

  trackPixelLayers_ = iBook.book1D("trackPixelLayers" + hitsRemain + "l", "Pixel layers with measurement - " + hitsRemain + " layers", 11, -0.5, 10.5);
  trackTrackerLayers_ = iBook.book1D("trackTrackerLayers" + hitsRemain + "l", "Tracker layers with measurement - " + hitsRemain + " layers", 11, -0.5, 10.5);

  trackPtAllPt_ = iBook.book1D("trackPt" + hitsRemain + "lAllPt", "Track p_{T} - " + hitsRemain + " layers", 41, 0.0, 2.0);
  trackChi2ndofAllPt_ = iBook.book1D("trackChi2ndof" + hitsRemain + "lAllPt", "Chi^{2} / ndof - " + hitsRemain + " layers", 40, 0.0, 2.0);

  trackEfficiencyCalc_ = iBook.book1D("trackEfficiencyCalc" + hitsRemain + "l", "Number of shortened matched and full tracks - " + hitsRemain + " layers", 3, -0.5, 2.5);
}
void TrackingResolutionAlignment::analyze(edm::Event const &iEvent, edm::EventSetup const &iSetup)
{

  // std::cout << "Started the analyzer" << std::endl;

  edm::Handle<std::vector<reco::Track>> tracks;
  edm::Handle<std::vector<reco::Vertex>> vertices;
  edm::Handle<std::vector<reco::Track>> tracks_rereco;

  iEvent.getByToken(tracksToken, tracks);
  iEvent.getByToken(primVertexToken, vertices);
  iEvent.getByToken(tracksRerecoToken, tracks_rereco);

  const reco::Vertex vertex = vertices->at(0);

  int hitsRemain_int = stoi(hitsRemain);
  int numTracks = 0;
  int numRerecoTracks = 0;
  int numRerecoMatchedTracks = 0;

  for (std::vector<reco::Track>::const_iterator track = tracks->begin(); track != tracks->end(); ++track)
  {

    // std::cout << "Started loop on generalTracks" << std::endl;

    reco::HitPattern hp = track->hitPattern();
    if (int(int(hp.numberOfValidHits()) - int(hp.numberOfAllHits(reco::HitPattern::TRACK_HITS))) != 0)
    {
      break;
    }

    Double_t dxy = (track->dxy(vertex.position()));
    Double_t dz = (track->dz(vertex.position()));
    TLorentzVector tvec;
    tvec.SetPtEtaPhiM(track->pt(), track->eta(), track->phi(), 0.0);

    if (hp.trackerLayersWithMeasurement() > minNumberOfLayers)
    {

      // std::cout << "Tracks with more trackerLayersWithMeasurement than minNumberOfLayers" << std::endl;

      if (abs(dxy) < maxDxy)
      {

        // std::cout << "Tracks with dxy smaller than maxDxy" << std::endl;

        if (abs(dz) < maxDz)
        {

          // std::cout << "Tracks with dz smaller than maxDz" << std::endl;

          if (abs(track->eta()) > maxTracksEta or track->pt() < minTracksPt)
            break;

          // std::cout << "Tracks inside eta region and with pt higher than minDz" << std::endl;

          ++numTracks;

          for (std::vector<reco::Track>::const_iterator track_rereco = tracks_rereco->begin(); track_rereco != tracks_rereco->end(); ++track_rereco)
          {

            ++numRerecoTracks;

            // std::cout << "Started loop on reRECO tracks" << std::endl;

            TLorentzVector trerecovec;
            trerecovec.SetPtEtaPhiM(track_rereco->pt(), track_rereco->eta(), track_rereco->phi(), 0.0);
            double deltaR = tvec.DeltaR(trerecovec);
            if (deltaR < maxDr)
            {

              ++numRerecoMatchedTracks;

              if (track_rereco->pt() >= minTracksPt && track_rereco->pt() <= maxTracksPt && abs(track_rereco->eta()) >= minTracksEta && abs(track_rereco->eta()) <= maxTracksEta)
              {

                int track_trackerLayersWithMeasurement = track_rereco->hitPattern().trackerLayersWithMeasurement();
                int track_pixelLayersWithMeasurement = track_rereco->hitPattern().pixelLayersWithMeasurement();

                if (track_trackerLayersWithMeasurement < 8 * hitsRemain_int)
                {
                  // std::cout << iEvent.id() << std::endl;
                  // std::cout << "Tracker layers of short track: " << track_trackerLayersWithMeasurement << std::endl;
                  // std::cout << "pT resolution: " << 1.0 * track_rereco->pt() / track->pt() << std::endl;
                  // std::cout << "pT of short track: " << 1.0 * track_rereco->pt() << std::endl;
                  // std::cout << "eta of short track: " << 1.0 * track_rereco->eta() << std::endl;
                  // std::cout << "phi of short track: " << 1.0 * track_rereco->phi() << std::endl;
                  // std::cout << "chi2/ndof: " << 1.0 * track_rereco->chi2() / track_rereco->ndof() << std::endl;
                  reco::HitPattern hitpattern = track_rereco->hitPattern();
                  reco::HitPattern selTrack_hitpattern = track->hitPattern();
                  try
                  {

                    auto hb = track_rereco->recHitsBegin();
                    auto sel_hb = track->recHitsBegin();

                    uint32_t thisLayer;
                    uint32_t prevLayer;
                    uint32_t thisSubStruct;
                    uint32_t prevSubStruct;
                    int pxbLayers = 0;
                    int pxfLayers = 0;
                    int tibLayers = 0;
                    int tidLayers = 0;
                    int tobLayers = 0;
                    int tecLayers = 0;

                    uint32_t sel_thisLayer;
                    uint32_t sel_prevLayer;
                    uint32_t sel_thisSubStruct;
                    uint32_t sel_prevSubStruct;
                    int sel_pxbLayers = 0;
                    int sel_pxfLayers = 0;
                    int sel_tibLayers = 0;
                    int sel_tidLayers = 0;
                    int sel_tobLayers = 0;
                    int sel_tecLayers = 0;

                    for (unsigned int h = 0; h < track_rereco->recHitsSize(); h++)
                    {

                      uint32_t pHit = hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, h);
                      uint32_t nHit = hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, h - 1);
                      auto recHit = *(hb + h);
                      auto const &hit = *recHit;

                      // define a sequence of hit layers:
                      thisLayer = hitpattern.getLayer(pHit);
                      prevLayer = hitpattern.getLayer(nHit);
                      thisSubStruct = hitpattern.getSubStructure(pHit);
                      prevSubStruct = hitpattern.getSubStructure(nHit);
                      // the condition !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct)) prevents two hits falling into the same layer and sub-structure
                      // but allows for hits being in the same layers, e. g., layer 1 of PXB and layer 1 of PXF, in the case of high |eta| tracks
                      if (!hit.isValid())
                      {
                        // std::cout << "hit.isValid() is false" << std::endl;
                        continue;
                      }

                      if (!(hitpattern.validHitFilter(pHit)))
                      {
                        // std::cout << "hitpattern.validHitFilter(pHit) is false" << std::endl;
                        continue;
                      }
                      if (hitpattern.getSubStructure(pHit) == 1 && !((thisLayer == prevLayer) && (thisSubStruct == prevSubStruct)))
                      {
                        pxbLayers++;
                      }
                      if (hitpattern.getSubStructure(pHit) == 2 && !((thisLayer == prevLayer) && (thisSubStruct == prevSubStruct)))
                      {
                        pxfLayers++;
                      }
                      if (hitpattern.getSubStructure(pHit) == 3 && !((thisLayer == prevLayer) && (thisSubStruct == prevSubStruct)))
                      {
                        tibLayers++;
                      }
                      if (hitpattern.getSubStructure(pHit) == 4 && !((thisLayer == prevLayer) && (thisSubStruct == prevSubStruct)))
                      {
                        tidLayers++;
                      }
                      if (hitpattern.getSubStructure(pHit) == 5 && !((thisLayer == prevLayer) && (thisSubStruct == prevSubStruct)))
                      {
                        tobLayers++;
                      }
                      if (hitpattern.getSubStructure(pHit) == 6 && !((thisLayer == prevLayer) && (thisSubStruct == prevSubStruct)))
                      {
                        tecLayers++;
                      }

                      // std::cout << "Short track: " << pxbLayers << " " << pxfLayers << " " << tibLayers << " " << tidLayers << " " << tobLayers << " " << tecLayers << " -- " << pxbLayers + pxfLayers + tibLayers + tidLayers + tobLayers + tecLayers << std::endl;
                    }

                    // if(checkHits){

                    for (unsigned int sel_h = 0; sel_h < track->recHitsSize(); sel_h++)
                    {

                      uint32_t sel_pHit = selTrack_hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, sel_h);
                      uint32_t sel_nHit = selTrack_hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, sel_h - 1);
                      auto sel_recHit = *(sel_hb + sel_h);
                      auto const &sel_hit = *sel_recHit;

                      // define a sequence of hit layers:
                      sel_thisLayer = selTrack_hitpattern.getLayer(sel_pHit);
                      sel_prevLayer = selTrack_hitpattern.getLayer(sel_nHit);
                      sel_thisSubStruct = selTrack_hitpattern.getSubStructure(sel_pHit);
                      sel_prevSubStruct = selTrack_hitpattern.getSubStructure(sel_nHit);
                      // the condition !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct)) prevents two hits falling into the same layer and sub-structure
                      // but allows for hits being in the same layers, e. g., layer 1 of PXB and layer 1 of PXF, in the case of high |eta| tracks
                      if (!sel_hit.isValid())
                      {
                        // std::cout << "sel_hit.isValid() is false" << std::endl;
                        continue;
                      }

                      if (!(selTrack_hitpattern.validHitFilter(sel_pHit)))
                      {
                        // std::cout << "selTrack_hitpattern.validHitFilter(sel_pHit) is false" << std::endl;
                        continue;
                      }
                      if (selTrack_hitpattern.getSubStructure(sel_pHit) == 1 && !((sel_thisLayer == sel_prevLayer) && (sel_thisSubStruct == sel_prevSubStruct)))
                      {
                        sel_pxbLayers++;
                      }
                      if (selTrack_hitpattern.getSubStructure(sel_pHit) == 2 && !((sel_thisLayer == sel_prevLayer) && (sel_thisSubStruct == sel_prevSubStruct)))
                      {
                        sel_pxfLayers++;
                      }
                      if (selTrack_hitpattern.getSubStructure(sel_pHit) == 3 && !((sel_thisLayer == sel_prevLayer) && (sel_thisSubStruct == sel_prevSubStruct)))
                      {
                        sel_tibLayers++;
                      }
                      if (selTrack_hitpattern.getSubStructure(sel_pHit) == 4 && !((sel_thisLayer == sel_prevLayer) && (sel_thisSubStruct == sel_prevSubStruct)))
                      {
                        sel_tidLayers++;
                      }
                      if (selTrack_hitpattern.getSubStructure(sel_pHit) == 5 && !((sel_thisLayer == sel_prevLayer) && (sel_thisSubStruct == sel_prevSubStruct)))
                      {
                        sel_tobLayers++;
                      }
                      if (selTrack_hitpattern.getSubStructure(sel_pHit) == 6 && !((sel_thisLayer == sel_prevLayer) && (sel_thisSubStruct == sel_prevSubStruct)))
                      {
                        sel_tecLayers++;
                      }

                      // std::cout << "Track: " << sel_pxbLayers << " " << sel_pxfLayers << " " << sel_tibLayers << " " << sel_tidLayers << " " << sel_tobLayers << " " << sel_tecLayers << " -- " << sel_pxbLayers + sel_pxfLayers + sel_tibLayers + sel_tidLayers + sel_tobLayers + sel_tecLayers << std::endl;
                    }
                  }
                  catch (...)
                  {
                    std::cout << "de-referenced track extra" << std::endl;
                  }
                }

                trackPixelLayers_->Fill(track_pixelLayersWithMeasurement);
                trackTrackerLayers_->Fill(track_trackerLayersWithMeasurement);

                trackPtAllPt_->Fill(1.0 * track_rereco->pt() / track->pt());

                double track_chi2perNdof = 0.0;

                if (track_rereco->ndof() > 0)
                  track_chi2perNdof = 1.0 * track_rereco->chi2() / track_rereco->ndof();

                trackChi2ndofAllPt_->Fill(track_chi2perNdof);
              }
            }
          }

          if (numRerecoTracks > 0)
            trackEfficiencyCalc_->Fill(1.0);
          if (numRerecoMatchedTracks > 0)
            trackEfficiencyCalc_->Fill(2.0);
        }
      }
    }
  }

  if (numTracks > 0)
    trackEfficiencyCalc_->Fill(0.0);

  // std::cout << "##################### END OF EVENT #####################" << std::endl;
}
// Define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackingResolutionAlignment);
