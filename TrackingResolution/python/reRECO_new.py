# Conditions read from  CMS_CONDITIONS  via FrontierProd 
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import multiprocessing
import glob

# full reconstruction sequence without very early local reconstruction
# modification: uses 'rCluster' modules as input Cluster for track reconstruction (instead of SiPixel-/ SiStripCluster) 
# adjust line 19 for input file
# adjust line 39794 for output file
# adjust line  25 for monitoring output file 
# adjust line for keep and drop (RECO) , 
# Always: ADJUST PROCESS SCHEDULE & input cluster collection l. 14 -15
# process name reRECO (cf l. 9) 

# replaced:
# cms.InputTag("siPixelClusters") => cms.InputTag(myCollection)
# cms.InputTag("siStripClusters") => cms.InputTag(myCollection)

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
hitsRemain = '3'
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


process.CkfBaseTrajectoryFilter_block = cms.PSet(
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

process.detachedQuadStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('detachedQuadStepChi2Est'),
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
        refToPSet_ = cms.string('detachedQuadStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.detachedQuadStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('detachedQuadStepTrajectoryFilterBase')
    ))
)

process.detachedQuadStepTrajectoryFilterBase = cms.PSet(
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

process.detachedTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('detachedTripletStepChi2Est'),
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
        refToPSet_ = cms.string('detachedTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.detachedTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('detachedTripletStepTrajectoryFilterBase')
    ))
)

process.detachedTripletStepTrajectoryFilterBase = cms.PSet(
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

process.detachedTripletStepTrajectoryFilterShape = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)


process.highPtTripletStepTrajectoryBuilder = cms.PSet(
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

process.highPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryFilterBase')
    ))
)

process.highPtTripletStepTrajectoryFilterBase = cms.PSet(
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


process.initialStepTrajectoryBuilder = cms.PSet(
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


process.initialStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryFilterBase')
    ))
)

process.initialStepTrajectoryFilterBase = cms.PSet(
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


#process.jetCoreRegionalStepTrajectoryBuilder = cms.PSet(
    #ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    #MeasurementTrackerName = cms.string(''),
    #TTRHBuilder = cms.string('WithTrackAngle'),
    #alwaysUseInvalidHits = cms.bool(True),
    #bestHitOnly = cms.bool(True),
    #estimator = cms.string('jetCoreRegionalStepChi2Est'),
    #foundHitBonus = cms.double(10.0),
    #inOutTrajectoryFilter = cms.PSet(
        #refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    #),
    #intermediateCleaning = cms.bool(True),
    #keepOriginalIfRebuildFails = cms.bool(False),
    #lockHits = cms.bool(True),
    #lostHitPenalty = cms.double(30.0),
    #maxCand = cms.int32(50),
    #maxDPhiForLooperReconstruction = cms.double(2.0),
    #maxPtForLooperReconstruction = cms.double(0.7),
    #minNrOfHitsForRebuild = cms.int32(5),
    #propagatorAlong = cms.string('PropagatorWithMaterial'),
    #propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    #requireSeedHitsInRebuild = cms.bool(True),
    #trajectoryFilter = cms.PSet(
        #refToPSet_ = cms.string('jetCoreRegionalStepTrajectoryFilter')
    #),
    #updator = cms.string('KFUpdator'),
    #useSameTrajFilter = cms.bool(True)
#)
#
#process.jetCoreRegionalStepTrajectoryFilter = cms.PSet(
    #ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    #chargeSignificance = cms.double(-1.0),
    #constantValueForLostHitsFractionFilter = cms.double(2.0),
    #extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    #maxCCCLostHits = cms.int32(9999),
    #maxConsecLostHits = cms.int32(1),
    #maxLostHits = cms.int32(999),
    #maxLostHitsFraction = cms.double(0.1),
    #maxNumberOfHits = cms.int32(100),
    #minGoodStripCharge = cms.PSet(
        #refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    #),
    #minHitsMinPt = cms.int32(3),
    #minNumberOfHitsForLoopers = cms.int32(13),
    #minNumberOfHitsPerLoop = cms.int32(4),
    #minPt = cms.double(0.1),
    #minimumNumberOfHits = cms.int32(4),
    #nSigmaMinPt = cms.double(5.0),
    #pixelSeedExtension = cms.bool(False),
    #seedExtension = cms.int32(0),
    #seedPairPenalty = cms.int32(0),
    #strictSeedExtension = cms.bool(False)
#)


process.lowPtQuadStepTrajectoryBuilder = cms.PSet(
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

process.lowPtQuadStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('lowPtQuadStepTrajectoryFilterBase')
    ))
)

process.lowPtQuadStepTrajectoryFilterBase = cms.PSet(
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

process.lowPtTripletStepStandardTrajectoryFilter = cms.PSet(
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

process.lowPtTripletStepTrajectoryBuilder = cms.PSet(
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

process.lowPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('lowPtTripletStepStandardTrajectoryFilter')
    ))
)


process.mixedTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('mixedTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('mixedTripletStepPropagator'),
    propagatorOpposite = cms.string('mixedTripletStepPropagatorOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('mixedTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.mixedTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
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
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)


process.pixelLessStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('pixelLessStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('pixelLessStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.pixelLessStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.pixelPairStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('pixelPairStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('pixelPairStepTrajectoryFilterInOut')
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
        refToPSet_ = cms.string('pixelPairStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.pixelPairStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('pixelPairStepTrajectoryFilterBase')
    ))
)

process.pixelPairStepTrajectoryFilterBase = cms.PSet(
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
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.pixelPairStepTrajectoryFilterInOut = cms.PSet(
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
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.pixelPairStepTrajectoryFilterShape = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)


process.tobTecStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('tobTecStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('tobTecStepInOutTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('tobTecStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.tobTecStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)


process.tobTecStepInOutTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)


process.MEtoEDMConverter = cms.EDProducer("MEtoEDMConverter",
    Frequency = cms.untracked.int32(50),
    MEPathToSave = cms.untracked.string(''),
    Name = cms.untracked.string('MEtoEDMConverter'),
    Verbosity = cms.untracked.int32(0),
    deleteAfterCopy = cms.untracked.bool(True)
)


process.MeasurementTrackerEvent = cms.EDProducer("MeasurementTrackerEventProducer",
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


process.ak4CaloJetsForTrk = cms.EDProducer("FastjetJetProducer",
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


process.caloTowerForTrk = cms.EDProducer("CaloTowersCreator",
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


process.chargeCut2069Clusters = cms.EDProducer("ClusterChargeMasker",
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)


process.detachedQuadStep = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorDetachedQuadStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.5, 0.0, 0.5),
    src = cms.InputTag("detachedQuadStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.detachedQuadStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtTripletStep","QualityMasks"),
    trajectories = cms.InputTag("lowPtTripletStepTracks")
)


process.detachedQuadStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"),
    trackingRegions = cms.InputTag("detachedQuadStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.detachedQuadStepHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0),
    CAPhiCut = cms.double(0),
    CAThetaCut = cms.double(0.0011),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("detachedQuadStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(2),
        value1 = cms.double(500),
        value2 = cms.double(100)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets__reRECO'),
    useBendingCorrection = cms.bool(True)
)


process.detachedQuadStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters")
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


process.detachedQuadStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
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
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets__reRECO'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets")
)


process.detachedQuadStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('detachedQuadStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('detachedQuadStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("detachedQuadStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("detachedQuadStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.detachedQuadStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(15.0),
        originRadius = cms.double(1.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.3),
        useMultipleScattering = cms.bool(False)
    )
)


process.detachedQuadStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('detachedQuadStep'),
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
    src = cms.InputTag("detachedQuadStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.detachedTripletStep = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorDetachedTripletStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.2, 0.3, 0.8),
    src = cms.InputTag("detachedTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.detachedTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedQuadStep","QualityMasks"),
    trajectories = cms.InputTag("detachedQuadStepTracks")
)


process.detachedTripletStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("lowPtTripletStepSeeds")
)


process.detachedTripletStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.detachedTripletStepHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.2),
    CAPhiCut = cms.double(0),
    CAThetaCut = cms.double(0.001),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("detachedTripletStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(2),
        value1 = cms.double(300),
        value2 = cms.double(10)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets__reRECO'),
    useBendingCorrection = cms.bool(True)
)


process.detachedTripletStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters")
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
        'BPix2+BPix3+FPix1_pos', 
        'BPix2+BPix3+FPix1_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+FPix3_pos', 
        'FPix1_neg+FPix2_neg+FPix3_neg'
    )
)


process.detachedTripletStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
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
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets__reRECO'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets")
)


process.detachedTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('detachedTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('detachedTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("detachedTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.detachedTripletStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(15.0),
        originRadius = cms.double(1.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.25),
        useMultipleScattering = cms.bool(False)
    )
)


process.detachedTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('detachedTripletStep'),
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
    src = cms.InputTag("detachedTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.duplicateTrackCandidates = cms.EDProducer("DuplicateTrackMerger",
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


process.duplicateTrackClassifier = cms.EDProducer("TrackCutClassifier",
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


process.earlyGeneralTracks = cms.EDProducer("TrackCollectionMerger",
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
        'lowPtTripletStep', 
        'detachedQuadStep', 
        'detachedTripletStep', 
        'pixelPairStep', 
        'mixedTripletStep', 
        'pixelLessStep', 
        'tobTecStep'
    ),
    lostHitPenalty = cms.double(5),
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag(
        "initialStepTracks", "highPtTripletStepTracks", "lowPtQuadStepTracks", "lowPtTripletStepTracks", 
        "detachedQuadStepTracks", "detachedTripletStepTracks", "pixelPairStepTracks", "mixedTripletStepTracks", "pixelLessStepTracks", 
        "tobTecStepTracks"
    )
)


process.firstStepPrimaryVertices = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
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


process.firstStepPrimaryVerticesUnsorted = cms.EDProducer("PrimaryVertexProducer",
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


process.generalTracks = cms.EDProducer("DuplicateListMerger",
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


process.highPtTripletStep = cms.EDProducer("TrackMVAClassifierPrompt",
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


process.highPtTripletStepClusters = cms.EDProducer("TrackClusterRemover",
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


process.highPtTripletStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("highPtTripletStepSeeds")
)


process.highPtTripletStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.highPtTripletStepHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
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


process.highPtTripletStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
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


process.highPtTripletStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
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


process.highPtTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
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


process.highPtTripletStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
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


process.highPtTripletStepTracks = cms.EDProducer("TrackProducer",
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


process.initialStep = cms.EDProducer("TrackMVAClassifierPrompt",
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


process.initialStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("initialStepSeeds")
)


process.initialStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("initialStepSeedLayers"),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.initialStepHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
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


process.initialStepHitTriplets = cms.EDProducer("PixelTripletHLTEDProducer",
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


process.initialStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
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


process.initialStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
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


process.initialStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
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


process.initialStepTrackRefsForJets = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("initialStepTracks")
)


process.initialStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
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


process.initialStepTracks = cms.EDProducer("TrackProducer",
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


#process.jetCoreClusterSplitter = cms.EDProducer("JetCoreClusterSplitter",
    #centralMIPCharge = cms.double(26000),
    #chargeFractionMin = cms.double(2.0),
    #chargePerUnit = cms.double(2000),
    #cores = cms.InputTag("ak5CaloJets"),
    #deltaRmax = cms.double(0.05),
    #forceXError = cms.double(100),
    #forceYError = cms.double(150),
    #fractionalWidth = cms.double(0.4),
    #pixelCPE = cms.string('PixelCPEGeneric'),
    #pixelClusters = cms.InputTag("siPixelCluster"),
    #ptMin = cms.double(200),
    #verbose = cms.bool(False),
    #vertices = cms.InputTag("offlinePrimaryVertices")
#)
#
#
#process.jetCoreRegionalStep = cms.EDProducer("TrackMVAClassifierPrompt",
    #beamspot = cms.InputTag("offlineBeamSpot"),
    #ignoreVertices = cms.bool(False),
    #mva = cms.PSet(
        #GBRForestFileName = cms.string(''),
        #GBRForestLabel = cms.string('MVASelectorJetCoreRegionalStep_Phase1')
    #),
    #qualityCuts = cms.vdouble(-0.2, 0.0, 0.4),
    #src = cms.InputTag("jetCoreRegionalStepTracks"),
    #vertices = cms.InputTag("firstStepPrimaryVertices")
#)
#
#
#process.jetCoreRegionalStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    #clusterCheck = cms.InputTag("trackerClusterCheck"),
    #layerPairs = cms.vuint32(0),
    #maxElement = cms.uint32(1000000),
    #produceIntermediateHitDoublets = cms.bool(False),
    #produceSeedingHitSets = cms.bool(True),
    #seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"),
    #trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"),
    #trackingRegionsSeedingLayers = cms.InputTag("")
#)
#
#
#process.jetCoreRegionalStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    #BPix = cms.PSet(
        #HitProducer = cms.string('siPixelRecHits'),
        #TTRHBuilder = cms.string('WithTrackAngle'),
        #hitErrorRPhi = cms.double(0.0027),
        #hitErrorRZ = cms.double(0.006),
        #useErrorsFromParam = cms.bool(True)
    #),
    #FPix = cms.PSet(
        #HitProducer = cms.string('siPixelRecHits'),
        #TTRHBuilder = cms.string('WithTrackAngle'),
        #hitErrorRPhi = cms.double(0.0051),
        #hitErrorRZ = cms.double(0.0036),
        #useErrorsFromParam = cms.bool(True)
    #),
    #TIB = cms.PSet(
        #TTRHBuilder = cms.string('WithTrackAngle'),
        #clusterChargeCut = cms.PSet(
            #refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        #),
        #matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    #),
    #layerList = cms.vstring(
        #'BPix1+BPix2', 
        #'BPix1+BPix3', 
        #'BPix1+BPix4', 
        #'BPix2+BPix3', 
        #'BPix2+BPix4', 
        #'BPix3+BPix4', 
        #'BPix1+FPix1_pos', 
        #'BPix1+FPix1_neg', 
        #'BPix2+FPix1_pos', 
        #'BPix2+FPix1_neg', 
        #'FPix1_pos+FPix2_pos', 
        #'FPix1_neg+FPix2_neg', 
        #'FPix1_pos+FPix3_pos', 
        #'FPix1_neg+FPix3_neg', 
        #'FPix2_pos+FPix3_pos', 
        #'FPix2_neg+FPix3_neg', 
        #'BPix4+TIB1', 
        #'BPix4+TIB2'
    #)
#)
#
#
#process.jetCoreRegionalStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    #MinOneOverPtError = cms.double(1),
    #OriginTransverseErrorMultiplier = cms.double(1),
    #SeedComparitorPSet = cms.PSet(
        #ComponentName = cms.string('none')
    #),
    #SeedMomentumForBOFF = cms.double(5),
    #TTRHBuilder = cms.string('WithTrackAngle'),
    #forceKinematicWithRegionDirection = cms.bool(True),
    #magneticField = cms.string('ParabolicMf'),
    #mightGet = cms.untracked.vstring('RegionsSeedingHitSets_jetCoreRegionalStepHitDoublets__reRECO'),
    #propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    #seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets")
#)
#
#
#process.jetCoreRegionalStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    #MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    #NavigationSchool = cms.string('SimpleNavigationSchool'),
    #RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    #SimpleMagneticField = cms.string(''),
    #TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    #TrajectoryBuilderPSet = cms.PSet(
        #refToPSet_ = cms.string('jetCoreRegionalStepTrajectoryBuilder')
    #),
    #TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    #TransientInitialStateEstimatorParameters = cms.PSet(
        #numberMeasurementsForFit = cms.int32(4),
        #propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        #propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    #),
    #cleanTrajectoryAfterInOut = cms.bool(True),
    #doSeedingRegionRebuilding = cms.bool(True),
    #maxNSeeds = cms.uint32(500000),
    #maxSeedsBeforeCleaning = cms.uint32(10000),
    #reverseTrajectories = cms.bool(False),
    #src = cms.InputTag("jetCoreRegionalStepSeeds"),
    #useHitsSplitting = cms.bool(True)
#)
#
#
#process.jetCoreRegionalStepTrackingRegions = cms.EDProducer("TauRegionalPixelSeedTrackingRegionEDProducer",
    #RegionPSet = cms.PSet(
        #JetSrc = cms.InputTag("jetsForCoreTracking"),
        #deltaEtaRegion = cms.double(0.2),
        #deltaPhiRegion = cms.double(0.2),
        #howToUseMeasurementTracker = cms.string('Never'),
        #measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"),
        #originHalfLength = cms.double(0.2),
        #originRadius = cms.double(0.2),
        #ptMin = cms.double(10),
        #searchOpt = cms.bool(False),
        #vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices")
    #)
#)
#
#
#process.jetCoreRegionalStepTracks = cms.EDProducer("TrackProducer",
    #AlgorithmName = cms.string('jetCoreRegionalStep'),
    #Fitter = cms.string('FlexibleKFFittingSmoother'),
    #GeometricInnerState = cms.bool(False),
    #MeasurementTracker = cms.string(''),
    #MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    #NavigationSchool = cms.string('SimpleNavigationSchool'),
    #Propagator = cms.string('RungeKuttaTrackerPropagator'),
    #SimpleMagneticField = cms.string(''),
    #TTRHBuilder = cms.string('WithAngleAndTemplate'),
    #TrajectoryInEvent = cms.bool(False),
    #alias = cms.untracked.string('ctfWithMaterialTracks'),
    #beamSpot = cms.InputTag("offlineBeamSpot"),
    #clusterRemovalInfo = cms.InputTag(""),
    #src = cms.InputTag("jetCoreRegionalStepTrackCandidates"),
    #useHitsSplitting = cms.bool(False),
    #useSimpleMF = cms.bool(False)
#)


process.lowPtQuadStep = cms.EDProducer("TrackMVAClassifierPrompt",
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


process.lowPtQuadStepClusters = cms.EDProducer("TrackClusterRemover",
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


process.lowPtQuadStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.lowPtQuadStepHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
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


process.lowPtQuadStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
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


process.lowPtQuadStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
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


process.lowPtQuadStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
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


process.lowPtQuadStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
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


process.lowPtQuadStepTracks = cms.EDProducer("TrackProducer",
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


process.lowPtTripletStep = cms.EDProducer("TrackMVAClassifierPrompt",
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


process.lowPtTripletStepClusters = cms.EDProducer("TrackClusterRemover",
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


process.lowPtTripletStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.lowPtTripletStepHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
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


process.lowPtTripletStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
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


process.lowPtTripletStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
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


process.lowPtTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
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


process.lowPtTripletStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
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


process.lowPtTripletStepTracks = cms.EDProducer("TrackProducer",
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


process.mergedDuplicateTracks = cms.EDProducer("TrackProducer",
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


process.mixedTripletStep = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorMixedTripletStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.5, 0.0, 0.5),
    src = cms.InputTag("mixedTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.mixedTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelPairStep","QualityMasks"),
    trajectories = cms.InputTag("pixelPairStepTracks")
)


process.mixedTripletStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("mixedTripletStepSeeds")
)


process.mixedTripletStepHitDoubletsA = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.mixedTripletStepHitDoubletsB = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.mixedTripletStepHitTripletsA = cms.EDProducer("PixelTripletLargeTipEDProducer",
    doublets = cms.InputTag("mixedTripletStepHitDoubletsA"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    maxElement = cms.uint32(1000000),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA__reRECO'),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.mixedTripletStepHitTripletsB = cms.EDProducer("PixelTripletLargeTipEDProducer",
    doublets = cms.InputTag("mixedTripletStepHitDoubletsB"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    maxElement = cms.uint32(1000000),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB__reRECO'),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.mixedTripletStepSeedLayersA = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg'
    )
)


process.mixedTripletStepSeedLayersB = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters")
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("mixedTripletStepClusters")
    ),
    layerList = cms.vstring('BPix3+BPix4+TIB1')
)


process.mixedTripletStepSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"), cms.InputTag("mixedTripletStepSeedsB"))
)


process.mixedTripletStepSeedsA = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA__reRECO'
    ),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA")
)


process.mixedTripletStepSeedsB = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB__reRECO'
    ),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB")
)


process.mixedTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('mixedTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('mixedTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("mixedTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.mixedTripletStepTrackingRegionsA = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(15.0),
        originRadius = cms.double(1.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.4),
        useMultipleScattering = cms.bool(False)
    )
)


process.mixedTripletStepTrackingRegionsB = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(10.0),
        originRadius = cms.double(1.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        useMultipleScattering = cms.bool(False)
    )
)


process.mixedTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('mixedTripletStep'),
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
    src = cms.InputTag("mixedTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.pixelLessLayerPairs4PixelLessTracking = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(

    ),
    FPix = cms.PSet(

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
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB = cms.PSet(

    ),
    TIB1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TID = cms.PSet(

    ),
    TID1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(3),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TID2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(3),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TID3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'TIB1+TIB2', 
        'TIB1+TIB3', 
        'TIB2+TIB3', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TIB2+TID1_pos', 
        'TIB2+TID1_neg', 
        'TIB1+TID2_pos', 
        'TIB1+TID2_neg', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TID3_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TID3_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg'
    )
)


process.pixelLessStep = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorPixelLessStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.4, 0.0, 0.4),
    src = cms.InputTag("pixelLessStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.pixelLessStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("mixedTripletStep","QualityMasks"),
    trajectories = cms.InputTag("mixedTripletStepTracks")
)


process.pixelLessStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelLessStepSeeds")
)


