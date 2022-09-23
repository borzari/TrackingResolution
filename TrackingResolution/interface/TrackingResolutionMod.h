#ifndef TrackingResolutionMod_h
#define TrackingResolutionMod_h

#include <string>
#include <vector>
#include <map>
#include <set>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
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

#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2DCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2DCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/Phase2TrackerRecHit1D.h"

class TrackingResolutionMod : public DQMEDAnalyzer {
public:
  TrackingResolutionMod( const edm::ParameterSet& );

protected:

//  void endLuminosityBlock(edm::LuminosityBlock const& lumiSeg, edm::EventSetup const& eSetup) override;
  void analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) override;
  void bookHistograms(DQMStore::IBooker &, edm::Run const &, edm::EventSetup const &) override;

private:

  edm::ParameterSet parameters_;
  TrackerHitAssociator::Config trackerHitAssociatorConfig_;
  bool checkType_;
  int genType_;
  edm::EventNumber_t evt;

  float rechitx;     // x position of hit
  float rechity;     // y position of hit

  float rechitresx;   // difference between reconstructed hit x position and 'true' x position
  float rechitresy;   // difference between reconstructed hit y position and 'true' y position
  float rechitpullx;  // x residual divideded by error
  float rechitpully;  // y residual divideded by error

  float simhitx;  // true x position of hit
  float simhity;  // true y position of hit

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
  const edm::InputTag siPixelRecHitsTag;
  const edm::EDGetTokenT<std::vector<reco::Muon>> muonsToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> tracksToken;
  const edm::EDGetTokenT<std::vector<reco::Vertex>> primVertexToken;
  const edm::EDGetTokenT<std::vector<reco::Track>> tracksRerecoToken;
  const edm::EDGetTokenT<edmNew::DetSetVector<SiPixelRecHit>> siPixelRecHitsToken;

  MonitorElement* allTracksTrackerLayers_;
  MonitorElement* trackPixelLayers_;
  MonitorElement* trackTrackerLayers_;
  MonitorElement* trackTrackerLayersMiss_;
  MonitorElement* trackEfficiencyCalc_;
  MonitorElement* trackHitResidual_;
  MonitorElement* shortTrackHitResidual_;
  MonitorElement* longTrackHitResidual_;
  MonitorElement* longGoodTrackHitResidual_;
  MonitorElement* trackDeltaRAllPt_;

  MonitorElement* trackMissInnAllPt_;
  MonitorElement* trackMissMidAllPt_;
  MonitorElement* trackMissOutAllPt_;

  MonitorElement* trackPtAllPt_;
  MonitorElement* trackPtLowPt_;
  MonitorElement* trackPtMedPt_;
  MonitorElement* trackPtHigPt_;

  MonitorElement* trackPtBarrel_;
  MonitorElement* trackPtBarend_;
  MonitorElement* trackPtEndcap_;

  MonitorElement* trackChi2ndofAllPt_;
  MonitorElement* trackChi2ndofLowPt_;
  MonitorElement* trackChi2ndofMedPt_;
  MonitorElement* trackChi2ndofHigPt_;

  MonitorElement* trackAlgo_;
  MonitorElement* trackAlgoOnlyMiss_;
  MonitorElement* trackOriginalAlgo_;
  MonitorElement* trackOriginalAlgoOnlyMiss_;

};
#endif
