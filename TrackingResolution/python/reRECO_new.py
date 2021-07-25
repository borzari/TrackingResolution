import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import multiprocessing
import glob

options = VarParsing ('analysis')

options.register ('outputFileName',
                                  '',
                                  VarParsing.multiplicity.singleton,
                                  VarParsing.varType.string,
                                  "Output file for edmFile")
options.register ('skipEvents',
                                  0,
                                  VarParsing.multiplicity.singleton,
                                  VarParsing.varType.int,
                                  "skipEvents")
options.parseArguments()

# TODO: add rCluster to output to keep
myCollection = "rCluster3"
if myCollection == "rClusterAll":
        myCollection = "rCluster"
process = cms.Process("reRECO")

if "*" in options.inputFiles[0]:
    filenames = glob.glob(options.inputFiles[0].replace("file://", ""))
    for i in range(len(filenames)):
        filenames[i] = "file://" + filenames[i]
    options.inputFiles = filenames

    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(filenames),
        secondaryFileNames = cms.untracked.vstring()
    )
else:
    process.source = cms.Source("PoolSource",
        skipEvents=cms.untracked.uint32(options.skipEvents),
        fileNames = cms.untracked.vstring(options.inputFiles),
        secondaryFileNames = cms.untracked.vstring()
    )

import RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi as _GroupedCkfTrajectoryBuilder_cfi
process.highPtTripletStepTrajectoryBuilder = _GroupedCkfTrajectoryBuilder_cfi.GroupedCkfTrajectoryBuilder.clone(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('highPtTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

import RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi
process.CkfBaseTrajectoryFilter_block = RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi.CkfBaseTrajectoryFilter_block.clone(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

import TrackingTools.TrajectoryFiltering.TrajectoryFilter_cff as _TrajectoryFilter_cff

process.highPtTripletStepTrajectoryFilter = _TrajectoryFilter_cff.CompositeTrajectoryFilter_block.clone(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryFilterBase')
    ))
)

_highPtTripletStepTrajectoryFilterBase = _TrajectoryFilter_cff.CkfBaseTrajectoryFilter_block.clone(
    minimumNumberOfHits = 3,
    minPt               = 0.2,
)
process.highPtTripletStepTrajectoryFilterBase = _highPtTripletStepTrajectoryFilterBase.clone(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.lowPtTripletStepTrajectoryBuilder = RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi.GroupedCkfTrajectoryBuilder.clone(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('lowPtTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('lowPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

from RecoPixelVertexing.PixelLowPtUtilities.ClusterShapeTrajectoryFilter_cfi import *
# Composite filter
process.lowPtTripletStepTrajectoryFilter = _TrajectoryFilter_cff.CompositeTrajectoryFilter_block.clone(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('lowPtTripletStepStandardTrajectoryFilter')
    ))
)

import TrackingTools.TrajectoryFiltering.TrajectoryFilter_cff as _TrajectoryFilter_cff
_lowPtTripletStepStandardTrajectoryFilterBase = _TrajectoryFilter_cff.CkfBaseTrajectoryFilter_block.clone(
    minimumNumberOfHits = 3,
    minPt               = 0.075,
)

process.lowPtTripletStepStandardTrajectoryFilter = _lowPtTripletStepStandardTrajectoryFilterBase.clone(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.SiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.SiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.SiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.SiStripClusterChargeCutTiny = cms.PSet(
    value = cms.double(800.0)
)

import RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi
process.lowPtQuadStepTrajectoryBuilder = RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi.GroupedCkfTrajectoryBuilder.clone(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('lowPtQuadStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('lowPtQuadStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

import TrackingTools.TrajectoryFiltering.TrajectoryFilter_cff as _TrajectoryFilter_cff
_lowPtQuadStepTrajectoryFilterBase = _TrajectoryFilter_cff.CkfBaseTrajectoryFilter_block.clone(
    minimumNumberOfHits = 3,
    minPt               = 0.075,
)
process.lowPtQuadStepTrajectoryFilterBase = _lowPtQuadStepTrajectoryFilterBase.clone(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

from RecoPixelVertexing.PixelLowPtUtilities.ClusterShapeTrajectoryFilter_cfi import *
# Composite filter
process.lowPtQuadStepTrajectoryFilter = _TrajectoryFilter_cff.CompositeTrajectoryFilter_block.clone(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('lowPtQuadStepTrajectoryFilterBase')
    ))
)

import TrackingTools.TrajectoryFiltering.TrajectoryFilter_cff
_initialStepTrajectoryFilterBase = TrackingTools.TrajectoryFiltering.TrajectoryFilter_cff.CkfBaseTrajectoryFilter_block.clone(
    minimumNumberOfHits = 3,
    minPt               = 0.2,
)
process.initialStepTrajectoryFilterBase = _initialStepTrajectoryFilterBase.clone(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

import RecoPixelVertexing.PixelLowPtUtilities.StripSubClusterShapeTrajectoryFilter_cfi
process.initialStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryFilterBase')
    ))
)

import RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi
process.initialStepTrajectoryBuilder = RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi.GroupedCkfTrajectoryBuilder.clone(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('initialStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

###################################################################################

process.chargeCut2069Clusters = cms.EDProducer("ClusterChargeMasker",
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

from RecoTracker.FinalTrackSelectors.TrackMVAClassifierPrompt_cfi import *
process.highPtTripletStep = TrackMVAClassifierPrompt.clone(
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorHighPtTripletStep_Phase1')
    ),
    qualityCuts = cms.vdouble(0.2, 0.3, 0.4),
    src = cms.InputTag("highPtTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)

import RecoTracker.IterativeTracking.iterativeTkConfig as _cfg
highPtTripletStepClustersAux = _cfg.clusterRemoverForIter('HighPtTripletStep')
process.highPtTripletStepClusters = highPtTripletStepClustersAux.clone(
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtQuadStep","QualityMasks"),
    trajectories = cms.InputTag("lowPtQuadStepTracks")
)

from RecoTracker.TkHitPairs.hitPairEDProducer_cfi import hitPairEDProducer as _hitPairEDProducer

process.highPtTripletStepHitDoublets = _hitPairEDProducer.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)

from RecoPixelVertexing.PixelTriplets.caHitTripletEDProducer_cfi import caHitTripletEDProducer as _caHitTripletEDProducer

process.highPtTripletStepHitTriplets = _caHitTripletEDProducer.clone(
    CAHardPtCut = cms.double(0.3),
    CAPhiCut = cms.double(0.07),
    CAThetaCut = cms.double(0.004),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8),
        value1 = cms.double(100),
        value2 = cms.double(6)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets__reRECO'),
    useBendingCorrection = cms.bool(True)
)

import RecoTracker.TkSeedingLayers.PixelLayerTriplets_cfi as _PixelLayerTriplets_cfi

process.highPtTripletStepSeedLayers = _PixelLayerTriplets_cfi.PixelLayerTriplets.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters")
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
        'BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix1+BPix3+FPix1_pos',
        'BPix1+BPix3+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'BPix1+BPix2+FPix2_pos',
        'BPix1+BPix2+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix2_neg+FPix3_neg',
        'BPix1+FPix1_pos+FPix3_pos',
        'BPix1+FPix1_neg+FPix3_neg'
    )
)

from RecoTracker.TkSeedGenerator.seedCreatorFromRegionConsecutiveHitsEDProducer_cff import seedCreatorFromRegionConsecutiveHitsEDProducer as _seedCreatorFromRegionConsecutiveHitsEDProducer

process.highPtTripletStepSeeds = _seedCreatorFromRegionConsecutiveHitsEDProducer.clone(
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets__reRECO'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets")
)

import RecoTracker.CkfPattern.CkfTrackCandidates_cfi as _CkfTrackCandidates_cfi

process.highPtTripletStepTrackCandidates = _CkfTrackCandidates_cfi.ckfTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("highPtTripletStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("highPtTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)

from RecoTracker.TkTrackingRegions.globalTrackingRegionFromBeamSpot_cfi import globalTrackingRegionFromBeamSpot as _globalTrackingRegionFromBeamSpot

process.highPtTripletStepTrackingRegions = _globalTrackingRegionFromBeamSpot.clone(
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.55),
        useMultipleScattering = cms.bool(False)
    )
)