process.pixelLessStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("pixelLessStepSeedLayers"),
    trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.pixelLessStepHitTriplets = cms.EDProducer("MultiHitFromChi2EDProducer",
    ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    chi2VsPtCut = cms.bool(True),
    chi2_cuts = cms.vdouble(3, 4, 5, 5),
    detIdsToDebug = cms.vint32(0, 0, 0),
    doublets = cms.InputTag("pixelLessStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    extraPhiKDBox = cms.double(0.005),
    extraRKDBox = cms.double(0.2),
    extraZKDBox = cms.double(0.2),
    fnSigmaRZ = cms.double(2),
    maxChi2 = cms.double(5),
    maxElement = cms.uint32(1000000),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets__reRECO'),
    phiPreFiltering = cms.double(0.3),
    pt_interv = cms.vdouble(0.4, 0.7, 1, 2),
    refitHits = cms.bool(True),
    useFixedPreFiltering = cms.bool(False)
)


process.pixelLessStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters")
    ),
    MTID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters")
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TIB1+TIB2+MTIB3', 
        'TIB1+TIB2+MTIB4', 
        'TIB1+TIB2+MTID1_pos', 
        'TIB1+TIB2+MTID1_neg', 
        'TID1_pos+TID2_pos+TID3_pos', 
        'TID1_neg+TID2_neg+TID3_neg', 
        'TID1_pos+TID2_pos+MTID3_pos', 
        'TID1_neg+TID2_neg+MTID3_neg', 
        'TID1_pos+TID2_pos+MTEC1_pos', 
        'TID1_neg+TID2_neg+MTEC1_neg', 
        'TID2_pos+TID3_pos+TEC1_pos', 
        'TID2_neg+TID3_neg+TEC1_neg', 
        'TID2_pos+TID3_pos+MTEC1_pos', 
        'TID2_neg+TID3_neg+MTEC1_neg', 
        'TEC1_pos+TEC2_pos+TEC3_pos', 
        'TEC1_neg+TEC2_neg+TEC3_neg', 
        'TEC1_pos+TEC2_pos+MTEC3_pos', 
        'TEC1_neg+TEC2_neg+MTEC3_neg', 
        'TEC1_pos+TEC2_pos+TEC4_pos', 
        'TEC1_neg+TEC2_neg+TEC4_neg', 
        'TEC1_pos+TEC2_pos+MTEC4_pos', 
        'TEC1_neg+TEC2_neg+MTEC4_neg', 
        'TEC2_pos+TEC3_pos+TEC4_pos', 
        'TEC2_neg+TEC3_neg+TEC4_neg', 
        'TEC2_pos+TEC3_pos+MTEC4_pos', 
        'TEC2_neg+TEC3_neg+MTEC4_neg', 
        'TEC2_pos+TEC3_pos+TEC5_pos', 
        'TEC2_neg+TEC3_neg+TEC5_neg', 
        'TEC2_pos+TEC3_pos+TEC6_pos', 
        'TEC2_neg+TEC3_neg+TEC6_neg', 
        'TEC3_pos+TEC4_pos+TEC5_pos', 
        'TEC3_neg+TEC4_neg+TEC5_neg', 
        'TEC3_pos+TEC4_pos+MTEC5_pos', 
        'TEC3_neg+TEC4_neg+MTEC5_neg', 
        'TEC3_pos+TEC5_pos+TEC6_pos', 
        'TEC3_neg+TEC5_neg+TEC6_neg', 
        'TEC4_pos+TEC5_pos+TEC6_pos', 
        'TEC4_neg+TEC5_neg+TEC6_neg'
    )
)


process.pixelLessStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
                ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets__reRECO', 
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets__reRECO'
    ),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("pixelLessStepHitTriplets")
)


process.pixelLessStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('pixelLessStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('pixelLessStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("pixelLessStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.pixelLessStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(12.0),
        originRadius = cms.double(1.0),
        precise = cms.bool(True),
        ptMin = cms.double(0.4),
        useMultipleScattering = cms.bool(False)
    )
)


process.pixelLessStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('pixelLessStep'),
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
    src = cms.InputTag("pixelLessStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.pixelPairStep = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorPixelPairStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.2, 0.0, 0.3),
    src = cms.InputTag("pixelPairStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.pixelPairStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedTripletStep","QualityMasks"),
    trajectories = cms.InputTag("detachedTripletStepTracks")
)


process.pixelPairStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelPairStepSeeds")
)


process.pixelPairStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("pixelPairStepSeedLayers"),
    trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.pixelPairStepHitDoubletsB = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag(""),
    trackingRegions = cms.InputTag(""),
    trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB")
)


process.pixelPairStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters")
    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg'
    )
)


process.pixelPairStepSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag("pixelPairStepSeedsA", "pixelPairStepSeedsB")
)


process.pixelPairStepSeedsA = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets__reRECO'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets")
)


process.pixelPairStepSeedsB = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB__reRECO'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB")
)


process.pixelPairStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('pixelPairStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("pixelPairStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.pixelPairStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(5),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag(myCollection),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)


process.pixelPairStepTrackingRegionsSeedLayersB = cms.EDProducer("PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        deltaEta_Cand = cms.double(-1),
        deltaPhi_Cand = cms.double(-1),
        extraEta = cms.double(0),
        extraPhi = cms.double(0),
        input = cms.InputTag(""),
        maxNVertices = cms.int32(5),
        measurementTrackerName = cms.InputTag(""),
        nSigmaZBeamSpot = cms.double(4),
        nSigmaZVertex = cms.double(3),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        searchOpt = cms.bool(False),
        seedingMode = cms.string('Global'),
        vertexCollection = cms.InputTag("firstStepPrimaryVertices"),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVertex = cms.double(0.03)
    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
    createPlottingFiles = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    ignoreSingleFPixPanelModules = cms.bool(True),
    inactivePixelDetectorLabels = cms.VInputTag("siPixelDigis"),
    layerList = cms.vstring(
        'BPix1+BPix4', 
        'BPix2+BPix4', 
        'BPix3+BPix4', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix1+FPix3_pos', 
        'BPix1+FPix3_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'BPix3+FPix1_pos', 
        'BPix3+FPix1_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix3_pos', 
        'FPix1_neg+FPix3_neg', 
        'FPix2_pos+FPix3_pos', 
        'FPix2_neg+FPix3_neg'
    )
)


process.pixelPairStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('pixelPairStep'),
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
    src = cms.InputTag("pixelPairStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.preDuplicateMergingGeneralTracks = cms.EDProducer("TrackCollectionMerger",
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    enableMerging = cms.bool(True),
    foundHitBonus = cms.double(100.0),
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'#, 
        #'muonSeededTracksInOutClassifier', 
        #'muonSeededTracksOutInClassifier'
    ),
    lostHitPenalty = cms.double(1.0),
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag("earlyGeneralTracks")#, "muonSeededTracksInOut", "muonSeededTracksOutIn")
)


process.siPixelClusterShapeCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag(myCollection)
)


process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag(myCollection)
)


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


process.tobTecStep = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorTobTecStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.6, -0.45, -0.3),
    src = cms.InputTag("tobTecStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.tobTecStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelLessStep","QualityMasks"),
    trajectories = cms.InputTag("pixelLessStepTracks")
)


process.tobTecStepHitDoubletsPair = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.tobTecStepHitDoubletsTripl = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.tobTecStepHitTripletsTripl = cms.EDProducer("MultiHitFromChi2EDProducer",
    ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    chi2VsPtCut = cms.bool(True),
    chi2_cuts = cms.vdouble(3, 4, 5, 5),
    detIdsToDebug = cms.vint32(0, 0, 0),
    doublets = cms.InputTag("tobTecStepHitDoubletsTripl"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    extraPhiKDBox = cms.double(0.01),
    extraRKDBox = cms.double(0.2),
    extraZKDBox = cms.double(0.2),
    fnSigmaRZ = cms.double(2),
    maxChi2 = cms.double(5),
    maxElement = cms.uint32(1000000),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl__reRECO'),
    phiPreFiltering = cms.double(0.3),
    pt_interv = cms.vdouble(0.4, 0.7, 1, 2),
    refitHits = cms.bool(True),
    useFixedPreFiltering = cms.bool(False)
)


process.tobTecStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTiny')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTiny')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters")
    ),
    layerList = cms.vstring(
        'TOB1+TOB2', 
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg'
    )
)


process.tobTecStepSeedLayersPair = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters")
    ),
    layerList = cms.vstring(
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_pos+TEC3_pos', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_pos+TEC4_pos', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_pos+TEC5_pos', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_pos+TEC6_pos', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_pos+TEC7_pos', 
        'TEC6_neg+TEC7_neg'
    )
)


process.tobTecStepSeedLayersTripl = cms.EDProducer("SeedingLayersEDProducer",
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters")
    ),
    layerList = cms.vstring(
        'TOB1+TOB2+MTOB3', 
        'TOB1+TOB2+MTOB4', 
        'TOB1+TOB2+MTEC1_pos', 
        'TOB1+TOB2+MTEC1_neg'
    )
)


process.tobTecStepSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("tobTecStepSeedsTripl"), cms.InputTag("tobTecStepSeedsPair"))
)


process.tobTecStepSeedsPair = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair__reRECO'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair")
)


process.tobTecStepSeedsTripl = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl__reRECO', 
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl__reRECO'
    ),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl")
)


process.tobTecStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('tobTecStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('tobTecStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("tobTecStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("tobTecStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.tobTecStepTrackingRegionsPair = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(30.0),
        originRadius = cms.double(6.0),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        useMultipleScattering = cms.bool(False)
    )
)


process.tobTecStepTrackingRegionsTripl = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(20.0),
        originRadius = cms.double(3.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.55),
        useMultipleScattering = cms.bool(False)
    )
)


process.tobTecStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('tobTecStep'),
    Fitter = cms.string('tobTecFlexibleKFFittingSmoother'),
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
    src = cms.InputTag("tobTecStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.trackerClusterCheck = cms.EDProducer("ClusterCheckerEDProducer",
    ClusterCollectionLabel = cms.InputTag(myCollection),
    MaxNumberOfCosmicClusters = cms.uint32(400000),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag(myCollection),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    doClusterCheck = cms.bool(False),
    silentClusterCheck = cms.untracked.bool(False)
)


process.firstStepGoodPrimaryVertices = cms.EDFilter("PrimaryVertexObjectFilter",
    filterParams = cms.PSet(
        maxRho = cms.double(2.0),
        maxZ = cms.double(15.0),
        minNdof = cms.double(25.0)
    ),
    src = cms.InputTag("firstStepPrimaryVertices")
)


process.jetsForCoreTracking = cms.EDFilter("CandPtrSelector",
    cut = cms.string('pt > 100 && abs(eta) < 2.5'),
    src = cms.InputTag("ak4CaloJetsForTrk")
)


#process.jetsForCoreTrackingPreSplitting = cms.EDFilter("CandPtrSelector",
    #cut = cms.string('pt > 100 && abs(eta) < 2.5'),
    #src = cms.InputTag("ak4CaloJetsForTrkPreSplitting")
#)


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
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
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


process.detachedQuadStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('detachedQuadStepChi2Est'),
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


