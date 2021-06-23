import FWCore.ParameterSet.Config as cms

from TrackingResolution.TrackingResolution.RClusterProducer_cfi import rCluster as rCluster

goodMuons = cms.EDFilter("GoodRecoMuonsFilter",
    trackslabel = cms.InputTag("generalTracks"),
    muonlabel = cms.InputTag("muons"),
    minPt = cms.double(15),
    maxAbsEta = cms.double(2.2),
    filter = cms.bool(True)
)

#rCluster20 = rCluster.clone()
#rCluster20.layersRemaining=cms.uint32(20)

#rCluster19 = rCluster.clone()
#rCluster19.layersRemaining=cms.uint32(19)

#rCluster18 = rCluster.clone()
#rCluster18.layersRemaining=cms.uint32(18)

#rCluster17 = rCluster.clone()
#rCluster17.layersRemaining=cms.uint32(17)

#rCluster16 = rCluster.clone()
#rCluster16.layersRemaining=cms.uint32(16)

#rCluster15 = rCluster.clone()
#rCluster15.layersRemaining=cms.uint32(15)

#rCluster14 = rCluster.clone()
#rCluster14.layersRemaining=cms.uint32(14)

#rCluster13 = rCluster.clone()
#rCluster13.layersRemaining=cms.uint32(13)

#rCluster12 = rCluster.clone()
#rCluster12.layersRemaining=cms.uint32(12)

#rCluster11 = rCluster.clone()
#rCluster11.layersRemaining=cms.uint32(11)

#rCluster10 = rCluster.clone()
#rCluster10.layersRemaining=cms.uint32(10)

#rCluster9 = rCluster.clone()
#rCluster9.layersRemaining=cms.uint32(9)

rCluster8 = rCluster.clone()
rCluster8.layersRemaining=cms.uint32(8)

rCluster7 = rCluster.clone()
rCluster7.layersRemaining=cms.uint32(7)

rCluster6 = rCluster.clone()
rCluster6.layersRemaining=cms.uint32(6)

rCluster5 = rCluster.clone()
rCluster5.layersRemaining=cms.uint32(5)

rCluster4 = rCluster.clone()
rCluster4.layersRemaining=cms.uint32(4)

rCluster3 = rCluster.clone()
rCluster3.layersRemaining=cms.uint32(3)

#rCluster2 = rCluster.clone()
#rCluster2.layersRemaining=cms.uint32(2)

#rCluster1 = rCluster.clone()
#rCluster1.layersRemaining=cms.uint32(1)

#rCluster0 = rCluster.clone()
#rCluster0.layersRemaining=cms.uint32(0)

RClusterSeq = cms.Sequence(goodMuons + rCluster + rCluster8 + rCluster7 + rCluster6 + rCluster5 + rCluster4 + rCluster3)