import RecoTracker.TrackProducer.TrackProducer_cfi
process.highPtTripletStepTracks = RecoTracker.TrackProducer.TrackProducer_cfi.TrackProducer.clone(
    AlgorithmName = cms.string('highPtTripletStep'),
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
    src = cms.InputTag("highPtTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)

process.lowPtQuadStep = TrackMVAClassifierPrompt.clone(
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorLowPtQuadStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.7, -0.35, -0.15),
    src = cms.InputTag("lowPtQuadStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)

lowPtQuadStepClustersAux = _cfg.clusterRemoverForIter('LowPtQuadStep')
process.lowPtQuadStepClusters = lowPtQuadStepClustersAux.clone(
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("initialStep","QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks")
)

process.lowPtQuadStepHitDoublets = _hitPairEDProducer.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)

from RecoPixelVertexing.PixelTriplets.caHitQuadrupletEDProducer_cfi import caHitQuadrupletEDProducer as _caHitQuadrupletEDProducer

process.lowPtQuadStepHitQuadruplets = _caHitQuadrupletEDProducer.clone(
    CAHardPtCut = cms.double(0),
    CAPhiCut = cms.double(0.3),
    CAThetaCut = cms.double(0.0017),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("lowPtQuadStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2),
        value1 = cms.double(1000),
        value2 = cms.double(150)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets__reRECO'),
    useBendingCorrection = cms.bool(True)
)

import RecoTracker.TkSeedingLayers.PixelLayerQuadruplets_cfi
process.lowPtQuadStepSeedLayers = RecoTracker.TkSeedingLayers.PixelLayerQuadruplets_cfi.PixelLayerQuadruplets.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters")
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

process.lowPtQuadStepSeeds = _seedCreatorFromRegionConsecutiveHitsEDProducer.clone(
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets__reRECO'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets")
)

process.lowPtQuadStepTrackCandidates = RecoTracker.CkfPattern.CkfTrackCandidates_cfi.ckfTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('lowPtQuadStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('lowPtQuadStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("lowPtQuadStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("lowPtQuadStepSeeds"),
    useHitsSplitting = cms.bool(True)
)

process.lowPtQuadStepTrackingRegions = _globalTrackingRegionFromBeamSpot.clone(
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.15),
        useMultipleScattering = cms.bool(False)
    )
)

process.lowPtQuadStepTracks = RecoTracker.TrackProducer.TrackProducer_cfi.TrackProducer.clone(
    AlgorithmName = cms.string('lowPtQuadStep'),
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
    src = cms.InputTag("lowPtQuadStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)

process.lowPtTripletStep =  TrackMVAClassifierPrompt.clone(
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorLowPtTripletStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.4, 0.0, 0.3),
    src = cms.InputTag("lowPtTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)

lowPtTripletStepClustersAux = _cfg.clusterRemoverForIter('LowPtTripletStep')
process.lowPtTripletStepClusters = lowPtTripletStepClustersAux.clone(
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("highPtTripletStep","QualityMasks"),
    trajectories = cms.InputTag("highPtTripletStepTracks")
)

process.lowPtTripletStepHitDoublets = _hitPairEDProducer.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)

process.lowPtTripletStepHitTriplets = _caHitTripletEDProducer.clone(
    CAHardPtCut = cms.double(0),
    CAPhiCut = cms.double(0.05),
    CAThetaCut = cms.double(0.002),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("lowPtTripletStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(2),
        value1 = cms.double(70),
        value2 = cms.double(8)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets__reRECO'),
    useBendingCorrection = cms.bool(True)
)

process.lowPtTripletStepSeedLayers = RecoTracker.TkSeedingLayers.PixelLayerTriplets_cfi.PixelLayerTriplets.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters")
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
        'BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix1+BPix3+FPix1_pos',
        'BPix1+BPix3+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'BPix1+BPix2+FPix2_pos',
        'BPix1+BPix2+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix2_neg+FPix3_neg',
        'BPix1+FPix1_pos+FPix3_pos',
        'BPix1+FPix1_neg+FPix3_neg'
    )
)

process.lowPtTripletStepSeeds = _seedCreatorFromRegionConsecutiveHitsEDProducer.clone(
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets__reRECO'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets")
)

process.lowPtTripletStepTrackCandidates = RecoTracker.CkfPattern.CkfTrackCandidates_cfi.ckfTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('lowPtTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('lowPtTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("lowPtTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)

process.lowPtTripletStepTrackingRegions = _globalTrackingRegionFromBeamSpot.clone(
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.2),
        useMultipleScattering = cms.bool(False)
    )
)

process.lowPtTripletStepTracks = RecoTracker.TrackProducer.TrackProducer_cfi.TrackProducer.clone(
    AlgorithmName = cms.string('lowPtTripletStep'),
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
    src = cms.InputTag("lowPtTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)

################################################################################################
process.firstStepGoodPrimaryVertices = cms.EDFilter("PrimaryVertexObjectFilter",
    filterParams = cms.PSet(
        maxRho = cms.double(2.0),
        maxZ = cms.double(15.0),
        minNdof = cms.double(25.0)
    ),
    src = cms.InputTag("firstStepPrimaryVertices")
)
################################################################################################

from CommonTools.RecoAlgos.sortedPrimaryVertices_cfi import sortedPrimaryVertices as _sortedPrimaryVertices
process.firstStepPrimaryVertices = _sortedPrimaryVertices.clone(
    assignment = cms.PSet(
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False)
    ),
    jets = cms.InputTag("ak4CaloJetsForTrk"),
    particles = cms.InputTag("initialStepTrackRefsForJets"),
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted")
)

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import offlinePrimaryVertices as _offlinePrimaryVertices
process.firstStepPrimaryVerticesUnsorted = _offlinePrimaryVertices.clone(
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(2.4),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("initialStepTracks"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
)

from RecoTracker.TkSeedGenerator.trackerClusterCheckDefault_cfi import trackerClusterCheckDefault as _trackerClusterCheckDefault
process.trackerClusterCheck = _trackerClusterCheckDefault.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    MaxNumberOfCosmicClusters = cms.uint32(400000),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClustersPreSplitting"),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    doClusterCheck = cms.bool(False),
    silentClusterCheck = cms.untracked.bool(False)
)

process.initialStep = TrackMVAClassifierPrompt.clone(
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorInitialStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.95, -0.85, -0.75),
    src = cms.InputTag("initialStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)

import RecoTracker.TkSeedingLayers.PixelLayerQuadruplets_cfi
process.initialStepSeedLayers = RecoTracker.TkSeedingLayers.PixelLayerQuadruplets_cfi.PixelLayerQuadruplets.clone(
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

process.initialStepTrackingRegions = _globalTrackingRegionFromBeamSpot.clone(
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

process.initialStepHitDoublets = _hitPairEDProducer.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("initialStepSeedLayers"),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)

from RecoPixelVertexing.PixelTriplets.pixelTripletHLTEDProducer_cfi import pixelTripletHLTEDProducer as _pixelTripletHLTEDProducer
process.initialStepHitTriplets = _pixelTripletHLTEDProducer.clone(
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

process.initialStepHitQuadruplets = _caHitQuadrupletEDProducer.clone(
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

process.initialStepSeeds = _seedCreatorFromRegionConsecutiveHitsEDProducer.clone(
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

process.initialStepTrackCandidates = RecoTracker.CkfPattern.CkfTrackCandidates_cfi.ckfTrackCandidates.clone(
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

process.initialStepTracks = RecoTracker.TrackProducer.TrackProducer_cfi.TrackProducer.clone(
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

from RecoJets.JetProducers.TracksForJets_cff import trackRefsForJets
process.initialStepTrackRefsForJets = trackRefsForJets.clone(
    particleType = cms.string('pi+'),
    src = cms.InputTag("initialStepTracks")
)

from RecoLocalCalo.CaloTowersCreator.calotowermaker_cfi import calotowermaker
process.caloTowerForTrk = calotowermaker.clone(
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring(
        'kTime',
        'kWeird',
        'kBad'
    ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HBThreshold = cms.double(0.7),
    HBThreshold1 = cms.double(0.7),
    HBThreshold2 = cms.double(0.7),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HEDThreshold = cms.double(0.2),
    HEDThreshold1 = cms.double(0.1),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HESThreshold = cms.double(0.2),
    HESThreshold1 = cms.double(0.1),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalPhase = cms.int32(1),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(True),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseSymEBTreshold = cms.bool(True),
    UseSymEETreshold = cms.bool(True),
    ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    hbheInput = cms.InputTag("hbheprereco"),
    hfInput = cms.InputTag("hfreco"),
    hoInput = cms.InputTag("horeco"),
    missingHcalRescaleFactorForEcal = cms.double(0)
)


from RecoJets.JetProducers.ak4CaloJets_cfi import ak4CaloJets as _ak4CaloJets
process.ak4CaloJetsForTrk = _ak4CaloJets.clone(
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("caloTowerForTrk"),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)

##############################################################################################################
process.jetsForCoreTracking = cms.EDFilter("CandPtrSelector",
    cut = cms.string('pt > 100 && abs(eta) < 2.5'),
    src = cms.InputTag("ak4CaloJetsForTrk")
)

process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag(myCollection)
)
##############################################################################################################

from RecoTracker.MeasurementDet.measurementTrackerEventDefault_cfi import measurementTrackerEventDefault as _measurementTrackerEventDefault
process.MeasurementTrackerEvent = _measurementTrackerEventDefault.clone(
    Phase2TrackerCluster1DProducer = cms.string(''),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
    inactivePixelDetectorLabels = cms.VInputTag("siPixelDigis"),
    inactiveStripDetectorLabels = cms.VInputTag("siStripDigis"),
    measurementTracker = cms.string(''),
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string(myCollection),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string(myCollection),
    switchOffPixelsIfEmpty = cms.bool(True)
)

process.siPixelClusterShapeCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag(myCollection)
)

from RecoTracker.FinalTrackSelectors.TrackCollectionMerger_cfi import *

process.earlyGeneralTracks =  TrackCollectionMerger.clone(
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    enableMerging = cms.bool(True),
    foundHitBonus = cms.double(10),
    inputClassifiers = cms.vstring(
        'initialStep',
        'highPtTripletStep',
#        'jetCoreRegionalStep', 
        'lowPtQuadStep',
        'lowPtTripletStep'#, 
#        'detachedQuadStep', 
#        'detachedTripletStep', 
#        'pixelPairStep', 
#        'mixedTripletStep', 
#        'pixelLessStep', 
#        'tobTecStep'
    ),
    lostHitPenalty = cms.double(5),
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag(
        "initialStepTracks", "highPtTripletStepTracks", "lowPtQuadStepTracks", "lowPtTripletStepTracks"#, "jetCoreRegionalStepTracks", 
        #"mixedTripletStepTracks", "pixelPairStepTracks", "detachedQuadStepTracks", "detachedTripletStepTracks", "pixelLessStepTracks", 
#        "tobTecStepTracks"
    )
)

process.preDuplicateMergingGeneralTracks = TrackCollectionMerger.clone(
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    enableMerging = cms.bool(True),
    foundHitBonus = cms.double(100.0),
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'
#        'muonSeededTracksInOutClassifier', 
#        'muonSeededTracksOutInClassifier'
    ),
    lostHitPenalty = cms.double(1.0),
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag("earlyGeneralTracks")#, "muonSeededTracksInOut", "muonSeededTracksOutIn")
)

from RecoTracker.FinalTrackSelectors.DuplicateTrackMerger_cfi import *
process.duplicateTrackCandidates = DuplicateTrackMerger.clone(
    GBRForestFileName = cms.string(''),
    chi2EstimatorName = cms.string('duplicateTrackCandidatesChi2Est'),
    forestLabel = cms.string('MVADuplicate'),
    maxDCA = cms.double(30),
    maxDLambda = cms.double(0.3),
    maxDPhi = cms.double(0.3),
    maxDQoP = cms.double(0.25),
    maxDdsz = cms.double(10),
    maxDdxy = cms.double(10),
    minBDTG = cms.double(-0.1),
    minDeltaR3d = cms.double(-4),
    minP = cms.double(0.4),
    minpT = cms.double(0.2),
    overlapCheckMaxHits = cms.uint32(4),
    overlapCheckMaxMissingLayers = cms.uint32(1),
    overlapCheckMinCosT = cms.double(0.99),
    propagatorName = cms.string('PropagatorWithMaterial'),
    source = cms.InputTag("preDuplicateMergingGeneralTracks"),
    ttrhBuilderName = cms.string('WithAngleAndTemplate'),
    useInnermostState = cms.bool(True)
)

process.mergedDuplicateTracks = RecoTracker.TrackProducer.TrackProducer_cfi.TrackProducer.clone(
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('RKFittingSmoother'),
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
    src = cms.InputTag("duplicateTrackCandidates","candidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)

from RecoTracker.FinalTrackSelectors.TrackCutClassifier_cff import *
process.duplicateTrackClassifier = TrackCutClassifier.clone(
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
        maxDr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDz = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24, 15),
        maxLostLayers = cms.vint32(99, 99, 99),
        maxRelPtErr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        min3DLayers = cms.vint32(0, 0, 0),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(0, 0, 0),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("mergedDuplicateTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)

from RecoTracker.FinalTrackSelectors.DuplicateListMerger_cfi import *
process.generalTracks = DuplicateListMerger.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates","candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates","candidates"),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    diffHitsCut = cms.int32(5),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier","MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks","MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder')
)

#from RecoLocalTracker.SiStripRecHitConverter.siStripRecHitConverter_cfi import siStripRecHitConverter as _siStripRecHitConverter
#process.siStripMatchedRecHits = _siStripRecHitConverter.clone(
#    ClusterProducer = cms.InputTag(myCollection),
#    MaskBadAPVFibers = cms.bool(False),
#    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
#    StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
#    VerbosityLevel = cms.untracked.int32(1),
#    matchedRecHits = cms.string('matchedRecHit'),
#    rphiRecHits = cms.string('rphiRecHit'),
#    siStripQualityLabel = cms.ESInputTag(""),
#    stereoRecHits = cms.string('stereoRecHit'),
#    useSiStripQuality = cms.bool(False)
#)

######################################################################################################
process.siStripMatchedRecHits = cms.EDProducer("SiStripRecHitConverter",
    ClusterProducer = cms.InputTag(myCollection),
    MaskBadAPVFibers = cms.bool(False),
    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
    StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
    VerbosityLevel = cms.untracked.int32(1),
    matchedRecHits = cms.string('matchedRecHit'),
    rphiRecHits = cms.string('rphiRecHit'),
    siStripQualityLabel = cms.ESInputTag(""),
    stereoRecHits = cms.string('stereoRecHit'),
    useSiStripQuality = cms.bool(False)
)
######################################################################################################

process.reconstruction_step_track = cms.Path(cms.Task(process.chargeCut2069Clusters,process.highPtTripletStep,process.highPtTripletStepClusters,process.highPtTripletStepHitDoublets,process.highPtTripletStepHitTriplets,process.highPtTripletStepSeedLayers,process.highPtTripletStepSeeds,process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackingRegions,process.highPtTripletStepTracks,process.lowPtQuadStep,process.lowPtQuadStepClusters,process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeeds,process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackingRegions,process.lowPtQuadStepTracks,process.lowPtTripletStep,process.lowPtTripletStepClusters,process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitTriplets,process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeeds,process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackingRegions,process.lowPtTripletStepTracks,process.firstStepGoodPrimaryVertices,process.firstStepPrimaryVertices,process.firstStepPrimaryVerticesUnsorted,process.trackerClusterCheck,process.initialStep,process.initialStepSeedLayers,process.initialStepTrackingRegions,process.initialStepHitDoublets,process.initialStepHitTriplets,process.initialStepHitQuadruplets,process.initialStepSeeds,process.initialStepTrackCandidates,process.initialStepTracks,process.initialStepTrackRefsForJets,process.caloTowerForTrk,process.ak4CaloJetsForTrk,process.jetsForCoreTracking,process.siPixelRecHits,process.MeasurementTrackerEvent,process.siPixelClusterShapeCache,process.earlyGeneralTracks,process.preDuplicateMergingGeneralTracks,process.duplicateTrackCandidates,process.mergedDuplicateTracks,process.duplicateTrackClassifier,process.generalTracks,process.siStripMatchedRecHits))

process.MEtoEDMConverter = cms.EDProducer("MEtoEDMConverter",
    Frequency = cms.untracked.int32(50),
    MEPathToSave = cms.untracked.string(''),
    Name = cms.untracked.string('MEtoEDMConverter'),
    Verbosity = cms.untracked.int32(0),
    deleteAfterCopy = cms.untracked.bool(True)
)

process.MEtoMEComparitor = cms.EDAnalyzer("MEtoMEComparitor",
    Diffgoodness = cms.double(0.1),
    KSgoodness = cms.double(0.9),
    MEtoEDMLabel = cms.string('MEtoEDMConverter'),
    OverAllgoodness = cms.double(0.9),
    autoProcess = cms.bool(True),
    dirDepth = cms.uint32(1),
    lumiInstance = cms.string('MEtoEDMConverterLumi'),
    processNew = cms.string('RERECO'),
    processRef = cms.string('HLT'),
    runInstance = cms.string('MEtoEDMConverterRun')
)


process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string (options.outputFileName),
    outputCommands = cms.untracked.vstring( (
    'drop *',
    'keep reco*_*_*_HITREMOVER',
    'keep reco*_offlinePrimaryVertices__RECO',
    'keep recoMuons_muons_*_RECO',
    'keep recoTracks_generalTracks*_*_reRECO',
         ) ),
    splitLevel = cms.untracked.int32(0)
)


process.DBService = cms.Service("DBService")


process.DQMStore = cms.Service("DQMStore")


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring('particleFlowDisplacedVertexCandidate'),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonGEMDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapAuto = cms.untracked.bool(False),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.Chi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2'),
    MaxChi2 = cms.double(30),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    )
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.FlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('FlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('LooperFittingSmoother'),
    standardFitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK')
)


process.GlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('GlobalDetLayerGeometry')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.KFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.KFUpdatorESProducer = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('KFUpdator')
)


process.LooperFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('LooperFittingSmoother'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('LooperFitter'),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('LooperSmoother'),
    appendToDataLabel = cms.string('')
)


process.LooperTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('LooperFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.LooperTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('LooperSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string(''),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('PixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PixelCPEGenericESProducer = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag(""),
    PixelErrorParametrization = cms.string('NOTcmsim'),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAAlignmentOffsets = cms.bool(False),
    useLAWidthFromDB = cms.bool(True)
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1),
    useOldAnalPropLogic = cms.bool(False),
    useRungeKutta = cms.bool(False)
)


process.RKFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.RKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('RKFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.RKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('RKSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.RungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('RungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('SimpleStripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPETemplateReco'),
    StripCPE = cms.string('StripCPEfromTrackAngle')
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.duplicateTrackCandidatesChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('duplicateTrackCandidatesChi2Est'),
    MaxChi2 = cms.double(100),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring(
            'kNonRespondingIsolated', 
            'kDeadVFE', 
            'kDeadFE', 
            'kNoDataNoTP'
        ),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring(
            'kDAC', 
            'kNoLaser', 
            'kNoisy', 
            'kNNoisy', 
            'kNNNoisy', 
            'kNNNNoisy', 
            'kNNNNNoisy', 
            'kFixedG6', 
            'kFixedG1', 
            'kFixedG0'
        ),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring(
            'kFaultyHardware', 
            'kDead', 
            'kKilled'
        ),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring(
            'kPoorReco', 
            'kPoorCalib', 
            'kNoisy', 
            'kSaturated'
        ),
        kRecovered = cms.vstring(
            'kLeadingEdgeRecovered', 
            'kTowerRecovered'
        ),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring(
            'kWeird', 
            'kDiWeird'
        )
    ),
    timeThresh = cms.double(2.0)
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring(
        'HcalCellMask', 
        'HcalCellOff', 
        'HcalCellDead'
    ),
    RecoveredRecHitBits = cms.vstring(''),
    SeverityLevels = cms.VPSet(
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(0),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring('HBHEIsolatedNoise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring(
                'HBHEHpdHitMultiplicity', 
                'HBHEFlatNoise', 
                'HBHESpikeNoise', 
                'HBHETS4TS5Noise', 
                'HBHENegativeNoise', 
                'HBHEOOTPU'
            )
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring(
                'HFLongShort', 
                'HFS8S1Ratio', 
                'HFPET', 
                'HFSignalAsymmetry'
            )
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(
                'HcalCellOff', 
                'HcalCellDead'
            ),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring('')
        )
    ),
    appendToDataLabel = cms.string(''),
    phase = cms.uint32(1)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.highPtTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('highPtTripletStepChi2Est'),
    MaxChi2 = cms.double(30),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3),
    pTChargeCutThreshold = cms.double(15.0)
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.initialStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('initialStepChi2Est'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.initialStepChi2EstPreSplitting = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('initialStepChi2EstPreSplitting'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.lowPtQuadStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('lowPtQuadStepChi2Est'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3),
    pTChargeCutThreshold = cms.double(-1)
)


process.lowPtQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('lowPtQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.lowPtTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('lowPtTripletStepChi2Est'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.lowPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('lowPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    )
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.templates = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPETemplateReco'),
    DoCosmics = cms.bool(False),
    DoLorentz = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    speed = cms.int32(-2)
)


process.trackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('trackAlgoPriorityOrder'),
    algoOrder = cms.vstring(
        'initialStep', 
        'lowPtQuadStep', 
        'highPtTripletStep', 
        'lowPtTripletStep', 
        'detachedQuadStep', 
        'detachedTripletStep', 
        'pixelPairStep', 
        'mixedTripletStep', 
        'pixelLessStep', 
        'tobTecStep', 
        'jetCoreRegionalStep', 
        'muonSeededStepInOut', 
        'muonSeededStepOutIn'
    ),
    appendToDataLabel = cms.string('')
)


process.trackCounting3D3rdComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.trajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('TrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.ttrhbwr = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('StripCPEfromTrackAngle')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('102X_upgrade2018_realistic_v15'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(100.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(True),
    useHFUpgrade = cms.bool(True),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(False),
    useLayer0Weight = cms.bool(True)
)


process.essourceEcalNextToDead = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalNextToDeadChannelRcd')
)


process.essourceEcalSev = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.essourceSev = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.prefer("es_hardcode")

###################################################################################

hits = "3"
myCollection = "rCluster"+hits

process.chargeCut2069Clusters3 = process.chargeCut2069Clusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.highPtTripletStep3 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters3 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtQuadStepTracks"+hits)
)

process.highPtTripletStepHitDoublets3 = process.highPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"+hits)
)

process.highPtTripletStepHitTriplets3 = process.highPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.highPtTripletStepSeedLayers3 = process.highPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    )
)

process.highPtTripletStepSeeds3 = process.highPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+hits)
)