process.detachedQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('detachedQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.detachedTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('detachedTripletStepChi2Est'),
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


process.detachedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('detachedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
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


process.highPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('highPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
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


process.jetCoreRegionalStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('jetCoreRegionalStepChi2Est'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
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


process.mixedTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('mixedTripletStepChi2Est'),
    MaxChi2 = cms.double(16.0),
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


process.mixedTripletStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('mixedTripletStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    )
)


process.mixedTripletStepPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('mixedTripletStepPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.mixedTripletStepPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('mixedTripletStepPropagatorOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.mixedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('mixedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.pixelLessStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('pixelLessStepChi2Est'),
    MaxChi2 = cms.double(16.0),
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


process.pixelLessStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('pixelLessStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    doStripShapeCut = cms.bool(False)
)


process.pixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('pixelLessStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.pixelPairStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('pixelPairStepChi2Est'),
    MaxChi2 = cms.double(9.0),
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


process.pixelPairStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('pixelPairStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.095)
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


process.tobTecFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('tobTecFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('tobTecStepFitterSmootherForLoopers'),
    standardFitter = cms.string('tobTecStepFitterSmoother')
)


process.tobTecStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('tobTecStepChi2Est'),
    MaxChi2 = cms.double(16.0),
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


process.tobTecStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('tobTecStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    doStripShapeCut = cms.bool(False)
)


process.tobTecStepFitterSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('tobTecStepFitterSmoother'),
    EstimateCut = cms.double(30),
    Fitter = cms.string('tobTecStepRKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('tobTecStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.tobTecStepFitterSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('tobTecStepFitterSmootherForLoopers'),
    EstimateCut = cms.double(30),
    Fitter = cms.string('tobTecStepRKFitterForLoopers'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('tobTecStepRKSmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.tobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('tobTecStepRKFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.tobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('tobTecStepRKFitterForLoopers'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.tobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('tobTecStepRKSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.tobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('tobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.tobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('tobTecStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.09)
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


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
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


process.reconstruction_step = cms.Path(cms.Task(process.MeasurementTrackerEvent, process.ak4CaloJetsForTrk, process.caloTowerForTrk, process.chargeCut2069Clusters, process.detachedQuadStep, process.detachedQuadStepClusters, process.detachedQuadStepHitDoublets, process.detachedQuadStepHitQuadruplets, process.detachedQuadStepSeedLayers, process.detachedQuadStepSeeds, process.detachedQuadStepTrackCandidates, process.detachedQuadStepTrackingRegions, process.detachedQuadStepTracks, process.detachedTripletStep, process.detachedTripletStepClusters, process.detachedTripletStepHitDoublets, process.detachedTripletStepHitTriplets, process.detachedTripletStepSeedLayers, process.detachedTripletStepSeedClusterMask, process.detachedTripletStepSeeds, process.detachedTripletStepTrackCandidates, process.detachedTripletStepTrackingRegions, process.detachedTripletStepTracks, process.duplicateTrackCandidates, process.duplicateTrackClassifier, process.earlyGeneralTracks, process.firstStepGoodPrimaryVertices, process.firstStepPrimaryVertices, process.firstStepPrimaryVerticesUnsorted, process.generalTracks, process.highPtTripletStep, process.highPtTripletStepClusters, process.highPtTripletStepHitDoublets, process.highPtTripletStepHitTriplets, process.highPtTripletStepSeedLayers, process.highPtTripletStepSeeds, process.highPtTripletStepTrackCandidates, process.highPtTripletStepTrackingRegions, process.highPtTripletStepTracks, process.initialStep, process.initialStepHitDoublets, process.initialStepHitQuadruplets, process.initialStepSeedLayers, process.initialStepSeedClusterMask, process.initialStepSeeds, process.initialStepTrackCandidates, process.initialStepTrackRefsForJets, process.initialStepTrackingRegions, process.initialStepTracks, process.jetsForCoreTracking, process.lowPtQuadStep, process.lowPtQuadStepClusters, process.lowPtQuadStepHitDoublets, process.lowPtQuadStepHitQuadruplets, process.lowPtQuadStepSeedLayers, process.lowPtQuadStepSeeds, process.lowPtQuadStepTrackCandidates, process.lowPtQuadStepTrackingRegions, process.lowPtQuadStepTracks, process.lowPtTripletStep, process.lowPtTripletStepClusters, process.lowPtTripletStepHitDoublets, process.lowPtTripletStepHitTriplets, process.lowPtTripletStepSeedLayers, process.lowPtTripletStepSeeds, process.lowPtTripletStepTrackCandidates, process.lowPtTripletStepTrackingRegions, process.lowPtTripletStepTracks, process.mergedDuplicateTracks, process.mixedTripletStep, process.mixedTripletStepClusters, process.mixedTripletStepHitDoubletsA, process.mixedTripletStepHitDoubletsB, process.mixedTripletStepHitTripletsA, process.mixedTripletStepHitTripletsB, process.mixedTripletStepSeedLayersA, process.mixedTripletStepSeedLayersB, process.mixedTripletStepSeedClusterMask, process.mixedTripletStepSeeds, process.mixedTripletStepSeedsA, process.mixedTripletStepSeedsB, process.mixedTripletStepTrackCandidates, process.mixedTripletStepTrackingRegionsA, process.mixedTripletStepTrackingRegionsB, process.mixedTripletStepTracks, process.pixelLessStep, process.pixelLessStepClusters, process.pixelLessStepHitDoublets, process.pixelLessStepHitTriplets, process.pixelLessStepSeedLayers, process.pixelLessStepSeedClusterMask, process.pixelLessStepSeeds, process.pixelLessStepTrackCandidates, process.pixelLessStepTrackingRegions, process.pixelLessStepTracks, process.pixelPairStep, process.pixelPairStepClusters, process.pixelPairStepHitDoublets, process.pixelPairStepHitDoubletsB, process.pixelPairStepSeedLayers, process.pixelPairStepSeeds, process.pixelPairStepSeedsA, process.pixelPairStepSeedsB, process.pixelPairStepTrackCandidates, process.pixelPairStepTrackingRegions, process.pixelPairStepTrackingRegionsSeedLayersB, process.pixelPairStepTracks, process.preDuplicateMergingGeneralTracks, process.siPixelClusterShapeCache, process.siPixelRecHits, process.tobTecStep, process.tobTecStepClusters, process.tobTecStepHitDoubletsPair, process.tobTecStepHitDoubletsTripl, process.tobTecStepHitTripletsTripl, process.tobTecStepSeedLayersPair, process.tobTecStepSeedLayersTripl, process.tobTecStepSeeds, process.tobTecStepSeedsPair, process.tobTecStepSeedsTripl, process.tobTecStepTrackCandidates, process.tobTecStepTrackingRegionsPair, process.tobTecStepTrackingRegionsTripl, process.tobTecStepTracks, process.trackerClusterCheck,process.siStripMatchedRecHits))


hits = "3"
myCollection = "rCluster"+hits


process.MeasurementTrackerEvent3 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection),
)

process.ak4CaloJetsForTrk3 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits),
)

process.caloTowerForTrk3 = process.caloTowerForTrk.clone()

process.chargeCut2069Clusters3 = process.chargeCut2069Clusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.detachedQuadStep3 = process.detachedQuadStep.clone(
    src = cms.InputTag("detachedQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedQuadStepClusters3 = process.detachedQuadStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtTripletStepTracks"+hits)
)

process.detachedQuadStepHitDoublets3 = process.detachedQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+hits)
)

process.detachedQuadStepHitQuadruplets3 = process.detachedQuadStepHitQuadruplets.clone(
    doublets = cms.InputTag("detachedQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+hits+'__reRECO'),

)

process.detachedQuadStepSeedLayers3 = process.detachedQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
)

process.detachedQuadStepSeeds3 = process.detachedQuadStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+hits)
)

process.detachedQuadStepTrackCandidates3 = process.detachedQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedQuadStepClusters"+hits),
    src = cms.InputTag("detachedQuadStepSeeds"+hits)
)

process.detachedQuadStepTrackingRegions3 = process.detachedQuadStepTrackingRegions.clone()

process.detachedQuadStepTracks3 = process.detachedQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedQuadStepTrackCandidates"+hits)
)

process.detachedTripletStep3 = process.detachedTripletStep.clone(
    src = cms.InputTag("detachedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedTripletStepClusters3 = process.detachedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedQuadStepTracks"+hits)
)

process.detachedTripletStepHitDoublets3 = process.detachedTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"+hits),
)

process.detachedTripletStepHitTriplets3 = process.detachedTripletStepHitTriplets.clone(
    doublets = cms.InputTag("detachedTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+hits+'__reRECO')
)

process.detachedTripletStepSeedLayers3 = process.detachedTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    )
)

process.detachedTripletStepSeedClusterMask3 = process.detachedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.detachedTripletStepSeeds3 = process.detachedTripletStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+hits)
)

process.detachedTripletStepTrackCandidates3 = process.detachedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"+hits),
    src = cms.InputTag("detachedTripletStepSeeds"+hits)
)

process.detachedTripletStepTrackingRegions3 = process.detachedTripletStepTrackingRegions.clone()

process.detachedTripletStepTracks3 = process.detachedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedTripletStepTrackCandidates"+hits)
)

process.duplicateTrackCandidates3 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.duplicateTrackClassifier3 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.earlyGeneralTracks3 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits, 
        'highPtTripletStep'+hits, 
#        'jetCoreRegionalStep'+hits, 
        'lowPtQuadStep'+hits, 
        'lowPtTripletStep'+hits, 
        'detachedQuadStep'+hits, 
        'detachedTripletStep'+hits, 
        'pixelPairStep'+hits, 
        'mixedTripletStep'+hits, 
        'pixelLessStep'+hits, 
        'tobTecStep'+hits
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits, 
        "detachedQuadStepTracks"+hits, "detachedTripletStepTracks"+hits, "pixelPairStepTracks"+hits, "mixedTripletStepTracks"+hits, "pixelLessStepTracks"+hits, 
        "tobTecStepTracks"+hits
    )
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

process.generalTracks3 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.highPtTripletStep3 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters3 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
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

process.highPtTripletStepSeedClusterMask3 = process.highPtTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("highPtTripletStepSeeds"+hits)
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

process.initialStep3 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepHitDoublets3 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitQuadruplets3 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
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

process.initialStepSeedClusterMask3 = process.initialStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepSeeds3 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates3 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilder')
    ),
    src = cms.InputTag("initialStepSeeds"+hits),
)

process.initialStepTrackRefsForJets3 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.initialStepTrackingRegions3 = process.initialStepTrackingRegions.clone()

process.initialStepTracks3 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits),
)

process.jetsForCoreTracking3 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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

process.mergedDuplicateTracks3 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.mixedTripletStep3 = process.mixedTripletStep.clone(
    src = cms.InputTag("mixedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.mixedTripletStepClusters3 = process.mixedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelPairStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelPairStepTracks"+hits)
)

process.mixedTripletStepHitDoubletsA3 = process.mixedTripletStepHitDoubletsA.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"+hits)
)

process.mixedTripletStepHitDoubletsB3 = process.mixedTripletStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"+hits)
)

process.mixedTripletStepHitTripletsA3 = process.mixedTripletStepHitTripletsA.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO')
)

process.mixedTripletStepHitTripletsB3 = process.mixedTripletStepHitTripletsB.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO')
)

process.mixedTripletStepSeedLayersA3 = process.mixedTripletStepSeedLayersA.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.mixedTripletStepSeedLayersB3 = process.mixedTripletStepSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    )
)

process.mixedTripletStepSeedClusterMask3 = process.mixedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepSeeds3 = process.mixedTripletStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"+hits), cms.InputTag("mixedTripletStepSeedsB"+hits))
)

process.mixedTripletStepSeedsA3 = process.mixedTripletStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+hits)
)

process.mixedTripletStepSeedsB3 = process.mixedTripletStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+hits)
)

process.mixedTripletStepTrackCandidates3 = process.mixedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"+hits),
    src = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepTrackingRegionsA3 = process.mixedTripletStepTrackingRegionsA.clone()

process.mixedTripletStepTrackingRegionsB3 = process.mixedTripletStepTrackingRegionsB.clone()

process.mixedTripletStepTracks3 = process.mixedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("mixedTripletStepTrackCandidates"+hits)
)

process.pixelLessStep3 = process.pixelLessStep.clone(
    src = cms.InputTag("pixelLessStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelLessStepClusters3 = process.pixelLessStepClusters.clone(
oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("mixedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("mixedTripletStepTracks"+hits)
)

process.pixelLessStepHitDoublets3 = process.pixelLessStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"+hits)
)

process.pixelLessStepHitTriplets3 = process.pixelLessStepHitTriplets.clone(
    doublets = cms.InputTag("pixelLessStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+hits+'__reRECO')
)

process.pixelLessStepSeedLayers3 = process.pixelLessStepSeedLayers.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    MTID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.pixelLessStepSeedClusterMask3 = process.pixelLessStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepSeeds3 = process.pixelLessStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+hits)
)

process.pixelLessStepTrackCandidates3 = process.pixelLessStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"+hits),
    src = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepTrackingRegions3 = process.pixelLessStepTrackingRegions.clone()

process.pixelLessStepTracks3 = process.pixelLessStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelLessStepTrackCandidates"+hits)
)


process.pixelPairStep3 = process.pixelPairStep.clone(
    src = cms.InputTag("pixelPairStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelPairStepClusters3 = process.pixelPairStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedTripletStepTracks"+hits)
)

process.pixelPairStepHitDoublets3 = process.pixelPairStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+hits)
)

process.pixelPairStepHitDoubletsB3 = process.pixelPairStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+hits)
)

process.pixelPairStepSeedLayers3 = process.pixelPairStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    )
)

process.pixelPairStepSeedClusterMask3 = process.pixelPairStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepSeeds3 = process.pixelPairStepSeeds.clone(
    seedCollections = cms.VInputTag("pixelPairStepSeedsA"+hits, "pixelPairStepSeedsB"+hits)
)

process.pixelPairStepSeedsA3 = process.pixelPairStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+hits)
)

process.pixelPairStepSeedsB3 = process.pixelPairStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+hits)
)

process.pixelPairStepTrackCandidates3 = process.pixelPairStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"+hits),
    src = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTrackingRegions3 = process.pixelPairStepTrackingRegions.clone(
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(5),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag(myCollection),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)

process.pixelPairStepTrackingRegionsSeedLayersB3 = process.pixelPairStepTrackingRegionsSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        deltaEta_Cand = cms.double(-1),
        deltaPhi_Cand = cms.double(-1),
        extraEta = cms.double(0),
        extraPhi = cms.double(0),
        input = cms.InputTag(""),
        maxNVertices = cms.int32(5),
        measurementTrackerName = cms.InputTag(""),
        nSigmaZBeamSpot = cms.double(4),
        nSigmaZVertex = cms.double(3),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        searchOpt = cms.bool(False),
        seedingMode = cms.string('Global'),
        vertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVertex = cms.double(0.03)
    )
)

process.pixelPairStepTracks3 = process.pixelPairStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelPairStepTrackCandidates"+hits)
)

process.preDuplicateMergingGeneralTracks3 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits 
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.siPixelClusterShapeCache3 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.siPixelRecHits3 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.tobTecStep3 = process.tobTecStep.clone(
    src = cms.InputTag("tobTecStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.tobTecStepClusters3 = process.tobTecStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelLessStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelLessStepTracks"+hits)
)

process.tobTecStepHitDoubletsPair3 = process.tobTecStepHitDoubletsPair.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"+hits)
)

process.tobTecStepHitDoubletsTripl3 = process.tobTecStepHitDoubletsTripl.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"+hits)
)

process.tobTecStepHitTripletsTripl3 = process.tobTecStepHitTripletsTripl.clone(
    doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+hits+'__reRECO')
)

process.tobTecStepSeedLayersPair3 = process.tobTecStepSeedLayersPair.clone(
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeedLayersTripl3 = process.tobTecStepSeedLayersTripl.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeeds3 = process.tobTecStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("tobTecStepSeedsTripl"+hits), cms.InputTag("tobTecStepSeedsPair"+hits))
)

process.tobTecStepSeedsPair3 = process.tobTecStepSeedsPair.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+hits)
)

process.tobTecStepSeedsTripl3 = process.tobTecStepSeedsTripl.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+hits)
)

process.tobTecStepTrackCandidates3 = process.tobTecStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("tobTecStepClusters"+hits),
    src = cms.InputTag("tobTecStepSeeds"+hits)
)

process.tobTecStepTrackingRegionsPair3 = process.tobTecStepTrackingRegionsPair.clone()

process.tobTecStepTrackingRegionsTripl3 = process.tobTecStepTrackingRegionsTripl.clone()

process.tobTecStepTracks3 = process.tobTecStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("tobTecStepTrackCandidates"+hits)
)

process.trackerClusterCheck3 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.siStripMatchedRecHits3 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)


