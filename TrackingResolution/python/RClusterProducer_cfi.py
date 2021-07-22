import FWCore.ParameterSet.Config as cms

# searches for muon tracks with sufficient number of hits and removes the corresponding
# cluster of all but N inner hits of that tracks.

rCluster = cms.EDProducer(
    "RClusterProducer",
    allTracks=cms.InputTag("generalTracks"),
    matchElectrons=cms.InputTag("gedGsfElectrons"),
    matchMuons=cms.InputTag("muons"),
    matchTo=cms.string("Muon"),
    requiredDr=cms.double(0.01),
    minNumberOfLayers=cms.int32(10),
    layersRemaining=cms.uint32(50),
    onlyValidHits=cms.bool(True),
    debug=cms.bool(False),
    selectedStripCluster=cms.InputTag("siStripClusters"),
    selectedPixelCluster=cms.InputTag("siPixelClusters"),
    PrimaryVertex=cms.InputTag("offlinePrimaryVertices"),
)