process.highPtTripletStepTrackCandidates3 = process.highPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("highPtTripletStepClusters"+hits),
    src = cms.InputTag("highPtTripletStepSeeds"+hits)
)

process.highPtTripletStepTrackingRegions3 = process.highPtTripletStepTrackingRegions.clone()

process.highPtTripletStepTracks3 = process.highPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("highPtTripletStepTrackCandidates"+hits)
)

process.lowPtQuadStep3 = process.lowPtQuadStep.clone(
    src = cms.InputTag("lowPtQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtQuadStepClusters3 = process.lowPtQuadStepClusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("initialStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks"+hits)
)

process.lowPtQuadStepHitDoublets3 = process.lowPtQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"+hits)
)

process.lowPtQuadStepHitQuadruplets3 = process.lowPtQuadStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+hits+'__reRECO')
)

process.lowPtQuadStepSeedLayers3 = process.lowPtQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    )
)

process.lowPtQuadStepSeeds3 = process.lowPtQuadStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+hits)
)

process.lowPtQuadStepTrackCandidates3 = process.lowPtQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+hits),
    src = cms.InputTag("lowPtQuadStepSeeds"+hits)
)

process.lowPtQuadStepTrackingRegions3 = process.lowPtQuadStepTrackingRegions.clone()

