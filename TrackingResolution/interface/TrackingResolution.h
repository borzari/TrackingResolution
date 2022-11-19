#ifndef TrackingResolution_h
#define TrackingResolution_h

#include <string>
#include <vector>
#include <map>
#include <set>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

class TrackingResolution : public DQMEDAnalyzer {
public:
  TrackingResolution( const edm::ParameterSet& );

protected:

//  void endLuminosityBlock(edm::LuminosityBlock const& lumiSeg, edm::EventSetup const& eSetup) override;
  void analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) override;
  void bookHistograms(DQMStore::IBooker &, edm::Run const &, edm::EventSetup const &) override;

private:

  edm::ParameterSet parameters_;

  std::string moduleName_;
  std::string folderName_;

  std::string hitsRemain;

  double minTracksEta;
  double maxTracksEta;
  double minTracksPt;
  double maxTracksPt;

  double lowPtRegion;
  double medPtRegion;
  double higPtRegion;

  double maxDxy;
  double maxDz;
  double maxDr;
  double minNumberOfLayers;

  const edm::InputTag muonsTag;
  const edm::InputTag tracksTag;
  const edm::InputTag primVertexTag;
  const edm::InputTag tracksRerecoTag;
  const edm::InputTag initialStepRerecoTag;
  const edm::InputTag highPtTripletStepRerecoTag;
  const edm::InputTag jetCoreRegionalStepRerecoTag;
  const edm::InputTag lowPtQuadStepRerecoTag;
  const edm::InputTag lowPtTripletStepRerecoTag;
  const edm::InputTag detachedQuadStepRerecoTag;
  const edm::InputTag detachedTripletStepRerecoTag;
  const edm::InputTag pixelPairStepRerecoTag;
  const edm::InputTag mixedTripletStepRerecoTag;
  const edm::InputTag pixelLessStepRerecoTag;
  const edm::InputTag tobTecStepRerecoTag;
  const edm::InputTag muonSeededTracksInOutRerecoTag;
  const edm::InputTag muonSeededTracksOutInRerecoTag;
  const edm::InputTag earlyGeneralTracksRerecoTag;
  const edm::InputTag preDuplicateMergingGeneralTracksRerecoTag;
  const edm::InputTag mergedDuplicateTracksRerecoTag;
  const edm::EDGetTokenT<std::vector<reco::Muon>> muonsToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> tracksToken;
  const edm::EDGetTokenT<std::vector<reco::Vertex>> primVertexToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> tracksRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> initialStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> highPtTripletStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> jetCoreRegionalStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> lowPtQuadStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> lowPtTripletStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> detachedQuadStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> detachedTripletStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> pixelPairStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> mixedTripletStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> pixelLessStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> tobTecStepRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> muonSeededTracksInOutRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> muonSeededTracksOutInRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> earlyGeneralTracksRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> preDuplicateMergingGeneralTracksRerecoToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> mergedDuplicateTracksRerecoToken;

  MonitorElement* trackPixelLayers_;
  MonitorElement* trackTrackerLayers_;
  MonitorElement* trackEfficiencyCalc_;

  MonitorElement* trackMissInnAllPt_;
  MonitorElement* trackMissMidAllPt_;
  MonitorElement* trackMissOutAllPt_;

  MonitorElement* missInnAllPt_;
  MonitorElement* missMidAllPt_;
  MonitorElement* missOutAllPt_;

  MonitorElement* trackPtAllPt_;
  MonitorElement* trackPtLowPt_;
  MonitorElement* trackPtMedPt_;
  MonitorElement* trackPtHigPt_;

  MonitorElement* trackChi2ndofAllPt_;
  MonitorElement* trackChi2ndofLowPt_;
  MonitorElement* trackChi2ndofMedPt_;
  MonitorElement* trackChi2ndofHigPt_;

};
#endif
