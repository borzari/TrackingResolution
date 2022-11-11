//
// Original Author:  Alexandra Tews
//
// This producer makes a preselection of quality tracks.
// It then loops over the selected track collection
// and retrieves the Rechits for each track.
// RecHIts can be linked to clusters that are identified via the rawId
// and their position in the vector container DetSetVector<>.
// The output DetSetVector holds all but some selected cluster.
// The Number of hits (cluster) to remain for each quality track can be specified.
//
// Created: 13.07.17
//
//
//

#include <memory>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <TLorentzVector.h>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackBase.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/Common/interface/SortedCollection.h"
#include "DataFormats/Common/interface/OwnVector.h"
#include "DataFormats/Common/interface/ClonePolicy.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHit.h"
#include "DataFormats/HcalRecHit/interface/HBHERecHit.h"
#include "DataFormats/HcalRecHit/interface/HFRecHit.h"
#include "DataFormats/HcalRecHit/interface/HORecHit.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/TrackerRecHit2D/interface/BaseTrackerRecHit.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "Geometry/Records/interface/IdealGeometryRecord.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "FWCore/Framework/interface/global/EDProducer.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/SiPixelCluster/interface/SiPixelCluster.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2D.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Provenance/interface/ProductID.h"
#include "DataFormats/Common/interface/ContainerMask.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/TrackerRecHit2D/interface/ClusterRemovalInfo.h"
#include "TrackingTools/PatternTools/interface/TrackCollectionTokens.h"
#include "RecoTracker/TransientTrackingRecHit/interface/Traj2TrackHits.h"
#include<limits>

class RClusterProducerAlignment : public edm::stream::EDProducer<> {
   public:
      explicit RClusterProducerAlignment(const edm::ParameterSet&);
      ~RClusterProducerAlignment();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginStream(edm::StreamID) override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endStream() override;

      edm::EDGetTokenT<std::vector<reco::Track>> tracksToken;
      edm::EDGetTokenT<std::vector<reco::Muon>> muonsToken;
      edm::EDGetTokenT<edm::OwnVector<TrackingRecHit,edm::ClonePolicy<TrackingRecHit>>> generalTracksHitsToken;
      edm::EDGetTokenT<reco::VertexCollection> PrimVtxToken;

      int minNumberOfLayers;
      double_t matchInDr;
      bool onlyValidHits;
      bool debug;
      double maxDxy;
      double maxDz;

};

RClusterProducerAlignment::RClusterProducerAlignment(const edm::ParameterSet& iConfig)
{

   produces<reco::TrackCollection>("").setBranchAlias("");

   tracksToken = consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("allTracks"));
   muonsToken = consumes<std::vector<reco::Muon>>(iConfig.getParameter<edm::InputTag>("matchMuons"));
   PrimVtxToken = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("PrimaryVertex"));

   minNumberOfLayers = iConfig.getParameter<int>("minNumberOfLayers");
   matchInDr = iConfig.getParameter<double_t>("requiredDr");
   onlyValidHits = iConfig.getParameter<bool>("onlyValidHits");
   debug = iConfig.getParameter<bool>("debug");
   maxDxy = iConfig.getParameter<double_t>("maxDxy");
   maxDz = iConfig.getParameter<double_t>("maxDz");
}


RClusterProducerAlignment::~RClusterProducerAlignment()
{}