process.reconstruction_step3 = cms.Path(cms.Task(process.MeasurementTrackerEvent3, process.ak4CaloJetsForTrk3, process.caloTowerForTrk3, process.chargeCut2069Clusters3, process.detachedQuadStep3, process.detachedQuadStepClusters3, process.detachedQuadStepHitDoublets3, process.detachedQuadStepHitQuadruplets3, process.detachedQuadStepSeedLayers3, process.detachedQuadStepSeeds3, process.detachedQuadStepTrackCandidates3, process.detachedQuadStepTrackingRegions3, process.detachedQuadStepTracks3, process.detachedTripletStep3, process.detachedTripletStepClusters3, process.detachedTripletStepHitDoublets3, process.detachedTripletStepHitTriplets3, process.detachedTripletStepSeedLayers3, process.detachedTripletStepSeedClusterMask3, process.detachedTripletStepSeeds3, process.detachedTripletStepTrackCandidates3, process.detachedTripletStepTrackingRegions3, process.detachedTripletStepTracks3, process.duplicateTrackCandidates3, process.duplicateTrackClassifier3, process.earlyGeneralTracks3, process.firstStepGoodPrimaryVertices3, process.firstStepPrimaryVertices3, process.firstStepPrimaryVerticesUnsorted3, process.generalTracks3, process.highPtTripletStep3, process.highPtTripletStepClusters3, process.highPtTripletStepHitDoublets3, process.highPtTripletStepHitTriplets3, process.highPtTripletStepSeedLayers3, process.highPtTripletStepSeeds3, process.highPtTripletStepTrackCandidates3, process.highPtTripletStepTrackingRegions3, process.highPtTripletStepTracks3, process.initialStep3, process.initialStepHitDoublets3, process.initialStepHitQuadruplets3, process.initialStepSeedLayers3, process.initialStepSeedClusterMask3, process.initialStepSeeds3, process.initialStepTrackCandidates3, process.initialStepTrackRefsForJets3, process.initialStepTrackingRegions3, process.initialStepTracks3, process.jetsForCoreTracking3, process.lowPtQuadStep3, process.lowPtQuadStepClusters3, process.lowPtQuadStepHitDoublets3, process.lowPtQuadStepHitQuadruplets3, process.lowPtQuadStepSeedLayers3, process.lowPtQuadStepSeeds3, process.lowPtQuadStepTrackCandidates3, process.lowPtQuadStepTrackingRegions3, process.lowPtQuadStepTracks3, process.lowPtTripletStep3, process.lowPtTripletStepClusters3, process.lowPtTripletStepHitDoublets3, process.lowPtTripletStepHitTriplets3, process.lowPtTripletStepSeedLayers3, process.lowPtTripletStepSeeds3, process.lowPtTripletStepTrackCandidates3, process.lowPtTripletStepTrackingRegions3, process.lowPtTripletStepTracks3, process.mergedDuplicateTracks3, process.mixedTripletStep3, process.mixedTripletStepClusters3, process.mixedTripletStepHitDoubletsA3, process.mixedTripletStepHitDoubletsB3, process.mixedTripletStepHitTripletsA3, process.mixedTripletStepHitTripletsB3, process.mixedTripletStepSeedLayersA3, process.mixedTripletStepSeedLayersB3, process.mixedTripletStepSeedClusterMask3, process.mixedTripletStepSeeds3, process.mixedTripletStepSeedsA3, process.mixedTripletStepSeedsB3, process.mixedTripletStepTrackCandidates3, process.mixedTripletStepTrackingRegionsA3, process.mixedTripletStepTrackingRegionsB3, process.mixedTripletStepTracks3, process.pixelLessStep3, process.pixelLessStepClusters3, process.pixelLessStepHitDoublets3, process.pixelLessStepHitTriplets3, process.pixelLessStepSeedLayers3, process.pixelLessStepSeedClusterMask3, process.pixelLessStepSeeds3, process.pixelLessStepTrackCandidates3, process.pixelLessStepTrackingRegions3, process.pixelLessStepTracks3, process.pixelPairStep3, process.pixelPairStepClusters3, process.pixelPairStepHitDoublets3, process.pixelPairStepHitDoubletsB3, process.pixelPairStepSeedLayers3, process.pixelPairStepSeeds3, process.pixelPairStepSeedsA3, process.pixelPairStepSeedsB3, process.pixelPairStepTrackCandidates3, process.pixelPairStepTrackingRegions3, process.pixelPairStepTrackingRegionsSeedLayersB3, process.pixelPairStepTracks3, process.preDuplicateMergingGeneralTracks3, process.siPixelClusterShapeCache3, process.siPixelRecHits3, process.tobTecStep3, process.tobTecStepClusters3, process.tobTecStepHitDoubletsPair3, process.tobTecStepHitDoubletsTripl3, process.tobTecStepHitTripletsTripl3, process.tobTecStepSeedLayersPair3, process.tobTecStepSeedLayersTripl3, process.tobTecStepSeeds3, process.tobTecStepSeedsPair3, process.tobTecStepSeedsTripl3, process.tobTecStepTrackCandidates3, process.tobTecStepTrackingRegionsPair3, process.tobTecStepTrackingRegionsTripl3, process.tobTecStepTracks3, process.trackerClusterCheck3,process.siStripMatchedRecHits3))


hits = "4"
myCollection = "rCluster"+hits


process.MeasurementTrackerEvent4 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection),
)

process.ak4CaloJetsForTrk4 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits),
)

process.caloTowerForTrk4 = process.caloTowerForTrk.clone()

process.chargeCut2069Clusters4 = process.chargeCut2069Clusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.detachedQuadStep4 = process.detachedQuadStep.clone(
    src = cms.InputTag("detachedQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedQuadStepClusters4 = process.detachedQuadStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtTripletStepTracks"+hits)
)

process.detachedQuadStepHitDoublets4 = process.detachedQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+hits)
)

process.detachedQuadStepHitQuadruplets4 = process.detachedQuadStepHitQuadruplets.clone(
    doublets = cms.InputTag("detachedQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+hits+'__reRECO'),

)

process.detachedQuadStepSeedLayers4 = process.detachedQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
)

process.detachedQuadStepSeeds4 = process.detachedQuadStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+hits)
)

process.detachedQuadStepTrackCandidates4 = process.detachedQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedQuadStepClusters"+hits),
    src = cms.InputTag("detachedQuadStepSeeds"+hits)
)

process.detachedQuadStepTrackingRegions4 = process.detachedQuadStepTrackingRegions.clone()

process.detachedQuadStepTracks4 = process.detachedQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedQuadStepTrackCandidates"+hits)
)

process.detachedTripletStep4 = process.detachedTripletStep.clone(
    src = cms.InputTag("detachedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedTripletStepClusters4 = process.detachedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedQuadStepTracks"+hits)
)

process.detachedTripletStepHitDoublets4 = process.detachedTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"+hits),
)

process.detachedTripletStepHitTriplets4 = process.detachedTripletStepHitTriplets.clone(
    doublets = cms.InputTag("detachedTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+hits+'__reRECO')
)

process.detachedTripletStepSeedLayers4 = process.detachedTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    )
)

process.detachedTripletStepSeedClusterMask4 = process.detachedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.detachedTripletStepSeeds4 = process.detachedTripletStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+hits)
)

process.detachedTripletStepTrackCandidates4 = process.detachedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"+hits),
    src = cms.InputTag("detachedTripletStepSeeds"+hits)
)

process.detachedTripletStepTrackingRegions4 = process.detachedTripletStepTrackingRegions.clone()

process.detachedTripletStepTracks4 = process.detachedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedTripletStepTrackCandidates"+hits)
)

process.duplicateTrackCandidates4 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.duplicateTrackClassifier4 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.earlyGeneralTracks4 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits, 
        'highPtTripletStep'+hits, 
#        'jetCoreRegionalStep'+hits, 
        'lowPtQuadStep'+hits, 
        'lowPtTripletStep'+hits, 
        'detachedQuadStep'+hits, 
        'detachedTripletStep'+hits, 
        'pixelPairStep'+hits, 
        'mixedTripletStep'+hits, 
        'pixelLessStep'+hits, 
        'tobTecStep'+hits
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits, 
        "detachedQuadStepTracks"+hits, "detachedTripletStepTracks"+hits, "pixelPairStepTracks"+hits, "mixedTripletStepTracks"+hits, "pixelLessStepTracks"+hits, 
        "tobTecStepTracks"+hits
    )
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

process.generalTracks4 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.highPtTripletStep4 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters4 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
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

process.highPtTripletStepSeedClusterMask4 = process.highPtTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("highPtTripletStepSeeds"+hits)
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

process.initialStep4 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepHitDoublets4 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitQuadruplets4 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
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

process.initialStepSeedClusterMask4 = process.initialStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepSeeds4 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates4 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilder')
    ),
    src = cms.InputTag("initialStepSeeds"+hits),
)

process.initialStepTrackRefsForJets4 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.initialStepTrackingRegions4 = process.initialStepTrackingRegions.clone()

process.initialStepTracks4 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits),
)

process.jetsForCoreTracking4 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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

process.mergedDuplicateTracks4 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.mixedTripletStep4 = process.mixedTripletStep.clone(
    src = cms.InputTag("mixedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.mixedTripletStepClusters4 = process.mixedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelPairStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelPairStepTracks"+hits)
)

process.mixedTripletStepHitDoubletsA4 = process.mixedTripletStepHitDoubletsA.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"+hits)
)

process.mixedTripletStepHitDoubletsB4 = process.mixedTripletStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"+hits)
)

process.mixedTripletStepHitTripletsA4 = process.mixedTripletStepHitTripletsA.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO')
)

process.mixedTripletStepHitTripletsB4 = process.mixedTripletStepHitTripletsB.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO')
)

process.mixedTripletStepSeedLayersA4 = process.mixedTripletStepSeedLayersA.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.mixedTripletStepSeedLayersB4 = process.mixedTripletStepSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    )
)

process.mixedTripletStepSeedClusterMask4 = process.mixedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepSeeds4 = process.mixedTripletStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"+hits), cms.InputTag("mixedTripletStepSeedsB"+hits))
)

process.mixedTripletStepSeedsA4 = process.mixedTripletStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+hits)
)

process.mixedTripletStepSeedsB4 = process.mixedTripletStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+hits)
)

process.mixedTripletStepTrackCandidates4 = process.mixedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"+hits),
    src = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepTrackingRegionsA4 = process.mixedTripletStepTrackingRegionsA.clone()

process.mixedTripletStepTrackingRegionsB4 = process.mixedTripletStepTrackingRegionsB.clone()

process.mixedTripletStepTracks4 = process.mixedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("mixedTripletStepTrackCandidates"+hits)
)

process.pixelLessStep4 = process.pixelLessStep.clone(
    src = cms.InputTag("pixelLessStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelLessStepClusters4 = process.pixelLessStepClusters.clone(
oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("mixedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("mixedTripletStepTracks"+hits)
)

process.pixelLessStepHitDoublets4 = process.pixelLessStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"+hits)
)

process.pixelLessStepHitTriplets4 = process.pixelLessStepHitTriplets.clone(
    doublets = cms.InputTag("pixelLessStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+hits+'__reRECO')
)

process.pixelLessStepSeedLayers4 = process.pixelLessStepSeedLayers.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    MTID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.pixelLessStepSeedClusterMask4 = process.pixelLessStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepSeeds4 = process.pixelLessStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+hits)
)

process.pixelLessStepTrackCandidates4 = process.pixelLessStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"+hits),
    src = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepTrackingRegions4 = process.pixelLessStepTrackingRegions.clone()

process.pixelLessStepTracks4 = process.pixelLessStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelLessStepTrackCandidates"+hits)
)


process.pixelPairStep4 = process.pixelPairStep.clone(
    src = cms.InputTag("pixelPairStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelPairStepClusters4 = process.pixelPairStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedTripletStepTracks"+hits)
)

process.pixelPairStepHitDoublets4 = process.pixelPairStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+hits)
)

process.pixelPairStepHitDoubletsB4 = process.pixelPairStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+hits)
)

process.pixelPairStepSeedLayers4 = process.pixelPairStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    )
)

process.pixelPairStepSeeds4 = process.pixelPairStepSeeds.clone(
    seedCollections = cms.VInputTag("pixelPairStepSeedsA"+hits, "pixelPairStepSeedsB"+hits)
)

process.pixelPairStepSeedsA4 = process.pixelPairStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+hits)
)

process.pixelPairStepSeedsB4 = process.pixelPairStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+hits)
)

process.pixelPairStepTrackCandidates4 = process.pixelPairStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"+hits),
    src = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTrackingRegions4 = process.pixelPairStepTrackingRegions.clone(
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(5),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag(myCollection),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)

process.pixelPairStepTrackingRegionsSeedLayersB4 = process.pixelPairStepTrackingRegionsSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        deltaEta_Cand = cms.double(-1),
        deltaPhi_Cand = cms.double(-1),
        extraEta = cms.double(0),
        extraPhi = cms.double(0),
        input = cms.InputTag(""),
        maxNVertices = cms.int32(5),
        measurementTrackerName = cms.InputTag(""),
        nSigmaZBeamSpot = cms.double(4),
        nSigmaZVertex = cms.double(3),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        searchOpt = cms.bool(False),
        seedingMode = cms.string('Global'),
        vertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVertex = cms.double(0.03)
    )
)

process.pixelPairStepSeedClusterMask4 = process.pixelPairStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTracks4 = process.pixelPairStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelPairStepTrackCandidates"+hits)
)

process.preDuplicateMergingGeneralTracks4 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits 
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.siPixelClusterShapeCache4 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.siPixelRecHits4 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.tobTecStep4 = process.tobTecStep.clone(
    src = cms.InputTag("tobTecStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.tobTecStepClusters4 = process.tobTecStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelLessStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelLessStepTracks"+hits)
)

process.tobTecStepHitDoubletsPair4 = process.tobTecStepHitDoubletsPair.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"+hits)
)

process.tobTecStepHitDoubletsTripl4 = process.tobTecStepHitDoubletsTripl.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"+hits)
)

process.tobTecStepHitTripletsTripl4 = process.tobTecStepHitTripletsTripl.clone(
    doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+hits+'__reRECO')
)

process.tobTecStepSeedLayersPair4 = process.tobTecStepSeedLayersPair.clone(
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeedLayersTripl4 = process.tobTecStepSeedLayersTripl.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeeds4 = process.tobTecStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("tobTecStepSeedsTripl"+hits), cms.InputTag("tobTecStepSeedsPair"+hits))
)

process.tobTecStepSeedsPair4 = process.tobTecStepSeedsPair.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+hits)
)

process.tobTecStepSeedsTripl4 = process.tobTecStepSeedsTripl.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+hits)
)

process.tobTecStepTrackCandidates4 = process.tobTecStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("tobTecStepClusters"+hits),
    src = cms.InputTag("tobTecStepSeeds"+hits)
)

process.tobTecStepTrackingRegionsPair4 = process.tobTecStepTrackingRegionsPair.clone()

process.tobTecStepTrackingRegionsTripl4 = process.tobTecStepTrackingRegionsTripl.clone()

process.tobTecStepTracks4 = process.tobTecStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("tobTecStepTrackCandidates"+hits)
)

process.trackerClusterCheck4 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.siStripMatchedRecHits4 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)


process.reconstruction_step4 = cms.Path(cms.Task(process.MeasurementTrackerEvent4, process.ak4CaloJetsForTrk4, process.caloTowerForTrk4, process.chargeCut2069Clusters4, process.detachedQuadStep4, process.detachedQuadStepClusters4, process.detachedQuadStepHitDoublets4, process.detachedQuadStepHitQuadruplets4, process.detachedQuadStepSeedLayers4, process.detachedQuadStepSeeds4, process.detachedQuadStepTrackCandidates4, process.detachedQuadStepTrackingRegions4, process.detachedQuadStepTracks4, process.detachedTripletStep4, process.detachedTripletStepClusters4, process.detachedTripletStepHitDoublets4, process.detachedTripletStepHitTriplets4, process.detachedTripletStepSeedLayers4, process.detachedTripletStepSeedClusterMask4, process.detachedTripletStepSeeds4, process.detachedTripletStepTrackCandidates4, process.detachedTripletStepTrackingRegions4, process.detachedTripletStepTracks4, process.duplicateTrackCandidates4, process.duplicateTrackClassifier4, process.earlyGeneralTracks4, process.firstStepGoodPrimaryVertices4, process.firstStepPrimaryVertices4, process.firstStepPrimaryVerticesUnsorted4, process.generalTracks4, process.highPtTripletStep4, process.highPtTripletStepClusters4, process.highPtTripletStepHitDoublets4, process.highPtTripletStepHitTriplets4, process.highPtTripletStepSeedLayers4, process.highPtTripletStepSeeds4, process.highPtTripletStepTrackCandidates4, process.highPtTripletStepTrackingRegions4, process.highPtTripletStepTracks4, process.initialStep4, process.initialStepHitDoublets4, process.initialStepHitQuadruplets4, process.initialStepSeedLayers4, process.initialStepSeedClusterMask4, process.initialStepSeeds4, process.initialStepTrackCandidates4, process.initialStepTrackRefsForJets4, process.initialStepTrackingRegions4, process.initialStepTracks4, process.jetsForCoreTracking4, process.lowPtQuadStep4, process.lowPtQuadStepClusters4, process.lowPtQuadStepHitDoublets4, process.lowPtQuadStepHitQuadruplets4, process.lowPtQuadStepSeedLayers4, process.lowPtQuadStepSeeds4, process.lowPtQuadStepTrackCandidates4, process.lowPtQuadStepTrackingRegions4, process.lowPtQuadStepTracks4, process.lowPtTripletStep4, process.lowPtTripletStepClusters4, process.lowPtTripletStepHitDoublets4, process.lowPtTripletStepHitTriplets4, process.lowPtTripletStepSeedLayers4, process.lowPtTripletStepSeeds4, process.lowPtTripletStepTrackCandidates4, process.lowPtTripletStepTrackingRegions4, process.lowPtTripletStepTracks4, process.mergedDuplicateTracks4, process.mixedTripletStep4, process.mixedTripletStepClusters4, process.mixedTripletStepHitDoubletsA4, process.mixedTripletStepHitDoubletsB4, process.mixedTripletStepHitTripletsA4, process.mixedTripletStepHitTripletsB4, process.mixedTripletStepSeedLayersA4, process.mixedTripletStepSeedLayersB4, process.mixedTripletStepSeedClusterMask4, process.mixedTripletStepSeeds4, process.mixedTripletStepSeedsA4, process.mixedTripletStepSeedsB4, process.mixedTripletStepTrackCandidates4, process.mixedTripletStepTrackingRegionsA4, process.mixedTripletStepTrackingRegionsB4, process.mixedTripletStepTracks4, process.pixelLessStep4, process.pixelLessStepClusters4, process.pixelLessStepHitDoublets4, process.pixelLessStepHitTriplets4, process.pixelLessStepSeedLayers4, process.pixelLessStepSeedClusterMask4, process.pixelLessStepSeeds4, process.pixelLessStepTrackCandidates4, process.pixelLessStepTrackingRegions4, process.pixelLessStepTracks4, process.pixelPairStep4, process.pixelPairStepClusters4, process.pixelPairStepHitDoublets4, process.pixelPairStepHitDoubletsB4, process.pixelPairStepSeedLayers4, process.pixelPairStepSeeds4, process.pixelPairStepSeedsA4, process.pixelPairStepSeedsB4, process.pixelPairStepTrackCandidates4, process.pixelPairStepTrackingRegions4, process.pixelPairStepTrackingRegionsSeedLayersB4, process.pixelPairStepTracks4, process.preDuplicateMergingGeneralTracks4, process.siPixelClusterShapeCache4, process.siPixelRecHits4, process.tobTecStep4, process.tobTecStepClusters4, process.tobTecStepHitDoubletsPair4, process.tobTecStepHitDoubletsTripl4, process.tobTecStepHitTripletsTripl4, process.tobTecStepSeedLayersPair4, process.tobTecStepSeedLayersTripl4, process.tobTecStepSeeds4, process.tobTecStepSeedsPair4, process.tobTecStepSeedsTripl4, process.tobTecStepTrackCandidates4, process.tobTecStepTrackingRegionsPair4, process.tobTecStepTrackingRegionsTripl4, process.tobTecStepTracks4, process.trackerClusterCheck4, process.siStripMatchedRecHits4))


