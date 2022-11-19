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
  initialStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("initialStepRerecoInputTag", edm::InputTag("initialStepTracks", "", "reRECO"))),
  highPtTripletStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("highPtTripletStepRerecoInputTag", edm::InputTag("highPtTripletStepTracks", "", "reRECO"))),
  jetCoreRegionalStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("jetCoreRegionalStepRerecoInputTag", edm::InputTag("jetCoreRegionalStepTracks", "", "reRECO"))),
  lowPtQuadStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("lowPtQuadStepRerecoInputTag", edm::InputTag("lowPtQuadStepTracks", "", "reRECO"))),
  lowPtTripletStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("lowPtTripletStepRerecoInputTag", edm::InputTag("lowPtTripletStepTracks", "", "reRECO"))),
  detachedQuadStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("detachedQuadStepRerecoInputTag", edm::InputTag("detachedQuadStepTracks", "", "reRECO"))),
  detachedTripletStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("detachedTripletStepRerecoInputTag", edm::InputTag("detachedTripletStepTracks", "", "reRECO"))),
  pixelPairStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("pixelPairStepRerecoInputTag", edm::InputTag("pixelPairStepTracks", "", "reRECO"))),
  mixedTripletStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("mixedTripletStepRerecoInputTag", edm::InputTag("mixedTripletStepTracks", "", "reRECO"))),
  pixelLessStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("pixelLessStepRerecoInputTag", edm::InputTag("pixelLessStepTracks", "", "reRECO"))),
  tobTecStepRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("tobTecStepRerecoInputTag", edm::InputTag("tobTecStepTracks", "", "reRECO"))),
  muonSeededTracksInOutRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("muonSeededTracksInOutRerecoInputTag", edm::InputTag("muonSeededTracksInOut", "", "reRECO"))),
  muonSeededTracksOutInRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("muonSeededTracksOutInRerecoInputTag", edm::InputTag("muonSeededTracksOutIn", "", "reRECO"))),
  earlyGeneralTracksRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("earlyGeneralTracksRerecoInputTag", edm::InputTag("earlyGeneralTracks", "", "reRECO"))),
  preDuplicateMergingGeneralTracksRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("preDuplicateMergingGeneralTracksRerecoInputTag", edm::InputTag("preDuplicateMergingGeneralTracks", "", "reRECO"))),
  mergedDuplicateTracksRerecoTag(parameters_.getUntrackedParameter<edm::InputTag>("mergedDuplicateTracksRerecoInputTag", edm::InputTag("mergedDuplicateTracks", "", "reRECO"))),
  muonsToken(consumes<std::vector<reco::Muon>>(muonsTag)),
  tracksToken(consumes<std::vector<reco::Track>>(tracksTag)),
  primVertexToken(consumes<std::vector<reco::Vertex>>(primVertexTag)),
  tracksRerecoToken(consumes<std::vector<reco::Track>>(tracksRerecoTag)),
  initialStepRerecoToken(consumes<std::vector<reco::Track>>(initialStepRerecoTag)),
  highPtTripletStepRerecoToken(consumes<std::vector<reco::Track>>(highPtTripletStepRerecoTag)),
  jetCoreRegionalStepRerecoToken(consumes<std::vector<reco::Track>>(jetCoreRegionalStepRerecoTag)),
  lowPtQuadStepRerecoToken(consumes<std::vector<reco::Track>>(lowPtQuadStepRerecoTag)),
  lowPtTripletStepRerecoToken(consumes<std::vector<reco::Track>>(lowPtTripletStepRerecoTag)),
  detachedQuadStepRerecoToken(consumes<std::vector<reco::Track>>(detachedQuadStepRerecoTag)),
  detachedTripletStepRerecoToken(consumes<std::vector<reco::Track>>(detachedTripletStepRerecoTag)),
  pixelPairStepRerecoToken(consumes<std::vector<reco::Track>>(pixelPairStepRerecoTag)),
  mixedTripletStepRerecoToken(consumes<std::vector<reco::Track>>(mixedTripletStepRerecoTag)),
  pixelLessStepRerecoToken(consumes<std::vector<reco::Track>>(pixelLessStepRerecoTag)),
  tobTecStepRerecoToken(consumes<std::vector<reco::Track>>(tobTecStepRerecoTag)),
  muonSeededTracksInOutRerecoToken(consumes<std::vector<reco::Track>>(muonSeededTracksInOutRerecoTag)),
  muonSeededTracksOutInRerecoToken(consumes<std::vector<reco::Track>>(muonSeededTracksOutInRerecoTag)),
  earlyGeneralTracksRerecoToken(consumes<std::vector<reco::Track>>(earlyGeneralTracksRerecoTag)),
  preDuplicateMergingGeneralTracksRerecoToken(consumes<std::vector<reco::Track>>(preDuplicateMergingGeneralTracksRerecoTag)),
  mergedDuplicateTracksRerecoToken(consumes<std::vector<reco::Track>>(mergedDuplicateTracksRerecoTag))
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

  trackMissInnAllPt_ = iBook.book1D("trackMissInn"+hitsRemain+"lAllPt", "Track missing inner hits - "+hitsRemain+" layers",21,-0.5,20.5);
  trackMissMidAllPt_ = iBook.book1D("trackMissMid"+hitsRemain+"lAllPt", "Track missing middle hits - "+hitsRemain+" layers",21,-0.5,20.5);
  trackMissOutAllPt_ = iBook.book1D("trackMissOut"+hitsRemain+"lAllPt", "Track missing outer hits - "+hitsRemain+" layers",21,-0.5,20.5);

  missInnAllPt_ = iBook.book1D("missInn"+hitsRemain+"lAllPt", "Missing inner hits - "+hitsRemain+" layers",21,-0.5,20.5);
  missMidAllPt_ = iBook.book1D("missMid"+hitsRemain+"lAllPt", "Missing middle hits - "+hitsRemain+" layers",21,-0.5,20.5);
  missOutAllPt_ = iBook.book1D("missOut"+hitsRemain+"lAllPt", "Missing outer hits - "+hitsRemain+" layers",21,-0.5,20.5);

  trackEfficiencyCalc_ = iBook.book1D("trackEfficiencyCalc"+hitsRemain+"l", "Number of shortened matched and full tracks - "+hitsRemain+" layers",15,-0.5,14.5);

}
void TrackingResolution::analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) {

  edm::Handle< std::vector<reco::Muon> > muons;
  edm::Handle< std::vector<reco::Track> > tracks;
  edm::Handle< std::vector<reco::Vertex> > vertices;
  edm::Handle< std::vector<reco::Track> > tracks_rereco;
  edm::Handle< std::vector<reco::Track> > initialStepTracks;
  edm::Handle< std::vector<reco::Track> > highPtTripletStepTracks;
  edm::Handle< std::vector<reco::Track> > jetCoreRegionalStepTracks;
  edm::Handle< std::vector<reco::Track> > lowPtQuadStepTracks;
  edm::Handle< std::vector<reco::Track> > lowPtTripletStepTracks;
  edm::Handle< std::vector<reco::Track> > detachedQuadStepTracks;
  edm::Handle< std::vector<reco::Track> > detachedTripletStepTracks;
  edm::Handle< std::vector<reco::Track> > pixelPairStepTracks;
  edm::Handle< std::vector<reco::Track> > mixedTripletStepTracks;
  edm::Handle< std::vector<reco::Track> > pixelLessStepTracks;
  edm::Handle< std::vector<reco::Track> > tobTecStepTracks;
  edm::Handle< std::vector<reco::Track> > muonSeededTracksInOut;
  edm::Handle< std::vector<reco::Track> > muonSeededTracksOutIn;
  edm::Handle< std::vector<reco::Track> > earlyGeneralTracks;
  edm::Handle< std::vector<reco::Track> > preDuplicateMergingGeneralTracks;
  edm::Handle< std::vector<reco::Track> > mergedDuplicateTracks;

  iEvent.getByToken(muonsToken, muons);
  iEvent.getByToken(tracksToken, tracks);
  iEvent.getByToken(primVertexToken, vertices);
  iEvent.getByToken(tracksRerecoToken, tracks_rereco);
  iEvent.getByToken(initialStepRerecoToken, initialStepTracks);
  iEvent.getByToken(highPtTripletStepRerecoToken, highPtTripletStepTracks);
  iEvent.getByToken(jetCoreRegionalStepRerecoToken, jetCoreRegionalStepTracks);
  iEvent.getByToken(lowPtQuadStepRerecoToken, lowPtQuadStepTracks);
  iEvent.getByToken(lowPtTripletStepRerecoToken, lowPtTripletStepTracks);
  iEvent.getByToken(detachedQuadStepRerecoToken, detachedQuadStepTracks);
  iEvent.getByToken(detachedTripletStepRerecoToken, detachedTripletStepTracks);
  iEvent.getByToken(pixelPairStepRerecoToken, pixelPairStepTracks);
  iEvent.getByToken(mixedTripletStepRerecoToken, mixedTripletStepTracks);
  iEvent.getByToken(pixelLessStepRerecoToken, pixelLessStepTracks);
  iEvent.getByToken(tobTecStepRerecoToken, tobTecStepTracks);
  iEvent.getByToken(muonSeededTracksInOutRerecoToken, muonSeededTracksInOut);
  iEvent.getByToken(muonSeededTracksOutInRerecoToken, muonSeededTracksOutIn);
  iEvent.getByToken(earlyGeneralTracksRerecoToken, earlyGeneralTracks);
  iEvent.getByToken(preDuplicateMergingGeneralTracksRerecoToken, preDuplicateMergingGeneralTracks);
  iEvent.getByToken(mergedDuplicateTracksRerecoToken, mergedDuplicateTracks);

  std::ofstream outdata;

  outdata.open("pickingEvents.dat", std::ios::app); // opens the file
  if( !outdata ) { // file couldn't be opened
    std::cerr << "Error: file could not be opened" << std::endl;
    exit(1);
  }

  const reco::Vertex vertex = vertices->at(0);

  int hitsRemain_int = stoi(hitsRemain);
  int numInitStep = 0; int numHighPtTripStep = 0; int numJetCoreStep = 0; int numLowPtQuadStep = 0; int numLowPtTripStep = 0; int numDetQuadStep = 0; int numDetTripStep = 0; int numPixPairStep = 0; int numMixTripStep = 0; int numPixLesstep = 0; int numTobTecStep = 0; int numMuInOutStep = 0; int numMuOutInStep = 0;
  int numInitStepMatched = 0; int numHighPtTripStepMatched = 0; int numJetCoreStepMatched = 0; int numLowPtQuadStepMatched = 0; int numLowPtTripStepMatched = 0; int numDetQuadStepMatched = 0; int numDetTripStepMatched = 0;
  int numPixPairStepMatched = 0; int numMixTripStepMatched = 0; int numPixLesstepMatched = 0; int numTobTecStepMatched = 0; int numMuInOutStepMatched = 0; int numMuOutInStepMatched = 0;
  int numTracks = 0;
  int numRerecoTracks = 0;
  int numRerecoMatchedTracks = 0;
  int numEarlyTracks = 0;
  int numEarlyMatchedTracks = 0;
  int numPreDuplicateTracks = 0;
  int numPreDuplicateMatchedTracks = 0;
  int numMergedDuplicateTracks = 0;
  int numMergedDuplicateMatchedTracks = 0;

  //for (std::vector<reco::Muon>::const_iterator muon = muons->begin(); muon != muons->end(); ++muon) {

    //TLorentzVector mvec;
    //mvec.SetPtEtaPhiM(muon->pt(),muon->eta(),muon->phi(),muon->mass());

    for (std::vector<reco::Track>::const_iterator track = tracks->begin(); track != tracks->end(); ++track) {

      Double_t dxy = (track->dxy(vertex.position()));
      Double_t dz = (track->dz(vertex.position()));
      TLorentzVector tvec;
      tvec.SetPtEtaPhiM(track->pt(),track->eta(),track->phi(),0.0);
      //if(tvec.DeltaR(mvec)<maxDr){

        if(track->hitPattern().trackerLayersWithMeasurement() > minNumberOfLayers){

          if(abs(dxy) < maxDxy){

            if(abs(dz) < maxDz){

              if(abs(track->eta())>maxTracksEta or track->pt()<minTracksPt) break;

              //trackEfficiencyCalc_->Fill(0.0);
              ++numTracks;

              for (std::vector<reco::Track>::const_iterator initialStepTrack = initialStepTracks->begin(); initialStepTrack != initialStepTracks->end(); ++initialStepTrack) {
                ++numInitStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(initialStepTrack->pt(),initialStepTrack->eta(),initialStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numInitStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator highPtTripletStepTrack = highPtTripletStepTracks->begin(); highPtTripletStepTrack != highPtTripletStepTracks->end(); ++highPtTripletStepTrack) {
                ++numHighPtTripStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(highPtTripletStepTrack->pt(),highPtTripletStepTrack->eta(),highPtTripletStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numHighPtTripStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator jetCoreRegionalStepTrack = jetCoreRegionalStepTracks->begin(); jetCoreRegionalStepTrack != jetCoreRegionalStepTracks->end(); ++jetCoreRegionalStepTrack) {
                ++numJetCoreStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(jetCoreRegionalStepTrack->pt(),jetCoreRegionalStepTrack->eta(),jetCoreRegionalStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numJetCoreStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator lowPtQuadStepTrack = lowPtQuadStepTracks->begin(); lowPtQuadStepTrack != lowPtQuadStepTracks->end(); ++lowPtQuadStepTrack) {
                ++numLowPtQuadStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(lowPtQuadStepTrack->pt(),lowPtQuadStepTrack->eta(),lowPtQuadStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numLowPtQuadStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator lowPtTripletStepTrack = lowPtTripletStepTracks->begin(); lowPtTripletStepTrack != lowPtTripletStepTracks->end(); ++lowPtTripletStepTrack) {
                ++numLowPtTripStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(lowPtTripletStepTrack->pt(),lowPtTripletStepTrack->eta(),lowPtTripletStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numLowPtTripStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator detachedQuadStepTrack = detachedQuadStepTracks->begin(); detachedQuadStepTrack != detachedQuadStepTracks->end(); ++detachedQuadStepTrack) {
                ++numDetQuadStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(detachedQuadStepTrack->pt(),detachedQuadStepTrack->eta(),detachedQuadStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numDetQuadStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator detachedTripletStepTrack = detachedTripletStepTracks->begin(); detachedTripletStepTrack != detachedTripletStepTracks->end(); ++detachedTripletStepTrack) {
                ++numDetTripStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(detachedTripletStepTrack->pt(),detachedTripletStepTrack->eta(),detachedTripletStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numDetTripStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator pixelPairStepTrack = pixelPairStepTracks->begin(); pixelPairStepTrack != pixelPairStepTracks->end(); ++pixelPairStepTrack) {
                ++numPixPairStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(pixelPairStepTrack->pt(),pixelPairStepTrack->eta(),pixelPairStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numPixPairStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator mixedTripletStepTrack = mixedTripletStepTracks->begin(); mixedTripletStepTrack != mixedTripletStepTracks->end(); ++mixedTripletStepTrack) {
                ++numMixTripStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(mixedTripletStepTrack->pt(),mixedTripletStepTrack->eta(),mixedTripletStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numMixTripStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator pixelLessStepTrack = pixelLessStepTracks->begin(); pixelLessStepTrack != pixelLessStepTracks->end(); ++pixelLessStepTrack) {
                ++numPixLesstep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(pixelLessStepTrack->pt(),pixelLessStepTrack->eta(),pixelLessStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numPixLesstepMatched;
              }

              for (std::vector<reco::Track>::const_iterator tobTecStepTrack = tobTecStepTracks->begin(); tobTecStepTrack != tobTecStepTracks->end(); ++tobTecStepTrack) {
                ++numTobTecStep;
                //++numSumAllIter;
                //++numSumAllIterMuons;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(tobTecStepTrack->pt(),tobTecStepTrack->eta(),tobTecStepTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr){++numSumAllMatchedIter; ++numSumAllMatchedIterMuons;}
                if(deltaR < maxDr) ++numTobTecStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator muonSeededTrackInOut = muonSeededTracksInOut->begin(); muonSeededTrackInOut != muonSeededTracksInOut->end(); ++muonSeededTrackInOut) {
                ++numMuInOutStep;
                //++numSumAllIterMuons;
                //++numEarlyMuonsTracks;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(muonSeededTrackInOut->pt(),muonSeededTrackInOut->eta(),muonSeededTrackInOut->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr) {++numSumAllMatchedIterMuons; ++numEarlyMuonsMatchedTracks;}
                if(deltaR < maxDr) ++numMuInOutStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator muonSeededTrackOutIn = muonSeededTracksOutIn->begin(); muonSeededTrackOutIn != muonSeededTracksOutIn->end(); ++muonSeededTrackOutIn) {
                ++numMuOutInStep;
                //++numSumAllIterMuons;
                //++numEarlyMuonsTracks;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(muonSeededTrackOutIn->pt(),muonSeededTrackOutIn->eta(),muonSeededTrackOutIn->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr) {++numSumAllMatchedIterMuons; ++numEarlyMuonsMatchedTracks;}
                if(deltaR < maxDr) ++numMuOutInStepMatched;
              }

              for (std::vector<reco::Track>::const_iterator earlyGeneralTrack = earlyGeneralTracks->begin(); earlyGeneralTrack != earlyGeneralTracks->end(); ++earlyGeneralTrack) {
                ++numEarlyTracks;
                //++numEarlyMuonsTracks;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(earlyGeneralTrack->pt(),earlyGeneralTrack->eta(),earlyGeneralTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                //if(deltaR < maxDr) {++numEarlyMatchedTracks; ++numEarlyMuonsMatchedTracks;}
                if(deltaR < maxDr) ++numEarlyMatchedTracks;
              }

              for (std::vector<reco::Track>::const_iterator preDuplicateMergingGeneralTrack = preDuplicateMergingGeneralTracks->begin(); preDuplicateMergingGeneralTrack != preDuplicateMergingGeneralTracks->end(); ++preDuplicateMergingGeneralTrack) {
                ++numPreDuplicateTracks;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(preDuplicateMergingGeneralTrack->pt(),preDuplicateMergingGeneralTrack->eta(),preDuplicateMergingGeneralTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                if(deltaR < maxDr) ++numPreDuplicateMatchedTracks;
              }

              for (std::vector<reco::Track>::const_iterator mergedDuplicateTrack = mergedDuplicateTracks->begin(); mergedDuplicateTrack != mergedDuplicateTracks->end(); ++mergedDuplicateTrack) {
                ++numMergedDuplicateTracks;
                TLorentzVector trerecovec;
                trerecovec.SetPtEtaPhiM(mergedDuplicateTrack->pt(),mergedDuplicateTrack->eta(),mergedDuplicateTrack->phi(),0.0);
                double deltaR = tvec.DeltaR(trerecovec);
                if(deltaR < maxDr) ++numMergedDuplicateMatchedTracks;
              }

              int numSumAllIter = numInitStep + numHighPtTripStep + numJetCoreStep + numLowPtQuadStep + numLowPtTripStep + numDetQuadStep + numDetTripStep + numPixPairStep + numMixTripStep + numPixLesstep + numTobTecStep;

              int numSumAllMatchedIter = numInitStepMatched + numHighPtTripStepMatched + numJetCoreStepMatched + numLowPtQuadStepMatched + numLowPtTripStepMatched + numDetQuadStepMatched + numDetTripStepMatched + numPixPairStepMatched + numMixTripStepMatched + numPixLesstepMatched + numTobTecStepMatched;

              int numSumAllIterMuons = numSumAllIter + numMuInOutStep + numMuOutInStep;

              int numSumAllMatchedIterMuons = numSumAllMatchedIter + numMuInOutStepMatched + numMuOutInStepMatched;

              int numEarlyMuonsTracks = numEarlyTracks + numMuInOutStep + numMuOutInStep;

              int numEarlyMuonsMatchedTracks = numEarlyMatchedTracks + numMuInOutStepMatched + numMuOutInStepMatched;

              if(numSumAllIter > 0) trackEfficiencyCalc_->Fill(1.0);
              if(numSumAllMatchedIter > 0) trackEfficiencyCalc_->Fill(2.0);
              if(numSumAllIterMuons > 0) trackEfficiencyCalc_->Fill(3.0);
              if(numSumAllMatchedIterMuons > 0) trackEfficiencyCalc_->Fill(4.0);
              if(numEarlyTracks > 0) trackEfficiencyCalc_->Fill(5.0);
              if(numEarlyMatchedTracks > 0) trackEfficiencyCalc_->Fill(6.0);
              if(numEarlyMuonsTracks > 0) trackEfficiencyCalc_->Fill(7.0);
              if(numEarlyMuonsMatchedTracks > 0) trackEfficiencyCalc_->Fill(8.0);
              if(numPreDuplicateTracks > 0) trackEfficiencyCalc_->Fill(9.0);
              if(numPreDuplicateMatchedTracks > 0) trackEfficiencyCalc_->Fill(10.0);
              if(numMergedDuplicateTracks > 0) trackEfficiencyCalc_->Fill(11.0);
              if(numMergedDuplicateMatchedTracks > 0) trackEfficiencyCalc_->Fill(12.0);

              for (std::vector<reco::Track>::const_iterator track_rereco = tracks_rereco->begin(); track_rereco != tracks_rereco->end(); ++track_rereco) {

                ++numRerecoTracks;

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

                    if(hitsRemain_int == 7 && track_trackerLayersWithMeasurement < hitsRemain_int) outdata << iEvent.id() << std::endl;

                    reco::HitPattern hitpattern = track_rereco->hitPattern();

                    int lost = hitpattern.numberOfLostTrackerHits(reco::HitPattern::TRACK_HITS);
                    int lostIn = hitpattern.numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
                    int lostOut = hitpattern.numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);

                    trackMissInnAllPt_->Fill(lostIn);
                    trackMissMidAllPt_->Fill(lost);
                    trackMissOutAllPt_->Fill(lostOut);

                    int hitlost = hitpattern.numberOfLostHits(reco::HitPattern::TRACK_HITS);
                    int hitlostIn = hitpattern.numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS);
                    int hitlostOut = hitpattern.numberOfLostHits(reco::HitPattern::MISSING_OUTER_HITS);

                    //int lostSum = hitpattern.numberOfLostPixelHits(reco::HitPattern::TRACK_HITS) + hitpattern.numberOfLostStripHits(reco::HitPattern::TRACK_HITS);
                    //int lostInSum = hitpattern.numberOfLostPixelHits(reco::HitPattern::MISSING_INNER_HITS) + hitpattern.numberOfLostStripHits(reco::HitPattern::MISSING_INNER_HITS);
                    //int lostOutSum = hitpattern.numberOfLostPixelHits(reco::HitPattern::MISSING_OUTER_HITS) + hitpattern.numberOfLostStripHits(reco::HitPattern::MISSING_OUTER_HITS);

                    missInnAllPt_->Fill(hitlostIn);
                    missMidAllPt_->Fill(hitlost);
                    missOutAllPt_->Fill(hitlostOut);

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

              if(numRerecoTracks > 0) trackEfficiencyCalc_->Fill(13.0);
              if(numRerecoMatchedTracks > 0) trackEfficiencyCalc_->Fill(14.0);

            }

          }

        }

      //}

    }

    if(numTracks > 0) trackEfficiencyCalc_->Fill(0.0);

  //}

  outdata.close();
  //std::cout << numTracks << std::endl;

}
//void TrackingResolution::endLuminosityBlock(edm::LuminosityBlock const& lumiBlock, edm::EventSetup const& eSetup){}
// Define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackingResolution);