process.lowPtQuadStepTracks3 = process.lowPtQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtQuadStepTrackCandidates"+hits)
)

process.lowPtTripletStep3 = process.lowPtTripletStep.clone(
    src = cms.InputTag("lowPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtTripletStepClusters3 = process.lowPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("highPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("highPtTripletStepTracks"+hits)
)

process.lowPtTripletStepHitDoublets3 = process.lowPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"+hits)
)

process.lowPtTripletStepHitTriplets3 = process.lowPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.lowPtTripletStepSeedLayers3 = process.lowPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    )
)

process.lowPtTripletStepSeeds3 = process.lowPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+hits)
)

process.lowPtTripletStepTrackCandidates3 = process.lowPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+hits),
    src = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.lowPtTripletStepTrackingRegions3 = process.lowPtTripletStepTrackingRegions.clone()

process.lowPtTripletStepTracks3 = process.lowPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtTripletStepTrackCandidates"+hits)
)

process.firstStepGoodPrimaryVertices3 = process.firstStepGoodPrimaryVertices.clone(
    src = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.firstStepPrimaryVertices3 = process.firstStepPrimaryVertices.clone(
    jets = cms.InputTag("ak4CaloJetsForTrk"+hits),
    particles = cms.InputTag("initialStepTrackRefsForJets"+hits),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.firstStepPrimaryVerticesUnsorted3 = process.firstStepPrimaryVerticesUnsorted.clone(
    TrackLabel = cms.InputTag("initialStepTracks"+hits)
)

process.trackerClusterCheck3 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.initialStep3 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepSeedLayers3 = process.initialStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)

process.initialStepTrackingRegions3 = process.initialStepTrackingRegions.clone()

process.initialStepHitDoublets3 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitTriplets3 = process.initialStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepHitQuadruplets3 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepSeeds3 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates3 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepTracks3 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits)
)

process.initialStepTrackRefsForJets3 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.caloTowerForTrk3 = process.caloTowerForTrk.clone()

process.ak4CaloJetsForTrk3 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.jetsForCoreTracking3 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
)

process.siPixelRecHits3 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.MeasurementTrackerEvent3 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection)
)

process.siPixelClusterShapeCache3 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.earlyGeneralTracks3 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits,
        'highPtTripletStep'+hits,
        'lowPtQuadStep'+hits,
        'lowPtTripletStep'+hits 
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits
    )
)

process.preDuplicateMergingGeneralTracks3 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.duplicateTrackCandidates3 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.mergedDuplicateTracks3 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.duplicateTrackClassifier3 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.generalTracks3 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.siStripMatchedRecHits3 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)