hits = "5"
myCollection = "rCluster"+hits


process.MeasurementTrackerEvent5 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection),
)

process.ak4CaloJetsForTrk5 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits),
)

process.caloTowerForTrk5 = process.caloTowerForTrk.clone()

process.chargeCut2069Clusters5 = process.chargeCut2069Clusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.detachedQuadStep5 = process.detachedQuadStep.clone(
    src = cms.InputTag("detachedQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedQuadStepClusters5 = process.detachedQuadStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtTripletStepTracks"+hits)
)

process.detachedQuadStepHitDoublets5 = process.detachedQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+hits)
)

process.detachedQuadStepHitQuadruplets5 = process.detachedQuadStepHitQuadruplets.clone(
    doublets = cms.InputTag("detachedQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+hits+'__reRECO'),

)

process.detachedQuadStepSeedLayers5 = process.detachedQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
)

process.detachedQuadStepSeeds5 = process.detachedQuadStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+hits)
)

process.detachedQuadStepTrackCandidates5 = process.detachedQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedQuadStepClusters"+hits),
    src = cms.InputTag("detachedQuadStepSeeds"+hits)
)

process.detachedQuadStepTrackingRegions5 = process.detachedQuadStepTrackingRegions.clone()

process.detachedQuadStepTracks5 = process.detachedQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedQuadStepTrackCandidates"+hits)
)

process.detachedTripletStep5 = process.detachedTripletStep.clone(
    src = cms.InputTag("detachedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedTripletStepClusters5 = process.detachedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedQuadStepTracks"+hits)
)

process.detachedTripletStepHitDoublets5 = process.detachedTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"+hits),
)

process.detachedTripletStepHitTriplets5 = process.detachedTripletStepHitTriplets.clone(
    doublets = cms.InputTag("detachedTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+hits+'__reRECO')
)

process.detachedTripletStepSeedLayers5 = process.detachedTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    )
)

process.detachedTripletStepSeedClusterMask5 = process.detachedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.detachedTripletStepSeeds5 = process.detachedTripletStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+hits)
)

process.detachedTripletStepTrackCandidates5 = process.detachedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"+hits),
    src = cms.InputTag("detachedTripletStepSeeds"+hits)
)

process.detachedTripletStepTrackingRegions5 = process.detachedTripletStepTrackingRegions.clone()

process.detachedTripletStepTracks5 = process.detachedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedTripletStepTrackCandidates"+hits)
)

process.duplicateTrackCandidates5 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.duplicateTrackClassifier5 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.earlyGeneralTracks5 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits, 
        'highPtTripletStep'+hits, 
#        'jetCoreRegionalStep'+hits, 
        'lowPtQuadStep'+hits, 
        'lowPtTripletStep'+hits, 
        'detachedQuadStep'+hits, 
        'detachedTripletStep'+hits, 
        'pixelPairStep'+hits, 
        'mixedTripletStep'+hits, 
        'pixelLessStep'+hits, 
        'tobTecStep'+hits
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits, 
        "detachedQuadStepTracks"+hits, "detachedTripletStepTracks"+hits, "pixelPairStepTracks"+hits, "mixedTripletStepTracks"+hits, "pixelLessStepTracks"+hits, 
        "tobTecStepTracks"+hits
    )
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

process.generalTracks5 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.highPtTripletStep5 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters5 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
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

process.highPtTripletStepSeedClusterMask5 = process.highPtTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("highPtTripletStepSeeds"+hits)
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

process.initialStep5 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepHitDoublets5 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitQuadruplets5 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
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

process.initialStepSeedClusterMask5 = process.initialStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepSeeds5 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates5 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilder')
    ),
    src = cms.InputTag("initialStepSeeds"+hits),
)

process.initialStepTrackRefsForJets5 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.initialStepTrackingRegions5 = process.initialStepTrackingRegions.clone()

process.initialStepTracks5 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits),
)

process.jetsForCoreTracking5 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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

process.mergedDuplicateTracks5 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.mixedTripletStep5 = process.mixedTripletStep.clone(
    src = cms.InputTag("mixedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.mixedTripletStepClusters5 = process.mixedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelPairStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelPairStepTracks"+hits)
)

process.mixedTripletStepHitDoubletsA5 = process.mixedTripletStepHitDoubletsA.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"+hits)
)

process.mixedTripletStepHitDoubletsB5 = process.mixedTripletStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"+hits)
)

process.mixedTripletStepHitTripletsA5 = process.mixedTripletStepHitTripletsA.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO')
)

process.mixedTripletStepHitTripletsB5 = process.mixedTripletStepHitTripletsB.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO')
)

process.mixedTripletStepSeedLayersA5 = process.mixedTripletStepSeedLayersA.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.mixedTripletStepSeedLayersB5 = process.mixedTripletStepSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    )
)

process.mixedTripletStepSeedClusterMask5 = process.mixedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepSeeds5 = process.mixedTripletStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"+hits), cms.InputTag("mixedTripletStepSeedsB"+hits))
)

process.mixedTripletStepSeedsA5 = process.mixedTripletStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+hits)
)

process.mixedTripletStepSeedsB5 = process.mixedTripletStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+hits)
)

process.mixedTripletStepTrackCandidates5 = process.mixedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"+hits),
    src = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepTrackingRegionsA5 = process.mixedTripletStepTrackingRegionsA.clone()

process.mixedTripletStepTrackingRegionsB5 = process.mixedTripletStepTrackingRegionsB.clone()

process.mixedTripletStepTracks5 = process.mixedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("mixedTripletStepTrackCandidates"+hits)
)

process.pixelLessStep5 = process.pixelLessStep.clone(
    src = cms.InputTag("pixelLessStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelLessStepClusters5 = process.pixelLessStepClusters.clone(
oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("mixedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("mixedTripletStepTracks"+hits)
)

process.pixelLessStepHitDoublets5 = process.pixelLessStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"+hits)
)

process.pixelLessStepHitTriplets5 = process.pixelLessStepHitTriplets.clone(
    doublets = cms.InputTag("pixelLessStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+hits+'__reRECO')
)

process.pixelLessStepSeedLayers5 = process.pixelLessStepSeedLayers.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    MTID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.pixelLessStepSeedClusterMask5 = process.pixelLessStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepSeeds5 = process.pixelLessStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+hits)
)

process.pixelLessStepTrackCandidates5 = process.pixelLessStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"+hits),
    src = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepTrackingRegions5 = process.pixelLessStepTrackingRegions.clone()

process.pixelLessStepTracks5 = process.pixelLessStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelLessStepTrackCandidates"+hits)
)


process.pixelPairStep5 = process.pixelPairStep.clone(
    src = cms.InputTag("pixelPairStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelPairStepClusters5 = process.pixelPairStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedTripletStepTracks"+hits)
)

process.pixelPairStepHitDoublets5 = process.pixelPairStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+hits)
)

process.pixelPairStepHitDoubletsB5 = process.pixelPairStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+hits)
)

process.pixelPairStepSeedLayers5 = process.pixelPairStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    )
)

process.pixelPairStepSeeds5 = process.pixelPairStepSeeds.clone(
    seedCollections = cms.VInputTag("pixelPairStepSeedsA"+hits, "pixelPairStepSeedsB"+hits)
)

process.pixelPairStepSeedsA5 = process.pixelPairStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+hits)
)

process.pixelPairStepSeedsB5 = process.pixelPairStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+hits)
)

process.pixelPairStepTrackCandidates5 = process.pixelPairStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"+hits),
    src = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTrackingRegions5 = process.pixelPairStepTrackingRegions.clone(
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(5),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag(myCollection),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)

process.pixelPairStepTrackingRegionsSeedLayersB5 = process.pixelPairStepTrackingRegionsSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        deltaEta_Cand = cms.double(-1),
        deltaPhi_Cand = cms.double(-1),
        extraEta = cms.double(0),
        extraPhi = cms.double(0),
        input = cms.InputTag(""),
        maxNVertices = cms.int32(5),
        measurementTrackerName = cms.InputTag(""),
        nSigmaZBeamSpot = cms.double(4),
        nSigmaZVertex = cms.double(3),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        searchOpt = cms.bool(False),
        seedingMode = cms.string('Global'),
        vertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVertex = cms.double(0.03)
    )
)

process.pixelPairStepSeedClusterMask5 = process.pixelPairStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTracks5 = process.pixelPairStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelPairStepTrackCandidates"+hits)
)

process.preDuplicateMergingGeneralTracks5 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits 
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.siPixelClusterShapeCache5 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.siPixelRecHits5 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.tobTecStep5 = process.tobTecStep.clone(
    src = cms.InputTag("tobTecStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.tobTecStepClusters5 = process.tobTecStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelLessStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelLessStepTracks"+hits)
)

process.tobTecStepHitDoubletsPair5 = process.tobTecStepHitDoubletsPair.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"+hits)
)

process.tobTecStepHitDoubletsTripl5 = process.tobTecStepHitDoubletsTripl.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"+hits)
)

process.tobTecStepHitTripletsTripl5 = process.tobTecStepHitTripletsTripl.clone(
    doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+hits+'__reRECO')
)

process.tobTecStepSeedLayersPair5 = process.tobTecStepSeedLayersPair.clone(
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeedLayersTripl5 = process.tobTecStepSeedLayersTripl.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeeds5 = process.tobTecStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("tobTecStepSeedsTripl"+hits), cms.InputTag("tobTecStepSeedsPair"+hits))
)

process.tobTecStepSeedsPair5 = process.tobTecStepSeedsPair.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+hits)
)

process.tobTecStepSeedsTripl5 = process.tobTecStepSeedsTripl.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+hits)
)

process.tobTecStepTrackCandidates5 = process.tobTecStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("tobTecStepClusters"+hits),
    src = cms.InputTag("tobTecStepSeeds"+hits)
)

process.tobTecStepTrackingRegionsPair5 = process.tobTecStepTrackingRegionsPair.clone()

process.tobTecStepTrackingRegionsTripl5 = process.tobTecStepTrackingRegionsTripl.clone()

process.tobTecStepTracks5 = process.tobTecStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("tobTecStepTrackCandidates"+hits)
)

process.trackerClusterCheck5 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.siStripMatchedRecHits5 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)


process.reconstruction_step5 = cms.Path(cms.Task(process.MeasurementTrackerEvent5, process.ak4CaloJetsForTrk5, process.caloTowerForTrk5, process.chargeCut2069Clusters5, process.detachedQuadStep5, process.detachedQuadStepClusters5, process.detachedQuadStepHitDoublets5, process.detachedQuadStepHitQuadruplets5, process.detachedQuadStepSeedLayers5, process.detachedQuadStepSeeds5, process.detachedQuadStepTrackCandidates5, process.detachedQuadStepTrackingRegions5, process.detachedQuadStepTracks5, process.detachedTripletStep5, process.detachedTripletStepClusters5, process.detachedTripletStepHitDoublets5, process.detachedTripletStepHitTriplets5, process.detachedTripletStepSeedLayers5, process.detachedTripletStepSeedClusterMask5, process.detachedTripletStepSeeds5, process.detachedTripletStepTrackCandidates5, process.detachedTripletStepTrackingRegions5, process.detachedTripletStepTracks5, process.duplicateTrackCandidates5, process.duplicateTrackClassifier5, process.earlyGeneralTracks5, process.firstStepGoodPrimaryVertices5, process.firstStepPrimaryVertices5, process.firstStepPrimaryVerticesUnsorted5, process.generalTracks5, process.highPtTripletStep5, process.highPtTripletStepClusters5, process.highPtTripletStepHitDoublets5, process.highPtTripletStepHitTriplets5, process.highPtTripletStepSeedLayers5, process.highPtTripletStepSeeds5, process.highPtTripletStepTrackCandidates5, process.highPtTripletStepTrackingRegions5, process.highPtTripletStepTracks5, process.initialStep5, process.initialStepHitDoublets5, process.initialStepHitQuadruplets5, process.initialStepSeedLayers5, process.initialStepSeedClusterMask5, process.initialStepSeeds5, process.initialStepTrackCandidates5, process.initialStepTrackRefsForJets5, process.initialStepTrackingRegions5, process.initialStepTracks5, process.jetsForCoreTracking5, process.lowPtQuadStep5, process.lowPtQuadStepClusters5, process.lowPtQuadStepHitDoublets5, process.lowPtQuadStepHitQuadruplets5, process.lowPtQuadStepSeedLayers5, process.lowPtQuadStepSeeds5, process.lowPtQuadStepTrackCandidates5, process.lowPtQuadStepTrackingRegions5, process.lowPtQuadStepTracks5, process.lowPtTripletStep5, process.lowPtTripletStepClusters5, process.lowPtTripletStepHitDoublets5, process.lowPtTripletStepHitTriplets5, process.lowPtTripletStepSeedLayers5, process.lowPtTripletStepSeeds5, process.lowPtTripletStepTrackCandidates5, process.lowPtTripletStepTrackingRegions5, process.lowPtTripletStepTracks5, process.mergedDuplicateTracks5, process.mixedTripletStep5, process.mixedTripletStepClusters5, process.mixedTripletStepHitDoubletsA5, process.mixedTripletStepHitDoubletsB5, process.mixedTripletStepHitTripletsA5, process.mixedTripletStepHitTripletsB5, process.mixedTripletStepSeedLayersA5, process.mixedTripletStepSeedLayersB5, process.mixedTripletStepSeedClusterMask5, process.mixedTripletStepSeeds5, process.mixedTripletStepSeedsA5, process.mixedTripletStepSeedsB5, process.mixedTripletStepTrackCandidates5, process.mixedTripletStepTrackingRegionsA5, process.mixedTripletStepTrackingRegionsB5, process.mixedTripletStepTracks5, process.pixelLessStep5, process.pixelLessStepClusters5, process.pixelLessStepHitDoublets5, process.pixelLessStepHitTriplets5, process.pixelLessStepSeedLayers5, process.pixelLessStepSeedClusterMask5, process.pixelLessStepSeeds5, process.pixelLessStepTrackCandidates5, process.pixelLessStepTrackingRegions5, process.pixelLessStepTracks5, process.pixelPairStep5, process.pixelPairStepClusters5, process.pixelPairStepHitDoublets5, process.pixelPairStepHitDoubletsB5, process.pixelPairStepSeedLayers5, process.pixelPairStepSeeds5, process.pixelPairStepSeedsA5, process.pixelPairStepSeedsB5, process.pixelPairStepTrackCandidates5, process.pixelPairStepTrackingRegions5, process.pixelPairStepTrackingRegionsSeedLayersB5, process.pixelPairStepTracks5, process.preDuplicateMergingGeneralTracks5, process.siPixelClusterShapeCache5, process.siPixelRecHits5, process.tobTecStep5, process.tobTecStepClusters5, process.tobTecStepHitDoubletsPair5, process.tobTecStepHitDoubletsTripl5, process.tobTecStepHitTripletsTripl5, process.tobTecStepSeedLayersPair5, process.tobTecStepSeedLayersTripl5, process.tobTecStepSeeds5, process.tobTecStepSeedsPair5, process.tobTecStepSeedsTripl5, process.tobTecStepTrackCandidates5, process.tobTecStepTrackingRegionsPair5, process.tobTecStepTrackingRegionsTripl5, process.tobTecStepTracks5, process.trackerClusterCheck5, process.siStripMatchedRecHits5))


