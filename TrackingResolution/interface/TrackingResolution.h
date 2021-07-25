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

  void endLuminosityBlock(edm::LuminosityBlock const& lumiSeg, edm::EventSetup const& eSetup) override;
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
  const edm::EDGetTokenT<std::vector<reco::Muon>> muonsToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> tracksToken;
  const edm::EDGetTokenT<std::vector<reco::Vertex>> primVertexToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> tracksRerecoToken;

  MonitorElement* trackPixelLayers_;
  MonitorElement* trackTrackerLayers_;

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
