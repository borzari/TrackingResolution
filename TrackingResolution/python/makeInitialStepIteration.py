import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackMVAClassifierPrompt_cfi import *
import RecoTracker.IterativeTracking.iterativeTkConfig as _cfg
from RecoTracker.TkHitPairs.hitPairEDProducer_cfi import hitPairEDProducer as _hitPairEDProducer
from RecoPixelVertexing.PixelTriplets.caHitTripletEDProducer_cfi import caHitTripletEDProducer as _caHitTripletEDProducer
import RecoTracker.TkSeedingLayers.PixelLayerTriplets_cfi as _PixelLayerTriplets_cfi
from RecoTracker.TkSeedGenerator.seedCreatorFromRegionConsecutiveHitsEDProducer_cff import seedCreatorFromRegionConsecutiveHitsEDProducer as _seedCreatorFromRegionConsecutiveHitsEDProducer
import RecoTracker.CkfPattern.CkfTrackCandidates_cfi as _CkfTrackCandidates_cfi
from RecoTracker.TkTrackingRegions.globalTrackingRegionFromBeamSpot_cfi import globalTrackingRegionFromBeamSpot as _globalTrackingRegionFromBeamSpot
import RecoTracker.TrackProducer.TrackProducer_cfi
from RecoPixelVertexing.PixelTriplets.caHitQuadrupletEDProducer_cfi import caHitQuadrupletEDProducer as _caHitQuadrupletEDProducer
import RecoTracker.TkSeedingLayers.PixelLayerQuadruplets_cfi
from RecoTracker.TkSeedGenerator.trackerClusterCheckDefault_cfi import trackerClusterCheckDefault as _trackerClusterCheckDefault
import RecoTracker.TkSeedingLayers.PixelLayerQuadruplets_cfi
from RecoPixelVertexing.PixelTriplets.pixelTripletHLTEDProducer_cfi import pixelTripletHLTEDProducer as _pixelTripletHLTEDProducer

def makeInitialStepIteration():

    hits = "3"
    myCollection = "rCluster"+hits

    ### Initial Step

    theTask = cms.Task()

    vars()["initialStepSeedLayers"+hits] = initialStepSeedLayers.clone(
        BPix = cms.PSet(
            HitProducer = cms.string('siPixelRecHits'+hits),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        FPix = cms.PSet(
            HitProducer = cms.string('siPixelRecHits'+hits),
            TTRHBuilder = cms.string('WithTrackAngle')
        )
    )
    theTask.add(vars()["initialStepSeedLayers"+hits])

    vars()["initialStepTrackingRegions"+hits] = initialStepTrackingRegions.clone()
    theTask.add(vars()["initialStepTrackingRegions"+hits])

    vars()["initialStepHitDoublets"+hits] = initialStepHitDoublets.clone(
        clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
        seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
        trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
    )
    theTask.add(vars()["initialStepHitDoublets"+hits])

    vars()["initialStepHitTriplets"+hits] = initialStepHitTriplets.clone(
        SeedComparitorPSet = cms.PSet(
            clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
        ),
        doublets = cms.InputTag("initialStepHitDoublets"+hits),
        mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
    )
    theTask.add(vars()["initialStepHitTriplets"+hits])

    vars()["initialStepHitQuadruplets"+hits] = initialStepHitQuadruplets.clone(
        SeedComparitorPSet = cms.PSet(
            clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
        ),
        doublets = cms.InputTag("initialStepHitDoublets"+hits),
        mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
    )
    theTask.add(vars()["initialStepHitQuadruplets"+hits])

    vars()["initialStepSeeds"+hits] = initialStepSeeds.clone(
        SeedComparitorPSet = cms.PSet(
            ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
        ),
        mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
        seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
    )
    theTask.add(vars()["initialStepSeeds"+hits])

    vars()["initialStepTrackCandidates"+hits] = initialStepTrackCandidates.clone(
        MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
        src = cms.InputTag("initialStepSeeds"+hits)
    )
    theTask.add(theTask.add(vars()["initialStepSeeds"+hits]))

    vars()["initialStepTracks"+hits] = initialStepTracks.clone(
        MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
        src = cms.InputTag("initialStepTrackCandidates"+hits)
    )
    theTask.add(vars()["initialStepTracks"+hits])

    vars()["initialStepTrackRefsForJets"+hits] = initialStepTrackRefsForJets.clone(
        src = cms.InputTag("initialStepTracks"+hits)
    )
    theTask.add(vars()["initialStepTrackRefsForJets"+hits])

    vars()["initialStep"+hits] = initialStep.clone(
        src = cms.InputTag("initialStepTracks"+hits),
        vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
    )
    theTask.add(vars()["initialStep"+hits])

    vars()["initialStepTask"+hits] = theTask.copy()

    return vars()["initialStepTask"+hits]