hits = "6"
myCollection = "rCluster"+hits


process.MeasurementTrackerEvent6 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection),
)

process.ak4CaloJetsForTrk6 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits),
)

process.caloTowerForTrk6 = process.caloTowerForTrk.clone()

process.chargeCut2069Clusters6 = process.chargeCut2069Clusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.detachedQuadStep6 = process.detachedQuadStep.clone(
    src = cms.InputTag("detachedQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedQuadStepClusters6 = process.detachedQuadStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtTripletStepTracks"+hits)
)

process.detachedQuadStepHitDoublets6 = process.detachedQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+hits)
)

process.detachedQuadStepHitQuadruplets6 = process.detachedQuadStepHitQuadruplets.clone(
    doublets = cms.InputTag("detachedQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+hits+'__reRECO'),

)

process.detachedQuadStepSeedLayers6 = process.detachedQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
)

process.detachedQuadStepSeeds6 = process.detachedQuadStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+hits)
)

process.detachedQuadStepTrackCandidates6 = process.detachedQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedQuadStepClusters"+hits),
    src = cms.InputTag("detachedQuadStepSeeds"+hits)
)

process.detachedQuadStepTrackingRegions6 = process.detachedQuadStepTrackingRegions.clone()

process.detachedQuadStepTracks6 = process.detachedQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedQuadStepTrackCandidates"+hits)
)

process.detachedTripletStep6 = process.detachedTripletStep.clone(
    src = cms.InputTag("detachedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedTripletStepClusters6 = process.detachedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedQuadStepTracks"+hits)
)

process.detachedTripletStepHitDoublets6 = process.detachedTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"+hits),
)

process.detachedTripletStepHitTriplets6 = process.detachedTripletStepHitTriplets.clone(
    doublets = cms.InputTag("detachedTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+hits+'__reRECO')
)

process.detachedTripletStepSeedLayers6 = process.detachedTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    )
)

process.detachedTripletStepSeedClusterMask6 = process.detachedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.detachedTripletStepSeeds6 = process.detachedTripletStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+hits)
)

process.detachedTripletStepTrackCandidates6 = process.detachedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"+hits),
    src = cms.InputTag("detachedTripletStepSeeds"+hits)
)

process.detachedTripletStepTrackingRegions6 = process.detachedTripletStepTrackingRegions.clone()

process.detachedTripletStepTracks6 = process.detachedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedTripletStepTrackCandidates"+hits)
)

process.duplicateTrackCandidates6 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.duplicateTrackClassifier6 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.earlyGeneralTracks6 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits, 
        'highPtTripletStep'+hits, 
#        'jetCoreRegionalStep'+hits, 
        'lowPtQuadStep'+hits, 
        'lowPtTripletStep'+hits, 
        'detachedQuadStep'+hits, 
        'detachedTripletStep'+hits, 
        'pixelPairStep'+hits, 
        'mixedTripletStep'+hits, 
        'pixelLessStep'+hits, 
        'tobTecStep'+hits
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits, 
        "detachedQuadStepTracks"+hits, "detachedTripletStepTracks"+hits, "pixelPairStepTracks"+hits, "mixedTripletStepTracks"+hits, "pixelLessStepTracks"+hits, 
        "tobTecStepTracks"+hits
    )
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

process.generalTracks6 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.highPtTripletStep6 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters6 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
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

process.highPtTripletStepSeedClusterMask6 = process.highPtTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("highPtTripletStepSeeds"+hits)
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

process.initialStep6 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepHitDoublets6 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitQuadruplets6 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
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

process.initialStepSeedClusterMask6 = process.initialStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepSeeds6 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates6 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilder')
    ),
    src = cms.InputTag("initialStepSeeds"+hits),
)

process.initialStepTrackRefsForJets6 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.initialStepTrackingRegions6 = process.initialStepTrackingRegions.clone()

process.initialStepTracks6 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits),
)

process.jetsForCoreTracking6 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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

process.mergedDuplicateTracks6 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.mixedTripletStep6 = process.mixedTripletStep.clone(
    src = cms.InputTag("mixedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.mixedTripletStepClusters6 = process.mixedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelPairStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelPairStepTracks"+hits)
)

process.mixedTripletStepHitDoubletsA6 = process.mixedTripletStepHitDoubletsA.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"+hits)
)

process.mixedTripletStepHitDoubletsB6 = process.mixedTripletStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"+hits)
)

process.mixedTripletStepHitTripletsA6 = process.mixedTripletStepHitTripletsA.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO')
)

process.mixedTripletStepHitTripletsB6 = process.mixedTripletStepHitTripletsB.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO')
)

process.mixedTripletStepSeedLayersA6 = process.mixedTripletStepSeedLayersA.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.mixedTripletStepSeedLayersB6 = process.mixedTripletStepSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    )
)

process.mixedTripletStepSeedClusterMask6 = process.mixedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepSeeds6 = process.mixedTripletStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"+hits), cms.InputTag("mixedTripletStepSeedsB"+hits))
)

process.mixedTripletStepSeedsA6 = process.mixedTripletStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+hits)
)

process.mixedTripletStepSeedsB6 = process.mixedTripletStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+hits)
)

process.mixedTripletStepTrackCandidates6 = process.mixedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"+hits),
    src = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepTrackingRegionsA6 = process.mixedTripletStepTrackingRegionsA.clone()

process.mixedTripletStepTrackingRegionsB6 = process.mixedTripletStepTrackingRegionsB.clone()

process.mixedTripletStepTracks6 = process.mixedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("mixedTripletStepTrackCandidates"+hits)
)

process.pixelLessStep6 = process.pixelLessStep.clone(
    src = cms.InputTag("pixelLessStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelLessStepClusters6 = process.pixelLessStepClusters.clone(
oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("mixedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("mixedTripletStepTracks"+hits)
)

process.pixelLessStepHitDoublets6 = process.pixelLessStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"+hits)
)

process.pixelLessStepHitTriplets6 = process.pixelLessStepHitTriplets.clone(
    doublets = cms.InputTag("pixelLessStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+hits+'__reRECO')
)

process.pixelLessStepSeedLayers6 = process.pixelLessStepSeedLayers.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    MTID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.pixelLessStepSeedClusterMask6 = process.pixelLessStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepSeeds6 = process.pixelLessStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+hits)
)

process.pixelLessStepTrackCandidates6 = process.pixelLessStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"+hits),
    src = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepTrackingRegions6 = process.pixelLessStepTrackingRegions.clone()

process.pixelLessStepTracks6 = process.pixelLessStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelLessStepTrackCandidates"+hits)
)


process.pixelPairStep6 = process.pixelPairStep.clone(
    src = cms.InputTag("pixelPairStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelPairStepClusters6 = process.pixelPairStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedTripletStepTracks"+hits)
)

process.pixelPairStepHitDoublets6 = process.pixelPairStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+hits)
)

process.pixelPairStepHitDoubletsB6 = process.pixelPairStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+hits)
)

process.pixelPairStepSeedLayers6 = process.pixelPairStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    )
)

process.pixelPairStepSeeds6 = process.pixelPairStepSeeds.clone(
    seedCollections = cms.VInputTag("pixelPairStepSeedsA"+hits, "pixelPairStepSeedsB"+hits)
)

process.pixelPairStepSeedsA6 = process.pixelPairStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+hits)
)

process.pixelPairStepSeedsB6 = process.pixelPairStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+hits)
)

process.pixelPairStepTrackCandidates6 = process.pixelPairStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"+hits),
    src = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTrackingRegions6 = process.pixelPairStepTrackingRegions.clone(
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(5),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag(myCollection),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)

process.pixelPairStepTrackingRegionsSeedLayersB6 = process.pixelPairStepTrackingRegionsSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        deltaEta_Cand = cms.double(-1),
        deltaPhi_Cand = cms.double(-1),
        extraEta = cms.double(0),
        extraPhi = cms.double(0),
        input = cms.InputTag(""),
        maxNVertices = cms.int32(5),
        measurementTrackerName = cms.InputTag(""),
        nSigmaZBeamSpot = cms.double(4),
        nSigmaZVertex = cms.double(3),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        searchOpt = cms.bool(False),
        seedingMode = cms.string('Global'),
        vertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVertex = cms.double(0.03)
    )
)

process.pixelPairStepSeedClusterMask6 = process.pixelPairStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTracks6 = process.pixelPairStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelPairStepTrackCandidates"+hits)
)

process.preDuplicateMergingGeneralTracks6 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits 
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.siPixelClusterShapeCache6 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.siPixelRecHits6 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.tobTecStep6 = process.tobTecStep.clone(
    src = cms.InputTag("tobTecStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.tobTecStepClusters6 = process.tobTecStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelLessStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelLessStepTracks"+hits)
)

process.tobTecStepHitDoubletsPair6 = process.tobTecStepHitDoubletsPair.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"+hits)
)

process.tobTecStepHitDoubletsTripl6 = process.tobTecStepHitDoubletsTripl.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"+hits)
)

process.tobTecStepHitTripletsTripl6 = process.tobTecStepHitTripletsTripl.clone(
    doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+hits+'__reRECO')
)

process.tobTecStepSeedLayersPair6 = process.tobTecStepSeedLayersPair.clone(
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeedLayersTripl6 = process.tobTecStepSeedLayersTripl.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeeds6 = process.tobTecStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("tobTecStepSeedsTripl"+hits), cms.InputTag("tobTecStepSeedsPair"+hits))
)

process.tobTecStepSeedsPair6 = process.tobTecStepSeedsPair.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+hits)
)

process.tobTecStepSeedsTripl6 = process.tobTecStepSeedsTripl.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+hits)
)

process.tobTecStepTrackCandidates6 = process.tobTecStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("tobTecStepClusters"+hits),
    src = cms.InputTag("tobTecStepSeeds"+hits)
)

process.tobTecStepTrackingRegionsPair6 = process.tobTecStepTrackingRegionsPair.clone()

process.tobTecStepTrackingRegionsTripl6 = process.tobTecStepTrackingRegionsTripl.clone()

process.tobTecStepTracks6 = process.tobTecStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("tobTecStepTrackCandidates"+hits)
)

process.trackerClusterCheck6 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.siStripMatchedRecHits6 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)


process.reconstruction_step6 = cms.Path(cms.Task(process.MeasurementTrackerEvent6, process.ak4CaloJetsForTrk6, process.caloTowerForTrk6, process.chargeCut2069Clusters6, process.detachedQuadStep6, process.detachedQuadStepClusters6, process.detachedQuadStepHitDoublets6, process.detachedQuadStepHitQuadruplets6, process.detachedQuadStepSeedLayers6, process.detachedQuadStepSeeds6, process.detachedQuadStepTrackCandidates6, process.detachedQuadStepTrackingRegions6, process.detachedQuadStepTracks6, process.detachedTripletStep6, process.detachedTripletStepClusters6, process.detachedTripletStepHitDoublets6, process.detachedTripletStepHitTriplets6, process.detachedTripletStepSeedLayers6, process.detachedTripletStepSeedClusterMask6, process.detachedTripletStepSeeds6, process.detachedTripletStepTrackCandidates6, process.detachedTripletStepTrackingRegions6, process.detachedTripletStepTracks6, process.duplicateTrackCandidates6, process.duplicateTrackClassifier6, process.earlyGeneralTracks6, process.firstStepGoodPrimaryVertices6, process.firstStepPrimaryVertices6, process.firstStepPrimaryVerticesUnsorted6, process.generalTracks6, process.highPtTripletStep6, process.highPtTripletStepClusters6, process.highPtTripletStepHitDoublets6, process.highPtTripletStepHitTriplets6, process.highPtTripletStepSeedLayers6, process.highPtTripletStepSeeds6, process.highPtTripletStepTrackCandidates6, process.highPtTripletStepTrackingRegions6, process.highPtTripletStepTracks6, process.initialStep6, process.initialStepHitDoublets6, process.initialStepHitQuadruplets6, process.initialStepSeedLayers6, process.initialStepSeedClusterMask6, process.initialStepSeeds6, process.initialStepTrackCandidates6, process.initialStepTrackRefsForJets6, process.initialStepTrackingRegions6, process.initialStepTracks6, process.jetsForCoreTracking6, process.lowPtQuadStep6, process.lowPtQuadStepClusters6, process.lowPtQuadStepHitDoublets6, process.lowPtQuadStepHitQuadruplets6, process.lowPtQuadStepSeedLayers6, process.lowPtQuadStepSeeds6, process.lowPtQuadStepTrackCandidates6, process.lowPtQuadStepTrackingRegions6, process.lowPtQuadStepTracks6, process.lowPtTripletStep6, process.lowPtTripletStepClusters6, process.lowPtTripletStepHitDoublets6, process.lowPtTripletStepHitTriplets6, process.lowPtTripletStepSeedLayers6, process.lowPtTripletStepSeeds6, process.lowPtTripletStepTrackCandidates6, process.lowPtTripletStepTrackingRegions6, process.lowPtTripletStepTracks6, process.mergedDuplicateTracks6, process.mixedTripletStep6, process.mixedTripletStepClusters6, process.mixedTripletStepHitDoubletsA6, process.mixedTripletStepHitDoubletsB6, process.mixedTripletStepHitTripletsA6, process.mixedTripletStepHitTripletsB6, process.mixedTripletStepSeedLayersA6, process.mixedTripletStepSeedLayersB6, process.mixedTripletStepSeedClusterMask6, process.mixedTripletStepSeeds6, process.mixedTripletStepSeedsA6, process.mixedTripletStepSeedsB6, process.mixedTripletStepTrackCandidates6, process.mixedTripletStepTrackingRegionsA6, process.mixedTripletStepTrackingRegionsB6, process.mixedTripletStepTracks6, process.pixelLessStep6, process.pixelLessStepClusters6, process.pixelLessStepHitDoublets6, process.pixelLessStepHitTriplets6, process.pixelLessStepSeedLayers6, process.pixelLessStepSeedClusterMask6, process.pixelLessStepSeeds6, process.pixelLessStepTrackCandidates6, process.pixelLessStepTrackingRegions6, process.pixelLessStepTracks6, process.pixelPairStep6, process.pixelPairStepClusters6, process.pixelPairStepHitDoublets6, process.pixelPairStepHitDoubletsB6, process.pixelPairStepSeedLayers6, process.pixelPairStepSeeds6, process.pixelPairStepSeedsA6, process.pixelPairStepSeedsB6, process.pixelPairStepTrackCandidates6, process.pixelPairStepTrackingRegions6, process.pixelPairStepTrackingRegionsSeedLayersB6, process.pixelPairStepTracks6, process.preDuplicateMergingGeneralTracks6, process.siPixelClusterShapeCache6, process.siPixelRecHits6, process.tobTecStep6, process.tobTecStepClusters6, process.tobTecStepHitDoubletsPair6, process.tobTecStepHitDoubletsTripl6, process.tobTecStepHitTripletsTripl6, process.tobTecStepSeedLayersPair6, process.tobTecStepSeedLayersTripl6, process.tobTecStepSeeds6, process.tobTecStepSeedsPair6, process.tobTecStepSeedsTripl6, process.tobTecStepTrackCandidates6, process.tobTecStepTrackingRegionsPair6, process.tobTecStepTrackingRegionsTripl6, process.tobTecStepTracks6, process.trackerClusterCheck6, process.siStripMatchedRecHits6))


hits = "7"
myCollection = "rCluster"+hits


process.MeasurementTrackerEvent7 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection),
)

process.ak4CaloJetsForTrk7 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits),
)

process.caloTowerForTrk7 = process.caloTowerForTrk.clone()

process.chargeCut2069Clusters7 = process.chargeCut2069Clusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.detachedQuadStep7 = process.detachedQuadStep.clone(
    src = cms.InputTag("detachedQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedQuadStepClusters7 = process.detachedQuadStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtTripletStepTracks"+hits)
)

process.detachedQuadStepHitDoublets7 = process.detachedQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+hits)
)

process.detachedQuadStepHitQuadruplets7 = process.detachedQuadStepHitQuadruplets.clone(
    doublets = cms.InputTag("detachedQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+hits+'__reRECO'),

)

process.detachedQuadStepSeedLayers7 = process.detachedQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
)

process.detachedQuadStepSeeds7 = process.detachedQuadStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+hits)
)

process.detachedQuadStepTrackCandidates7 = process.detachedQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedQuadStepClusters"+hits),
    src = cms.InputTag("detachedQuadStepSeeds"+hits)
)

process.detachedQuadStepTrackingRegions7 = process.detachedQuadStepTrackingRegions.clone()

