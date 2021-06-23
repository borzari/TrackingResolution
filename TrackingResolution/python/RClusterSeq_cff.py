import FWCore.ParameterSet.Config as cms

from TrackingResolution.TrackingResolution.RClusterProducer_cfi import (
    rCluster as rCluster,
)

goodMuons = cms.EDFilter(
    "GoodRecoMuonsFilter",
    trackslabel=cms.InputTag("generalTracks"),
    muonlabel=cms.InputTag("muons"),
    minPt=cms.double(15),
    maxAbsEta=cms.double(2.2),
    filter=cms.bool(True),
)

for suf in range(3, 9):
    moduleLabel = "rCluster" + str(suf)
    vars()[moduleLabel] = rCluster.clone(layersRemaining=cms.uint32(suf))

RClusterSeq = cms.Sequence(
    goodMuons
    + rCluster
    + rCluster8
    + rCluster7
    + rCluster6
    + rCluster5
    + rCluster4
    + rCluster3
)
