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

    initialStepSeedLayers = RecoTracker.TkSeedingLayers.PixelLayerQuadruplets_cfi.PixelLayerQuadruplets.clone(
        BPix = cms.PSet(
            HitProducer = cms.string('siPixelRecHits'),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        FPix = cms.PSet(
            HitProducer = cms.string('siPixelRecHits'),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        MTEC = cms.PSet(

        ),
        MTIB = cms.PSet(

        ),
        MTID = cms.PSet(

        ),
        MTOB = cms.PSet(

        ),
        TEC = cms.PSet(

        ),
        TIB = cms.PSet(

        ),
        TID = cms.PSet(

        ),
        TOB = cms.PSet(

        ),
        layerList = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4',
            'BPix1+BPix2+BPix3+FPix1_pos',
            'BPix1+BPix2+BPix3+FPix1_neg',
            'BPix1+BPix2+FPix1_pos+FPix2_pos',
            'BPix1+BPix2+FPix1_neg+FPix2_neg',
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
        )
    )

    initialStepTrackingRegions = _globalTrackingRegionFromBeamSpot.clone(
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            nSigmaZ = cms.double(4),
            originHalfLength = cms.double(0),
            originRadius = cms.double(0.02),
            precise = cms.bool(True),
            ptMin = cms.double(0.5),
            useMultipleScattering = cms.bool(False)
        )
    )

    initialStepHitDoublets = _hitPairEDProducer.clone(
        clusterCheck = cms.InputTag("trackerClusterCheck"),
        layerPairs = cms.vuint32(0, 1, 2),
        maxElement = cms.uint32(0),
        produceIntermediateHitDoublets = cms.bool(True),
        produceSeedingHitSets = cms.bool(False),
        seedingLayers = cms.InputTag("initialStepSeedLayers"),
        trackingRegions = cms.InputTag("initialStepTrackingRegions"),
        trackingRegionsSeedingLayers = cms.InputTag("")
    )

    initialStepHitTriplets = _pixelTripletHLTEDProducer.clone(
        SeedComparitorPSet = cms.PSet(
            ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
            clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
            clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
        ),
        doublets = cms.InputTag("initialStepHitDoublets"),
        extraHitRPhitolerance = cms.double(0.032),
        extraHitRZtolerance = cms.double(0.037),
        maxElement = cms.uint32(1000000),
        mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets__reRECO'),
        phiPreFiltering = cms.double(0.3),
        produceIntermediateHitTriplets = cms.bool(False),
        produceSeedingHitSets = cms.bool(True),
        useBending = cms.bool(True),
        useFixedPreFiltering = cms.bool(False),
        useMultScattering = cms.bool(True)
    )

    initialStepHitQuadruplets = _caHitQuadrupletEDProducer.clone(
        CAHardPtCut = cms.double(0),
        CAPhiCut = cms.double(0.2),
        CAThetaCut = cms.double(0.0012),
        SeedComparitorPSet = cms.PSet(
            ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
            clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
            clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
        ),
        doublets = cms.InputTag("initialStepHitDoublets"),
        extraHitRPhitolerance = cms.double(0.032),
        fitFastCircle = cms.bool(True),
        fitFastCircleChi2Cut = cms.bool(True),
        maxChi2 = cms.PSet(
            enabled = cms.bool(True),
            pt1 = cms.double(0.7),
            pt2 = cms.double(2),
            value1 = cms.double(200),
            value2 = cms.double(50)
        ),
        mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets__reRECO'),
        useBendingCorrection = cms.bool(True)
    )

    initialStepSeeds = _seedCreatorFromRegionConsecutiveHitsEDProducer.clone(
        MinOneOverPtError = cms.double(1),
        OriginTransverseErrorMultiplier = cms.double(1),
        SeedComparitorPSet = cms.PSet(
            ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
            ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
            ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
            FilterAtHelixStage = cms.bool(False),
            FilterPixelHits = cms.bool(True),
            FilterStripHits = cms.bool(False)
        ),
        SeedMomentumForBOFF = cms.double(5),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string('ParabolicMf'),
        mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets__reRECO'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf'),
        seedingHitSets = cms.InputTag("initialStepHitQuadruplets")
    )

    initialStepTrackCandidates = RecoTracker.CkfPattern.CkfTrackCandidates_cfi.ckfTrackCandidates.clone(
        MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
        NavigationSchool = cms.string('SimpleNavigationSchool'),
        RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
        SimpleMagneticField = cms.string(''),
        TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
        TrajectoryBuilderPSet = cms.PSet(
            refToPSet_ = cms.string('initialStepTrajectoryBuilder')
        ),
        TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
        TransientInitialStateEstimatorParameters = cms.PSet(
            numberMeasurementsForFit = cms.int32(4),
            propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
            propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
        ),
        cleanTrajectoryAfterInOut = cms.bool(True),
        doSeedingRegionRebuilding = cms.bool(True),
        maxNSeeds = cms.uint32(500000),
        maxSeedsBeforeCleaning = cms.uint32(5000),
        numHitsForSeedCleaner = cms.int32(50),
        onlyPixelHitsForSeedCleaner = cms.bool(True),
        reverseTrajectories = cms.bool(False),
        src = cms.InputTag("initialStepSeeds"),
        useHitsSplitting = cms.bool(True)
    )

    initialStepTracks = RecoTracker.TrackProducer.TrackProducer_cfi.TrackProducer.clone(
        AlgorithmName = cms.string('initialStep'),
        Fitter = cms.string('FlexibleKFFittingSmoother'),
        GeometricInnerState = cms.bool(False),
        MeasurementTracker = cms.string(''),
        MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
        NavigationSchool = cms.string('SimpleNavigationSchool'),
        Propagator = cms.string('RungeKuttaTrackerPropagator'),
        SimpleMagneticField = cms.string(''),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        TrajectoryInEvent = cms.bool(False),
        alias = cms.untracked.string('ctfWithMaterialTracks'),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        clusterRemovalInfo = cms.InputTag(""),
        src = cms.InputTag("initialStepTrackCandidates"),
        useHitsSplitting = cms.bool(False),
        useSimpleMF = cms.bool(False)
    )

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
    theTask.add(vars()["initialStepSeeds"+hits])

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
