#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TMath.h"
#include "TLorentzVector.h"
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackBase.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackResiduals.h"
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
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"

//--- for SimHit association
#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"
#include "Geometry/CommonTopologies/interface/PixelTopology.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"
#include "Geometry/CommonDetUnit/interface/GeomDetType.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "Geometry/CommonDetUnit/interface/GluedGeomDet.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerNumberingBuilder/interface/GeometricDet.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetType.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"

#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

#include "Geometry/TrackerGeometryBuilder/interface/PixelTopologyBuilder.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/CommonDetUnit/interface/GeomDetType.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "TrackingResolution/TrackingResolution/interface/TrackingResolutionMod.h"
// -----------------------------
// constructors and destructor
// -----------------------------
TrackingResolutionMod::TrackingResolutionMod(const edm::ParameterSet& ps):
  parameters_(ps),
  //trackerHitAssociatorConfig_(ps, consumesCollector()),
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

void TrackingResolutionMod::bookHistograms(DQMStore::IBooker &iBook, edm::Run const& iRun, edm::EventSetup const& iSetup) {

  std::string currentFolder = folderName_+"/" ;
  iBook.setCurrentFolder(currentFolder);

  trackAlgo_ = iBook.book1D("shortTrackAlgos"+hitsRemain+"l", "reRECO tracks RECO algo - "+hitsRemain+" layers",30,-0.5,29.5);
  trackAlgoBefMatch_ = iBook.book1D("shortTrackAlgosBefMatch"+hitsRemain+"l", "reRECO tracks RECO algo before matching - "+hitsRemain+" layers",30,-0.5,29.5);
  trackAlgoOnlyMiss_ = iBook.book1D("shortTrackAlgosOnlyMiss"+hitsRemain+"l", "reRECO tracks (not matching hits) RECO algo - "+hitsRemain+" layers",30,-0.5,29.5);
  originalTrackAlgo_ = iBook.book1D("originalTrackAlgos"+hitsRemain+"l", "RECO tracks RECO algo - "+hitsRemain+" layers",30,-0.5,29.5);

  trackOriginalAlgo_ = iBook.book1D("shortTrackOriginalAlgos"+hitsRemain+"l", "reRECO tracks RECO original algo - "+hitsRemain+" layers",30,-0.5,29.5);
  trackOriginalAlgoOnlyMiss_ = iBook.book1D("shortTrackOriginalAlgosOnlyMiss"+hitsRemain+"l", "reRECO tracks (not matching hits) RECO original algo - "+hitsRemain+" layers",30,-0.5,29.5);
  originalTrackOriginalAlgo_ = iBook.book1D("originalTrackOriginalAlgos"+hitsRemain+"l", "RECO tracks RECO original algo - "+hitsRemain+" layers",30,-0.5,29.5);

  allTracksTrackerLayers_ = iBook.book1D("allTracksTrackerLayers"+hitsRemain+"l", "Tracker layers with measurement (all reRECO tracks) - "+hitsRemain+" layers",11,-0.5,10.5);
  trackPixelLayers_ = iBook.book1D("trackPixelLayers"+hitsRemain+"l", "Pixel layers with measurement - "+hitsRemain+" layers",11,-0.5,10.5);
  trackTrackerLayers_ = iBook.book1D("trackTrackerLayers"+hitsRemain+"l", "Tracker layers with measurement - "+hitsRemain+" layers",11,-0.5,10.5);
  trackTrackerLayersMiss_ = iBook.book1D("trackTrackerLayersMiss"+hitsRemain+"l", "Tracker layers with measurement missing layers - "+hitsRemain+" layers",11,-0.5,10.5);

  trackEfficiencyCalc_ = iBook.book1D("trackEfficiencyCalc"+hitsRemain+"l", "Number of shortened matched and full tracks - "+hitsRemain+" layers",4,-0.5,3.5);

  //trackHitResidual_ = iBook.book1D("trackHitResidual"+hitsRemain+"l", "Shortened and full track hit residual distance - "+hitsRemain+" layers",50,0.0,7.0);
  //shortTrackHitResidual_ = iBook.book1D("shortTrackHitResidual"+hitsRemain+"l", "Shortened track hit residual - "+hitsRemain+" layers",50,0.0,4.0);
  //longTrackHitResidual_ = iBook.book1D("longTrackHitResidual"+hitsRemain+"l", "Long track hit residual - "+hitsRemain+" layers",50,0.0,4.0);
  //longGoodTrackHitResidual_ = iBook.book1D("longGoodTrackHitResidual"+hitsRemain+"l", "Long track good hit residual - "+hitsRemain+" layers",50,0.0,4.0);

//trackHitResidual_ = iBook.book1D("trackHitResidual"+hitsRemain+"l", "Shortened and full track hit residual distance - "+hitsRemain+" layers",50,-1.0,1.0);
//shortTrackHitResidual_ = iBook.book1D("shortTrackHitResidual"+hitsRemain+"l", "Shortened track hit residual - "+hitsRemain+" layers",50,-1.0,1.0);
  longTrackHitResidual_ = iBook.book1D("longTrackHitResidual"+hitsRemain+"l", "Long track hit residual - "+hitsRemain+" layers",50,-1.0,1.0);
  longGoodTrackHitResidual_ = iBook.book1D("longGoodTrackHitResidual"+hitsRemain+"l", "Long track good hit residual - "+hitsRemain+" layers",50,-1.0,1.0);

  trackDeltaRAllPt_ = iBook.book1D("trackDeltaR"+hitsRemain+"lAllPt", "Track #DeltaR - "+hitsRemain+" layers",50,0.0,1.0);

  trackMissInnAllPt_ = iBook.book1D("trackMissInn"+hitsRemain+"lAllPt", "Track missing inner hits - "+hitsRemain+" layers",21,-0.5,20.5);
  trackMissMidAllPt_ = iBook.book1D("trackMissMid"+hitsRemain+"lAllPt", "Track missing middle hits - "+hitsRemain+" layers",21,-0.5,20.5);
  trackMissOutAllPt_ = iBook.book1D("trackMissOut"+hitsRemain+"lAllPt", "Track missing outer hits - "+hitsRemain+" layers",21,-0.5,20.5);

  trackPtAllPt_ = iBook.book1D("trackPt"+hitsRemain+"lAllPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);
  trackPtLowPt_ = iBook.book1D("trackPt"+hitsRemain+"lLowPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);
  trackPtMedPt_ = iBook.book1D("trackPt"+hitsRemain+"lMedPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);
  trackPtHigPt_ = iBook.book1D("trackPt"+hitsRemain+"lHigPt", "Track p_{T} - "+hitsRemain+" layers",41,0.0,2.0);

  trackPtBarrel_ = iBook.book1D("trackPt"+hitsRemain+"lBarrel", "Track p_{T} - "+hitsRemain+" layers - Barrel",41,0.0,2.0);
  trackPtBarend_ = iBook.book1D("trackPt"+hitsRemain+"lBarend", "Track p_{T} - "+hitsRemain+" layers - Barrel + Endcap",41,0.0,2.0);
  trackPtEndcap_ = iBook.book1D("trackPt"+hitsRemain+"lEndcap", "Track p_{T} - "+hitsRemain+" layers - Endcap",41,0.0,2.0);

  trackChi2ndofAllPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lAllPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofLowPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lLowPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofMedPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lMedPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);
  trackChi2ndofHigPt_ = iBook.book1D("trackChi2ndof"+hitsRemain+"lHigPt", "Chi^{2} / ndof - "+hitsRemain+" layers",40,0.0,2.0);

}
void TrackingResolutionMod::analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) {

  std::ofstream outdata; // general_info.dat
  std::ofstream outdata2; // missingInnMid_lessTrackerLayers_events_"+hitsRemain+"layers.dat
  std::ofstream outdata3; // missingInnMid_correctTrackerLayers_events_"+hitsRemain+"layers.dat
  std::ofstream outdata4; // lessTrackerLayers_notMissingInnMid_events_"+hitsRemain+"layers.dat

  outdata.open("general_info.dat", std::ios::app); // opens the file
  if( !outdata ) { // file couldn't be opened
    std::cerr << "Error: file could not be opened" << std::endl;
    exit(1);
  }

  edm::Handle< std::vector<reco::Track> > tracks;
  edm::Handle< std::vector<reco::Vertex> > vertices;
  edm::Handle< std::vector<reco::Track> > tracks_rereco;

  iEvent.getByToken(tracksToken, tracks);
  iEvent.getByToken(primVertexToken, vertices);
  iEvent.getByToken(tracksRerecoToken, tracks_rereco);

  const reco::Vertex vertex = vertices->at(0);

  int ntracks = 0;
  int ntracks_rereco = 0;
  int hitsRemain_int = stoi(hitsRemain);

  outdata2.open("missingInnMid_lessTrackerLayers_events_"+hitsRemain+"layers.dat", std::ios::app); // opens the file
  if( !outdata2 ) { // file couldn't be opened
    std::cerr << "Error: file could not be opened" << std::endl;
    exit(1);
  }

  outdata3.open("missingInnMid_correctTrackerLayers_events_"+hitsRemain+"layers.dat", std::ios::app); // opens the file
  if( !outdata3 ) { // file couldn't be opened
    std::cerr << "Error: file could not be opened" << std::endl;
    exit(1);
  }

  outdata4.open("lessTrackerLayers_notMissingInnMid_events_"+hitsRemain+"layers.dat", std::ios::app); // opens the file
  if( !outdata4 ) { // file couldn't be opened
    std::cerr << "Error: file could not be opened" << std::endl;
    exit(1);
  }

  for (std::vector<reco::Track>::const_iterator track = tracks->begin(); track != tracks->end(); ++track) {

    ntracks = ntracks + 1;

  }

  for (std::vector<reco::Track>::const_iterator track_rereco = tracks_rereco->begin(); track_rereco != tracks_rereco->end(); ++track_rereco) {

    ntracks_rereco = ntracks_rereco + 1;
    int allTracks_trackerLayersWithMeasurement = track_rereco->hitPattern().trackerLayersWithMeasurement();
    allTracksTrackerLayers_->Fill(allTracks_trackerLayersWithMeasurement);

  }

    for (std::vector<reco::Track>::const_iterator track = tracks->begin(); track != tracks->end(); ++track) {

      Double_t dxy = (track->dxy(vertex.position()));
      Double_t dz = (track->dz(vertex.position()));
      TLorentzVector tvec;
      tvec.SetPtEtaPhiM(track->pt(),track->eta(),track->phi(),0.0);

        if(track->hitPattern().trackerLayersWithMeasurement() > minNumberOfLayers){

          if(abs(dxy) < maxDxy){

            if(abs(dz) < maxDz){

              if(abs(track->eta())>maxTracksEta or track->pt()<minTracksPt) break;

              trackEfficiencyCalc_->Fill(0.0);

              for (std::vector<reco::Track>::const_iterator track_rereco = tracks_rereco->begin(); track_rereco != tracks_rereco->end(); ++track_rereco) {

                std::vector<double> longx;
                std::vector<double> longy;
                std::vector<double> shortx;
                std::vector<double> shorty;
                std::vector<double> longx_lastShortLayer;
                std::vector<double> longy_lastShortLayer;
                std::vector<double> longx_lastShortLayerGood;
                std::vector<double> longy_lastShortLayerGood;
                std::vector<double> shortx_lastShortLayer;
                std::vector<double> shorty_lastShortLayer;
                bool checkHits = false;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(track_rereco->pt(),track_rereco->eta(),track_rereco->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                trackDeltaRAllPt_->Fill(deltaR);
                trackAlgoBefMatch_->Fill(track_rereco->algo());
                if(deltaR < maxDr){

                  trackEfficiencyCalc_->Fill(3.0);

                  if(track_rereco->pt()>=minTracksPt && track_rereco->pt()<=maxTracksPt && abs(track_rereco->eta())>=minTracksEta && abs(track_rereco->eta())<=maxTracksEta){

                    int track_trackerLayersWithMeasurement = track_rereco->hitPattern().trackerLayersWithMeasurement();
                    int track_pixelLayersWithMeasurement = track_rereco->hitPattern().pixelLayersWithMeasurement();

                    reco::HitPattern hitpattern = track_rereco->hitPattern();
                    int valid = hitpattern.numberOfValidTrackerHits();
                    int lostMid = hitpattern.numberOfLostTrackerHits(reco::HitPattern::TRACK_HITS);
                    int lostIn = hitpattern.numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
                    int lostOut = hitpattern.numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);

                    int selTrack_trackerLayersWithMeasurement = track->hitPattern().trackerLayersWithMeasurement();

                    reco::HitPattern selTrack_hitpattern = track->hitPattern();
                    int selTrack_valid = selTrack_hitpattern.numberOfValidTrackerHits();
                    int selTrack_lostMid = selTrack_hitpattern.numberOfLostTrackerHits(reco::HitPattern::TRACK_HITS);
                    int selTrack_lostIn = selTrack_hitpattern.numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
                    int selTrack_lostOut = selTrack_hitpattern.numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);

                    const Int_t trackAlgoNum = track_rereco->algo();
                    if(track_trackerLayersWithMeasurement == hitsRemain_int) {trackAlgo_->Fill(trackAlgoNum);}
                    else {trackAlgoOnlyMiss_->Fill(trackAlgoNum);}
                    const auto trackAlgo = track_rereco->algoName();
                    const auto selTrack_trackAlgo = track->algoName();

                    const Int_t originalTrackAlgoNum = track->algo();
                    originalTrackAlgo_->Fill(originalTrackAlgoNum);
                    const Int_t originalTrackOriginalAlgoNum = track->originalAlgo();
                    originalTrackOriginalAlgo_->Fill(originalTrackOriginalAlgoNum);

                    const Int_t trackOriginalAlgoNum = track_rereco->originalAlgo();
                    if(track_trackerLayersWithMeasurement == hitsRemain_int) {trackOriginalAlgo_->Fill(trackOriginalAlgoNum);}
                    else {trackOriginalAlgoOnlyMiss_->Fill(trackOriginalAlgoNum);}

                    const auto selTrack_tot = selTrack_valid + selTrack_lostMid + selTrack_lostIn + selTrack_lostOut;
                    const auto tot = valid + lostMid + lostIn + lostOut;

                    outdata << "Long  -- LayersRemain: " << hitsRemain_int << ". Layers w/ Measurement: " << selTrack_trackerLayersWithMeasurement << ". Valid: " << selTrack_valid << ". Total: " << selTrack_tot << ". MissInn: " << selTrack_lostIn << ". MissMid: " << selTrack_lostMid << ". MissOut: " << selTrack_lostOut << ". Track algo: " << selTrack_trackAlgo << "." << std::endl;

                    outdata << "Short -- LayersRemain: " << hitsRemain_int << ". Layers w/ Measurement: " << track_trackerLayersWithMeasurement << ". Valid: " << valid << ". Total: " << tot << ". MissInn: " << lostIn << ". MissMid: " << lostMid << ". MissOut: " << lostOut << ". Track algo: " << trackAlgo << ".";

                    if(hitsRemain_int!=track_trackerLayersWithMeasurement){
                      outdata << " ############################" << std::endl;
                      checkHits = true;
                    }
                    else{
                      outdata << std::endl;
                    }

// From here until line 541 is an attempt to calculate hits residuals ===========================================================================================================================================================================================

                    try{

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
                      int sequLayers = 0;

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
                      int sel_sequLayers = 0;

                      for(unsigned int h=0;h<track_rereco->recHitsSize();h++){

                        uint32_t pHit = hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, h);
                        uint32_t nHit = hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, h-1);
                        auto recHit = *(hb+h);
                        auto const & hit = *recHit;

                        // define a sequence of hit layers:
                        thisLayer =  hitpattern.getLayer(pHit);
                        prevLayer =  hitpattern.getLayer(nHit);
                        thisSubStruct =  hitpattern.getSubStructure(pHit);
                        prevSubStruct =  hitpattern.getSubStructure(nHit);
                        // the condition !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct)) prevents two hits falling into the same layer and sub-structure
                        // but allows for hits being in the same layers, e. g., layer 1 of PXB and layer 1 of PXF, in the case of high |eta| tracks
                        if (hitpattern.getSubStructure(pHit)==1 && !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct))){
                          pxbLayers ++;
                        }
                        if (hitpattern.getSubStructure(pHit)==2 && !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct))){
                          pxfLayers ++;
                        }
                        if (hitpattern.getSubStructure(pHit)==3 && !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct))){
                          tibLayers ++;
                        }
                        if (hitpattern.getSubStructure(pHit)==4 && !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct))){
                          tidLayers ++;
                        }
                        if (hitpattern.getSubStructure(pHit)==5 && !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct))){
                          tobLayers ++;
                        }
                        if (hitpattern.getSubStructure(pHit)==6 && !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct))){
                          tecLayers ++;
                        }

                        sequLayers = pxbLayers+pxfLayers+tibLayers+tidLayers+tobLayers+tecLayers;
                        //std::cout << "Short -- " <<  sequLayers << " : " << pxbLayers << " "<< pxfLayers << " "<< tibLayers << " "<< tidLayers << " "<< tobLayers << " "<< tecLayers <<std::endl;

                        if (!hit.isValid()){
                          outdata<< "hit.isValid == False: " << h <<std::endl;
                          continue;
                        }

                        if (!(hitpattern.validHitFilter(pHit))){
                          outdata<< "hitpattern.validHitFilter == False: " << h <<std::endl;
                          continue;
                        }

                        if(checkHits){

                          auto const track_residuals = track_rereco->residuals();
                          auto const residualx_hit = track_residuals.residualX(h);
                          auto const residualy_hit = track_residuals.residualY(h);
                          shortx.push_back(residualx_hit);
                          shorty.push_back(residualy_hit);

                          if(sequLayers == track_trackerLayersWithMeasurement){

                            shortx_lastShortLayer.push_back(residualx_hit);
                            shorty_lastShortLayer.push_back(residualy_hit);

                            //std::cout << "Short -- sequLayers: " << sequLayers << " -- hit residuals: " << residualx_hit << " " << residualy_hit << std::endl;

                          }

                        }

                      }

                      //if(checkHits){

                        for(unsigned int sel_h=0;sel_h<track->recHitsSize();sel_h++){

                          uint32_t sel_pHit = selTrack_hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, sel_h);
                          uint32_t sel_nHit = selTrack_hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, sel_h-1);
                          auto sel_recHit = *(sel_hb+sel_h);
                          auto const & sel_hit = *sel_recHit;

                          // define a sequence of hit layers:
                          sel_thisLayer =  selTrack_hitpattern.getLayer(sel_pHit);
                          sel_prevLayer =  selTrack_hitpattern.getLayer(sel_nHit);
                          sel_thisSubStruct =  selTrack_hitpattern.getSubStructure(sel_pHit);
                          sel_prevSubStruct =  selTrack_hitpattern.getSubStructure(sel_nHit);
                          // the condition !((thisLayer==prevLayer)&&(thisSubStruct==prevSubStruct)) prevents two hits falling into the same layer and sub-structure
                          // but allows for hits being in the same layers, e. g., layer 1 of PXB and layer 1 of PXF, in the case of high |eta| tracks
                          if (selTrack_hitpattern.getSubStructure(sel_pHit)==1 && !((sel_thisLayer==sel_prevLayer)&&(sel_thisSubStruct==sel_prevSubStruct))){
                            sel_pxbLayers ++;
                          }
                          if (selTrack_hitpattern.getSubStructure(sel_pHit)==2 && !((sel_thisLayer==sel_prevLayer)&&(sel_thisSubStruct==sel_prevSubStruct))){
                            sel_pxfLayers ++;
                          }
                          if (selTrack_hitpattern.getSubStructure(sel_pHit)==3 && !((sel_thisLayer==sel_prevLayer)&&(sel_thisSubStruct==sel_prevSubStruct))){
                            sel_tibLayers ++;
                          }
                          if (selTrack_hitpattern.getSubStructure(sel_pHit)==4 && !((sel_thisLayer==sel_prevLayer)&&(sel_thisSubStruct==sel_prevSubStruct))){
                            sel_tidLayers ++;
                          }
                          if (selTrack_hitpattern.getSubStructure(sel_pHit)==5 && !((sel_thisLayer==sel_prevLayer)&&(sel_thisSubStruct==sel_prevSubStruct))){
                            sel_tobLayers ++;
                          }
                          if (selTrack_hitpattern.getSubStructure(sel_pHit)==6 && !((sel_thisLayer==sel_prevLayer)&&(sel_thisSubStruct==sel_prevSubStruct))){
                            sel_tecLayers ++;
                          }

                          sel_sequLayers = sel_pxbLayers+sel_pxfLayers+sel_tibLayers+sel_tidLayers+sel_tobLayers+sel_tecLayers;

                          if (!sel_hit.isValid()){
                            continue;
                          }

                          if (!(selTrack_hitpattern.validHitFilter(sel_pHit))){
                            continue;
                          }

                          //if(checkHits){

                            auto const track_residuals = track->residuals();
                            auto const residualx_hit = track_residuals.residualX(sel_h);
                            auto const residualy_hit = track_residuals.residualY(sel_h);
                            longx.push_back(residualx_hit);
                            longy.push_back(residualy_hit);

                          if(checkHits){

                            if(sel_sequLayers == (track_trackerLayersWithMeasurement + 1)){

                              longx_lastShortLayer.push_back(residualx_hit);
                              longy_lastShortLayer.push_back(residualy_hit);

                              //std::cout << "Long -- hitsRemain: " << hitsRemain_int << " -- shortTrackerLayersWithMeasurement: " << track_trackerLayersWithMeasurement << " -- sel_sequLayers: " << sel_sequLayers << " -- hit residuals: " << residualx_hit << " " << residualy_hit << std::endl;

                            }

                          }

                          else{

                            if(sel_sequLayers == track_trackerLayersWithMeasurement){

                              longx_lastShortLayerGood.push_back(residualx_hit);
                              longy_lastShortLayerGood.push_back(residualy_hit);

                              //std::cout << "LongGood -- hitsRemain: " << hitsRemain_int << " -- shortTrackerLayersWithMeasurement: " << track_trackerLayersWithMeasurement << " -- sel_sequLayers: " << sel_sequLayers << " -- hit residuals: " << residualx_hit << " " << residualy_hit << std::endl;

                            }

                          }

                        }

                        if(checkHits){

                          for(std::vector<double>::size_type hs = 0; hs < shortx_lastShortLayer.size(); ++hs){
                            std::vector<double> min_resdist;
                            std::vector<double> min_resshort;
                            for(std::vector<double>::size_type hl = 0; hl < longx_lastShortLayer.size(); ++hl){
                              double resshort = shortx_lastShortLayer[hs];
                              double dist = sqrt((pow((shortx_lastShortLayer[hs] - longx_lastShortLayer[hl]),2.0)));
                              min_resdist.push_back(dist);
                              min_resshort.push_back(resshort);
                            }
                            //double min_dist = *min_element(min_resdist.begin(), min_resdist.end());
                            //double short_min_res = *min_element(min_resshort.begin(), min_resshort.end());
                            //trackHitResidual_->Fill(min_dist);
                            //shortTrackHitResidual_->Fill(short_min_res);
                          }

                          std::vector<double> min_reslong;
                          for(std::vector<double>::size_type hl = 0; hl < longx_lastShortLayer.size(); ++hl){
                            //double reslong = sqrt((pow((longx_lastShortLayer[hl]),2.0))+(pow((longy_lastShortLayer[hl]),2.0)));
                            double reslong = longx_lastShortLayer[hl];
                            min_reslong.push_back(reslong);
                          }
                          double long_min_res = *min_element(min_reslong.begin(), min_reslong.end());
                          longTrackHitResidual_->Fill(long_min_res);
                          //longGoodTrackHitResidual_->Fill(long_min_res);

                        }

                        else{

                          std::vector<double> min_reslong_good;
                          for(std::vector<double>::size_type hlg = 0; hlg < longx_lastShortLayerGood.size(); ++hlg){
                            //double reslonggood = sqrt((pow((longx_lastShortLayerGood[hlg]),2.0))+(pow((longy_lastShortLayerGood[hlg]),2.0)));
                            double reslonggood = longx_lastShortLayerGood[hlg];
                            min_reslong_good.push_back(reslonggood);
                          }
                          double long_min_res_good = *min_element(min_reslong_good.begin(), min_reslong_good.end());
                          longGoodTrackHitResidual_->Fill(long_min_res_good);

                        }

                      //}

                    }

                    catch(...){
                      std::cout << "de-referenced track extra" << std::endl;
                    }

