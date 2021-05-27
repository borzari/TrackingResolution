// Original Author:  Viktor Gerhard Kutzner
//         Created:  Sun, 03 Jan 2021 19:15:47 GMT

#include <memory>
#include <stdio.h>
#include <stdlib.h>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackBase.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include <TLorentzVector.h>

class Breno_GoodRecoMuonsFilter : public edm::stream::EDFilter<> {
  public:
    explicit Breno_GoodRecoMuonsFilter(const edm::ParameterSet&);
    ~Breno_GoodRecoMuonsFilter();

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  private:
    virtual void beginStream(edm::StreamID) override;
    virtual bool filter(edm::Event&, const edm::EventSetup&) override;
    virtual void endStream() override;

    edm::EDGetTokenT<std::vector<reco::Muon>> muonsToken; 
    edm::EDGetTokenT<std::vector<reco::Track>> tracksToken;
    float minpt_;
    float maxabseta_;
};

Breno_GoodRecoMuonsFilter::Breno_GoodRecoMuonsFilter(const edm::ParameterSet& iConfig)
{
  muonsToken = consumes<std::vector<reco::Muon>>(iConfig.getParameter<edm::InputTag>("muonlabel"));
  tracksToken = consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("trackslabel"));
  minpt_     = iConfig.getParameter<double>("minPt");
  maxabseta_ = iConfig.getParameter<double>("maxAbsEta");
}

Breno_GoodRecoMuonsFilter::~Breno_GoodRecoMuonsFilter()
{
}

bool
Breno_GoodRecoMuonsFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;
  Handle<std::vector<reco::Muon>> muons;
  iEvent.getByToken( muonsToken, muons);
      
  Handle<reco::TrackCollection> tracks;
  iEvent.getByToken(tracksToken, tracks);
	
  bool result = false;
  for( const auto& muon : *muons){
    if ((muon.pt() > minpt_) && (abs(muon.eta()) < maxabseta_)) {
	   	   
      // track matching:
      for( const auto& track : *tracks){
        TLorentzVector pTrack (track.px(), track.py(), track.pz(), track.pt());
        TLorentzVector pMuon (muon.px(), muon.py(), muon.pz(), muon.pt());
        Double_t dr = pTrack.DeltaR(pMuon);
        if (dr<0.05) {
          reco::HitPattern hitpattern = track.hitPattern();
          if (hitpattern.trackerLayersWithMeasurement()>10) {
            result = true;
            break;
          }
        }
      }
    }
  }
   
  return result;
}

void
Breno_GoodRecoMuonsFilter::beginStream(edm::StreamID)
{
}

void
Breno_GoodRecoMuonsFilter::endStream() {
}

void
Breno_GoodRecoMuonsFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
DEFINE_FWK_MODULE(Breno_GoodRecoMuonsFilter);