void
RClusterProducerAlignment::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  // register input collections:

  Handle<reco::TrackCollection> tracks;
  iEvent.getByToken(tracksToken, tracks);

  Handle<std::vector<reco::Muon>> muons;
  iEvent.getByToken( muonsToken, muons);

  Handle<reco::VertexCollection> vtx_h;
  iEvent.getByToken(PrimVtxToken, vtx_h);
  const reco::Vertex vtx = vtx_h->at(0);

  // register output collection:
  std::unique_ptr <reco::TrackCollection> goodTracks(new reco::TrackCollection);

  // Preselection of long quality tracks

  std::vector<reco::Track> selTracks;
  reco::Track bestTrack;
  unsigned int tMuon = 0;
  Double_t fitProb = 100;
  unsigned int candidates = 0;

  int ntracks = 0;

  for( const auto& track : *tracks){

    ntracks = ntracks + 1;

    reco::HitPattern hitpattern = track.hitPattern();
    bool passedMinNumberLayers = false;
    bool isMatched = false;
    Double_t dRmin = 10;
    Double_t chiNdof = track.normalizedChi2();
    Double_t dxy = std::abs(track.dxy(vtx.position()));
    Double_t dz = std::abs(track.dz(vtx.position()));

    if (hitpattern.trackerLayersWithMeasurement() >= minNumberOfLayers) passedMinNumberLayers = true;

    TLorentzVector pTrack (track.px(), track.py(), track.pz(), track.pt());

    // Long track needs to be close to a good muon

    for( const auto& m : *muons){
      if (m.isTrackerMuon()){
        tMuon++;
        reco::Track matchedTrack = *(m.innerTrack());
        TLorentzVector pMatched (matchedTrack.px(), matchedTrack.py(),matchedTrack.pz(), matchedTrack.pt());
        // match to general track in deltaR
        Double_t dr = pTrack.DeltaR(pMatched);
        if (dr < dRmin) dRmin = dr;
      }
    }

    if (dRmin<matchInDr) isMatched = true;
    // do vertex consistency:
    bool vertex_match = dxy < maxDxy && dz < maxDz;
    if (!(vertex_match)) continue;
    if (track.validFraction()<1.0) continue;
    if (passedMinNumberLayers && isMatched){
      candidates ++;
      // only save the track with the smallest chiNdof
      if (chiNdof < fitProb){
        fitProb = chiNdof;
        bestTrack = track;
        bestTrack.setExtra(track.extra());
      }
      if(debug) std::cout << " deltaR (general) track to matched Track: " << dRmin << std::endl;
      if(debug) std::cout << "chi2Ndof:" << chiNdof << " best Track: " << fitProb << std::endl;
    }
  }

  selTracks.push_back(bestTrack);

  //std::cout << layersRemaining << " hits: Event " << iEvent.id() << " has " << ntracks << " tracks." << std::endl;
  if (debug) std::cout << " number of Tracker Muons: " << tMuon << ", thereof " << selTracks.size() << " tracks passed preselection." << std::endl;

  // shorten preselected tracks
  bool hitIsNotValid = false;

  int tracksCounter = 0;
  for( const auto& track : selTracks){

    reco::HitPattern hitpattern = track.hitPattern();
    int notValidLayers = 0;
    tracksCounter ++;
    int deref = 0;

    try{ // (Un)Comment this line with /* to (not) allow for events with not valid hits
      auto hb = track.recHitsBegin();

      for(unsigned int h=0;h<track.recHitsSize();h++){

        auto recHit = *(hb+h);
        auto const & hit = *recHit;

        if (onlyValidHits && !hit.isValid()){
          hitIsNotValid = true;
          continue;
        }
      }
    }
    catch(...){
      if(debug) deref = deref + 1;//std::cout << "de-referenced track extra" << std::endl;
    }

    if(hitIsNotValid==true) break; // (Un)Comment this line with */ to (not) allow for events with not valid hits

    int deref2 = 0;

    try{
      auto hb = track.recHitsBegin();

      for(unsigned int h=0;h<track.recHitsSize();h++){

        uint32_t pHit = hitpattern.getHitPattern(reco::HitPattern::TRACK_HITS, h);

        auto recHit = *(hb+h);
        auto const & hit = *recHit;

        if (onlyValidHits && !hit.isValid()){
          if(debug) std::cout<< "hit not valid: " << h <<std::endl;
          ++notValidLayers; // Comment this line to not skip the not valid hits in tracks -> will reconstruct many tracks with less layers than layersRemaining
          continue;
        }

        // loop over the hits of the track.
        if (onlyValidHits && !(hitpattern.validHitFilter(pHit))){
          if(debug) std::cout<< "hit not valid: " << h <<std::endl;
          continue;
        }

      }
      goodTracks->push_back(track);
    }
    catch(...){
      deref2 = deref2 + 1;//std::cout << "de-referenced track extra" << std::endl;
    }
  }

  // save track collection in event and remaining pixel/strip clusters:
  iEvent.put(std::move(goodTracks), "");

  //if(layersRemaining == 8) std::cout << "====================================================================================" << std::endl;

}

void
RClusterProducerAlignment::beginStream(edm::StreamID)
{}

void
RClusterProducerAlignment::endStream() {
}


void
RClusterProducerAlignment::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(RClusterProducerAlignment);