process.reconstruction_step_track3 = cms.Path(cms.Task(process.chargeCut2069Clusters3,process.highPtTripletStep3,process.highPtTripletStepClusters3,process.highPtTripletStepHitDoublets3,process.highPtTripletStepHitTriplets3,process.highPtTripletStepSeedLayers3,process.highPtTripletStepSeeds3,process.highPtTripletStepTrackCandidates3,process.highPtTripletStepTrackingRegions3,process.highPtTripletStepTracks3,process.lowPtQuadStep3,process.lowPtQuadStepClusters3,process.lowPtQuadStepHitDoublets3,process.lowPtQuadStepHitQuadruplets3,process.lowPtQuadStepSeedLayers3,process.lowPtQuadStepSeeds3,process.lowPtQuadStepTrackCandidates3,process.lowPtQuadStepTrackingRegions3,process.lowPtQuadStepTracks3,process.lowPtTripletStep3,process.lowPtTripletStepClusters3,process.lowPtTripletStepHitDoublets3,process.lowPtTripletStepHitTriplets3,process.lowPtTripletStepSeedLayers3,process.lowPtTripletStepSeeds3,process.lowPtTripletStepTrackCandidates3,process.lowPtTripletStepTrackingRegions3,process.lowPtTripletStepTracks3,process.firstStepGoodPrimaryVertices3,process.firstStepPrimaryVertices3,process.firstStepPrimaryVerticesUnsorted3,process.trackerClusterCheck3,process.initialStep3,process.initialStepSeedLayers3,process.initialStepTrackingRegions3,process.initialStepHitDoublets3,process.initialStepHitTriplets3,process.initialStepHitQuadruplets3,process.initialStepSeeds3,process.initialStepTrackCandidates3,process.initialStepTracks3,process.firstStepPrimaryVertices3,process.firstStepPrimaryVerticesUnsorted3,process.initialStepTrackRefsForJets3,process.caloTowerForTrk3,process.ak4CaloJetsForTrk3,process.jetsForCoreTracking3,process.siPixelRecHits3,process.MeasurementTrackerEvent3,process.siPixelClusterShapeCache3,process.earlyGeneralTracks3,process.preDuplicateMergingGeneralTracks3,process.duplicateTrackCandidates3,process.mergedDuplicateTracks3,process.duplicateTrackClassifier3,process.generalTracks3,process.siStripMatchedRecHits3))

hits = "4"
myCollection = "rCluster"+hits

process.chargeCut2069Clusters4 = process.chargeCut2069Clusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.highPtTripletStep4 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters4 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtQuadStepTracks"+hits)
)

process.highPtTripletStepHitDoublets4 = process.highPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"+hits)
)

process.highPtTripletStepHitTriplets4 = process.highPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.highPtTripletStepSeedLayers4 = process.highPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    )
)

process.highPtTripletStepSeeds4 = process.highPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+hits)
)

process.highPtTripletStepTrackCandidates4 = process.highPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("highPtTripletStepClusters"+hits),
    src = cms.InputTag("highPtTripletStepSeeds"+hits)
)

process.highPtTripletStepTrackingRegions4 = process.highPtTripletStepTrackingRegions.clone()

process.highPtTripletStepTracks4 = process.highPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("highPtTripletStepTrackCandidates"+hits)
)

process.lowPtQuadStep4 = process.lowPtQuadStep.clone(
    src = cms.InputTag("lowPtQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtQuadStepClusters4 = process.lowPtQuadStepClusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("initialStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks"+hits)
)

process.lowPtQuadStepHitDoublets4 = process.lowPtQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"+hits)
)

process.lowPtQuadStepHitQuadruplets4 = process.lowPtQuadStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+hits+'__reRECO')
)

process.lowPtQuadStepSeedLayers4 = process.lowPtQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    )
)

process.lowPtQuadStepSeeds4 = process.lowPtQuadStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+hits)
)

process.lowPtQuadStepTrackCandidates4 = process.lowPtQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+hits),
    src = cms.InputTag("lowPtQuadStepSeeds"+hits)
)

process.lowPtQuadStepTrackingRegions4 = process.lowPtQuadStepTrackingRegions.clone()

process.lowPtQuadStepTracks4 = process.lowPtQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtQuadStepTrackCandidates"+hits)
)

process.lowPtTripletStep4 = process.lowPtTripletStep.clone(
    src = cms.InputTag("lowPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtTripletStepClusters4 = process.lowPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("highPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("highPtTripletStepTracks"+hits)
)

process.lowPtTripletStepHitDoublets4 = process.lowPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"+hits)
)

process.lowPtTripletStepHitTriplets4 = process.lowPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.lowPtTripletStepSeedLayers4 = process.lowPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    )
)

process.lowPtTripletStepSeeds4 = process.lowPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+hits)
)

process.lowPtTripletStepTrackCandidates4 = process.lowPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+hits),
    src = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.lowPtTripletStepTrackingRegions4 = process.lowPtTripletStepTrackingRegions.clone()

process.lowPtTripletStepTracks4 = process.lowPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtTripletStepTrackCandidates"+hits)
)

process.firstStepGoodPrimaryVertices4 = process.firstStepGoodPrimaryVertices.clone(
    src = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.firstStepPrimaryVertices4 = process.firstStepPrimaryVertices.clone(
    jets = cms.InputTag("ak4CaloJetsForTrk"+hits),
    particles = cms.InputTag("initialStepTrackRefsForJets"+hits),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.firstStepPrimaryVerticesUnsorted4 = process.firstStepPrimaryVerticesUnsorted.clone(
    TrackLabel = cms.InputTag("initialStepTracks"+hits)
)

process.trackerClusterCheck4 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.initialStep4 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepSeedLayers4 = process.initialStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)

process.initialStepTrackingRegions4 = process.initialStepTrackingRegions.clone()

process.initialStepHitDoublets4 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitTriplets4 = process.initialStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepHitQuadruplets4 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepSeeds4 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates4 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepTracks4 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits)
)

process.initialStepTrackRefsForJets4 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.caloTowerForTrk4 = process.caloTowerForTrk.clone()

process.ak4CaloJetsForTrk4 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.jetsForCoreTracking4 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
)

process.siPixelRecHits4 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.MeasurementTrackerEvent4 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection)
)

process.siPixelClusterShapeCache4 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.earlyGeneralTracks4 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits,
        'highPtTripletStep'+hits,
        'lowPtQuadStep'+hits,
        'lowPtTripletStep'+hits 
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits
    )
)

process.preDuplicateMergingGeneralTracks4 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.duplicateTrackCandidates4 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.mergedDuplicateTracks4 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.duplicateTrackClassifier4 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.generalTracks4 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.siStripMatchedRecHits4 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)

process.reconstruction_step_track4 = cms.Path(cms.Task(process.chargeCut2069Clusters4,process.highPtTripletStep4,process.highPtTripletStepClusters4,process.highPtTripletStepHitDoublets4,process.highPtTripletStepHitTriplets4,process.highPtTripletStepSeedLayers4,process.highPtTripletStepSeeds4,process.highPtTripletStepTrackCandidates4,process.highPtTripletStepTrackingRegions4,process.highPtTripletStepTracks4,process.lowPtQuadStep4,process.lowPtQuadStepClusters4,process.lowPtQuadStepHitDoublets4,process.lowPtQuadStepHitQuadruplets4,process.lowPtQuadStepSeedLayers4,process.lowPtQuadStepSeeds4,process.lowPtQuadStepTrackCandidates4,process.lowPtQuadStepTrackingRegions4,process.lowPtQuadStepTracks4,process.lowPtTripletStep4,process.lowPtTripletStepClusters4,process.lowPtTripletStepHitDoublets4,process.lowPtTripletStepHitTriplets4,process.lowPtTripletStepSeedLayers4,process.lowPtTripletStepSeeds4,process.lowPtTripletStepTrackCandidates4,process.lowPtTripletStepTrackingRegions4,process.lowPtTripletStepTracks4,process.firstStepGoodPrimaryVertices4,process.firstStepPrimaryVertices4,process.firstStepPrimaryVerticesUnsorted4,process.trackerClusterCheck4,process.initialStep4,process.initialStepSeedLayers4,process.initialStepTrackingRegions4,process.initialStepHitDoublets4,process.initialStepHitTriplets4,process.initialStepHitQuadruplets4,process.initialStepSeeds4,process.initialStepTrackCandidates4,process.initialStepTracks4,process.firstStepPrimaryVertices4,process.firstStepPrimaryVerticesUnsorted4,process.initialStepTrackRefsForJets4,process.caloTowerForTrk4,process.ak4CaloJetsForTrk4,process.jetsForCoreTracking4,process.siPixelRecHits4,process.MeasurementTrackerEvent4,process.siPixelClusterShapeCache4,process.earlyGeneralTracks4,process.preDuplicateMergingGeneralTracks4,process.duplicateTrackCandidates4,process.mergedDuplicateTracks4,process.duplicateTrackClassifier4,process.generalTracks4,process.siStripMatchedRecHits4))

hits = "5"
myCollection = "rCluster"+hits

process.chargeCut2069Clusters5 = process.chargeCut2069Clusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.highPtTripletStep5 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters5 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtQuadStepTracks"+hits)
)

process.highPtTripletStepHitDoublets5 = process.highPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"+hits)
)

process.highPtTripletStepHitTriplets5 = process.highPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.highPtTripletStepSeedLayers5 = process.highPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    )
)

process.highPtTripletStepSeeds5 = process.highPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+hits)
)

process.highPtTripletStepTrackCandidates5 = process.highPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("highPtTripletStepClusters"+hits),
    src = cms.InputTag("highPtTripletStepSeeds"+hits)
)