process.detachedQuadStepTracks7 = process.detachedQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedQuadStepTrackCandidates"+hits)
)

process.detachedTripletStep7 = process.detachedTripletStep.clone(
    src = cms.InputTag("detachedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedTripletStepClusters7 = process.detachedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedQuadStepTracks"+hits)
)

process.detachedTripletStepHitDoublets7 = process.detachedTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"+hits),
)

process.detachedTripletStepHitTriplets7 = process.detachedTripletStepHitTriplets.clone(
    doublets = cms.InputTag("detachedTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+hits+'__reRECO')
)

process.detachedTripletStepSeedLayers7 = process.detachedTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    )
)

process.detachedTripletStepSeedClusterMask7 = process.detachedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.detachedTripletStepSeeds7 = process.detachedTripletStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+hits)
)

process.detachedTripletStepTrackCandidates7 = process.detachedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"+hits),
    src = cms.InputTag("detachedTripletStepSeeds"+hits)
)

process.detachedTripletStepTrackingRegions7 = process.detachedTripletStepTrackingRegions.clone()

process.detachedTripletStepTracks7 = process.detachedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedTripletStepTrackCandidates"+hits)
)

process.duplicateTrackCandidates7 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.duplicateTrackClassifier7 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.earlyGeneralTracks7 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits, 
        'highPtTripletStep'+hits, 
#        'jetCoreRegionalStep'+hits, 
        'lowPtQuadStep'+hits, 
        'lowPtTripletStep'+hits, 
        'detachedQuadStep'+hits, 
        'detachedTripletStep'+hits, 
        'pixelPairStep'+hits, 
        'mixedTripletStep'+hits, 
        'pixelLessStep'+hits, 
        'tobTecStep'+hits
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits, 
        "detachedQuadStepTracks"+hits, "detachedTripletStepTracks"+hits, "pixelPairStepTracks"+hits, "mixedTripletStepTracks"+hits, "pixelLessStepTracks"+hits, 
        "tobTecStepTracks"+hits
    )
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

process.generalTracks7 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.highPtTripletStep7 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters7 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
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

process.highPtTripletStepSeedClusterMask7 = process.highPtTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("highPtTripletStepSeeds"+hits)
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

process.initialStep7 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepHitDoublets7 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitQuadruplets7 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
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

process.initialStepSeedClusterMask7 = process.initialStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepSeeds7 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates7 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilder')
    ),
    src = cms.InputTag("initialStepSeeds"+hits),
)

process.initialStepTrackRefsForJets7 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.initialStepTrackingRegions7 = process.initialStepTrackingRegions.clone()

process.initialStepTracks7 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits),
)

process.jetsForCoreTracking7 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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

process.mergedDuplicateTracks7 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.mixedTripletStep7 = process.mixedTripletStep.clone(
    src = cms.InputTag("mixedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.mixedTripletStepClusters7 = process.mixedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelPairStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelPairStepTracks"+hits)
)

process.mixedTripletStepHitDoubletsA7 = process.mixedTripletStepHitDoubletsA.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"+hits)
)

process.mixedTripletStepHitDoubletsB7 = process.mixedTripletStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"+hits)
)

process.mixedTripletStepHitTripletsA7 = process.mixedTripletStepHitTripletsA.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO')
)

process.mixedTripletStepHitTripletsB7 = process.mixedTripletStepHitTripletsB.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO')
)

process.mixedTripletStepSeedLayersA7 = process.mixedTripletStepSeedLayersA.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.mixedTripletStepSeedLayersB7 = process.mixedTripletStepSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    )
)

process.mixedTripletStepSeedClusterMask7 = process.mixedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepSeeds7 = process.mixedTripletStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"+hits), cms.InputTag("mixedTripletStepSeedsB"+hits))
)

process.mixedTripletStepSeedsA7 = process.mixedTripletStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+hits)
)

process.mixedTripletStepSeedsB7 = process.mixedTripletStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+hits)
)

process.mixedTripletStepTrackCandidates7 = process.mixedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"+hits),
    src = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepTrackingRegionsA7 = process.mixedTripletStepTrackingRegionsA.clone()

process.mixedTripletStepTrackingRegionsB7 = process.mixedTripletStepTrackingRegionsB.clone()

process.mixedTripletStepTracks7 = process.mixedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("mixedTripletStepTrackCandidates"+hits)
)

process.pixelLessStep7 = process.pixelLessStep.clone(
    src = cms.InputTag("pixelLessStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelLessStepClusters7 = process.pixelLessStepClusters.clone(
oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("mixedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("mixedTripletStepTracks"+hits)
)

process.pixelLessStepHitDoublets7 = process.pixelLessStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"+hits)
)

process.pixelLessStepHitTriplets7 = process.pixelLessStepHitTriplets.clone(
    doublets = cms.InputTag("pixelLessStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+hits+'__reRECO')
)

process.pixelLessStepSeedLayers7 = process.pixelLessStepSeedLayers.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    MTID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.pixelLessStepSeedClusterMask7 = process.pixelLessStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepSeeds7 = process.pixelLessStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+hits)
)

process.pixelLessStepTrackCandidates7 = process.pixelLessStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"+hits),
    src = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepTrackingRegions7 = process.pixelLessStepTrackingRegions.clone()

process.pixelLessStepTracks7 = process.pixelLessStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelLessStepTrackCandidates"+hits)
)


process.pixelPairStep7 = process.pixelPairStep.clone(
    src = cms.InputTag("pixelPairStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelPairStepClusters7 = process.pixelPairStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedTripletStepTracks"+hits)
)

process.pixelPairStepHitDoublets7 = process.pixelPairStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+hits)
)

process.pixelPairStepHitDoubletsB7 = process.pixelPairStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+hits)
)

process.pixelPairStepSeedLayers7 = process.pixelPairStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    )
)

process.pixelPairStepSeeds7 = process.pixelPairStepSeeds.clone(
    seedCollections = cms.VInputTag("pixelPairStepSeedsA"+hits, "pixelPairStepSeedsB"+hits)
)

process.pixelPairStepSeedsA7 = process.pixelPairStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+hits)
)

process.pixelPairStepSeedsB7 = process.pixelPairStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+hits)
)

process.pixelPairStepTrackCandidates7 = process.pixelPairStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"+hits),
    src = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTrackingRegions7 = process.pixelPairStepTrackingRegions.clone(
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(5),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag(myCollection),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)

process.pixelPairStepTrackingRegionsSeedLayersB7 = process.pixelPairStepTrackingRegionsSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        deltaEta_Cand = cms.double(-1),
        deltaPhi_Cand = cms.double(-1),
        extraEta = cms.double(0),
        extraPhi = cms.double(0),
        input = cms.InputTag(""),
        maxNVertices = cms.int32(5),
        measurementTrackerName = cms.InputTag(""),
        nSigmaZBeamSpot = cms.double(4),
        nSigmaZVertex = cms.double(3),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        searchOpt = cms.bool(False),
        seedingMode = cms.string('Global'),
        vertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVertex = cms.double(0.03)
    )
)

process.pixelPairStepSeedClusterMask7 = process.pixelPairStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTracks7 = process.pixelPairStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelPairStepTrackCandidates"+hits)
)

process.preDuplicateMergingGeneralTracks7 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits 
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.siPixelClusterShapeCache7 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.siPixelRecHits7 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.tobTecStep7 = process.tobTecStep.clone(
    src = cms.InputTag("tobTecStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.tobTecStepClusters7 = process.tobTecStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelLessStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelLessStepTracks"+hits)
)

process.tobTecStepHitDoubletsPair7 = process.tobTecStepHitDoubletsPair.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"+hits)
)

process.tobTecStepHitDoubletsTripl7 = process.tobTecStepHitDoubletsTripl.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"+hits)
)

process.tobTecStepHitTripletsTripl7 = process.tobTecStepHitTripletsTripl.clone(
    doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+hits+'__reRECO')
)

process.tobTecStepSeedLayersPair7 = process.tobTecStepSeedLayersPair.clone(
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeedLayersTripl7 = process.tobTecStepSeedLayersTripl.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeeds7 = process.tobTecStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("tobTecStepSeedsTripl"+hits), cms.InputTag("tobTecStepSeedsPair"+hits))
)

process.tobTecStepSeedsPair7 = process.tobTecStepSeedsPair.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+hits)
)

process.tobTecStepSeedsTripl7 = process.tobTecStepSeedsTripl.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+hits)
)

process.tobTecStepTrackCandidates7 = process.tobTecStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("tobTecStepClusters"+hits),
    src = cms.InputTag("tobTecStepSeeds"+hits)
)

process.tobTecStepTrackingRegionsPair7 = process.tobTecStepTrackingRegionsPair.clone()

process.tobTecStepTrackingRegionsTripl7 = process.tobTecStepTrackingRegionsTripl.clone()

process.tobTecStepTracks7 = process.tobTecStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("tobTecStepTrackCandidates"+hits)
)

process.trackerClusterCheck7 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.siStripMatchedRecHits7 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)


process.reconstruction_step7 = cms.Path(cms.Task(process.MeasurementTrackerEvent7, process.ak4CaloJetsForTrk7, process.caloTowerForTrk7, process.chargeCut2069Clusters7, process.detachedQuadStep7, process.detachedQuadStepClusters7, process.detachedQuadStepHitDoublets7, process.detachedQuadStepHitQuadruplets7, process.detachedQuadStepSeedLayers7, process.detachedQuadStepSeeds7, process.detachedQuadStepTrackCandidates7, process.detachedQuadStepTrackingRegions7, process.detachedQuadStepTracks7, process.detachedTripletStep7, process.detachedTripletStepClusters7, process.detachedTripletStepHitDoublets7, process.detachedTripletStepHitTriplets7, process.detachedTripletStepSeedLayers7, process.detachedTripletStepSeedClusterMask7, process.detachedTripletStepSeeds7, process.detachedTripletStepTrackCandidates7, process.detachedTripletStepTrackingRegions7, process.detachedTripletStepTracks7, process.duplicateTrackCandidates7, process.duplicateTrackClassifier7, process.earlyGeneralTracks7, process.firstStepGoodPrimaryVertices7, process.firstStepPrimaryVertices7, process.firstStepPrimaryVerticesUnsorted7, process.generalTracks7, process.highPtTripletStep7, process.highPtTripletStepClusters7, process.highPtTripletStepHitDoublets7, process.highPtTripletStepHitTriplets7, process.highPtTripletStepSeedLayers7, process.highPtTripletStepSeeds7, process.highPtTripletStepTrackCandidates7, process.highPtTripletStepTrackingRegions7, process.highPtTripletStepTracks7, process.initialStep7, process.initialStepHitDoublets7, process.initialStepHitQuadruplets7, process.initialStepSeedLayers7, process.initialStepSeedClusterMask7, process.initialStepSeeds7, process.initialStepTrackCandidates7, process.initialStepTrackRefsForJets7, process.initialStepTrackingRegions7, process.initialStepTracks7, process.jetsForCoreTracking7, process.lowPtQuadStep7, process.lowPtQuadStepClusters7, process.lowPtQuadStepHitDoublets7, process.lowPtQuadStepHitQuadruplets7, process.lowPtQuadStepSeedLayers7, process.lowPtQuadStepSeeds7, process.lowPtQuadStepTrackCandidates7, process.lowPtQuadStepTrackingRegions7, process.lowPtQuadStepTracks7, process.lowPtTripletStep7, process.lowPtTripletStepClusters7, process.lowPtTripletStepHitDoublets7, process.lowPtTripletStepHitTriplets7, process.lowPtTripletStepSeedLayers7, process.lowPtTripletStepSeeds7, process.lowPtTripletStepTrackCandidates7, process.lowPtTripletStepTrackingRegions7, process.lowPtTripletStepTracks7, process.mergedDuplicateTracks7, process.mixedTripletStep7, process.mixedTripletStepClusters7, process.mixedTripletStepHitDoubletsA7, process.mixedTripletStepHitDoubletsB7, process.mixedTripletStepHitTripletsA7, process.mixedTripletStepHitTripletsB7, process.mixedTripletStepSeedLayersA7, process.mixedTripletStepSeedLayersB7, process.mixedTripletStepSeedClusterMask7, process.mixedTripletStepSeeds7, process.mixedTripletStepSeedsA7, process.mixedTripletStepSeedsB7, process.mixedTripletStepTrackCandidates7, process.mixedTripletStepTrackingRegionsA7, process.mixedTripletStepTrackingRegionsB7, process.mixedTripletStepTracks7, process.pixelLessStep7, process.pixelLessStepClusters7, process.pixelLessStepHitDoublets7, process.pixelLessStepHitTriplets7, process.pixelLessStepSeedLayers7, process.pixelLessStepSeedClusterMask7, process.pixelLessStepSeeds7, process.pixelLessStepTrackCandidates7, process.pixelLessStepTrackingRegions7, process.pixelLessStepTracks7, process.pixelPairStep7, process.pixelPairStepClusters7, process.pixelPairStepHitDoublets7, process.pixelPairStepHitDoubletsB7, process.pixelPairStepSeedLayers7, process.pixelPairStepSeeds7, process.pixelPairStepSeedsA7, process.pixelPairStepSeedsB7, process.pixelPairStepTrackCandidates7, process.pixelPairStepTrackingRegions7, process.pixelPairStepTrackingRegionsSeedLayersB7, process.pixelPairStepTracks7, process.preDuplicateMergingGeneralTracks7, process.siPixelClusterShapeCache7, process.siPixelRecHits7, process.tobTecStep7, process.tobTecStepClusters7, process.tobTecStepHitDoubletsPair7, process.tobTecStepHitDoubletsTripl7, process.tobTecStepHitTripletsTripl7, process.tobTecStepSeedLayersPair7, process.tobTecStepSeedLayersTripl7, process.tobTecStepSeeds7, process.tobTecStepSeedsPair7, process.tobTecStepSeedsTripl7, process.tobTecStepTrackCandidates7, process.tobTecStepTrackingRegionsPair7, process.tobTecStepTrackingRegionsTripl7, process.tobTecStepTracks7, process.trackerClusterCheck7, process.siStripMatchedRecHits7))


hits = "8"
myCollection = "rCluster"+hits


process.MeasurementTrackerEvent8 = process.MeasurementTrackerEvent.clone(
    pixelClusterProducer = cms.string(myCollection),
    stripClusterProducer = cms.string(myCollection),
)

process.ak4CaloJetsForTrk8 = process.ak4CaloJetsForTrk.clone(
    src = cms.InputTag("caloTowerForTrk"+hits),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+hits),
)

process.caloTowerForTrk8 = process.caloTowerForTrk.clone()

process.chargeCut2069Clusters8 = process.chargeCut2069Clusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection)
)

process.detachedQuadStep8 = process.detachedQuadStep.clone(
    src = cms.InputTag("detachedQuadStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedQuadStepClusters8 = process.detachedQuadStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("lowPtTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("lowPtTripletStepTracks"+hits)
)

process.detachedQuadStepHitDoublets8 = process.detachedQuadStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+hits)
)

process.detachedQuadStepHitQuadruplets8 = process.detachedQuadStepHitQuadruplets.clone(
    doublets = cms.InputTag("detachedQuadStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+hits+'__reRECO'),

)

process.detachedQuadStepSeedLayers8 = process.detachedQuadStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters"+hits)
    ),
)

process.detachedQuadStepSeeds8 = process.detachedQuadStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+hits)
)

process.detachedQuadStepTrackCandidates8 = process.detachedQuadStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedQuadStepClusters"+hits),
    src = cms.InputTag("detachedQuadStepSeeds"+hits)
)

process.detachedQuadStepTrackingRegions8 = process.detachedQuadStepTrackingRegions.clone()

process.detachedQuadStepTracks8 = process.detachedQuadStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedQuadStepTrackCandidates"+hits)
)

process.detachedTripletStep8 = process.detachedTripletStep.clone(
    src = cms.InputTag("detachedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.detachedTripletStepClusters8 = process.detachedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedQuadStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedQuadStepTracks"+hits)
)

process.detachedTripletStepHitDoublets8 = process.detachedTripletStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"+hits),
)

process.detachedTripletStepHitTriplets8 = process.detachedTripletStepHitTriplets.clone(
    doublets = cms.InputTag("detachedTripletStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+hits+'__reRECO')
)

process.detachedTripletStepSeedLayers8 = process.detachedTripletStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters"+hits)
    )
)

process.detachedTripletStepSeedClusterMask8 = process.detachedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("lowPtTripletStepSeeds"+hits)
)

process.detachedTripletStepSeeds8 = process.detachedTripletStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+hits)
)

process.detachedTripletStepTrackCandidates8 = process.detachedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"+hits),
    src = cms.InputTag("detachedTripletStepSeeds"+hits)
)

process.detachedTripletStepTrackingRegions8 = process.detachedTripletStepTrackingRegions.clone()

process.detachedTripletStepTracks8 = process.detachedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("detachedTripletStepTrackCandidates"+hits)
)

