import FWCore.ParameterSet.Config as cms

process = cms.Process("reRECO")

from TrackingResolution.TrackingResolution.RClusterProducer_cfi import (
    rCluster as rCluster,
)

RClusterTask = cms.Task()

RClusterTask.add(rCluster)

goodMuons = cms.EDFilter(
    "GoodRecoMuonsFilter",
    trackslabel=cms.InputTag("generalTracks"),
    muonlabel=cms.InputTag("muons"),
    minPt=cms.double(15),
    maxAbsEta=cms.double(2.2),
    maxDr=cms.double(0.01),
    minNumberOfLayers=cms.int32(10),
    filter=cms.bool(True),
)

for suf in range(3, 9):
    moduleLabel = "rCluster" + str(suf)
    vars()[moduleLabel] = rCluster.clone(layersRemaining=cms.uint32(suf))
    RClusterTask.add(vars()[moduleLabel])

RClusterSeq = cms.Sequence(goodMuons, RClusterTask)