process.highPtTripletStepTrackingRegions5 = process.highPtTripletStepTrackingRegions.clone()

process.highPtTripletStepTracks5 = process.highPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("highPtTripletStepTrackCandidates"+hits)
)

process.lowPtQuadStep5 = process.lowPtQuadStep.clone(
    src = cms.InputTag("lowPtQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtQuadStepClusters5 = process.lowPtQuadStepClusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("initialStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks"+hits)
)

process.lowPtQuadStepHitDoublets5 = process.lowPtQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"+hits)
)

process.lowPtQuadStepHitQuadruplets5 = process.lowPtQuadStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+hits+'__reRECO')
)

process.lowPtQuadStepSeedLayers5 = process.lowPtQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    )
)

process.lowPtQuadStepSeeds5 = process.lowPtQuadStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+hits)
)

process.lowPtQuadStepTrackCandidates5 = process.lowPtQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+hits),
    src = cms.InputTag("lowPtQuadStepSeeds"+hits)
)

process.lowPtQuadStepTrackingRegions5 = process.lowPtQuadStepTrackingRegions.clone()

process.lowPtQuadStepTracks5 = process.lowPtQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtQuadStepTrackCandidates"+hits)
)

process.lowPtTripletStep5 = process.lowPtTripletStep.clone(
    src = cms.InputTag("lowPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtTripletStepClusters5 = process.lowPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("highPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("highPtTripletStepTracks"+hits)
)

process.lowPtTripletStepHitDoublets5 = process.lowPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"+hits)
)

process.lowPtTripletStepHitTriplets5 = process.lowPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.lowPtTripletStepSeedLayers5 = process.lowPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    )
)

process.lowPtTripletStepSeeds5 = process.lowPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+hits)
)

process.lowPtTripletStepTrackCandidates5 = process.lowPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+hits),
    src = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.lowPtTripletStepTrackingRegions5 = process.lowPtTripletStepTrackingRegions.clone()

process.lowPtTripletStepTracks5 = process.lowPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtTripletStepTrackCandidates"+hits)
)

process.firstStepGoodPrimaryVertices5 = process.firstStepGoodPrimaryVertices.clone(
    src = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.firstStepPrimaryVertices5 = process.firstStepPrimaryVertices.clone(
    jets = cms.InputTag("ak4CaloJetsForTrk"+hits),
    particles = cms.InputTag("initialStepTrackRefsForJets"+hits),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.firstStepPrimaryVerticesUnsorted5 = process.firstStepPrimaryVerticesUnsorted.clone(
    TrackLabel = cms.InputTag("initialStepTracks"+hits)
)

process.trackerClusterCheck5 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.initialStep5 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepSeedLayers5 = process.initialStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)

process.initialStepTrackingRegions5 = process.initialStepTrackingRegions.clone()

process.initialStepHitDoublets5 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitTriplets5 = process.initialStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepHitQuadruplets5 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepSeeds5 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates5 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepTracks5 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits)
)

process.initialStepTrackRefsForJets5 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.caloTowerForTrk5 = process.caloTowerForTrk.clone()

process.ak4CaloJetsForTrk5 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.jetsForCoreTracking5 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
)

process.siPixelRecHits5 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.MeasurementTrackerEvent5 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection)
)

process.siPixelClusterShapeCache5 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.earlyGeneralTracks5 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits,
        'highPtTripletStep'+hits,
        'lowPtQuadStep'+hits,
        'lowPtTripletStep'+hits 
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits
    )
)

process.preDuplicateMergingGeneralTracks5 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.duplicateTrackCandidates5 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.mergedDuplicateTracks5 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.duplicateTrackClassifier5 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.generalTracks5 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.siStripMatchedRecHits5 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)

process.reconstruction_step_track5 = cms.Path(cms.Task(process.chargeCut2069Clusters5,process.highPtTripletStep5,process.highPtTripletStepClusters5,process.highPtTripletStepHitDoublets5,process.highPtTripletStepHitTriplets5,process.highPtTripletStepSeedLayers5,process.highPtTripletStepSeeds5,process.highPtTripletStepTrackCandidates5,process.highPtTripletStepTrackingRegions5,process.highPtTripletStepTracks5,process.lowPtQuadStep5,process.lowPtQuadStepClusters5,process.lowPtQuadStepHitDoublets5,process.lowPtQuadStepHitQuadruplets5,process.lowPtQuadStepSeedLayers5,process.lowPtQuadStepSeeds5,process.lowPtQuadStepTrackCandidates5,process.lowPtQuadStepTrackingRegions5,process.lowPtQuadStepTracks5,process.lowPtTripletStep5,process.lowPtTripletStepClusters5,process.lowPtTripletStepHitDoublets5,process.lowPtTripletStepHitTriplets5,process.lowPtTripletStepSeedLayers5,process.lowPtTripletStepSeeds5,process.lowPtTripletStepTrackCandidates5,process.lowPtTripletStepTrackingRegions5,process.lowPtTripletStepTracks5,process.firstStepGoodPrimaryVertices5,process.firstStepPrimaryVertices5,process.firstStepPrimaryVerticesUnsorted5,process.trackerClusterCheck5,process.initialStep5,process.initialStepSeedLayers5,process.initialStepTrackingRegions5,process.initialStepHitDoublets5,process.initialStepHitTriplets5,process.initialStepHitQuadruplets5,process.initialStepSeeds5,process.initialStepTrackCandidates5,process.initialStepTracks5,process.firstStepPrimaryVertices5,process.firstStepPrimaryVerticesUnsorted5,process.initialStepTrackRefsForJets5,process.caloTowerForTrk5,process.ak4CaloJetsForTrk5,process.jetsForCoreTracking5,process.siPixelRecHits5,process.MeasurementTrackerEvent5,process.siPixelClusterShapeCache5,process.earlyGeneralTracks5,process.preDuplicateMergingGeneralTracks5,process.duplicateTrackCandidates5,process.mergedDuplicateTracks5,process.duplicateTrackClassifier5,process.generalTracks5,process.siStripMatchedRecHits5))

hits = "6"
myCollection = "rCluster"+hits

process.chargeCut2069Clusters6 = process.chargeCut2069Clusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.highPtTripletStep6 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters6 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtQuadStepTracks"+hits)
)

process.highPtTripletStepHitDoublets6 = process.highPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"+hits)
)

process.highPtTripletStepHitTriplets6 = process.highPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.highPtTripletStepSeedLayers6 = process.highPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    )
)

process.highPtTripletStepSeeds6 = process.highPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+hits)
)

process.highPtTripletStepTrackCandidates6 = process.highPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("highPtTripletStepClusters"+hits),
    src = cms.InputTag("highPtTripletStepSeeds"+hits)
)

process.highPtTripletStepTrackingRegions6 = process.highPtTripletStepTrackingRegions.clone()

process.highPtTripletStepTracks6 = process.highPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("highPtTripletStepTrackCandidates"+hits)
)

process.lowPtQuadStep6 = process.lowPtQuadStep.clone(
    src = cms.InputTag("lowPtQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtQuadStepClusters6 = process.lowPtQuadStepClusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("initialStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks"+hits)
)

process.lowPtQuadStepHitDoublets6 = process.lowPtQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"+hits)
)

process.lowPtQuadStepHitQuadruplets6 = process.lowPtQuadStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+hits+'__reRECO')
)

process.lowPtQuadStepSeedLayers6 = process.lowPtQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    )
)

process.lowPtQuadStepSeeds6 = process.lowPtQuadStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+hits)
)

process.lowPtQuadStepTrackCandidates6 = process.lowPtQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+hits),
    src = cms.InputTag("lowPtQuadStepSeeds"+hits)
)

process.lowPtQuadStepTrackingRegions6 = process.lowPtQuadStepTrackingRegions.clone()

process.lowPtQuadStepTracks6 = process.lowPtQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtQuadStepTrackCandidates"+hits)
)

process.lowPtTripletStep6 = process.lowPtTripletStep.clone(
    src = cms.InputTag("lowPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtTripletStepClusters6 = process.lowPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("highPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("highPtTripletStepTracks"+hits)
)

process.lowPtTripletStepHitDoublets6 = process.lowPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"+hits)
)

process.lowPtTripletStepHitTriplets6 = process.lowPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.lowPtTripletStepSeedLayers6 = process.lowPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    )
)

process.lowPtTripletStepSeeds6 = process.lowPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+hits)
)

process.lowPtTripletStepTrackCandidates6 = process.lowPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+hits),
    src = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.lowPtTripletStepTrackingRegions6 = process.lowPtTripletStepTrackingRegions.clone()

process.lowPtTripletStepTracks6 = process.lowPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtTripletStepTrackCandidates"+hits)
)