process.duplicateTrackCandidates8 = process.duplicateTrackCandidates.clone(
    source = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.duplicateTrackClassifier8 = process.duplicateTrackClassifier.clone(
    src = cms.InputTag("mergedDuplicateTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.earlyGeneralTracks8 = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep'+hits, 
        'highPtTripletStep'+hits, 
#        'jetCoreRegionalStep'+hits, 
        'lowPtQuadStep'+hits, 
        'lowPtTripletStep'+hits, 
        'detachedQuadStep'+hits, 
        'detachedTripletStep'+hits, 
        'pixelPairStep'+hits, 
        'mixedTripletStep'+hits, 
        'pixelLessStep'+hits, 
        'tobTecStep'+hits
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks"+hits, "highPtTripletStepTracks"+hits, "lowPtQuadStepTracks"+hits, "lowPtTripletStepTracks"+hits, 
        "detachedQuadStepTracks"+hits, "detachedTripletStepTracks"+hits, "pixelPairStepTracks"+hits, "mixedTripletStepTracks"+hits, "pixelLessStepTracks"+hits, 
        "tobTecStepTracks"+hits
    )
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

process.generalTracks8 = process.generalTracks.clone(
    candidateComponents = cms.InputTag("duplicateTrackCandidates"+hits,"candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates"+hits,"candidates"),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+hits,"MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"+hits),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+hits,"MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+hits)
)

process.highPtTripletStep8 = process.highPtTripletStep.clone(
    src = cms.InputTag("highPtTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.highPtTripletStepClusters8 = process.highPtTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+hits),
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

process.highPtTripletStepSeedClusterMask8 = process.highPtTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("highPtTripletStepSeeds"+hits)
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

process.initialStep8 = process.initialStep.clone(
    src = cms.InputTag("initialStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.initialStepHitDoublets8 = process.initialStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("initialStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"+hits)
)

process.initialStepHitQuadruplets8 = process.initialStepHitQuadruplets.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+hits+'__reRECO')
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

process.initialStepSeedClusterMask8 = process.initialStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("initialStepSeeds"+hits)
)

process.initialStepSeeds8 = process.initialStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+hits)
)

process.initialStepTrackCandidates8 = process.initialStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilder')
    ),
    src = cms.InputTag("initialStepSeeds"+hits),
)

process.initialStepTrackRefsForJets8 = process.initialStepTrackRefsForJets.clone(
    src = cms.InputTag("initialStepTracks"+hits)
)

process.initialStepTrackingRegions8 = process.initialStepTrackingRegions.clone()

process.initialStepTracks8 = process.initialStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("initialStepTrackCandidates"+hits),
)

process.jetsForCoreTracking8 = process.jetsForCoreTracking.clone(
    src = cms.InputTag("ak4CaloJetsForTrk"+hits)
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
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

process.mergedDuplicateTracks8 = process.mergedDuplicateTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("duplicateTrackCandidates"+hits,"candidates")
)

process.mixedTripletStep8 = process.mixedTripletStep.clone(
    src = cms.InputTag("mixedTripletStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.mixedTripletStepClusters8 = process.mixedTripletStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelPairStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelPairStepTracks"+hits)
)

process.mixedTripletStepHitDoubletsA8 = process.mixedTripletStepHitDoubletsA.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"+hits)
)

process.mixedTripletStepHitDoubletsB8 = process.mixedTripletStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+hits),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"+hits)
)

process.mixedTripletStepHitTripletsA8 = process.mixedTripletStepHitTripletsA.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO')
)

process.mixedTripletStepHitTripletsB8 = process.mixedTripletStepHitTripletsB.clone(
    doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO')
)

process.mixedTripletStepSeedLayersA8 = process.mixedTripletStepSeedLayersA.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.mixedTripletStepSeedLayersB8 = process.mixedTripletStepSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("mixedTripletStepClusters"+hits)
    )
)

process.mixedTripletStepSeedClusterMask8 = process.mixedTripletStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepSeeds8 = process.mixedTripletStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"+hits), cms.InputTag("mixedTripletStepSeedsB"+hits))
)

process.mixedTripletStepSeedsA8 = process.mixedTripletStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+hits)
)

process.mixedTripletStepSeedsB8 = process.mixedTripletStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+hits+'__reRECO', 
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+hits)
)

process.mixedTripletStepTrackCandidates8 = process.mixedTripletStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"+hits),
    src = cms.InputTag("mixedTripletStepSeeds"+hits)
)

process.mixedTripletStepTrackingRegionsA8 = process.mixedTripletStepTrackingRegionsA.clone()

process.mixedTripletStepTrackingRegionsB8 = process.mixedTripletStepTrackingRegionsB.clone()

process.mixedTripletStepTracks8 = process.mixedTripletStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("mixedTripletStepTrackCandidates"+hits)
)

process.pixelLessStep8 = process.pixelLessStep.clone(
    src = cms.InputTag("pixelLessStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelLessStepClusters8 = process.pixelLessStepClusters.clone(
oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("mixedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("mixedTripletStepTracks"+hits)
)

process.pixelLessStepHitDoublets8 = process.pixelLessStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"+hits)
)

process.pixelLessStepHitTriplets8 = process.pixelLessStepHitTriplets.clone(
    doublets = cms.InputTag("pixelLessStepHitDoublets"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+hits+'__reRECO')
)

process.pixelLessStepSeedLayers8 = process.pixelLessStepSeedLayers.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    MTID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits)
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"+hits),
        useRingSlector = cms.bool(True)
    )
)

process.pixelLessStepSeedClusterMask8 = process.pixelLessStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepSeeds8 = process.pixelLessStepSeeds.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+hits)
)

process.pixelLessStepTrackCandidates8 = process.pixelLessStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"+hits),
    src = cms.InputTag("pixelLessStepSeeds"+hits)
)

process.pixelLessStepTrackingRegions8 = process.pixelLessStepTrackingRegions.clone()

process.pixelLessStepTracks8 = process.pixelLessStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelLessStepTrackCandidates"+hits)
)


process.pixelPairStep8 = process.pixelPairStep.clone(
    src = cms.InputTag("pixelPairStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.pixelPairStepClusters8 = process.pixelPairStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("detachedTripletStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("detachedTripletStepTracks"+hits)
)

process.pixelPairStepHitDoublets8 = process.pixelPairStepHitDoublets.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+hits),
    trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+hits)
)

process.pixelPairStepHitDoubletsB8 = process.pixelPairStepHitDoubletsB.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+hits)
)

process.pixelPairStepSeedLayers8 = process.pixelPairStepSeedLayers.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    )
)

process.pixelPairStepSeeds8 = process.pixelPairStepSeeds.clone(
    seedCollections = cms.VInputTag("pixelPairStepSeedsA"+hits, "pixelPairStepSeedsB"+hits)
)

process.pixelPairStepSeedsA8 = process.pixelPairStepSeedsA.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+hits)
)

process.pixelPairStepSeedsB8 = process.pixelPairStepSeedsB.clone(
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+hits)
)

process.pixelPairStepTrackCandidates8 = process.pixelPairStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"+hits),
    src = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTrackingRegions8 = process.pixelPairStepTrackingRegions.clone(
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(5),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag(myCollection),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)

process.pixelPairStepTrackingRegionsSeedLayersB8 = process.pixelPairStepTrackingRegionsSeedLayersB.clone(
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'+hits),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters"+hits)
    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        deltaEta_Cand = cms.double(-1),
        deltaPhi_Cand = cms.double(-1),
        extraEta = cms.double(0),
        extraPhi = cms.double(0),
        input = cms.InputTag(""),
        maxNVertices = cms.int32(5),
        measurementTrackerName = cms.InputTag(""),
        nSigmaZBeamSpot = cms.double(4),
        nSigmaZVertex = cms.double(3),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        searchOpt = cms.bool(False),
        seedingMode = cms.string('Global'),
        vertexCollection = cms.InputTag("firstStepPrimaryVertices"+hits),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVertex = cms.double(0.03)
    )
)

process.pixelPairStepSeedClusterMask8 = process.pixelPairStepSeedClusterMask.clone(
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trajectories = cms.InputTag("pixelPairStepSeeds"+hits)
)

process.pixelPairStepTracks8 = process.pixelPairStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("pixelPairStepTrackCandidates"+hits)
)

process.preDuplicateMergingGeneralTracks8 = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+hits 
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks"+hits)
)

process.siPixelClusterShapeCache8 = process.siPixelClusterShapeCache.clone(
    src = cms.InputTag(myCollection)
)

process.siPixelRecHits8 = process.siPixelRecHits.clone(
    src = cms.InputTag(myCollection)
)

process.tobTecStep8 = process.tobTecStep.clone(
    src = cms.InputTag("tobTecStepTracks"+hits),
    vertices = cms.InputTag("firstStepPrimaryVertices"+hits)
)

process.tobTecStepClusters8 = process.tobTecStepClusters.clone(
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+hits),
    pixelClusters = cms.InputTag(myCollection),
    stripClusters = cms.InputTag(myCollection),
    trackClassifier = cms.InputTag("pixelLessStep"+hits,"QualityMasks"),
    trajectories = cms.InputTag("pixelLessStepTracks"+hits)
)

process.tobTecStepHitDoubletsPair8 = process.tobTecStepHitDoubletsPair.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"+hits)
)

process.tobTecStepHitDoubletsTripl8 = process.tobTecStepHitDoubletsTripl.clone(
    clusterCheck = cms.InputTag("trackerClusterCheck"+hits),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+hits),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"+hits)
)

process.tobTecStepHitTripletsTripl8 = process.tobTecStepHitTripletsTripl.clone(
    doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+hits),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+hits+'__reRECO')
)

process.tobTecStepSeedLayersPair8 = process.tobTecStepSeedLayersPair.clone(
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeedLayersTripl8 = process.tobTecStepSeedLayersTripl.clone(
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits),
        useRingSlector = cms.bool(True)
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits"+hits,"matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"+hits)
    )
)

process.tobTecStepSeeds8 = process.tobTecStepSeeds.clone(
    seedCollections = cms.VInputTag(cms.InputTag("tobTecStepSeedsTripl"+hits), cms.InputTag("tobTecStepSeedsPair"+hits))
)

process.tobTecStepSeedsPair8 = process.tobTecStepSeedsPair.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+hits+'__reRECO'),
    seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+hits)
)

process.tobTecStepSeedsTripl8 = process.tobTecStepSeedsTripl.clone(
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+hits),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+hits+'__reRECO', 
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+hits+'__reRECO'
    ),
    seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+hits)
)

process.tobTecStepTrackCandidates8 = process.tobTecStepTrackCandidates.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    clustersToSkip = cms.InputTag("tobTecStepClusters"+hits),
    src = cms.InputTag("tobTecStepSeeds"+hits)
)

process.tobTecStepTrackingRegionsPair8 = process.tobTecStepTrackingRegionsPair.clone()

process.tobTecStepTrackingRegionsTripl8 = process.tobTecStepTrackingRegionsTripl.clone()

process.tobTecStepTracks8 = process.tobTecStepTracks.clone(
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+hits),
    src = cms.InputTag("tobTecStepTrackCandidates"+hits)
)

process.trackerClusterCheck8 = process.trackerClusterCheck.clone(
    ClusterCollectionLabel = cms.InputTag(myCollection),
    PixelClusterCollectionLabel = cms.InputTag(myCollection)
)

process.siStripMatchedRecHits8 = process.siStripMatchedRecHits.clone(
    ClusterProducer = cms.InputTag(myCollection)
)


process.reconstruction_step8 = cms.Path(cms.Task(process.MeasurementTrackerEvent8, process.ak4CaloJetsForTrk8, process.caloTowerForTrk8, process.chargeCut2069Clusters8, process.detachedQuadStep8, process.detachedQuadStepClusters8, process.detachedQuadStepHitDoublets8, process.detachedQuadStepHitQuadruplets8, process.detachedQuadStepSeedLayers8, process.detachedQuadStepSeeds8, process.detachedQuadStepTrackCandidates8, process.detachedQuadStepTrackingRegions8, process.detachedQuadStepTracks8, process.detachedTripletStep8, process.detachedTripletStepClusters8, process.detachedTripletStepHitDoublets8, process.detachedTripletStepHitTriplets8, process.detachedTripletStepSeedLayers8, process.detachedTripletStepSeedClusterMask8, process.detachedTripletStepSeeds8, process.detachedTripletStepTrackCandidates8, process.detachedTripletStepTrackingRegions8, process.detachedTripletStepTracks8, process.duplicateTrackCandidates8, process.duplicateTrackClassifier8, process.earlyGeneralTracks8, process.firstStepGoodPrimaryVertices8, process.firstStepPrimaryVertices8, process.firstStepPrimaryVerticesUnsorted8, process.generalTracks8, process.highPtTripletStep8, process.highPtTripletStepClusters8, process.highPtTripletStepHitDoublets8, process.highPtTripletStepHitTriplets8, process.highPtTripletStepSeedLayers8, process.highPtTripletStepSeeds8, process.highPtTripletStepTrackCandidates8, process.highPtTripletStepTrackingRegions8, process.highPtTripletStepTracks8, process.initialStep8, process.initialStepHitDoublets8, process.initialStepHitQuadruplets8, process.initialStepSeedLayers8, process.initialStepSeedClusterMask8, process.initialStepSeeds8, process.initialStepTrackCandidates8, process.initialStepTrackRefsForJets8, process.initialStepTrackingRegions8, process.initialStepTracks8, process.jetsForCoreTracking8, process.lowPtQuadStep8, process.lowPtQuadStepClusters8, process.lowPtQuadStepHitDoublets8, process.lowPtQuadStepHitQuadruplets8, process.lowPtQuadStepSeedLayers8, process.lowPtQuadStepSeeds8, process.lowPtQuadStepTrackCandidates8, process.lowPtQuadStepTrackingRegions8, process.lowPtQuadStepTracks8, process.lowPtTripletStep8, process.lowPtTripletStepClusters8, process.lowPtTripletStepHitDoublets8, process.lowPtTripletStepHitTriplets8, process.lowPtTripletStepSeedLayers8, process.lowPtTripletStepSeeds8, process.lowPtTripletStepTrackCandidates8, process.lowPtTripletStepTrackingRegions8, process.lowPtTripletStepTracks8, process.mergedDuplicateTracks8, process.mixedTripletStep8, process.mixedTripletStepClusters8, process.mixedTripletStepHitDoubletsA8, process.mixedTripletStepHitDoubletsB8, process.mixedTripletStepHitTripletsA8, process.mixedTripletStepHitTripletsB8, process.mixedTripletStepSeedLayersA8, process.mixedTripletStepSeedLayersB8, process.mixedTripletStepSeedClusterMask8, process.mixedTripletStepSeeds8, process.mixedTripletStepSeedsA8, process.mixedTripletStepSeedsB8, process.mixedTripletStepTrackCandidates8, process.mixedTripletStepTrackingRegionsA8, process.mixedTripletStepTrackingRegionsB8, process.mixedTripletStepTracks8, process.pixelLessStep8, process.pixelLessStepClusters8, process.pixelLessStepHitDoublets8, process.pixelLessStepHitTriplets8, process.pixelLessStepSeedLayers8, process.pixelLessStepSeedClusterMask8, process.pixelLessStepSeeds8, process.pixelLessStepTrackCandidates8, process.pixelLessStepTrackingRegions8, process.pixelLessStepTracks8, process.pixelPairStep8, process.pixelPairStepClusters8, process.pixelPairStepHitDoublets8, process.pixelPairStepHitDoubletsB8, process.pixelPairStepSeedLayers8, process.pixelPairStepSeeds8, process.pixelPairStepSeedsA8, process.pixelPairStepSeedsB8, process.pixelPairStepTrackCandidates8, process.pixelPairStepTrackingRegions8, process.pixelPairStepTrackingRegionsSeedLayersB8, process.pixelPairStepTracks8, process.preDuplicateMergingGeneralTracks8, process.siPixelClusterShapeCache8, process.siPixelRecHits8, process.tobTecStep8, process.tobTecStepClusters8, process.tobTecStepHitDoubletsPair8, process.tobTecStepHitDoubletsTripl8, process.tobTecStepHitTripletsTripl8, process.tobTecStepSeedLayersPair8, process.tobTecStepSeedLayersTripl8, process.tobTecStepSeeds8, process.tobTecStepSeedsPair8, process.tobTecStepSeedsTripl8, process.tobTecStepTrackCandidates8, process.tobTecStepTrackingRegionsPair8, process.tobTecStepTrackingRegionsTripl8, process.tobTecStepTracks8, process.trackerClusterCheck8, process.siStripMatchedRecHits8))


process.endjob_step = cms.EndPath(cms.Task(process.MEtoEDMConverter))


process.RECOoutput_step = cms.EndPath(process.RECOoutput)


process.schedule = cms.Schedule(*[ process.reconstruction_step, process.reconstruction_step3, process.reconstruction_step4, process.reconstruction_step5, process.reconstruction_step6, process.reconstruction_step7, process.reconstruction_step8, process.endjob_step, process.RECOoutput_step ])