// End of attempt at calculating hitResiduals ===========================================================================================================================================================================================

                    trackPixelLayers_->Fill(track_pixelLayersWithMeasurement);
                    trackTrackerLayers_->Fill(track_trackerLayersWithMeasurement);
                    if(track_trackerLayersWithMeasurement != hitsRemain_int) trackTrackerLayersMiss_->Fill(track_trackerLayersWithMeasurement);

                    trackMissInnAllPt_->Fill(lostIn);
                    trackMissMidAllPt_->Fill(lostMid);
                    trackMissOutAllPt_->Fill(lostOut);

                    if(track_trackerLayersWithMeasurement < hitsRemain_int && (lostMid != 0 || lostIn != 0)) outdata2 << iEvent.id() << std::endl; // missingInnMid_lessTrackerLayers_events_"+hitsRemain+"layers.dat
                    if(track_trackerLayersWithMeasurement == hitsRemain_int && (lostMid != 0 || lostIn != 0)) outdata3 << iEvent.id() << std::endl; // missingInnMid_correctTrackerLayers_events_"+hitsRemain+"layers.dat
                    if(track_trackerLayersWithMeasurement < hitsRemain_int && (lostMid == 0 && lostIn == 0)) outdata4 << iEvent.id() << std::endl; // lessTrackerLayers_notMissingInnMid_events_"+hitsRemain+"layers.dat

                    trackPtAllPt_->Fill(1.0*track_rereco->pt()/track->pt());

                    if(abs(track_rereco->eta())<=1.0){

                      trackPtBarrel_->Fill(1.0*track_rereco->pt()/track->pt());

                    }

                    if(abs(track_rereco->eta())>1.0 and abs(track_rereco->eta())<=2.0){

                      trackPtBarend_->Fill(1.0*track_rereco->pt()/track->pt());

                    }

                    if(abs(track_rereco->eta())>2.0){

                      trackPtEndcap_->Fill(1.0*track_rereco->pt()/track->pt());

                    }

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

                    if(hitsRemain_int==8) outdata << "=================================================================================================" << std::endl;

                    outdata.close();

                  }

                }

              }

            }

          }

        }

    }

  outdata2.close();
  outdata3.close();
  outdata4.close();

}
// Define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackingResolutionMod);