process.firstStepGoodPrimaryVertices6 = process.firstStepGoodPrimaryVertices.clone(
    src = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.firstStepPrimaryVertices6 = process.firstStepPrimaryVertices.clone(
    jets = cms.InputTag("ak4CaloJetsForTrk"+hits),
    particles = cms.InputTag("initialStepTrackRefsForJets"+hits),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.firstStepPrimaryVerticesUnsorted6 = process.firstStepPrimaryVerticesUnsorted.clone(
    TrackLabel = cms.InputTag("initialStepTracks"+hits)
)

process.trackerClusterCheck6 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.initialStep6 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepSeedLayers6 = process.initialStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)

process.initialStepTrackingRegions6 = process.initialStepTrackingRegions.clone()

process.initialStepHitDoublets6 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitTriplets6 = process.initialStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepHitQuadruplets6 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepSeeds6 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates6 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepTracks6 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits)
)

process.initialStepTrackRefsForJets6 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.caloTowerForTrk6 = process.caloTowerForTrk.clone()

process.ak4CaloJetsForTrk6 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.jetsForCoreTracking6 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
)

process.siPixelRecHits6 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.MeasurementTrackerEvent6 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection)
)

process.siPixelClusterShapeCache6 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.earlyGeneralTracks6 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits,
        'highPtTripletStep'+hits,
        'lowPtQuadStep'+hits,
        'lowPtTripletStep'+hits 
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits
    )
)

process.preDuplicateMergingGeneralTracks6 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.duplicateTrackCandidates6 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.mergedDuplicateTracks6 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.duplicateTrackClassifier6 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.generalTracks6 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.siStripMatchedRecHits6 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)

process.reconstruction_step_track6 = cms.Path(cms.Task(process.chargeCut2069Clusters6,process.highPtTripletStep6,process.highPtTripletStepClusters6,process.highPtTripletStepHitDoublets6,process.highPtTripletStepHitTriplets6,process.highPtTripletStepSeedLayers6,process.highPtTripletStepSeeds6,process.highPtTripletStepTrackCandidates6,process.highPtTripletStepTrackingRegions6,process.highPtTripletStepTracks6,process.lowPtQuadStep6,process.lowPtQuadStepClusters6,process.lowPtQuadStepHitDoublets6,process.lowPtQuadStepHitQuadruplets6,process.lowPtQuadStepSeedLayers6,process.lowPtQuadStepSeeds6,process.lowPtQuadStepTrackCandidates6,process.lowPtQuadStepTrackingRegions6,process.lowPtQuadStepTracks6,process.lowPtTripletStep6,process.lowPtTripletStepClusters6,process.lowPtTripletStepHitDoublets6,process.lowPtTripletStepHitTriplets6,process.lowPtTripletStepSeedLayers6,process.lowPtTripletStepSeeds6,process.lowPtTripletStepTrackCandidates6,process.lowPtTripletStepTrackingRegions6,process.lowPtTripletStepTracks6,process.firstStepGoodPrimaryVertices6,process.firstStepPrimaryVertices6,process.firstStepPrimaryVerticesUnsorted6,process.trackerClusterCheck6,process.initialStep6,process.initialStepSeedLayers6,process.initialStepTrackingRegions6,process.initialStepHitDoublets6,process.initialStepHitTriplets6,process.initialStepHitQuadruplets6,process.initialStepSeeds6,process.initialStepTrackCandidates6,process.initialStepTracks6,process.firstStepPrimaryVertices6,process.firstStepPrimaryVerticesUnsorted6,process.initialStepTrackRefsForJets6,process.caloTowerForTrk6,process.ak4CaloJetsForTrk6,process.jetsForCoreTracking6,process.siPixelRecHits6,process.MeasurementTrackerEvent6,process.siPixelClusterShapeCache6,process.earlyGeneralTracks6,process.preDuplicateMergingGeneralTracks6,process.duplicateTrackCandidates6,process.mergedDuplicateTracks6,process.duplicateTrackClassifier6,process.generalTracks6,process.siStripMatchedRecHits6))

hits = "7"
myCollection = "rCluster"+hits

process.chargeCut2069Clusters7 = process.chargeCut2069Clusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.highPtTripletStep7 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters7 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtQuadStepTracks"+hits)
)

process.highPtTripletStepHitDoublets7 = process.highPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"+hits)
)

process.highPtTripletStepHitTriplets7 = process.highPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.highPtTripletStepSeedLayers7 = process.highPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    )
)

process.highPtTripletStepSeeds7 = process.highPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+hits)
)

process.highPtTripletStepTrackCandidates7 = process.highPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("highPtTripletStepClusters"+hits),
    src = cms.InputTag("highPtTripletStepSeeds"+hits)
)

process.highPtTripletStepTrackingRegions7 = process.highPtTripletStepTrackingRegions.clone()

process.highPtTripletStepTracks7 = process.highPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("highPtTripletStepTrackCandidates"+hits)
)

process.lowPtQuadStep7 = process.lowPtQuadStep.clone(
    src = cms.InputTag("lowPtQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtQuadStepClusters7 = process.lowPtQuadStepClusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("initialStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks"+hits)
)

process.lowPtQuadStepHitDoublets7 = process.lowPtQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"+hits)
)

process.lowPtQuadStepHitQuadruplets7 = process.lowPtQuadStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+hits+'__reRECO')
)

process.lowPtQuadStepSeedLayers7 = process.lowPtQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    )
)

process.lowPtQuadStepSeeds7 = process.lowPtQuadStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+hits)
)

process.lowPtQuadStepTrackCandidates7 = process.lowPtQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+hits),
    src = cms.InputTag("lowPtQuadStepSeeds"+hits)
)

process.lowPtQuadStepTrackingRegions7 = process.lowPtQuadStepTrackingRegions.clone()

process.lowPtQuadStepTracks7 = process.lowPtQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtQuadStepTrackCandidates"+hits)
)

process.lowPtTripletStep7 = process.lowPtTripletStep.clone(
    src = cms.InputTag("lowPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtTripletStepClusters7 = process.lowPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("highPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("highPtTripletStepTracks"+hits)
)

process.lowPtTripletStepHitDoublets7 = process.lowPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"+hits)
)

process.lowPtTripletStepHitTriplets7 = process.lowPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.lowPtTripletStepSeedLayers7 = process.lowPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    )
)

process.lowPtTripletStepSeeds7 = process.lowPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+hits)
)

process.lowPtTripletStepTrackCandidates7 = process.lowPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+hits),
    src = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.lowPtTripletStepTrackingRegions7 = process.lowPtTripletStepTrackingRegions.clone()

process.lowPtTripletStepTracks7 = process.lowPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtTripletStepTrackCandidates"+hits)
)

process.firstStepGoodPrimaryVertices7 = process.firstStepGoodPrimaryVertices.clone(
    src = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.firstStepPrimaryVertices7 = process.firstStepPrimaryVertices.clone(
    jets = cms.InputTag("ak4CaloJetsForTrk"+hits),
    particles = cms.InputTag("initialStepTrackRefsForJets"+hits),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.firstStepPrimaryVerticesUnsorted7 = process.firstStepPrimaryVerticesUnsorted.clone(
    TrackLabel = cms.InputTag("initialStepTracks"+hits)
)

process.trackerClusterCheck7 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.initialStep7 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepSeedLayers7 = process.initialStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)

process.initialStepTrackingRegions7 = process.initialStepTrackingRegions.clone()

process.initialStepHitDoublets7 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitTriplets7 = process.initialStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepHitQuadruplets7 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepSeeds7 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates7 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepTracks7 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits)
)

process.initialStepTrackRefsForJets7 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.caloTowerForTrk7 = process.caloTowerForTrk.clone()

process.ak4CaloJetsForTrk7 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.jetsForCoreTracking7 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
)

process.siPixelRecHits7 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.MeasurementTrackerEvent7 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection)
)

process.siPixelClusterShapeCache7 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.earlyGeneralTracks7 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits,
        'highPtTripletStep'+hits,
        'lowPtQuadStep'+hits,
        'lowPtTripletStep'+hits 
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits
    )
)

process.preDuplicateMergingGeneralTracks7 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.duplicateTrackCandidates7 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.mergedDuplicateTracks7 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.duplicateTrackClassifier7 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.generalTracks7 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.siStripMatchedRecHits7 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)

process.reconstruction_step_track7 = cms.Path(cms.Task(process.chargeCut2069Clusters7,process.highPtTripletStep7,process.highPtTripletStepClusters7,process.highPtTripletStepHitDoublets7,process.highPtTripletStepHitTriplets7,process.highPtTripletStepSeedLayers7,process.highPtTripletStepSeeds7,process.highPtTripletStepTrackCandidates7,process.highPtTripletStepTrackingRegions7,process.highPtTripletStepTracks7,process.lowPtQuadStep7,process.lowPtQuadStepClusters7,process.lowPtQuadStepHitDoublets7,process.lowPtQuadStepHitQuadruplets7,process.lowPtQuadStepSeedLayers7,process.lowPtQuadStepSeeds7,process.lowPtQuadStepTrackCandidates7,process.lowPtQuadStepTrackingRegions7,process.lowPtQuadStepTracks7,process.lowPtTripletStep7,process.lowPtTripletStepClusters7,process.lowPtTripletStepHitDoublets7,process.lowPtTripletStepHitTriplets7,process.lowPtTripletStepSeedLayers7,process.lowPtTripletStepSeeds7,process.lowPtTripletStepTrackCandidates7,process.lowPtTripletStepTrackingRegions7,process.lowPtTripletStepTracks7,process.firstStepGoodPrimaryVertices7,process.firstStepPrimaryVertices7,process.firstStepPrimaryVerticesUnsorted7,process.trackerClusterCheck7,process.initialStep7,process.initialStepSeedLayers7,process.initialStepTrackingRegions7,process.initialStepHitDoublets7,process.initialStepHitTriplets7,process.initialStepHitQuadruplets7,process.initialStepSeeds7,process.initialStepTrackCandidates7,process.initialStepTracks7,process.firstStepPrimaryVertices7,process.firstStepPrimaryVerticesUnsorted7,process.initialStepTrackRefsForJets7,process.caloTowerForTrk7,process.ak4CaloJetsForTrk7,process.jetsForCoreTracking7,process.siPixelRecHits7,process.MeasurementTrackerEvent7,process.siPixelClusterShapeCache7,process.earlyGeneralTracks7,process.preDuplicateMergingGeneralTracks7,process.duplicateTrackCandidates7,process.mergedDuplicateTracks7,process.duplicateTrackClassifier7,process.generalTracks7,process.siStripMatchedRecHits7))

hits = "8"
myCollection = "rCluster"+hits

process.chargeCut2069Clusters8 = process.chargeCut2069Clusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.highPtTripletStep8 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters8 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtQuadStepTracks"+hits)
)

process.highPtTripletStepHitDoublets8 = process.highPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"+hits)
)

process.highPtTripletStepHitTriplets8 = process.highPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.highPtTripletStepSeedLayers8 = process.highPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters"+hits)
    )
)

process.highPtTripletStepSeeds8 = process.highPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+hits)
)

process.highPtTripletStepTrackCandidates8 = process.highPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("highPtTripletStepClusters"+hits),
    src = cms.InputTag("highPtTripletStepSeeds"+hits)
)

process.highPtTripletStepTrackingRegions8 = process.highPtTripletStepTrackingRegions.clone()

process.highPtTripletStepTracks8 = process.highPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("highPtTripletStepTrackCandidates"+hits)
)

process.lowPtQuadStep8 = process.lowPtQuadStep.clone(
    src = cms.InputTag("lowPtQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtQuadStepClusters8 = process.lowPtQuadStepClusters.clone(
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("initialStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks"+hits)
)

process.lowPtQuadStepHitDoublets8 = process.lowPtQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"+hits)
)

process.lowPtQuadStepHitQuadruplets8 = process.lowPtQuadStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+hits+'__reRECO')
)

process.lowPtQuadStepSeedLayers8 = process.lowPtQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters"+hits)
    )
)

process.lowPtQuadStepSeeds8 = process.lowPtQuadStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+hits)
)

process.lowPtQuadStepTrackCandidates8 = process.lowPtQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+hits),
    src = cms.InputTag("lowPtQuadStepSeeds"+hits)
)

process.lowPtQuadStepTrackingRegions8 = process.lowPtQuadStepTrackingRegions.clone()

process.lowPtQuadStepTracks8 = process.lowPtQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtQuadStepTrackCandidates"+hits)
)

process.lowPtTripletStep8 = process.lowPtTripletStep.clone(
    src = cms.InputTag("lowPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.lowPtTripletStepClusters8 = process.lowPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("highPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("highPtTripletStepTracks"+hits)
)

process.lowPtTripletStepHitDoublets8 = process.lowPtTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"+hits)
)

process.lowPtTripletStepHitTriplets8 = process.lowPtTripletStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("lowPtTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+hits+'__reRECO')
)

process.lowPtTripletStepSeedLayers8 = process.lowPtTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters"+hits)
    )
)

process.lowPtTripletStepSeeds8 = process.lowPtTripletStepSeeds.clone(
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+hits)
)

process.lowPtTripletStepTrackCandidates8 = process.lowPtTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+hits),
    src = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.lowPtTripletStepTrackingRegions8 = process.lowPtTripletStepTrackingRegions.clone()

process.lowPtTripletStepTracks8 = process.lowPtTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("lowPtTripletStepTrackCandidates"+hits)
)

process.firstStepGoodPrimaryVertices8 = process.firstStepGoodPrimaryVertices.clone(
    src = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.firstStepPrimaryVertices8 = process.firstStepPrimaryVertices.clone(
    jets = cms.InputTag("ak4CaloJetsForTrk"+hits),
    particles = cms.InputTag("initialStepTrackRefsForJets"+hits),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.firstStepPrimaryVerticesUnsorted8 = process.firstStepPrimaryVerticesUnsorted.clone(
    TrackLabel = cms.InputTag("initialStepTracks"+hits)
)

process.trackerClusterCheck8 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.initialStep8 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepSeedLayers8 = process.initialStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)

process.initialStepTrackingRegions8 = process.initialStepTrackingRegions.clone()

process.initialStepHitDoublets8 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitTriplets8 = process.initialStepHitTriplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepHitQuadruplets8 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
)

process.initialStepSeeds8 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates8 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepTracks8 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits)
)

process.initialStepTrackRefsForJets8 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.caloTowerForTrk8 = process.caloTowerForTrk.clone()

process.ak4CaloJetsForTrk8 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits)
)

process.jetsForCoreTracking8 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
)

process.siPixelRecHits8 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.MeasurementTrackerEvent8 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection)
)

process.siPixelClusterShapeCache8 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.earlyGeneralTracks8 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits,
        'highPtTripletStep'+hits,
        'lowPtQuadStep'+hits,
        'lowPtTripletStep'+hits 
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits
    )
)

process.preDuplicateMergingGeneralTracks8 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.duplicateTrackCandidates8 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.mergedDuplicateTracks8 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.duplicateTrackClassifier8 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.generalTracks8 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.siStripMatchedRecHits8 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)

process.reconstruction_step_track8 = cms.Path(cms.Task(process.chargeCut2069Clusters8,process.highPtTripletStep8,process.highPtTripletStepClusters8,process.highPtTripletStepHitDoublets8,process.highPtTripletStepHitTriplets8,process.highPtTripletStepSeedLayers8,process.highPtTripletStepSeeds8,process.highPtTripletStepTrackCandidates8,process.highPtTripletStepTrackingRegions8,process.highPtTripletStepTracks8,process.lowPtQuadStep8,process.lowPtQuadStepClusters8,process.lowPtQuadStepHitDoublets8,process.lowPtQuadStepHitQuadruplets8,process.lowPtQuadStepSeedLayers8,process.lowPtQuadStepSeeds8,process.lowPtQuadStepTrackCandidates8,process.lowPtQuadStepTrackingRegions8,process.lowPtQuadStepTracks8,process.lowPtTripletStep8,process.lowPtTripletStepClusters8,process.lowPtTripletStepHitDoublets8,process.lowPtTripletStepHitTriplets8,process.lowPtTripletStepSeedLayers8,process.lowPtTripletStepSeeds8,process.lowPtTripletStepTrackCandidates8,process.lowPtTripletStepTrackingRegions8,process.lowPtTripletStepTracks8,process.firstStepGoodPrimaryVertices8,process.firstStepPrimaryVertices8,process.firstStepPrimaryVerticesUnsorted8,process.trackerClusterCheck8,process.initialStep8,process.initialStepSeedLayers8,process.initialStepTrackingRegions8,process.initialStepHitDoublets8,process.initialStepHitTriplets8,process.initialStepHitQuadruplets8,process.initialStepSeeds8,process.initialStepTrackCandidates8,process.initialStepTracks8,process.firstStepPrimaryVertices8,process.firstStepPrimaryVerticesUnsorted8,process.initialStepTrackRefsForJets8,process.caloTowerForTrk8,process.ak4CaloJetsForTrk8,process.jetsForCoreTracking8,process.siPixelRecHits8,process.MeasurementTrackerEvent8,process.siPixelClusterShapeCache8,process.earlyGeneralTracks8,process.preDuplicateMergingGeneralTracks8,process.duplicateTrackCandidates8,process.mergedDuplicateTracks8,process.duplicateTrackClassifier8,process.generalTracks8,process.siStripMatchedRecHits8))

process.endjob_step = cms.EndPath(cms.Task(process.MEtoEDMConverter))

process.RECOoutput_step = cms.EndPath(process.RECOoutput)

process.schedule = cms.Schedule(*[ process.reconstruction_step_track, process.reconstruction_step_track3, process.reconstruction_step_track4, process.reconstruction_step_track5, process.reconstruction_step_track6, process.reconstruction_step_track7, process.reconstruction_step_track8, process.endjob_step, process.RECOoutput_step ])

#process.schedule = cms.Schedule(*[ process.reconstruction_step_track, process.endjob_step, process.RECOoutput_step ])
