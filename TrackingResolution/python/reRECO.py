# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase1_2021_realistic --datatier GEN-SIM-RECO --era Run3 --eventcontent RECOSIM --filein file:SHORT_OUTPUT_FILE_NAME.root --fileout file:reRECO_OUTPUT_FILE_NAME.root --geometry DB:Extended --no_exec --number -1 --python_filename reRECO.py --step RAW2DIGI,RECO --customise Configuration/DataProcessing/Utils.addMonitoring
import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')

options.register ('layersThreshold',
                  3, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.int,          # string, int, or float
                  "Number of threshold layers (from 3 to 8 so far)")

options.parseArguments()

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('reRECO',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
#    input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

filenames = []

for i in range(len(options.inputFiles)):
    filenames.append('file:shortened_'+options.inputFiles[i]+'.root')

# Input source
process.source = cms.Source("PoolSource",
  secondaryFileNames = cms.untracked.vstring(),
  fileNames = cms.untracked.vstring(
    filenames
  )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

#############################################################################################

#layers = options.layersThreshold
layers = 0
if options.layersThreshold<3 or options.layersThreshold>8: layers = 3
else: layers = options.layersThreshold

myCollection = "rCluster"+str(layers)

process.MeasurementTrackerEvent.pixelClusterProducer = cms.string(myCollection)
process.MeasurementTrackerEvent.stripClusterProducer = cms.string(myCollection)

process.MeasurementTrackerEventPreSplitting.stripClusterProducer = cms.string(myCollection)

process.chargeCut2069Clusters.pixelClusters = cms.InputTag(myCollection)
process.chargeCut2069Clusters.stripClusters = cms.InputTag(myCollection)

process.detachedQuadStepClusters.pixelClusters = cms.InputTag(myCollection)
process.detachedQuadStepClusters.stripClusters = cms.InputTag(myCollection)

process.detachedTripletStepClusters.pixelClusters = cms.InputTag(myCollection)
process.detachedTripletStepClusters.stripClusters = cms.InputTag(myCollection)

process.highPtTripletStepClusters.pixelClusters = cms.InputTag(myCollection)
process.highPtTripletStepClusters.stripClusters = cms.InputTag(myCollection)

process.initialStepSeedClusterMask.pixelClusters = cms.InputTag(myCollection)
process.initialStepSeedClusterMask.stripClusters = cms.InputTag(myCollection)

process.lowPtQuadStepClusters.pixelClusters = cms.InputTag(myCollection)
process.lowPtQuadStepClusters.stripClusters = cms.InputTag(myCollection)

process.lowPtTripletStepClusters.pixelClusters = cms.InputTag(myCollection)
process.lowPtTripletStepClusters.stripClusters = cms.InputTag(myCollection)

process.mixedTripletStepClusters.pixelClusters = cms.InputTag(myCollection)
process.mixedTripletStepClusters.stripClusters = cms.InputTag(myCollection)

process.pixelLessStepClusters.pixelClusters = cms.InputTag(myCollection)
process.pixelLessStepClusters.stripClusters = cms.InputTag(myCollection)

process.pixelPairStepClusters.pixelClusters = cms.InputTag(myCollection)
process.pixelPairStepClusters.stripClusters = cms.InputTag(myCollection)

process.pixelPairStepSeedClusterMask.pixelClusters = cms.InputTag(myCollection)
process.pixelPairStepSeedClusterMask.stripClusters = cms.InputTag(myCollection)

process.siPixelClusterShapeCache.src = cms.InputTag(myCollection)

process.siPixelRecHits.src = cms.InputTag(myCollection)

process.siStripMatchedRecHits.ClusterProducer = cms.InputTag(myCollection)

process.tobTecStepClusters.pixelClusters = cms.InputTag(myCollection)
process.tobTecStepClusters.stripClusters = cms.InputTag(myCollection)

process.trackerClusterCheck.ClusterCollectionLabel = cms.InputTag(myCollection)
process.trackerClusterCheck.PixelClusterCollectionLabel = cms.InputTag(myCollection)

process.CommonClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)
process.CommonClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)

process.beamhaloTrackerSeeds.PixelClusterCollectionLabel = cms.InputTag(myCollection)
process.beamhaloTrackerSeeds.ClusterCollectionLabel = cms.InputTag(myCollection)

process.clusterSummaryProducer.stripClusters = cms.InputTag(myCollection)

process.clusterSummaryProducerNoSplitting.pixelClusters = cms.InputTag(myCollection)
process.clusterSummaryProducerNoSplitting.stripClusters = cms.InputTag(myCollection)

process.conv2Clusters.pixelClusters = cms.InputTag(myCollection)
process.conv2Clusters.stripClusters = cms.InputTag(myCollection)

process.convClusters.pixelClusters = cms.InputTag(myCollection)
process.convClusters.stripClusters = cms.InputTag(myCollection)

process.detachedTripletStepSeedClusterMask.pixelClusters = cms.InputTag(myCollection)
process.detachedTripletStepSeedClusterMask.stripClusters = cms.InputTag(myCollection)

process.globalMixedSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)
process.globalMixedSeeds.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)

process.globalPixelLessSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)
process.globalPixelLessSeeds.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)

process.globalPixelSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)
process.globalPixelSeeds.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)

process.globalSeedsFromPairsWithVertices.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)
process.globalSeedsFromPairsWithVertices.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)
process.globalSeedsFromPairsWithVertices.RegionFactoryPSet.RegionPSet.pixelClustersForScaling = cms.InputTag(myCollection)

process.globalSeedsFromTriplets.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)
process.globalSeedsFromTriplets.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)

process.globalTrackingRegionWithVertices.RegionPSet.pixelClustersForScaling = cms.InputTag(myCollection)

process.highPtTripletStepSeedClusterMask.pixelClusters = cms.InputTag(myCollection)
process.highPtTripletStepSeedClusterMask.stripClusters = cms.InputTag(myCollection)

process.mixedTripletStepSeedClusterMask.pixelClusters = cms.InputTag(myCollection)
process.mixedTripletStepSeedClusterMask.stripClusters = cms.InputTag(myCollection)

process.photonConvTrajSeedFromQuadruplets.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)
process.photonConvTrajSeedFromQuadruplets.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)

process.photonConvTrajSeedFromSingleLeg.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)
process.photonConvTrajSeedFromSingleLeg.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)

process.pixelClusterTagInfos.pixelhit = cms.InputTag(myCollection)

process.pixelLessStepSeedClusterMask.pixelClusters = cms.InputTag(myCollection)
process.pixelLessStepSeedClusterMask.stripClusters = cms.InputTag(myCollection)

process.pixelPairElectronTrackingRegions.RegionPSet.pixelClustersForScaling = cms.InputTag(myCollection)

process.pixelPairStepTrackingRegions.RegionPSet.pixelClustersForScaling = cms.InputTag(myCollection)

process.regionalCosmicTrackerSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)
process.regionalCosmicTrackerSeeds.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)

process.seedClusterRemover.pixelClusters = cms.InputTag(myCollection)
process.seedClusterRemover.stripClusters = cms.InputTag(myCollection)

process.seedClusterRemoverPhase2.pixelClusters = cms.InputTag(myCollection)

process.seedGeneratorFromRegionHitsEDProducer.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag(myCollection)
process.seedGeneratorFromRegionHitsEDProducer.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag(myCollection)

process.tpClusterProducer.pixelClusterSrc = cms.InputTag(myCollection)
process.tpClusterProducer.stripClusterSrc = cms.InputTag(myCollection)

process.trackClusterRemover.pixelClusters = cms.InputTag(myCollection)
process.trackClusterRemover.stripClusters = cms.InputTag(myCollection)

process.trackerClusterCheckPreSplitting.ClusterCollectionLabel = cms.InputTag(myCollection)

process.tripletElectronClusterMask.pixelClusters = cms.InputTag(myCollection)
process.tripletElectronClusterMask.stripClusters = cms.InputTag(myCollection)

#############################################################################################

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:reRECO_'+str(options.layersThreshold)+'layers_'+options.outputFile),
    outputCommands = cms.untracked.vstring( (
    'drop *',
    'keep reco*_*_*_HITREMOVER',
    'keep reco*_offlinePrimaryVertices__RECO',
    'keep recoMuons_muons_*_RECO',
    'keep recoTracks_generalTracks*_*_reRECO',
         ) ),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

process.reconstruction_trackingOnly_3layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_4layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_5layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_6layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_7layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_8layers = process.reconstruction_trackingOnly.copy()

####################################################################################################

layers = "3"

process.MeasurementTrackerEventPreSplitting3 = process.MeasurementTrackerEventPreSplitting.clone()
process.MeasurementTrackerEventPreSplitting3.stripClusterProducer = cms.string('rCluster'+layers)

process.trackExtrapolator3 = process.trackExtrapolator.clone()
process.trackExtrapolator3.trackSrc = cms.InputTag("generalTracks"+layers)

process.generalV0Candidates3 = process.generalV0Candidates.clone()
process.generalV0Candidates3.trackRecoAlgorithm = cms.InputTag("generalTracks"+layers)
process.generalV0Candidates3.vertices = cms.InputTag("offlinePrimaryVertices"+layers)

process.offlinePrimaryVertices3 = process.offlinePrimaryVertices.clone()
process.offlinePrimaryVertices3.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVertices3.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVertices3.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.offlinePrimaryVerticesWithBS3 = process.offlinePrimaryVerticesWithBS.clone()
process.offlinePrimaryVerticesWithBS3.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVerticesWithBS3.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVerticesWithBS3.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers,"WithBS")

process.trackRefsForJetsBeforeSorting3 = process.trackRefsForJetsBeforeSorting.clone()
process.trackRefsForJetsBeforeSorting3.src = cms.InputTag("trackWithVertexRefSelectorBeforeSorting"+layers)

process.trackWithVertexRefSelectorBeforeSorting3 = process.trackWithVertexRefSelectorBeforeSorting.clone()
process.trackWithVertexRefSelectorBeforeSorting3.src = cms.InputTag("generalTracks"+layers)
process.trackWithVertexRefSelectorBeforeSorting3.vertexTag = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.unsortedOfflinePrimaryVertices3 = process.unsortedOfflinePrimaryVertices.clone()
process.unsortedOfflinePrimaryVertices3.TrackLabel = cms.InputTag("generalTracks"+layers)

process.ak4CaloJetsForTrk3 = process.ak4CaloJetsForTrk.clone()
process.ak4CaloJetsForTrk3.srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.inclusiveSecondaryVertices3 = process.inclusiveSecondaryVertices.clone()
process.inclusiveSecondaryVertices3.secondaryVertices = cms.InputTag("trackVertexArbitrator"+layers)

process.inclusiveVertexFinder3 = process.inclusiveVertexFinder.clone() 
process.inclusiveVertexFinder3.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.inclusiveVertexFinder3.tracks = cms.InputTag("generalTracks"+layers)

process.trackVertexArbitrator3 = process.trackVertexArbitrator.clone() 
process.trackVertexArbitrator3.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.trackVertexArbitrator3.secondaryVertices = cms.InputTag("vertexMerger"+layers)
process.trackVertexArbitrator3.tracks = cms.InputTag("generalTracks"+layers)

process.vertexMerger3 = process.vertexMerger.clone()
process.vertexMerger3.secondaryVertices = cms.InputTag("inclusiveVertexFinder"+layers)

process.dedxHarmonic23 = process.dedxHarmonic2.clone()
process.dedxHarmonic23.tracks = cms.InputTag("generalTracks"+layers)

process.dedxHitInfo3 = process.dedxHitInfo.clone() 
process.dedxHitInfo3.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelAndStripHarmonic2T0853 = process.dedxPixelAndStripHarmonic2T085.clone() 
process.dedxPixelAndStripHarmonic2T0853.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelHarmonic23 = process.dedxPixelHarmonic2.clone() 
process.dedxPixelHarmonic23.tracks = cms.InputTag("generalTracks"+layers)

process.dedxTruncated403 = process.dedxTruncated40.clone()
process.dedxTruncated403.tracks = cms.InputTag("generalTracks"+layers)

process.detachedTripletStepSeedClusterMask3 = process.detachedTripletStepSeedClusterMask.clone() 
process.detachedTripletStepSeedClusterMask3.oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+layers)
process.detachedTripletStepSeedClusterMask3.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask3.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask3.trajectories = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.initialStepSeedClusterMask3 = process.initialStepSeedClusterMask.clone() 
process.initialStepSeedClusterMask3.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.initialStepSeedClusterMask3.pixelClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask3.stripClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask3.trajectories = cms.InputTag("initialStepSeeds"+layers)

process.mixedTripletStepSeedClusterMask3 = process.mixedTripletStepSeedClusterMask.clone() 
process.mixedTripletStepSeedClusterMask3.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+layers)
process.mixedTripletStepSeedClusterMask3.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask3.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask3.trajectories = cms.InputTag("mixedTripletStepSeeds"+layers)

process.newCombinedSeeds3 = process.newCombinedSeeds.clone()
process.newCombinedSeeds3.seedCollections = cms.VInputTag(
        "initialStepSeeds"+layers, "highPtTripletStepSeeds"+layers, "mixedTripletStepSeeds"+layers, "pixelLessStepSeeds"+layers, "tripletElectronSeeds"+layers,
        "pixelPairElectronSeeds"+layers, "stripPairElectronSeeds"+layers, "lowPtTripletStepSeeds"+layers, "lowPtQuadStepSeeds"+layers, "detachedTripletStepSeeds"+layers,
        "detachedQuadStepSeeds"+layers, "pixelPairStepSeeds"+layers
    )

process.pixelLessStepSeedClusterMask3 = process.pixelLessStepSeedClusterMask.clone() 
process.pixelLessStepSeedClusterMask3.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+layers)
process.pixelLessStepSeedClusterMask3.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask3.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask3.trajectories = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelPairElectronHitDoublets3 = process.pixelPairElectronHitDoublets.clone() 
process.pixelPairElectronHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairElectronHitDoublets3.seedingLayers = cms.InputTag("pixelPairElectronSeedLayers"+layers)
process.pixelPairElectronHitDoublets3.trackingRegions = cms.InputTag("pixelPairElectronTrackingRegions"+layers)

process.pixelPairElectronSeedLayers3 = process.pixelPairElectronSeedLayers.clone()
process.pixelPairElectronSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers3.BPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.pixelPairElectronSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers3.FPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.pixelPairElectronSeeds3 = process.pixelPairElectronSeeds.clone()
process.pixelPairElectronSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairElectronHitDoublets'+layers+'__reRECO')
process.pixelPairElectronSeeds3.seedingHitSets = cms.InputTag("pixelPairElectronHitDoublets"+layers)

process.pixelPairElectronTrackingRegions3 = process.pixelPairElectronTrackingRegions.clone() 
process.pixelPairElectronTrackingRegions3.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairElectronTrackingRegions3.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.stripPairElectronHitDoublets3 = process.stripPairElectronHitDoublets.clone() 
process.stripPairElectronHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.stripPairElectronHitDoublets3.seedingLayers = cms.InputTag("stripPairElectronSeedLayers"+layers)

process.stripPairElectronSeedLayers3 = process.stripPairElectronSeedLayers.clone() 
process.stripPairElectronSeedLayers3.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers3.TEC.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers3.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers3.TIB.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers3.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers3.TID.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.stripPairElectronSeeds3 = process.stripPairElectronSeeds.clone() 
process.stripPairElectronSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_stripPairElectronHitDoublets'+layers+'__reRECO')
process.stripPairElectronSeeds3.seedingHitSets = cms.InputTag("stripPairElectronHitDoublets"+layers)

process.tripletElectronClusterMask3 = process.tripletElectronClusterMask.clone()
process.tripletElectronClusterMask3.oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronClusterMask3.pixelClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask3.stripClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask3.trajectories = cms.InputTag("tripletElectronSeeds"+layers)

process.tripletElectronHitDoublets3 = process.tripletElectronHitDoublets.clone() 
process.tripletElectronHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tripletElectronHitDoublets3.seedingLayers = cms.InputTag("tripletElectronSeedLayers"+layers)

process.tripletElectronHitTriplets3 = process.tripletElectronHitTriplets.clone()
process.tripletElectronHitTriplets3.doublets = cms.InputTag("tripletElectronHitDoublets"+layers)
process.tripletElectronHitTriplets3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO')

process.tripletElectronSeedLayers3 = process.tripletElectronSeedLayers.clone()
process.tripletElectronSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers3.BPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers3.FPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)

process.tripletElectronSeeds3 = process.tripletElectronSeeds.clone()
process.tripletElectronSeeds3.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tripletElectronHitTriplets'+layers+'__reRECO',
        'IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO'
    )
process.tripletElectronSeeds3.seedingHitSets = cms.InputTag("tripletElectronHitTriplets"+layers)

process.conversionStepTracks3 = process.conversionStepTracks.clone()
process.conversionStepTracks3.TrackProducers = cms.VInputTag("convStepTracks"+layers)
process.conversionStepTracks3.selectedTrackQuals = cms.VInputTag("convStepSelector"+layers+":convStep"+layers)

process.earlyGeneralTracks3 = process.earlyGeneralTracks.clone()
process.earlyGeneralTracks3.inputClassifiers = cms.vstring(
        'initialStep'+layers,
        'highPtTripletStep'+layers,
        'jetCoreRegionalStep'+layers,
        'lowPtQuadStep'+layers,
        'lowPtTripletStep'+layers,
        'detachedQuadStep'+layers,
        'detachedTripletStep'+layers,
        'pixelPairStep'+layers,
        'mixedTripletStep'+layers,
        'pixelLessStep'+layers,
        'tobTecStep'+layers
    )
process.earlyGeneralTracks3.trackProducers = cms.VInputTag(
        "initialStepTracks"+layers, "highPtTripletStepTracks"+layers, "jetCoreRegionalStepTracks"+layers, "lowPtQuadStepTracks"+layers, "lowPtTripletStepTracks"+layers,
        "detachedQuadStepTracks"+layers, "detachedTripletStepTracks"+layers, "pixelPairStepTracks"+layers, "mixedTripletStepTracks"+layers, "pixelLessStepTracks"+layers,
        "tobTecStepTracks"+layers
    )

process.preDuplicateMergingGeneralTracks3 = process.preDuplicateMergingGeneralTracks.clone()
process.preDuplicateMergingGeneralTracks3.inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+layers,
        'muonSeededTracksInOutClassifier'+layers,
        'muonSeededTracksOutInClassifier'+layers
    )
process.preDuplicateMergingGeneralTracks3.trackProducers = cms.VInputTag("earlyGeneralTracks"+layers, "muonSeededTracksInOut"+layers, "muonSeededTracksOutIn"+layers)

process.trackerClusterCheck3 = process.trackerClusterCheck.clone()
process.trackerClusterCheck3.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.trackerClusterCheck3.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.convClusters3 = process.convClusters.clone()
process.convClusters3.oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"+layers)
process.convClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.convClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.convClusters3.trackClassifier = cms.InputTag("tobTecStep"+layers,"QualityMasks")
process.convClusters3.trajectories = cms.InputTag("tobTecStepTracks"+layers)

process.convLayerPairs3 = process.convLayerPairs.clone()
process.convLayerPairs3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs3.BPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs3.FPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs3.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs3.MTIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs3.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs3.MTOB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs3.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs3.TEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHitUnmatched")
process.convLayerPairs3.TEC.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs3.TEC.stereoRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHitUnmatched")
process.convLayerPairs3.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs3.TIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs3.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs3.TID.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs3.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs3.TOB.skipClusters = cms.InputTag("convClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.convStepSelector3 = process.convStepSelector.clone()
process.convStepSelector3.src = cms.InputTag("convStepTracks"+layers)
#process.convStepSelector3.trackSelectors.name = cms.string('convStep'+layers)
process.convStepSelector3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.convStepTracks3 = process.convStepTracks.clone()
process.convStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convStepTracks3.src = cms.InputTag("convTrackCandidates"+layers)

process.convTrackCandidates3 = process.convTrackCandidates.clone()
process.convTrackCandidates3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convTrackCandidates3.clustersToSkip = cms.InputTag("convClusters"+layers)
process.convTrackCandidates3.src = cms.InputTag("photonConvTrajSeedFromSingleLeg"+layers,"convSeedCandidates")

process.photonConvTrajSeedFromSingleLeg3 = process.photonConvTrajSeedFromSingleLeg.clone()
process.photonConvTrajSeedFromSingleLeg3.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg3.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg3.OrderedHitsFactoryPSet.SeedingLayers = cms.InputTag("convLayerPairs"+layers)
process.photonConvTrajSeedFromSingleLeg3.TrackRefitter = cms.InputTag("generalTracks"+layers)
process.photonConvTrajSeedFromSingleLeg3.primaryVerticesTag = cms.InputTag("firstStepPrimaryVertices"+layers)

process.MeasurementTrackerEvent3 = process.MeasurementTrackerEvent.clone()
process.MeasurementTrackerEvent3.pixelClusterProducer = cms.string('rCluster'+layers)
process.MeasurementTrackerEvent3.stripClusterProducer = cms.string('rCluster'+layers)

process.ak4CaloJetsForTrkPreSplitting3 = process.ak4CaloJetsForTrkPreSplitting.clone()
process.ak4CaloJetsForTrkPreSplitting3.srcPVs = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.firstStepPrimaryVerticesPreSplitting3 = process.firstStepPrimaryVerticesPreSplitting.clone()
process.firstStepPrimaryVerticesPreSplitting3.TrackLabel = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepHitDoubletsPreSplitting3 = process.initialStepHitDoubletsPreSplitting.clone()
process.initialStepHitDoubletsPreSplitting3.clusterCheck = cms.InputTag("trackerClusterCheckPreSplitting"+layers)

process.initialStepHitQuadrupletsPreSplitting3 = process.initialStepHitQuadrupletsPreSplitting.clone()
process.initialStepHitQuadrupletsPreSplitting3.doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"+layers)
process.initialStepHitQuadrupletsPreSplitting3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoubletsPreSplitting'+layers+'__reRECO')

process.initialStepSeedsPreSplitting3 = process.initialStepSeedsPreSplitting.clone()
process.initialStepSeedsPreSplitting3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadrupletsPreSplitting'+layers+'__reRECO')
process.initialStepSeedsPreSplitting3.seedingHitSets = cms.InputTag("initialStepHitQuadrupletsPreSplitting"+layers)

process.initialStepTrackCandidatesMkFitConfigPreSplitting3 = process.initialStepTrackCandidatesMkFitConfigPreSplitting.clone()
process.initialStepTrackCandidatesMkFitConfigPreSplitting3.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfigPreSplitting'+layers)

process.initialStepTrackCandidatesMkFitPreSplitting3 = process.initialStepTrackCandidatesMkFitPreSplitting.clone()
process.initialStepTrackCandidatesMkFitPreSplitting3.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfigPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting3.eventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting3.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFitPreSplitting3.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting3.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitSeedsPreSplitting3 = process.initialStepTrackCandidatesMkFitSeedsPreSplitting.clone()
process.initialStepTrackCandidatesMkFitSeedsPreSplitting3.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)

process.initialStepTrackCandidatesPreSplitting3 = process.initialStepTrackCandidatesPreSplitting.clone()
process.initialStepTrackCandidatesPreSplitting3.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFitPreSplitting'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesPreSplitting3.mkFitEventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting3.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting3.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidatesPreSplitting3.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting3.tracks = cms.InputTag("initialStepTrackCandidatesMkFitPreSplitting"+layers)

process.initialStepTrackRefsForJetsPreSplitting3 = process.initialStepTrackRefsForJetsPreSplitting.clone()
process.initialStepTrackRefsForJetsPreSplitting3.src = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepTracksPreSplitting3 = process.initialStepTracksPreSplitting.clone()
process.initialStepTracksPreSplitting3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"+layers)
process.initialStepTracksPreSplitting3.src = cms.InputTag("initialStepTrackCandidatesPreSplitting"+layers)

process.jetsForCoreTrackingPreSplitting3 = process.jetsForCoreTrackingPreSplitting.clone()
process.jetsForCoreTrackingPreSplitting3.src = cms.InputTag("ak4CaloJetsForTrkPreSplitting"+layers)

process.mkFitEventOfHitsPreSplitting3 = process.mkFitEventOfHitsPreSplitting.clone()
process.mkFitEventOfHitsPreSplitting3.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHitsPreSplitting3.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiStripHits3 = process.mkFitSiStripHits.clone()
process.mkFitSiStripHits3.rphiHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.mkFitSiStripHits3.stereoHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHit")

process.siPixelClusterShapeCache3 = process.siPixelClusterShapeCache.clone()
process.siPixelClusterShapeCache3.src = cms.InputTag("rCluster"+layers)

process.siPixelClusters3 = process.siPixelClusters.clone()
process.siPixelClusters3.cores = cms.InputTag("jetsForCoreTrackingPreSplitting"+layers)
process.siPixelClusters3.vertices = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.siPixelRecHits3 = process.siPixelRecHits.clone()
process.siPixelRecHits3.src = cms.InputTag("rCluster"+layers)

process.trackerClusterCheckPreSplitting3 = process.trackerClusterCheckPreSplitting.clone()
process.trackerClusterCheckPreSplitting3.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.duplicateTrackCandidates3 = process.duplicateTrackCandidates.clone()
process.duplicateTrackCandidates3.source = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.duplicateTrackClassifier3 = process.duplicateTrackClassifier.clone()
process.duplicateTrackClassifier3.src = cms.InputTag("mergedDuplicateTracks"+layers)
process.duplicateTrackClassifier3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.generalTracks3 = process.generalTracks.clone()
process.generalTracks3.candidateComponents = cms.InputTag("duplicateTrackCandidates"+layers,"candidateMap")
process.generalTracks3.candidateSource = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")
process.generalTracks3.mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+layers,"MVAValues")
process.generalTracks3.mergedSource = cms.InputTag("mergedDuplicateTracks"+layers)
process.generalTracks3.originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+layers,"MVAValues")
process.generalTracks3.originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.mergedDuplicateTracks3 = process.mergedDuplicateTracks.clone()
process.mergedDuplicateTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mergedDuplicateTracks3.src = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")

process.earlyMuons3 = process.earlyMuons.clone()
process.earlyMuons3.TrackExtractorPSet.inputTrackCollection = cms.InputTag("generalTracks"+layers)
process.earlyMuons3.inputCollectionLabels = cms.VInputTag("earlyGeneralTracks"+layers, "standAloneMuons:UpdatedAtVtx")
process.earlyMuons3.pvInputTag = cms.InputTag("offlinePrimaryVertices"+layers)

process.detachedQuadStep3 = process.detachedQuadStep.clone()
process.detachedQuadStep3.src = cms.InputTag("detachedQuadStepTracks"+layers)
process.detachedQuadStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedQuadStepClusters3 = process.detachedQuadStepClusters.clone()
process.detachedQuadStepClusters3.oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+layers)
process.detachedQuadStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters3.trackClassifier = cms.InputTag("lowPtTripletStep"+layers,"QualityMasks")
process.detachedQuadStepClusters3.trajectories = cms.InputTag("lowPtTripletStepTracks"+layers)

process.detachedQuadStepHitDoublets3 = process.detachedQuadStepHitDoublets.clone()
process.detachedQuadStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedQuadStepHitDoublets3.seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+layers)

process.detachedQuadStepHitQuadruplets3 = process.detachedQuadStepHitQuadruplets.clone()
process.detachedQuadStepHitQuadruplets3.doublets = cms.InputTag("detachedQuadStepHitDoublets"+layers)
process.detachedQuadStepHitQuadruplets3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+layers+'__reRECO')

process.detachedQuadStepSeedLayers3 = process.detachedQuadStepSeedLayers.clone()
process.detachedQuadStepSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers3.BPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers3.FPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)

process.detachedQuadStepSeeds3 = process.detachedQuadStepSeeds.clone()
process.detachedQuadStepSeeds3.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedQuadStepSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+layers+'__reRECO')
process.detachedQuadStepSeeds3.seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+layers)

process.detachedQuadStepTrackCandidates3 = process.detachedQuadStepTrackCandidates.clone()
process.detachedQuadStepTrackCandidates3.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedQuadStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidates3.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidates3.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidates3.mkFitSeeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidates3.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedQuadStepTrackCandidates3.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)
process.detachedQuadStepTrackCandidates3.tracks = cms.InputTag("detachedQuadStepTrackCandidatesMkFit"+layers)

process.detachedQuadStepTrackCandidatesMkFit3 = process.detachedQuadStepTrackCandidatesMkFit.clone()
process.detachedQuadStepTrackCandidatesMkFit3.clustersToSkip = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepTrackCandidatesMkFit3.config = cms.ESInputTag("","detachedQuadStepTrackCandidatesMkFitConfig"+layers)
process.detachedQuadStepTrackCandidatesMkFit3.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit3.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidatesMkFit3.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit3.seeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidatesMkFit3.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedQuadStepTrackCandidatesMkFitConfig3 = process.detachedQuadStepTrackCandidatesMkFitConfig.clone()
process.detachedQuadStepTrackCandidatesMkFitConfig3.ComponentName = cms.string('detachedQuadStepTrackCandidatesMkFitConfig'+layers)

process.detachedQuadStepTrackCandidatesMkFitSeeds3 = process.detachedQuadStepTrackCandidatesMkFitSeeds.clone()
process.detachedQuadStepTrackCandidatesMkFitSeeds3.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)

process.detachedQuadStepTracks3 = process.detachedQuadStepTracks.clone()
process.detachedQuadStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedQuadStepTracks3.src = cms.InputTag("detachedQuadStepTrackCandidates"+layers)

process.detachedTripletStep3 = process.detachedTripletStep.clone()
process.detachedTripletStep3.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier13 = process.detachedTripletStepClassifier1.clone()
process.detachedTripletStepClassifier13.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier13.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier23 = process.detachedTripletStepClassifier2.clone()
process.detachedTripletStepClassifier23.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier23.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClusters3 = process.detachedTripletStepClusters.clone()
process.detachedTripletStepClusters3.oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedTripletStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters3.trackClassifier = cms.InputTag("detachedQuadStep"+layers,"QualityMasks")
process.detachedTripletStepClusters3.trajectories = cms.InputTag("detachedQuadStepTracks"+layers)

process.detachedTripletStepHitDoublets3 = process.detachedTripletStepHitDoublets.clone()
process.detachedTripletStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedTripletStepHitDoublets3.seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+layers)

process.detachedTripletStepHitTriplets3 = process.detachedTripletStepHitTriplets.clone()
process.detachedTripletStepHitTriplets3.doublets = cms.InputTag("detachedTripletStepHitDoublets"+layers)
process.detachedTripletStepHitTriplets3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+layers+'__reRECO')

process.detachedTripletStepSeedLayers3 = process.detachedTripletStepSeedLayers.clone()
process.detachedTripletStepSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers3.BPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers3.FPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)

process.detachedTripletStepSeeds3 = process.detachedTripletStepSeeds.clone()
process.detachedTripletStepSeeds3.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedTripletStepSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+layers+'__reRECO')
process.detachedTripletStepSeeds3.seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+layers)

process.detachedTripletStepTrackCandidates3 = process.detachedTripletStepTrackCandidates.clone()
process.detachedTripletStepTrackCandidates3.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidates3.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidates3.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidates3.mkFitSeeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidates3.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedTripletStepTrackCandidates3.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)
process.detachedTripletStepTrackCandidates3.tracks = cms.InputTag("detachedTripletStepTrackCandidatesMkFit"+layers)

process.detachedTripletStepTrackCandidatesMkFit3 = process.detachedTripletStepTrackCandidatesMkFit.clone()
process.detachedTripletStepTrackCandidatesMkFit3.clustersToSkip = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepTrackCandidatesMkFit3.config = cms.ESInputTag("","detachedTripletStepTrackCandidatesMkFitConfig"+layers)
process.detachedTripletStepTrackCandidatesMkFit3.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit3.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidatesMkFit3.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit3.seeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidatesMkFit3.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedTripletStepTrackCandidatesMkFitConfig3 = process.detachedTripletStepTrackCandidatesMkFitConfig.clone()
process.detachedTripletStepTrackCandidatesMkFitConfig3.ComponentName = cms.string('detachedTripletStepTrackCandidatesMkFitConfig'+layers)

process.detachedTripletStepTrackCandidatesMkFitSeeds3 = process.detachedTripletStepTrackCandidatesMkFitSeeds.clone()
process.detachedTripletStepTrackCandidatesMkFitSeeds3.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)

process.detachedTripletStepTracks3 = process.detachedTripletStepTracks.clone()
process.detachedTripletStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedTripletStepTracks3.src = cms.InputTag("detachedTripletStepTrackCandidates"+layers)

process.highPtTripletStep3 = process.highPtTripletStep.clone()
process.highPtTripletStep3.src = cms.InputTag("highPtTripletStepTracks"+layers)
process.highPtTripletStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.highPtTripletStepClusters3 = process.highPtTripletStepClusters.clone()
process.highPtTripletStepClusters3.oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+layers)
process.highPtTripletStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters3.trackClassifier = cms.InputTag("lowPtQuadStep"+layers,"QualityMasks")
process.highPtTripletStepClusters3.trajectories = cms.InputTag("lowPtQuadStepTracks"+layers)

process.highPtTripletStepHitDoublets3 = process.highPtTripletStepHitDoublets.clone()
process.highPtTripletStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.highPtTripletStepHitDoublets3.seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+layers)

process.highPtTripletStepHitTriplets3 = process.highPtTripletStepHitTriplets.clone()
process.highPtTripletStepHitTriplets3.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.highPtTripletStepHitTriplets3.doublets = cms.InputTag("highPtTripletStepHitDoublets"+layers)
process.highPtTripletStepHitTriplets3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+layers+'__reRECO')

process.highPtTripletStepSeedLayers3 = process.highPtTripletStepSeedLayers.clone()
process.highPtTripletStepSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers3.BPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers3.FPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)

process.highPtTripletStepSeeds3 = process.highPtTripletStepSeeds.clone()
process.highPtTripletStepSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+layers+'__reRECO')
process.highPtTripletStepSeeds3.seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+layers)

process.highPtTripletStepTrackCandidates3 = process.highPtTripletStepTrackCandidates.clone()
process.highPtTripletStepTrackCandidates3.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_highPtTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidates3.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidates3.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidates3.mkFitSeeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidates3.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.highPtTripletStepTrackCandidates3.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)
process.highPtTripletStepTrackCandidates3.tracks = cms.InputTag("highPtTripletStepTrackCandidatesMkFit"+layers)

process.highPtTripletStepTrackCandidatesMkFit3 = process.highPtTripletStepTrackCandidatesMkFit.clone()
process.highPtTripletStepTrackCandidatesMkFit3.clustersToSkip = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepTrackCandidatesMkFit3.config = cms.ESInputTag("","highPtTripletStepTrackCandidatesMkFitConfig"+layers)
process.highPtTripletStepTrackCandidatesMkFit3.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit3.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidatesMkFit3.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit3.seeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidatesMkFit3.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.highPtTripletStepTrackCandidatesMkFitConfig3 = process.highPtTripletStepTrackCandidatesMkFitConfig.clone()
process.highPtTripletStepTrackCandidatesMkFitConfig3.ComponentName = cms.string('highPtTripletStepTrackCandidatesMkFitConfig'+layers)

process.highPtTripletStepTrackCandidatesMkFitSeeds3 = process.highPtTripletStepTrackCandidatesMkFitSeeds.clone()
process.highPtTripletStepTrackCandidatesMkFitSeeds3.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)

process.highPtTripletStepTracks3 = process.highPtTripletStepTracks.clone()
process.highPtTripletStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.highPtTripletStepTracks3.src = cms.InputTag("highPtTripletStepTrackCandidates"+layers)

process.firstStepPrimaryVertices3 = process.firstStepPrimaryVertices.clone()
process.firstStepPrimaryVertices3.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.firstStepPrimaryVertices3.particles = cms.InputTag("initialStepTrackRefsForJets"+layers)
process.firstStepPrimaryVertices3.vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.firstStepPrimaryVerticesUnsorted3 = process.firstStepPrimaryVerticesUnsorted.clone()
process.firstStepPrimaryVerticesUnsorted3.TrackLabel = cms.InputTag("initialStepTracks"+layers)

process.initialStep3 = process.initialStep.clone()
process.initialStep3.src = cms.InputTag("initialStepTracks"+layers)
process.initialStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepClassifier13 = process.initialStepClassifier1.clone()
process.initialStepClassifier13.src = cms.InputTag("initialStepTracks"+layers)
process.initialStepClassifier13.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepHitDoublets3 = process.initialStepHitDoublets.clone()
process.initialStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.initialStepHitDoublets3.seedingLayers = cms.InputTag("initialStepSeedLayers"+layers)

process.initialStepHitQuadruplets3 = process.initialStepHitQuadruplets.clone()
process.initialStepHitQuadruplets3.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepHitQuadruplets3.doublets = cms.InputTag("initialStepHitDoublets"+layers)
process.initialStepHitQuadruplets3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+layers+'__reRECO')

process.initialStepSeedLayers3 = process.initialStepSeedLayers.clone()
process.initialStepSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.initialStepSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)

process.initialStepSeeds3 = process.initialStepSeeds.clone()
process.initialStepSeeds3.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+layers+'__reRECO')
process.initialStepSeeds3.seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+layers)

process.initialStepTrackCandidates3 = process.initialStepTrackCandidates.clone()
process.initialStepTrackCandidates3.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidates3.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidates3.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidates3.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidates3.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidates3.seeds = cms.InputTag("initialStepSeeds"+layers)
process.initialStepTrackCandidates3.tracks = cms.InputTag("initialStepTrackCandidatesMkFit"+layers)

process.initialStepTrackCandidatesMkFit3 = process.initialStepTrackCandidatesMkFit.clone()
process.initialStepTrackCandidatesMkFit3.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfig"+layers)
process.initialStepTrackCandidatesMkFit3.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidatesMkFit3.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFit3.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidatesMkFit3.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidatesMkFit3.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitConfig3 = process.initialStepTrackCandidatesMkFitConfig.clone()
process.initialStepTrackCandidatesMkFitConfig3.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfig'+layers)

process.initialStepTrackCandidatesMkFitSeeds3 = process.initialStepTrackCandidatesMkFitSeeds.clone()
process.initialStepTrackCandidatesMkFitSeeds3.seeds = cms.InputTag("initialStepSeeds"+layers)

process.initialStepTrackRefsForJets3 = process.initialStepTrackRefsForJets.clone()
process.initialStepTrackRefsForJets3.src = cms.InputTag("initialStepTracks"+layers)

process.initialStepTracks3 = process.initialStepTracks.clone()
process.initialStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.initialStepTracks3.src = cms.InputTag("initialStepTrackCandidates"+layers)

process.mkFitEventOfHits3 = process.mkFitEventOfHits.clone()
process.mkFitEventOfHits3.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHits3.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.mkFitEventOfHits3.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiPixelHits3 = process.mkFitSiPixelHits.clone()
process.mkFitSiPixelHits3.hits = cms.InputTag("siPixelRecHits"+layers)

process.firstStepGoodPrimaryVertices3 = process.firstStepGoodPrimaryVertices.clone()
process.firstStepGoodPrimaryVertices3.src = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStep3 = process.jetCoreRegionalStep.clone()
process.jetCoreRegionalStep3.src = cms.InputTag("jetCoreRegionalStepTracks"+layers)
process.jetCoreRegionalStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStepHitDoublets3 = process.jetCoreRegionalStepHitDoublets.clone()
process.jetCoreRegionalStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.jetCoreRegionalStepHitDoublets3.seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"+layers)
process.jetCoreRegionalStepHitDoublets3.trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"+layers)

process.jetCoreRegionalStepSeedLayers3 = process.jetCoreRegionalStepSeedLayers.clone()
process.jetCoreRegionalStepSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers3.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")

process.jetCoreRegionalStepSeeds3 = process.jetCoreRegionalStepSeeds.clone()
process.jetCoreRegionalStepSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_jetCoreRegionalStepHitDoublets'+layers+'__reRECO')
process.jetCoreRegionalStepSeeds3.seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets"+layers)

process.jetCoreRegionalStepTrackCandidates3 = process.jetCoreRegionalStepTrackCandidates.clone()
process.jetCoreRegionalStepTrackCandidates3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackCandidates3.src = cms.InputTag("jetCoreRegionalStepSeeds"+layers)

process.jetCoreRegionalStepTrackingRegions3 = process.jetCoreRegionalStepTrackingRegions.clone()
process.jetCoreRegionalStepTrackingRegions3.RegionPSet.JetSrc = cms.InputTag("jetsForCoreTracking"+layers)
process.jetCoreRegionalStepTrackingRegions3.RegionPSet.measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackingRegions3.RegionPSet.vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices"+layers)

process.jetCoreRegionalStepTracks3 = process.jetCoreRegionalStepTracks.clone()
process.jetCoreRegionalStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTracks3.src = cms.InputTag("jetCoreRegionalStepTrackCandidates"+layers)

process.jetsForCoreTracking3 = process.jetsForCoreTracking.clone()
process.jetsForCoreTracking3.src = cms.InputTag("ak4CaloJetsForTrk"+layers)

process.lowPtQuadStep3 = process.lowPtQuadStep.clone()
process.lowPtQuadStep3.src = cms.InputTag("lowPtQuadStepTracks"+layers)
process.lowPtQuadStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtQuadStepClusters3 = process.lowPtQuadStepClusters.clone()
process.lowPtQuadStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters3.trackClassifier = cms.InputTag("initialStep"+layers,"QualityMasks")
process.lowPtQuadStepClusters3.trajectories = cms.InputTag("initialStepTracks"+layers)

process.lowPtQuadStepHitDoublets3 = process.lowPtQuadStepHitDoublets.clone()
process.lowPtQuadStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtQuadStepHitDoublets3.seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+layers)

process.lowPtQuadStepHitQuadruplets3 = process.lowPtQuadStepHitQuadruplets.clone()
process.lowPtQuadStepHitQuadruplets3.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtQuadStepHitQuadruplets3.doublets = cms.InputTag("lowPtQuadStepHitDoublets"+layers)
process.lowPtQuadStepHitQuadruplets3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+layers+'__reRECO')

process.lowPtQuadStepSeedLayers3 = process.lowPtQuadStepSeedLayers.clone()
process.lowPtQuadStepSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers3.BPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers3.FPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)

process.lowPtQuadStepSeeds3 = process.lowPtQuadStepSeeds.clone()
process.lowPtQuadStepSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+layers+'__reRECO')
process.lowPtQuadStepSeeds3.seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+layers)

process.lowPtQuadStepTrackCandidates3 = process.lowPtQuadStepTrackCandidates.clone()
process.lowPtQuadStepTrackCandidates3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTrackCandidates3.clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepTrackCandidates3.src = cms.InputTag("lowPtQuadStepSeeds"+layers)

process.lowPtQuadStepTracks3 = process.lowPtQuadStepTracks.clone()
process.lowPtQuadStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTracks3.src = cms.InputTag("lowPtQuadStepTrackCandidates"+layers)

process.lowPtTripletStep3 = process.lowPtTripletStep.clone()
process.lowPtTripletStep3.src = cms.InputTag("lowPtTripletStepTracks"+layers)
process.lowPtTripletStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtTripletStepClusters3 = process.lowPtTripletStepClusters.clone()
process.lowPtTripletStepClusters3.oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+layers)
process.lowPtTripletStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters3.trackClassifier = cms.InputTag("highPtTripletStep"+layers,"QualityMasks")
process.lowPtTripletStepClusters3.trajectories = cms.InputTag("highPtTripletStepTracks"+layers)

process.lowPtTripletStepHitDoublets3 = process.lowPtTripletStepHitDoublets.clone()
process.lowPtTripletStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtTripletStepHitDoublets3.seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+layers)

process.lowPtTripletStepHitTriplets3 = process.lowPtTripletStepHitTriplets.clone()
process.lowPtTripletStepHitTriplets3.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtTripletStepHitTriplets3.doublets = cms.InputTag("lowPtTripletStepHitDoublets"+layers)
process.lowPtTripletStepHitTriplets3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+layers+'__reRECO')

process.lowPtTripletStepSeedLayers3 = process.lowPtTripletStepSeedLayers.clone()
process.lowPtTripletStepSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers3.BPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers3.FPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)

process.lowPtTripletStepSeeds3 = process.lowPtTripletStepSeeds.clone()
process.lowPtTripletStepSeeds3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+layers+'__reRECO')
process.lowPtTripletStepSeeds3.seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+layers)

process.lowPtTripletStepTrackCandidates3 = process.lowPtTripletStepTrackCandidates.clone()
process.lowPtTripletStepTrackCandidates3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTrackCandidates3.clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepTrackCandidates3.src = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.lowPtTripletStepTracks3 = process.lowPtTripletStepTracks.clone()
process.lowPtTripletStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTracks3.src = cms.InputTag("lowPtTripletStepTrackCandidates"+layers)

process.chargeCut2069Clusters3 = process.chargeCut2069Clusters.clone()
process.chargeCut2069Clusters3.oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+layers)
process.chargeCut2069Clusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.chargeCut2069Clusters3.stripClusters = cms.InputTag("rCluster"+layers)

process.mixedTripletStep3 = process.mixedTripletStep.clone()
process.mixedTripletStep3.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier13 = process.mixedTripletStepClassifier1.clone()
process.mixedTripletStepClassifier13.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier13.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier23 = process.mixedTripletStepClassifier2.clone()
process.mixedTripletStepClassifier23.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier23.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClusters3 = process.mixedTripletStepClusters.clone()
process.mixedTripletStepClusters3.oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+layers)
process.mixedTripletStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters3.trackClassifier = cms.InputTag("pixelPairStep"+layers,"QualityMasks")
process.mixedTripletStepClusters3.trajectories = cms.InputTag("pixelPairStepTracks"+layers)

process.mixedTripletStepHitDoubletsA3 = process.mixedTripletStepHitDoubletsA.clone()
process.mixedTripletStepHitDoubletsA3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsA3.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+layers)

process.mixedTripletStepHitDoubletsB3 = process.mixedTripletStepHitDoubletsB.clone()
process.mixedTripletStepHitDoubletsB3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsB3.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+layers)

process.mixedTripletStepHitTripletsA3 = process.mixedTripletStepHitTripletsA.clone()
process.mixedTripletStepHitTripletsA3.doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+layers)
process.mixedTripletStepHitTripletsA3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO')

process.mixedTripletStepHitTripletsB3 = process.mixedTripletStepHitTripletsB.clone()
process.mixedTripletStepHitTripletsB3.doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+layers)
process.mixedTripletStepHitTripletsB3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO')

process.mixedTripletStepSeedLayersA3 = process.mixedTripletStepSeedLayersA.clone()
process.mixedTripletStepSeedLayersA3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA3.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA3.FPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA3.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersA3.TEC.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeedLayersB3 = process.mixedTripletStepSeedLayersB.clone()
process.mixedTripletStepSeedLayersB3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersB3.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersB3.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersB3.TIB.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeeds3 = process.mixedTripletStepSeeds.clone()
process.mixedTripletStepSeeds3.seedCollections = cms.VInputTag("mixedTripletStepSeedsA"+layers, "mixedTripletStepSeedsB"+layers)

process.mixedTripletStepSeedsA3 = process.mixedTripletStepSeedsA.clone()
process.mixedTripletStepSeedsA3.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsA3.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsA3.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+layers)

process.mixedTripletStepSeedsB3 = process.mixedTripletStepSeedsB.clone()
process.mixedTripletStepSeedsB3.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsB3.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsB3.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+layers)

process.mixedTripletStepTrackCandidates3 = process.mixedTripletStepTrackCandidates.clone()
process.mixedTripletStepTrackCandidates3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTrackCandidates3.clustersToSkip = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepTrackCandidates3.src = cms.InputTag("mixedTripletStepSeeds"+layers)

process.mixedTripletStepTracks3 = process.mixedTripletStepTracks.clone()
process.mixedTripletStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTracks3.src = cms.InputTag("mixedTripletStepTrackCandidates"+layers)

process.pixelLessStep3 = process.pixelLessStep.clone()
process.pixelLessStep3.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier13 = process.pixelLessStepClassifier1.clone()
process.pixelLessStepClassifier13.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier13.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier23 = process.pixelLessStepClassifier2.clone()
process.pixelLessStepClassifier23.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier23.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClusters3 = process.pixelLessStepClusters.clone()
process.pixelLessStepClusters3.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+layers)
process.pixelLessStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters3.trackClassifier = cms.InputTag("mixedTripletStep"+layers,"QualityMasks")
process.pixelLessStepClusters3.trajectories = cms.InputTag("mixedTripletStepTracks"+layers)

process.pixelLessStepHitDoublets3 = process.pixelLessStepHitDoublets.clone()
process.pixelLessStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelLessStepHitDoublets3.seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+layers)

process.pixelLessStepHitTriplets3 = process.pixelLessStepHitTriplets.clone()
process.pixelLessStepHitTriplets3.doublets = cms.InputTag("pixelLessStepHitDoublets"+layers)
process.pixelLessStepHitTriplets3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+layers+'__reRECO')

process.pixelLessStepSeedLayers3 = process.pixelLessStepSeedLayers.clone()
process.pixelLessStepSeedLayers3.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers3.MTEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers3.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers3.MTIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers3.MTID.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers3.MTID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers3.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers3.TEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers3.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers3.TIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers3.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers3.TID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.pixelLessStepSeeds3 = process.pixelLessStepSeeds.clone()
process.pixelLessStepSeeds3.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.pixelLessStepSeeds3.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+layers+'__reRECO'
    )
process.pixelLessStepSeeds3.seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+layers)

process.pixelLessStepTrackCandidates3 = process.pixelLessStepTrackCandidates.clone()
process.pixelLessStepTrackCandidates3.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitOutputWrapper_pixelLessStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidates3.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidates3.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidates3.mkFitSeeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidates3.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.pixelLessStepTrackCandidates3.seeds = cms.InputTag("pixelLessStepSeeds"+layers)
process.pixelLessStepTrackCandidates3.tracks = cms.InputTag("pixelLessStepTrackCandidatesMkFit"+layers)

process.pixelLessStepTrackCandidatesMkFit3 = process.pixelLessStepTrackCandidatesMkFit.clone()
process.pixelLessStepTrackCandidatesMkFit3.clustersToSkip = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepTrackCandidatesMkFit3.config = cms.ESInputTag("","pixelLessStepTrackCandidatesMkFitConfig"+layers)
process.pixelLessStepTrackCandidatesMkFit3.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidatesMkFit3.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidatesMkFit3.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidatesMkFit3.seeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidatesMkFit3.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.pixelLessStepTrackCandidatesMkFitSeeds3 = process.pixelLessStepTrackCandidatesMkFitSeeds.clone()
process.pixelLessStepTrackCandidatesMkFitSeeds3.seeds = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelLessStepTrackCandidatesMkFitConfig3 = process.pixelLessStepTrackCandidatesMkFitConfig.clone()
process.pixelLessStepTrackCandidatesMkFitConfig3.ComponentName = cms.string('pixelLessStepTrackCandidatesMkFitConfig'+layers)

process.pixelLessStepTracks3 = process.pixelLessStepTracks.clone()
process.pixelLessStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelLessStepTracks3.src = cms.InputTag("pixelLessStepTrackCandidates"+layers)

process.pixelPairStep3 = process.pixelPairStep.clone()
process.pixelPairStep3.src = cms.InputTag("pixelPairStepTracks"+layers)
process.pixelPairStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepClusters3 = process.pixelPairStepClusters.clone()
process.pixelPairStepClusters3.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+layers)
process.pixelPairStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters3.trackClassifier = cms.InputTag("detachedTripletStep"+layers,"QualityMasks")
process.pixelPairStepClusters3.trajectories = cms.InputTag("detachedTripletStepTracks"+layers)

process.pixelPairStepHitDoublets3 = process.pixelPairStepHitDoublets.clone()
process.pixelPairStepHitDoublets3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoublets3.seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+layers)
process.pixelPairStepHitDoublets3.trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+layers)

process.pixelPairStepHitDoubletsB3 = process.pixelPairStepHitDoubletsB.clone()
process.pixelPairStepHitDoubletsB3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoubletsB3.trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+layers)

process.pixelPairStepSeedLayers3 = process.pixelPairStepSeedLayers.clone()
process.pixelPairStepSeedLayers3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers3.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepSeedLayers3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers3.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)

process.pixelPairStepSeeds3 = process.pixelPairStepSeeds.clone()
process.pixelPairStepSeeds3.seedCollections = cms.VInputTag("pixelPairStepSeedsA"+layers, "pixelPairStepSeedsB"+layers)

process.pixelPairStepSeedsA3 = process.pixelPairStepSeedsA.clone()
process.pixelPairStepSeedsA3.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsA3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+layers+'__reRECO')
process.pixelPairStepSeedsA3.seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+layers)

process.pixelPairStepSeedsB3 = process.pixelPairStepSeedsB.clone()
process.pixelPairStepSeedsB3.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsB3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+layers+'__reRECO')
process.pixelPairStepSeedsB3.seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+layers)

process.pixelPairStepTrackCandidates3 = process.pixelPairStepTrackCandidates.clone()
process.pixelPairStepTrackCandidates3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTrackCandidates3.clustersToSkip = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackCandidates3.src = cms.InputTag("pixelPairStepSeeds"+layers)

process.pixelPairStepTrackingRegions3 = process.pixelPairStepTrackingRegions.clone()
process.pixelPairStepTrackingRegions3.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairStepTrackingRegions3.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.pixelPairStepTrackingRegionsSeedLayersB3 = process.pixelPairStepTrackingRegionsSeedLayersB.clone()
process.pixelPairStepTrackingRegionsSeedLayersB3.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB3.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB3.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB3.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB3.RegionPSet.vertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepTracks3 = process.pixelPairStepTracks.clone()
process.pixelPairStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTracks3.src = cms.InputTag("pixelPairStepTrackCandidates"+layers)

process.tobTecStep3 = process.tobTecStep.clone()
process.tobTecStep3.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStep3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier13 = process.tobTecStepClassifier1.clone()
process.tobTecStepClassifier13.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier13.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier23 = process.tobTecStepClassifier2.clone()
process.tobTecStepClassifier23.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier23.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClusters3 = process.tobTecStepClusters.clone()
process.tobTecStepClusters3.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.tobTecStepClusters3.pixelClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters3.stripClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters3.trackClassifier = cms.InputTag("pixelLessStep"+layers,"QualityMasks")
process.tobTecStepClusters3.trajectories = cms.InputTag("pixelLessStepTracks"+layers)

process.tobTecStepHitDoubletsPair3 = process.tobTecStepHitDoubletsPair.clone()
process.tobTecStepHitDoubletsPair3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsPair3.seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+layers)

process.tobTecStepHitDoubletsTripl3 = process.tobTecStepHitDoubletsTripl.clone()
process.tobTecStepHitDoubletsTripl3.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsTripl3.seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+layers)

process.tobTecStepHitTripletsTripl3 = process.tobTecStepHitTripletsTripl.clone()
process.tobTecStepHitTripletsTripl3.doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+layers)
process.tobTecStepHitTripletsTripl3.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+layers+'__reRECO')

process.tobTecStepSeedLayersPair3 = process.tobTecStepSeedLayersPair.clone()
process.tobTecStepSeedLayersPair3.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair3.TEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersPair3.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair3.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeedLayersTripl3 = process.tobTecStepSeedLayersTripl.clone()
process.tobTecStepSeedLayersTripl3.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl3.MTEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl3.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl3.MTOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl3.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersTripl3.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeeds3 = process.tobTecStepSeeds.clone()
process.tobTecStepSeeds3.seedCollections = cms.VInputTag("tobTecStepSeedsTripl"+layers, "tobTecStepSeedsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsPair3 = process.tobTecStepSeedsPair.clone()
process.tobTecStepSeedsPair3.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsPair3.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+layers+'__reRECO')
process.tobTecStepSeedsPair3.seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsTripl3 = process.tobTecStepSeedsTripl.clone()
process.tobTecStepSeedsTripl3.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsTripl3.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+layers+'__reRECO'
    )
process.tobTecStepSeedsTripl3.seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+layers)

process.tobTecStepTrackCandidates3 = process.tobTecStepTrackCandidates.clone()
process.tobTecStepTrackCandidates3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTrackCandidates3.clustersToSkip = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepTrackCandidates3.src = cms.InputTag("tobTecStepSeeds"+layers)

process.tobTecStepTracks3 = process.tobTecStepTracks.clone()
process.tobTecStepTracks3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTracks3.src = cms.InputTag("tobTecStepTrackCandidates"+layers)

process.muonSeededTracksOutInClassifier3 = process.muonSeededTracksOutInClassifier.clone()
process.muonSeededTracksOutInClassifier3.src = cms.InputTag("muonSeededTracksOutIn"+layers)
process.muonSeededTracksOutInClassifier3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.muonSeededSeedsInOut3 = process.muonSeededSeedsInOut.clone()
process.muonSeededSeedsInOut3.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesInOut3 = process.muonSeededTrackCandidatesInOut.clone()
process.muonSeededTrackCandidatesInOut3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesInOut3.src = cms.InputTag("muonSeededSeedsInOut"+layers)

process.muonSeededTracksInOut3 = process.muonSeededTracksInOut.clone()
process.muonSeededTracksInOut3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksInOut3.src = cms.InputTag("muonSeededTrackCandidatesInOut"+layers)

process.muonSeededSeedsOutIn3 = process.muonSeededSeedsOutIn.clone()
process.muonSeededSeedsOutIn3.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesOutIn3 = process.muonSeededTrackCandidatesOutIn.clone()
process.muonSeededTrackCandidatesOutIn3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesOutIn3.src = cms.InputTag("muonSeededSeedsOutIn"+layers)

process.muonSeededTracksOutIn3 = process.muonSeededTracksOutIn.clone()
process.muonSeededTracksOutIn3.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksOutIn3.src = cms.InputTag("muonSeededTrackCandidatesOutIn"+layers)

process.muonSeededTracksInOutClassifier3 = process.muonSeededTracksInOutClassifier.clone()
process.muonSeededTracksInOutClassifier3.src = cms.InputTag("muonSeededTracksInOut"+layers)
process.muonSeededTracksInOutClassifier3.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.clusterSummaryProducer3 = process.clusterSummaryProducer.clone()
process.clusterSummaryProducer3.stripClusters = cms.InputTag("rCluster"+layers)

process.siStripMatchedRecHits3 = process.siStripMatchedRecHits.clone()
process.siStripMatchedRecHits3.ClusterProducer = cms.InputTag("rCluster"+layers)

process.reconstruction_trackingOnly_3layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.trackExtrapolator,process.trackExtrapolator3)
process.reconstruction_trackingOnly_3layers.replace(process.generalV0Candidates,process.generalV0Candidates3)
process.reconstruction_trackingOnly_3layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices3)
process.reconstruction_trackingOnly_3layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS3)
process.reconstruction_trackingOnly_3layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting3)
process.reconstruction_trackingOnly_3layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting3)
process.reconstruction_trackingOnly_3layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices3)
process.reconstruction_trackingOnly_3layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk3)
process.reconstruction_trackingOnly_3layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices3)
process.reconstruction_trackingOnly_3layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder3)
process.reconstruction_trackingOnly_3layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator3)
process.reconstruction_trackingOnly_3layers.replace(process.vertexMerger,process.vertexMerger3)
process.reconstruction_trackingOnly_3layers.replace(process.dedxHarmonic2,process.dedxHarmonic23)
process.reconstruction_trackingOnly_3layers.replace(process.dedxHitInfo,process.dedxHitInfo3)
process.reconstruction_trackingOnly_3layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0853)
process.reconstruction_trackingOnly_3layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic23)
process.reconstruction_trackingOnly_3layers.replace(process.dedxTruncated40,process.dedxTruncated403)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask3)
process.reconstruction_trackingOnly_3layers.replace(process.newCombinedSeeds,process.newCombinedSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions3)
process.reconstruction_trackingOnly_3layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask3)
process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets3)
process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.conversionStepTracks,process.conversionStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.trackerClusterCheck,process.trackerClusterCheck3)
process.reconstruction_trackingOnly_3layers.replace(process.convClusters,process.convClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.convLayerPairs,process.convLayerPairs3)
process.reconstruction_trackingOnly_3layers.replace(process.convStepSelector,process.convStepSelector3)
process.reconstruction_trackingOnly_3layers.replace(process.convStepTracks,process.convStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.convTrackCandidates,process.convTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg3)
process.reconstruction_trackingOnly_3layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent3)
process.reconstruction_trackingOnly_3layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits3)
process.reconstruction_trackingOnly_3layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache3)
process.reconstruction_trackingOnly_3layers.replace(process.siPixelClusters,process.siPixelClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.siPixelRecHits,process.siPixelRecHits3)
process.reconstruction_trackingOnly_3layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting3)
process.reconstruction_trackingOnly_3layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier3)
process.reconstruction_trackingOnly_3layers.replace(process.generalTracks,process.generalTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.earlyMuons,process.earlyMuons3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStep,process.detachedQuadStep3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStep,process.detachedTripletStep3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier13)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier23)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStep,process.highPtTripletStep3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices3)
process.reconstruction_trackingOnly_3layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStep,process.initialStep3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepClassifier1,process.initialStepClassifier13)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeeds,process.initialStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets3)
process.reconstruction_trackingOnly_3layers.replace(process.initialStepTracks,process.initialStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits3)
process.reconstruction_trackingOnly_3layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits3)
process.reconstruction_trackingOnly_3layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices3)
process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep3)
process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions3)
process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStep,process.lowPtQuadStep3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStep,process.lowPtTripletStep3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStep,process.mixedTripletStep3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier13)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier23)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStep,process.pixelLessStep3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier13)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier23)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTrackCandidatesMkFitConfig,process.pixelLessStepTrackCandidatesMkFitConfig3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStep,process.pixelPairStep3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB3)
process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStep,process.tobTecStep3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier13)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier23)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepClusters,process.tobTecStepClusters3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates3)
process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepTracks,process.tobTecStepTracks3)
process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier3)
process.reconstruction_trackingOnly_3layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut3)
process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut3)
process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut3)
process.reconstruction_trackingOnly_3layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn3)
process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn3)
process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn3)
process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier3)
process.reconstruction_trackingOnly_3layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer3)
process.reconstruction_trackingOnly_3layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits3)

####################################################################################################

layers = "4"

process.MeasurementTrackerEventPreSplitting4 = process.MeasurementTrackerEventPreSplitting.clone()
process.MeasurementTrackerEventPreSplitting4.stripClusterProducer = cms.string('rCluster'+layers)

process.trackExtrapolator4 = process.trackExtrapolator.clone()
process.trackExtrapolator4.trackSrc = cms.InputTag("generalTracks"+layers)

process.generalV0Candidates4 = process.generalV0Candidates.clone()
process.generalV0Candidates4.trackRecoAlgorithm = cms.InputTag("generalTracks"+layers)
process.generalV0Candidates4.vertices = cms.InputTag("offlinePrimaryVertices"+layers)

process.offlinePrimaryVertices4 = process.offlinePrimaryVertices.clone()
process.offlinePrimaryVertices4.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVertices4.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVertices4.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.offlinePrimaryVerticesWithBS4 = process.offlinePrimaryVerticesWithBS.clone()
process.offlinePrimaryVerticesWithBS4.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVerticesWithBS4.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVerticesWithBS4.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers,"WithBS")

process.trackRefsForJetsBeforeSorting4 = process.trackRefsForJetsBeforeSorting.clone()
process.trackRefsForJetsBeforeSorting4.src = cms.InputTag("trackWithVertexRefSelectorBeforeSorting"+layers)

process.trackWithVertexRefSelectorBeforeSorting4 = process.trackWithVertexRefSelectorBeforeSorting.clone()
process.trackWithVertexRefSelectorBeforeSorting4.src = cms.InputTag("generalTracks"+layers)
process.trackWithVertexRefSelectorBeforeSorting4.vertexTag = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.unsortedOfflinePrimaryVertices4 = process.unsortedOfflinePrimaryVertices.clone()
process.unsortedOfflinePrimaryVertices4.TrackLabel = cms.InputTag("generalTracks"+layers)

process.ak4CaloJetsForTrk4 = process.ak4CaloJetsForTrk.clone()
process.ak4CaloJetsForTrk4.srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.inclusiveSecondaryVertices4 = process.inclusiveSecondaryVertices.clone()
process.inclusiveSecondaryVertices4.secondaryVertices = cms.InputTag("trackVertexArbitrator"+layers)

process.inclusiveVertexFinder4 = process.inclusiveVertexFinder.clone() 
process.inclusiveVertexFinder4.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.inclusiveVertexFinder4.tracks = cms.InputTag("generalTracks"+layers)

process.trackVertexArbitrator4 = process.trackVertexArbitrator.clone() 
process.trackVertexArbitrator4.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.trackVertexArbitrator4.secondaryVertices = cms.InputTag("vertexMerger"+layers)
process.trackVertexArbitrator4.tracks = cms.InputTag("generalTracks"+layers)

process.vertexMerger4 = process.vertexMerger.clone()
process.vertexMerger4.secondaryVertices = cms.InputTag("inclusiveVertexFinder"+layers)

process.dedxHarmonic24 = process.dedxHarmonic2.clone()
process.dedxHarmonic24.tracks = cms.InputTag("generalTracks"+layers)

process.dedxHitInfo4 = process.dedxHitInfo.clone() 
process.dedxHitInfo4.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelAndStripHarmonic2T0854 = process.dedxPixelAndStripHarmonic2T085.clone() 
process.dedxPixelAndStripHarmonic2T0854.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelHarmonic24 = process.dedxPixelHarmonic2.clone() 
process.dedxPixelHarmonic24.tracks = cms.InputTag("generalTracks"+layers)

process.dedxTruncated404 = process.dedxTruncated40.clone()
process.dedxTruncated404.tracks = cms.InputTag("generalTracks"+layers)

process.detachedTripletStepSeedClusterMask4 = process.detachedTripletStepSeedClusterMask.clone() 
process.detachedTripletStepSeedClusterMask4.oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+layers)
process.detachedTripletStepSeedClusterMask4.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask4.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask4.trajectories = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.initialStepSeedClusterMask4 = process.initialStepSeedClusterMask.clone() 
process.initialStepSeedClusterMask4.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.initialStepSeedClusterMask4.pixelClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask4.stripClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask4.trajectories = cms.InputTag("initialStepSeeds"+layers)

process.mixedTripletStepSeedClusterMask4 = process.mixedTripletStepSeedClusterMask.clone() 
process.mixedTripletStepSeedClusterMask4.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+layers)
process.mixedTripletStepSeedClusterMask4.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask4.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask4.trajectories = cms.InputTag("mixedTripletStepSeeds"+layers)

process.newCombinedSeeds4 = process.newCombinedSeeds.clone()
process.newCombinedSeeds4.seedCollections = cms.VInputTag(
        "initialStepSeeds"+layers, "highPtTripletStepSeeds"+layers, "mixedTripletStepSeeds"+layers, "pixelLessStepSeeds"+layers, "tripletElectronSeeds"+layers,
        "pixelPairElectronSeeds"+layers, "stripPairElectronSeeds"+layers, "lowPtTripletStepSeeds"+layers, "lowPtQuadStepSeeds"+layers, "detachedTripletStepSeeds"+layers,
        "detachedQuadStepSeeds"+layers, "pixelPairStepSeeds"+layers
    )

process.pixelLessStepSeedClusterMask4 = process.pixelLessStepSeedClusterMask.clone() 
process.pixelLessStepSeedClusterMask4.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+layers)
process.pixelLessStepSeedClusterMask4.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask4.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask4.trajectories = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelPairElectronHitDoublets4 = process.pixelPairElectronHitDoublets.clone() 
process.pixelPairElectronHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairElectronHitDoublets4.seedingLayers = cms.InputTag("pixelPairElectronSeedLayers"+layers)
process.pixelPairElectronHitDoublets4.trackingRegions = cms.InputTag("pixelPairElectronTrackingRegions"+layers)

process.pixelPairElectronSeedLayers4 = process.pixelPairElectronSeedLayers.clone()
process.pixelPairElectronSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers4.BPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.pixelPairElectronSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers4.FPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.pixelPairElectronSeeds4 = process.pixelPairElectronSeeds.clone()
process.pixelPairElectronSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairElectronHitDoublets'+layers+'__reRECO')
process.pixelPairElectronSeeds4.seedingHitSets = cms.InputTag("pixelPairElectronHitDoublets"+layers)

process.pixelPairElectronTrackingRegions4 = process.pixelPairElectronTrackingRegions.clone() 
process.pixelPairElectronTrackingRegions4.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairElectronTrackingRegions4.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.stripPairElectronHitDoublets4 = process.stripPairElectronHitDoublets.clone() 
process.stripPairElectronHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.stripPairElectronHitDoublets4.seedingLayers = cms.InputTag("stripPairElectronSeedLayers"+layers)

process.stripPairElectronSeedLayers4 = process.stripPairElectronSeedLayers.clone() 
process.stripPairElectronSeedLayers4.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers4.TEC.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers4.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers4.TIB.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers4.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers4.TID.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.stripPairElectronSeeds4 = process.stripPairElectronSeeds.clone() 
process.stripPairElectronSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_stripPairElectronHitDoublets'+layers+'__reRECO')
process.stripPairElectronSeeds4.seedingHitSets = cms.InputTag("stripPairElectronHitDoublets"+layers)

process.tripletElectronClusterMask4 = process.tripletElectronClusterMask.clone()
process.tripletElectronClusterMask4.oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronClusterMask4.pixelClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask4.stripClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask4.trajectories = cms.InputTag("tripletElectronSeeds"+layers)

process.tripletElectronHitDoublets4 = process.tripletElectronHitDoublets.clone() 
process.tripletElectronHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tripletElectronHitDoublets4.seedingLayers = cms.InputTag("tripletElectronSeedLayers"+layers)

process.tripletElectronHitTriplets4 = process.tripletElectronHitTriplets.clone()
process.tripletElectronHitTriplets4.doublets = cms.InputTag("tripletElectronHitDoublets"+layers)
process.tripletElectronHitTriplets4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO')

process.tripletElectronSeedLayers4 = process.tripletElectronSeedLayers.clone()
process.tripletElectronSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers4.BPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers4.FPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)

process.tripletElectronSeeds4 = process.tripletElectronSeeds.clone()
process.tripletElectronSeeds4.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tripletElectronHitTriplets'+layers+'__reRECO',
        'IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO'
    )
process.tripletElectronSeeds4.seedingHitSets = cms.InputTag("tripletElectronHitTriplets"+layers)

process.conversionStepTracks4 = process.conversionStepTracks.clone()
process.conversionStepTracks4.TrackProducers = cms.VInputTag("convStepTracks"+layers)
process.conversionStepTracks4.selectedTrackQuals = cms.VInputTag("convStepSelector"+layers+":convStep"+layers)

process.earlyGeneralTracks4 = process.earlyGeneralTracks.clone()
process.earlyGeneralTracks4.inputClassifiers = cms.vstring(
        'initialStep'+layers,
        'highPtTripletStep'+layers,
        'jetCoreRegionalStep'+layers,
        'lowPtQuadStep'+layers,
        'lowPtTripletStep'+layers,
        'detachedQuadStep'+layers,
        'detachedTripletStep'+layers,
        'pixelPairStep'+layers,
        'mixedTripletStep'+layers,
        'pixelLessStep'+layers,
        'tobTecStep'+layers
    )
process.earlyGeneralTracks4.trackProducers = cms.VInputTag(
        "initialStepTracks"+layers, "highPtTripletStepTracks"+layers, "jetCoreRegionalStepTracks"+layers, "lowPtQuadStepTracks"+layers, "lowPtTripletStepTracks"+layers,
        "detachedQuadStepTracks"+layers, "detachedTripletStepTracks"+layers, "pixelPairStepTracks"+layers, "mixedTripletStepTracks"+layers, "pixelLessStepTracks"+layers,
        "tobTecStepTracks"+layers
    )

process.preDuplicateMergingGeneralTracks4 = process.preDuplicateMergingGeneralTracks.clone()
process.preDuplicateMergingGeneralTracks4.inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+layers,
        'muonSeededTracksInOutClassifier'+layers,
        'muonSeededTracksOutInClassifier'+layers
    )
process.preDuplicateMergingGeneralTracks4.trackProducers = cms.VInputTag("earlyGeneralTracks"+layers, "muonSeededTracksInOut"+layers, "muonSeededTracksOutIn"+layers)

process.trackerClusterCheck4 = process.trackerClusterCheck.clone()
process.trackerClusterCheck4.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.trackerClusterCheck4.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.convClusters4 = process.convClusters.clone()
process.convClusters4.oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"+layers)
process.convClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.convClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.convClusters4.trackClassifier = cms.InputTag("tobTecStep"+layers,"QualityMasks")
process.convClusters4.trajectories = cms.InputTag("tobTecStepTracks"+layers)

process.convLayerPairs4 = process.convLayerPairs.clone()
process.convLayerPairs4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs4.BPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs4.FPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs4.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs4.MTIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs4.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs4.MTOB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs4.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs4.TEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHitUnmatched")
process.convLayerPairs4.TEC.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs4.TEC.stereoRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHitUnmatched")
process.convLayerPairs4.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs4.TIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs4.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs4.TID.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs4.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs4.TOB.skipClusters = cms.InputTag("convClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.convStepSelector4 = process.convStepSelector.clone()
process.convStepSelector4.src = cms.InputTag("convStepTracks"+layers)
#process.convStepSelector4.trackSelectors.name = cms.string('convStep'+layers)
process.convStepSelector4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.convStepTracks4 = process.convStepTracks.clone()
process.convStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convStepTracks4.src = cms.InputTag("convTrackCandidates"+layers)

process.convTrackCandidates4 = process.convTrackCandidates.clone()
process.convTrackCandidates4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convTrackCandidates4.clustersToSkip = cms.InputTag("convClusters"+layers)
process.convTrackCandidates4.src = cms.InputTag("photonConvTrajSeedFromSingleLeg"+layers,"convSeedCandidates")

process.photonConvTrajSeedFromSingleLeg4 = process.photonConvTrajSeedFromSingleLeg.clone()
process.photonConvTrajSeedFromSingleLeg4.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg4.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg4.OrderedHitsFactoryPSet.SeedingLayers = cms.InputTag("convLayerPairs"+layers)
process.photonConvTrajSeedFromSingleLeg4.TrackRefitter = cms.InputTag("generalTracks"+layers)
process.photonConvTrajSeedFromSingleLeg4.primaryVerticesTag = cms.InputTag("firstStepPrimaryVertices"+layers)

process.MeasurementTrackerEvent4 = process.MeasurementTrackerEvent.clone()
process.MeasurementTrackerEvent4.pixelClusterProducer = cms.string('rCluster'+layers)
process.MeasurementTrackerEvent4.stripClusterProducer = cms.string('rCluster'+layers)

process.ak4CaloJetsForTrkPreSplitting4 = process.ak4CaloJetsForTrkPreSplitting.clone()
process.ak4CaloJetsForTrkPreSplitting4.srcPVs = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.firstStepPrimaryVerticesPreSplitting4 = process.firstStepPrimaryVerticesPreSplitting.clone()
process.firstStepPrimaryVerticesPreSplitting4.TrackLabel = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepHitDoubletsPreSplitting4 = process.initialStepHitDoubletsPreSplitting.clone()
process.initialStepHitDoubletsPreSplitting4.clusterCheck = cms.InputTag("trackerClusterCheckPreSplitting"+layers)

process.initialStepHitQuadrupletsPreSplitting4 = process.initialStepHitQuadrupletsPreSplitting.clone()
process.initialStepHitQuadrupletsPreSplitting4.doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"+layers)
process.initialStepHitQuadrupletsPreSplitting4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoubletsPreSplitting'+layers+'__reRECO')

process.initialStepSeedsPreSplitting4 = process.initialStepSeedsPreSplitting.clone()
process.initialStepSeedsPreSplitting4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadrupletsPreSplitting'+layers+'__reRECO')
process.initialStepSeedsPreSplitting4.seedingHitSets = cms.InputTag("initialStepHitQuadrupletsPreSplitting"+layers)

process.initialStepTrackCandidatesMkFitConfigPreSplitting4 = process.initialStepTrackCandidatesMkFitConfigPreSplitting.clone()
process.initialStepTrackCandidatesMkFitConfigPreSplitting4.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfigPreSplitting'+layers)

process.initialStepTrackCandidatesMkFitPreSplitting4 = process.initialStepTrackCandidatesMkFitPreSplitting.clone()
process.initialStepTrackCandidatesMkFitPreSplitting4.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfigPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting4.eventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting4.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFitPreSplitting4.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting4.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitSeedsPreSplitting4 = process.initialStepTrackCandidatesMkFitSeedsPreSplitting.clone()
process.initialStepTrackCandidatesMkFitSeedsPreSplitting4.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)

process.initialStepTrackCandidatesPreSplitting4 = process.initialStepTrackCandidatesPreSplitting.clone()
process.initialStepTrackCandidatesPreSplitting4.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFitPreSplitting'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesPreSplitting4.mkFitEventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting4.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting4.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidatesPreSplitting4.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting4.tracks = cms.InputTag("initialStepTrackCandidatesMkFitPreSplitting"+layers)

process.initialStepTrackRefsForJetsPreSplitting4 = process.initialStepTrackRefsForJetsPreSplitting.clone()
process.initialStepTrackRefsForJetsPreSplitting4.src = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepTracksPreSplitting4 = process.initialStepTracksPreSplitting.clone()
process.initialStepTracksPreSplitting4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"+layers)
process.initialStepTracksPreSplitting4.src = cms.InputTag("initialStepTrackCandidatesPreSplitting"+layers)

process.jetsForCoreTrackingPreSplitting4 = process.jetsForCoreTrackingPreSplitting.clone()
process.jetsForCoreTrackingPreSplitting4.src = cms.InputTag("ak4CaloJetsForTrkPreSplitting"+layers)

process.mkFitEventOfHitsPreSplitting4 = process.mkFitEventOfHitsPreSplitting.clone()
process.mkFitEventOfHitsPreSplitting4.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHitsPreSplitting4.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiStripHits4 = process.mkFitSiStripHits.clone()
process.mkFitSiStripHits4.rphiHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.mkFitSiStripHits4.stereoHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHit")

process.siPixelClusterShapeCache4 = process.siPixelClusterShapeCache.clone()
process.siPixelClusterShapeCache4.src = cms.InputTag("rCluster"+layers)

process.siPixelClusters4 = process.siPixelClusters.clone()
process.siPixelClusters4.cores = cms.InputTag("jetsForCoreTrackingPreSplitting"+layers)
process.siPixelClusters4.vertices = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.siPixelRecHits4 = process.siPixelRecHits.clone()
process.siPixelRecHits4.src = cms.InputTag("rCluster"+layers)

process.trackerClusterCheckPreSplitting4 = process.trackerClusterCheckPreSplitting.clone()
process.trackerClusterCheckPreSplitting4.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.duplicateTrackCandidates4 = process.duplicateTrackCandidates.clone()
process.duplicateTrackCandidates4.source = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.duplicateTrackClassifier4 = process.duplicateTrackClassifier.clone()
process.duplicateTrackClassifier4.src = cms.InputTag("mergedDuplicateTracks"+layers)
process.duplicateTrackClassifier4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.generalTracks4 = process.generalTracks.clone()
process.generalTracks4.candidateComponents = cms.InputTag("duplicateTrackCandidates"+layers,"candidateMap")
process.generalTracks4.candidateSource = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")
process.generalTracks4.mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+layers,"MVAValues")
process.generalTracks4.mergedSource = cms.InputTag("mergedDuplicateTracks"+layers)
process.generalTracks4.originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+layers,"MVAValues")
process.generalTracks4.originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.mergedDuplicateTracks4 = process.mergedDuplicateTracks.clone()
process.mergedDuplicateTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mergedDuplicateTracks4.src = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")

process.earlyMuons4 = process.earlyMuons.clone()
process.earlyMuons4.TrackExtractorPSet.inputTrackCollection = cms.InputTag("generalTracks"+layers)
process.earlyMuons4.inputCollectionLabels = cms.VInputTag("earlyGeneralTracks"+layers, "standAloneMuons:UpdatedAtVtx")
process.earlyMuons4.pvInputTag = cms.InputTag("offlinePrimaryVertices"+layers)

process.detachedQuadStep4 = process.detachedQuadStep.clone()
process.detachedQuadStep4.src = cms.InputTag("detachedQuadStepTracks"+layers)
process.detachedQuadStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedQuadStepClusters4 = process.detachedQuadStepClusters.clone()
process.detachedQuadStepClusters4.oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+layers)
process.detachedQuadStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters4.trackClassifier = cms.InputTag("lowPtTripletStep"+layers,"QualityMasks")
process.detachedQuadStepClusters4.trajectories = cms.InputTag("lowPtTripletStepTracks"+layers)

process.detachedQuadStepHitDoublets4 = process.detachedQuadStepHitDoublets.clone()
process.detachedQuadStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedQuadStepHitDoublets4.seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+layers)

process.detachedQuadStepHitQuadruplets4 = process.detachedQuadStepHitQuadruplets.clone()
process.detachedQuadStepHitQuadruplets4.doublets = cms.InputTag("detachedQuadStepHitDoublets"+layers)
process.detachedQuadStepHitQuadruplets4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+layers+'__reRECO')

process.detachedQuadStepSeedLayers4 = process.detachedQuadStepSeedLayers.clone()
process.detachedQuadStepSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers4.BPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers4.FPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)

process.detachedQuadStepSeeds4 = process.detachedQuadStepSeeds.clone()
process.detachedQuadStepSeeds4.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedQuadStepSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+layers+'__reRECO')
process.detachedQuadStepSeeds4.seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+layers)

process.detachedQuadStepTrackCandidates4 = process.detachedQuadStepTrackCandidates.clone()
process.detachedQuadStepTrackCandidates4.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedQuadStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidates4.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidates4.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidates4.mkFitSeeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidates4.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedQuadStepTrackCandidates4.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)
process.detachedQuadStepTrackCandidates4.tracks = cms.InputTag("detachedQuadStepTrackCandidatesMkFit"+layers)

process.detachedQuadStepTrackCandidatesMkFit4 = process.detachedQuadStepTrackCandidatesMkFit.clone()
process.detachedQuadStepTrackCandidatesMkFit4.clustersToSkip = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepTrackCandidatesMkFit4.config = cms.ESInputTag("","detachedQuadStepTrackCandidatesMkFitConfig"+layers)
process.detachedQuadStepTrackCandidatesMkFit4.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit4.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidatesMkFit4.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit4.seeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidatesMkFit4.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedQuadStepTrackCandidatesMkFitConfig4 = process.detachedQuadStepTrackCandidatesMkFitConfig.clone()
process.detachedQuadStepTrackCandidatesMkFitConfig4.ComponentName = cms.string('detachedQuadStepTrackCandidatesMkFitConfig'+layers)

process.detachedQuadStepTrackCandidatesMkFitSeeds4 = process.detachedQuadStepTrackCandidatesMkFitSeeds.clone()
process.detachedQuadStepTrackCandidatesMkFitSeeds4.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)

process.detachedQuadStepTracks4 = process.detachedQuadStepTracks.clone()
process.detachedQuadStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedQuadStepTracks4.src = cms.InputTag("detachedQuadStepTrackCandidates"+layers)

process.detachedTripletStep4 = process.detachedTripletStep.clone()
process.detachedTripletStep4.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier14 = process.detachedTripletStepClassifier1.clone()
process.detachedTripletStepClassifier14.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier14.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier24 = process.detachedTripletStepClassifier2.clone()
process.detachedTripletStepClassifier24.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier24.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClusters4 = process.detachedTripletStepClusters.clone()
process.detachedTripletStepClusters4.oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedTripletStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters4.trackClassifier = cms.InputTag("detachedQuadStep"+layers,"QualityMasks")
process.detachedTripletStepClusters4.trajectories = cms.InputTag("detachedQuadStepTracks"+layers)

process.detachedTripletStepHitDoublets4 = process.detachedTripletStepHitDoublets.clone()
process.detachedTripletStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedTripletStepHitDoublets4.seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+layers)

process.detachedTripletStepHitTriplets4 = process.detachedTripletStepHitTriplets.clone()
process.detachedTripletStepHitTriplets4.doublets = cms.InputTag("detachedTripletStepHitDoublets"+layers)
process.detachedTripletStepHitTriplets4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+layers+'__reRECO')

process.detachedTripletStepSeedLayers4 = process.detachedTripletStepSeedLayers.clone()
process.detachedTripletStepSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers4.BPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers4.FPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)

process.detachedTripletStepSeeds4 = process.detachedTripletStepSeeds.clone()
process.detachedTripletStepSeeds4.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedTripletStepSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+layers+'__reRECO')
process.detachedTripletStepSeeds4.seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+layers)

process.detachedTripletStepTrackCandidates4 = process.detachedTripletStepTrackCandidates.clone()
process.detachedTripletStepTrackCandidates4.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidates4.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidates4.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidates4.mkFitSeeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidates4.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedTripletStepTrackCandidates4.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)
process.detachedTripletStepTrackCandidates4.tracks = cms.InputTag("detachedTripletStepTrackCandidatesMkFit"+layers)

process.detachedTripletStepTrackCandidatesMkFit4 = process.detachedTripletStepTrackCandidatesMkFit.clone()
process.detachedTripletStepTrackCandidatesMkFit4.clustersToSkip = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepTrackCandidatesMkFit4.config = cms.ESInputTag("","detachedTripletStepTrackCandidatesMkFitConfig"+layers)
process.detachedTripletStepTrackCandidatesMkFit4.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit4.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidatesMkFit4.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit4.seeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidatesMkFit4.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedTripletStepTrackCandidatesMkFitConfig4 = process.detachedTripletStepTrackCandidatesMkFitConfig.clone()
process.detachedTripletStepTrackCandidatesMkFitConfig4.ComponentName = cms.string('detachedTripletStepTrackCandidatesMkFitConfig'+layers)

process.detachedTripletStepTrackCandidatesMkFitSeeds4 = process.detachedTripletStepTrackCandidatesMkFitSeeds.clone()
process.detachedTripletStepTrackCandidatesMkFitSeeds4.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)

process.detachedTripletStepTracks4 = process.detachedTripletStepTracks.clone()
process.detachedTripletStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedTripletStepTracks4.src = cms.InputTag("detachedTripletStepTrackCandidates"+layers)

process.highPtTripletStep4 = process.highPtTripletStep.clone()
process.highPtTripletStep4.src = cms.InputTag("highPtTripletStepTracks"+layers)
process.highPtTripletStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.highPtTripletStepClusters4 = process.highPtTripletStepClusters.clone()
process.highPtTripletStepClusters4.oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+layers)
process.highPtTripletStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters4.trackClassifier = cms.InputTag("lowPtQuadStep"+layers,"QualityMasks")
process.highPtTripletStepClusters4.trajectories = cms.InputTag("lowPtQuadStepTracks"+layers)

process.highPtTripletStepHitDoublets4 = process.highPtTripletStepHitDoublets.clone()
process.highPtTripletStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.highPtTripletStepHitDoublets4.seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+layers)

process.highPtTripletStepHitTriplets4 = process.highPtTripletStepHitTriplets.clone()
process.highPtTripletStepHitTriplets4.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.highPtTripletStepHitTriplets4.doublets = cms.InputTag("highPtTripletStepHitDoublets"+layers)
process.highPtTripletStepHitTriplets4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+layers+'__reRECO')

process.highPtTripletStepSeedLayers4 = process.highPtTripletStepSeedLayers.clone()
process.highPtTripletStepSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers4.BPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers4.FPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)

process.highPtTripletStepSeeds4 = process.highPtTripletStepSeeds.clone()
process.highPtTripletStepSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+layers+'__reRECO')
process.highPtTripletStepSeeds4.seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+layers)

process.highPtTripletStepTrackCandidates4 = process.highPtTripletStepTrackCandidates.clone()
process.highPtTripletStepTrackCandidates4.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_highPtTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidates4.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidates4.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidates4.mkFitSeeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidates4.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.highPtTripletStepTrackCandidates4.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)
process.highPtTripletStepTrackCandidates4.tracks = cms.InputTag("highPtTripletStepTrackCandidatesMkFit"+layers)

process.highPtTripletStepTrackCandidatesMkFit4 = process.highPtTripletStepTrackCandidatesMkFit.clone()
process.highPtTripletStepTrackCandidatesMkFit4.clustersToSkip = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepTrackCandidatesMkFit4.config = cms.ESInputTag("","highPtTripletStepTrackCandidatesMkFitConfig"+layers)
process.highPtTripletStepTrackCandidatesMkFit4.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit4.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidatesMkFit4.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit4.seeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidatesMkFit4.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.highPtTripletStepTrackCandidatesMkFitConfig4 = process.highPtTripletStepTrackCandidatesMkFitConfig.clone()
process.highPtTripletStepTrackCandidatesMkFitConfig4.ComponentName = cms.string('highPtTripletStepTrackCandidatesMkFitConfig'+layers)

process.highPtTripletStepTrackCandidatesMkFitSeeds4 = process.highPtTripletStepTrackCandidatesMkFitSeeds.clone()
process.highPtTripletStepTrackCandidatesMkFitSeeds4.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)

process.highPtTripletStepTracks4 = process.highPtTripletStepTracks.clone()
process.highPtTripletStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.highPtTripletStepTracks4.src = cms.InputTag("highPtTripletStepTrackCandidates"+layers)

process.firstStepPrimaryVertices4 = process.firstStepPrimaryVertices.clone()
process.firstStepPrimaryVertices4.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.firstStepPrimaryVertices4.particles = cms.InputTag("initialStepTrackRefsForJets"+layers)
process.firstStepPrimaryVertices4.vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.firstStepPrimaryVerticesUnsorted4 = process.firstStepPrimaryVerticesUnsorted.clone()
process.firstStepPrimaryVerticesUnsorted4.TrackLabel = cms.InputTag("initialStepTracks"+layers)

process.initialStep4 = process.initialStep.clone()
process.initialStep4.src = cms.InputTag("initialStepTracks"+layers)
process.initialStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepClassifier14 = process.initialStepClassifier1.clone()
process.initialStepClassifier14.src = cms.InputTag("initialStepTracks"+layers)
process.initialStepClassifier14.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepHitDoublets4 = process.initialStepHitDoublets.clone()
process.initialStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.initialStepHitDoublets4.seedingLayers = cms.InputTag("initialStepSeedLayers"+layers)

process.initialStepHitQuadruplets4 = process.initialStepHitQuadruplets.clone()
process.initialStepHitQuadruplets4.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepHitQuadruplets4.doublets = cms.InputTag("initialStepHitDoublets"+layers)
process.initialStepHitQuadruplets4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+layers+'__reRECO')

process.initialStepSeedLayers4 = process.initialStepSeedLayers.clone()
process.initialStepSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.initialStepSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)

process.initialStepSeeds4 = process.initialStepSeeds.clone()
process.initialStepSeeds4.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+layers+'__reRECO')
process.initialStepSeeds4.seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+layers)

process.initialStepTrackCandidates4 = process.initialStepTrackCandidates.clone()
process.initialStepTrackCandidates4.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidates4.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidates4.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidates4.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidates4.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidates4.seeds = cms.InputTag("initialStepSeeds"+layers)
process.initialStepTrackCandidates4.tracks = cms.InputTag("initialStepTrackCandidatesMkFit"+layers)

process.initialStepTrackCandidatesMkFit4 = process.initialStepTrackCandidatesMkFit.clone()
process.initialStepTrackCandidatesMkFit4.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfig"+layers)
process.initialStepTrackCandidatesMkFit4.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidatesMkFit4.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFit4.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidatesMkFit4.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidatesMkFit4.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitConfig4 = process.initialStepTrackCandidatesMkFitConfig.clone()
process.initialStepTrackCandidatesMkFitConfig4.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfig'+layers)

process.initialStepTrackCandidatesMkFitSeeds4 = process.initialStepTrackCandidatesMkFitSeeds.clone()
process.initialStepTrackCandidatesMkFitSeeds4.seeds = cms.InputTag("initialStepSeeds"+layers)

process.initialStepTrackRefsForJets4 = process.initialStepTrackRefsForJets.clone()
process.initialStepTrackRefsForJets4.src = cms.InputTag("initialStepTracks"+layers)

process.initialStepTracks4 = process.initialStepTracks.clone()
process.initialStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.initialStepTracks4.src = cms.InputTag("initialStepTrackCandidates"+layers)

process.mkFitEventOfHits4 = process.mkFitEventOfHits.clone()
process.mkFitEventOfHits4.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHits4.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.mkFitEventOfHits4.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiPixelHits4 = process.mkFitSiPixelHits.clone()
process.mkFitSiPixelHits4.hits = cms.InputTag("siPixelRecHits"+layers)

process.firstStepGoodPrimaryVertices4 = process.firstStepGoodPrimaryVertices.clone()
process.firstStepGoodPrimaryVertices4.src = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStep4 = process.jetCoreRegionalStep.clone()
process.jetCoreRegionalStep4.src = cms.InputTag("jetCoreRegionalStepTracks"+layers)
process.jetCoreRegionalStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStepHitDoublets4 = process.jetCoreRegionalStepHitDoublets.clone()
process.jetCoreRegionalStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.jetCoreRegionalStepHitDoublets4.seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"+layers)
process.jetCoreRegionalStepHitDoublets4.trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"+layers)

process.jetCoreRegionalStepSeedLayers4 = process.jetCoreRegionalStepSeedLayers.clone()
process.jetCoreRegionalStepSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers4.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")

process.jetCoreRegionalStepSeeds4 = process.jetCoreRegionalStepSeeds.clone()
process.jetCoreRegionalStepSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_jetCoreRegionalStepHitDoublets'+layers+'__reRECO')
process.jetCoreRegionalStepSeeds4.seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets"+layers)

process.jetCoreRegionalStepTrackCandidates4 = process.jetCoreRegionalStepTrackCandidates.clone()
process.jetCoreRegionalStepTrackCandidates4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackCandidates4.src = cms.InputTag("jetCoreRegionalStepSeeds"+layers)

process.jetCoreRegionalStepTrackingRegions4 = process.jetCoreRegionalStepTrackingRegions.clone()
process.jetCoreRegionalStepTrackingRegions4.RegionPSet.JetSrc = cms.InputTag("jetsForCoreTracking"+layers)
process.jetCoreRegionalStepTrackingRegions4.RegionPSet.measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackingRegions4.RegionPSet.vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices"+layers)

process.jetCoreRegionalStepTracks4 = process.jetCoreRegionalStepTracks.clone()
process.jetCoreRegionalStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTracks4.src = cms.InputTag("jetCoreRegionalStepTrackCandidates"+layers)

process.jetsForCoreTracking4 = process.jetsForCoreTracking.clone()
process.jetsForCoreTracking4.src = cms.InputTag("ak4CaloJetsForTrk"+layers)

process.lowPtQuadStep4 = process.lowPtQuadStep.clone()
process.lowPtQuadStep4.src = cms.InputTag("lowPtQuadStepTracks"+layers)
process.lowPtQuadStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtQuadStepClusters4 = process.lowPtQuadStepClusters.clone()
process.lowPtQuadStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters4.trackClassifier = cms.InputTag("initialStep"+layers,"QualityMasks")
process.lowPtQuadStepClusters4.trajectories = cms.InputTag("initialStepTracks"+layers)

process.lowPtQuadStepHitDoublets4 = process.lowPtQuadStepHitDoublets.clone()
process.lowPtQuadStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtQuadStepHitDoublets4.seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+layers)

process.lowPtQuadStepHitQuadruplets4 = process.lowPtQuadStepHitQuadruplets.clone()
process.lowPtQuadStepHitQuadruplets4.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtQuadStepHitQuadruplets4.doublets = cms.InputTag("lowPtQuadStepHitDoublets"+layers)
process.lowPtQuadStepHitQuadruplets4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+layers+'__reRECO')

process.lowPtQuadStepSeedLayers4 = process.lowPtQuadStepSeedLayers.clone()
process.lowPtQuadStepSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers4.BPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers4.FPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)

process.lowPtQuadStepSeeds4 = process.lowPtQuadStepSeeds.clone()
process.lowPtQuadStepSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+layers+'__reRECO')
process.lowPtQuadStepSeeds4.seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+layers)

process.lowPtQuadStepTrackCandidates4 = process.lowPtQuadStepTrackCandidates.clone()
process.lowPtQuadStepTrackCandidates4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTrackCandidates4.clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepTrackCandidates4.src = cms.InputTag("lowPtQuadStepSeeds"+layers)

process.lowPtQuadStepTracks4 = process.lowPtQuadStepTracks.clone()
process.lowPtQuadStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTracks4.src = cms.InputTag("lowPtQuadStepTrackCandidates"+layers)

process.lowPtTripletStep4 = process.lowPtTripletStep.clone()
process.lowPtTripletStep4.src = cms.InputTag("lowPtTripletStepTracks"+layers)
process.lowPtTripletStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtTripletStepClusters4 = process.lowPtTripletStepClusters.clone()
process.lowPtTripletStepClusters4.oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+layers)
process.lowPtTripletStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters4.trackClassifier = cms.InputTag("highPtTripletStep"+layers,"QualityMasks")
process.lowPtTripletStepClusters4.trajectories = cms.InputTag("highPtTripletStepTracks"+layers)

process.lowPtTripletStepHitDoublets4 = process.lowPtTripletStepHitDoublets.clone()
process.lowPtTripletStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtTripletStepHitDoublets4.seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+layers)

process.lowPtTripletStepHitTriplets4 = process.lowPtTripletStepHitTriplets.clone()
process.lowPtTripletStepHitTriplets4.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtTripletStepHitTriplets4.doublets = cms.InputTag("lowPtTripletStepHitDoublets"+layers)
process.lowPtTripletStepHitTriplets4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+layers+'__reRECO')

process.lowPtTripletStepSeedLayers4 = process.lowPtTripletStepSeedLayers.clone()
process.lowPtTripletStepSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers4.BPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers4.FPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)

process.lowPtTripletStepSeeds4 = process.lowPtTripletStepSeeds.clone()
process.lowPtTripletStepSeeds4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+layers+'__reRECO')
process.lowPtTripletStepSeeds4.seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+layers)

process.lowPtTripletStepTrackCandidates4 = process.lowPtTripletStepTrackCandidates.clone()
process.lowPtTripletStepTrackCandidates4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTrackCandidates4.clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepTrackCandidates4.src = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.lowPtTripletStepTracks4 = process.lowPtTripletStepTracks.clone()
process.lowPtTripletStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTracks4.src = cms.InputTag("lowPtTripletStepTrackCandidates"+layers)

process.chargeCut2069Clusters4 = process.chargeCut2069Clusters.clone()
process.chargeCut2069Clusters4.oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+layers)
process.chargeCut2069Clusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.chargeCut2069Clusters4.stripClusters = cms.InputTag("rCluster"+layers)

process.mixedTripletStep4 = process.mixedTripletStep.clone()
process.mixedTripletStep4.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier14 = process.mixedTripletStepClassifier1.clone()
process.mixedTripletStepClassifier14.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier14.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier24 = process.mixedTripletStepClassifier2.clone()
process.mixedTripletStepClassifier24.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier24.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClusters4 = process.mixedTripletStepClusters.clone()
process.mixedTripletStepClusters4.oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+layers)
process.mixedTripletStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters4.trackClassifier = cms.InputTag("pixelPairStep"+layers,"QualityMasks")
process.mixedTripletStepClusters4.trajectories = cms.InputTag("pixelPairStepTracks"+layers)

process.mixedTripletStepHitDoubletsA4 = process.mixedTripletStepHitDoubletsA.clone()
process.mixedTripletStepHitDoubletsA4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsA4.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+layers)

process.mixedTripletStepHitDoubletsB4 = process.mixedTripletStepHitDoubletsB.clone()
process.mixedTripletStepHitDoubletsB4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsB4.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+layers)

process.mixedTripletStepHitTripletsA4 = process.mixedTripletStepHitTripletsA.clone()
process.mixedTripletStepHitTripletsA4.doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+layers)
process.mixedTripletStepHitTripletsA4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO')

process.mixedTripletStepHitTripletsB4 = process.mixedTripletStepHitTripletsB.clone()
process.mixedTripletStepHitTripletsB4.doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+layers)
process.mixedTripletStepHitTripletsB4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO')

process.mixedTripletStepSeedLayersA4 = process.mixedTripletStepSeedLayersA.clone()
process.mixedTripletStepSeedLayersA4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA4.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA4.FPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA4.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersA4.TEC.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeedLayersB4 = process.mixedTripletStepSeedLayersB.clone()
process.mixedTripletStepSeedLayersB4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersB4.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersB4.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersB4.TIB.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeeds4 = process.mixedTripletStepSeeds.clone()
process.mixedTripletStepSeeds4.seedCollections = cms.VInputTag("mixedTripletStepSeedsA"+layers, "mixedTripletStepSeedsB"+layers)

process.mixedTripletStepSeedsA4 = process.mixedTripletStepSeedsA.clone()
process.mixedTripletStepSeedsA4.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsA4.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsA4.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+layers)

process.mixedTripletStepSeedsB4 = process.mixedTripletStepSeedsB.clone()
process.mixedTripletStepSeedsB4.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsB4.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsB4.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+layers)

process.mixedTripletStepTrackCandidates4 = process.mixedTripletStepTrackCandidates.clone()
process.mixedTripletStepTrackCandidates4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTrackCandidates4.clustersToSkip = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepTrackCandidates4.src = cms.InputTag("mixedTripletStepSeeds"+layers)

process.mixedTripletStepTracks4 = process.mixedTripletStepTracks.clone()
process.mixedTripletStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTracks4.src = cms.InputTag("mixedTripletStepTrackCandidates"+layers)

process.pixelLessStep4 = process.pixelLessStep.clone()
process.pixelLessStep4.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier14 = process.pixelLessStepClassifier1.clone()
process.pixelLessStepClassifier14.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier14.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier24 = process.pixelLessStepClassifier2.clone()
process.pixelLessStepClassifier24.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier24.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClusters4 = process.pixelLessStepClusters.clone()
process.pixelLessStepClusters4.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+layers)
process.pixelLessStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters4.trackClassifier = cms.InputTag("mixedTripletStep"+layers,"QualityMasks")
process.pixelLessStepClusters4.trajectories = cms.InputTag("mixedTripletStepTracks"+layers)

process.pixelLessStepHitDoublets4 = process.pixelLessStepHitDoublets.clone()
process.pixelLessStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelLessStepHitDoublets4.seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+layers)

process.pixelLessStepHitTriplets4 = process.pixelLessStepHitTriplets.clone()
process.pixelLessStepHitTriplets4.doublets = cms.InputTag("pixelLessStepHitDoublets"+layers)
process.pixelLessStepHitTriplets4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+layers+'__reRECO')

process.pixelLessStepSeedLayers4 = process.pixelLessStepSeedLayers.clone()
process.pixelLessStepSeedLayers4.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers4.MTEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers4.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers4.MTIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers4.MTID.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers4.MTID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers4.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers4.TEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers4.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers4.TIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers4.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers4.TID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.pixelLessStepSeeds4 = process.pixelLessStepSeeds.clone()
process.pixelLessStepSeeds4.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.pixelLessStepSeeds4.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+layers+'__reRECO'
    )
process.pixelLessStepSeeds4.seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+layers)

process.pixelLessStepTrackCandidates4 = process.pixelLessStepTrackCandidates.clone()
process.pixelLessStepTrackCandidates4.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitOutputWrapper_pixelLessStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidates4.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidates4.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidates4.mkFitSeeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidates4.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.pixelLessStepTrackCandidates4.seeds = cms.InputTag("pixelLessStepSeeds"+layers)
process.pixelLessStepTrackCandidates4.tracks = cms.InputTag("pixelLessStepTrackCandidatesMkFit"+layers)

process.pixelLessStepTrackCandidatesMkFit4 = process.pixelLessStepTrackCandidatesMkFit.clone()
process.pixelLessStepTrackCandidatesMkFit4.clustersToSkip = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepTrackCandidatesMkFit4.config = cms.ESInputTag("","pixelLessStepTrackCandidatesMkFitConfig"+layers)
process.pixelLessStepTrackCandidatesMkFit4.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidatesMkFit4.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidatesMkFit4.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidatesMkFit4.seeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidatesMkFit4.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.pixelLessStepTrackCandidatesMkFitSeeds4 = process.pixelLessStepTrackCandidatesMkFitSeeds.clone()
process.pixelLessStepTrackCandidatesMkFitSeeds4.seeds = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelLessStepTrackCandidatesMkFitConfig4 = process.pixelLessStepTrackCandidatesMkFitConfig.clone()
process.pixelLessStepTrackCandidatesMkFitConfig4.ComponentName = cms.string('pixelLessStepTrackCandidatesMkFitConfig'+layers)

process.pixelLessStepTracks4 = process.pixelLessStepTracks.clone()
process.pixelLessStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelLessStepTracks4.src = cms.InputTag("pixelLessStepTrackCandidates"+layers)

process.pixelPairStep4 = process.pixelPairStep.clone()
process.pixelPairStep4.src = cms.InputTag("pixelPairStepTracks"+layers)
process.pixelPairStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepClusters4 = process.pixelPairStepClusters.clone()
process.pixelPairStepClusters4.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+layers)
process.pixelPairStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters4.trackClassifier = cms.InputTag("detachedTripletStep"+layers,"QualityMasks")
process.pixelPairStepClusters4.trajectories = cms.InputTag("detachedTripletStepTracks"+layers)

process.pixelPairStepHitDoublets4 = process.pixelPairStepHitDoublets.clone()
process.pixelPairStepHitDoublets4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoublets4.seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+layers)
process.pixelPairStepHitDoublets4.trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+layers)

process.pixelPairStepHitDoubletsB4 = process.pixelPairStepHitDoubletsB.clone()
process.pixelPairStepHitDoubletsB4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoubletsB4.trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+layers)

process.pixelPairStepSeedLayers4 = process.pixelPairStepSeedLayers.clone()
process.pixelPairStepSeedLayers4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers4.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepSeedLayers4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers4.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)

process.pixelPairStepSeeds4 = process.pixelPairStepSeeds.clone()
process.pixelPairStepSeeds4.seedCollections = cms.VInputTag("pixelPairStepSeedsA"+layers, "pixelPairStepSeedsB"+layers)

process.pixelPairStepSeedsA4 = process.pixelPairStepSeedsA.clone()
process.pixelPairStepSeedsA4.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsA4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+layers+'__reRECO')
process.pixelPairStepSeedsA4.seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+layers)

process.pixelPairStepSeedsB4 = process.pixelPairStepSeedsB.clone()
process.pixelPairStepSeedsB4.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsB4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+layers+'__reRECO')
process.pixelPairStepSeedsB4.seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+layers)

process.pixelPairStepTrackCandidates4 = process.pixelPairStepTrackCandidates.clone()
process.pixelPairStepTrackCandidates4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTrackCandidates4.clustersToSkip = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackCandidates4.src = cms.InputTag("pixelPairStepSeeds"+layers)

process.pixelPairStepTrackingRegions4 = process.pixelPairStepTrackingRegions.clone()
process.pixelPairStepTrackingRegions4.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairStepTrackingRegions4.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.pixelPairStepTrackingRegionsSeedLayersB4 = process.pixelPairStepTrackingRegionsSeedLayersB.clone()
process.pixelPairStepTrackingRegionsSeedLayersB4.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB4.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB4.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB4.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB4.RegionPSet.vertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepTracks4 = process.pixelPairStepTracks.clone()
process.pixelPairStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTracks4.src = cms.InputTag("pixelPairStepTrackCandidates"+layers)

process.tobTecStep4 = process.tobTecStep.clone()
process.tobTecStep4.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStep4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier14 = process.tobTecStepClassifier1.clone()
process.tobTecStepClassifier14.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier14.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier24 = process.tobTecStepClassifier2.clone()
process.tobTecStepClassifier24.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier24.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClusters4 = process.tobTecStepClusters.clone()
process.tobTecStepClusters4.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.tobTecStepClusters4.pixelClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters4.stripClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters4.trackClassifier = cms.InputTag("pixelLessStep"+layers,"QualityMasks")
process.tobTecStepClusters4.trajectories = cms.InputTag("pixelLessStepTracks"+layers)

process.tobTecStepHitDoubletsPair4 = process.tobTecStepHitDoubletsPair.clone()
process.tobTecStepHitDoubletsPair4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsPair4.seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+layers)

process.tobTecStepHitDoubletsTripl4 = process.tobTecStepHitDoubletsTripl.clone()
process.tobTecStepHitDoubletsTripl4.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsTripl4.seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+layers)

process.tobTecStepHitTripletsTripl4 = process.tobTecStepHitTripletsTripl.clone()
process.tobTecStepHitTripletsTripl4.doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+layers)
process.tobTecStepHitTripletsTripl4.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+layers+'__reRECO')

process.tobTecStepSeedLayersPair4 = process.tobTecStepSeedLayersPair.clone()
process.tobTecStepSeedLayersPair4.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair4.TEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersPair4.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair4.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeedLayersTripl4 = process.tobTecStepSeedLayersTripl.clone()
process.tobTecStepSeedLayersTripl4.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl4.MTEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl4.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl4.MTOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl4.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersTripl4.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeeds4 = process.tobTecStepSeeds.clone()
process.tobTecStepSeeds4.seedCollections = cms.VInputTag("tobTecStepSeedsTripl"+layers, "tobTecStepSeedsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsPair4 = process.tobTecStepSeedsPair.clone()
process.tobTecStepSeedsPair4.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsPair4.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+layers+'__reRECO')
process.tobTecStepSeedsPair4.seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsTripl4 = process.tobTecStepSeedsTripl.clone()
process.tobTecStepSeedsTripl4.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsTripl4.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+layers+'__reRECO'
    )
process.tobTecStepSeedsTripl4.seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+layers)

process.tobTecStepTrackCandidates4 = process.tobTecStepTrackCandidates.clone()
process.tobTecStepTrackCandidates4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTrackCandidates4.clustersToSkip = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepTrackCandidates4.src = cms.InputTag("tobTecStepSeeds"+layers)

process.tobTecStepTracks4 = process.tobTecStepTracks.clone()
process.tobTecStepTracks4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTracks4.src = cms.InputTag("tobTecStepTrackCandidates"+layers)

process.muonSeededTracksOutInClassifier4 = process.muonSeededTracksOutInClassifier.clone()
process.muonSeededTracksOutInClassifier4.src = cms.InputTag("muonSeededTracksOutIn"+layers)
process.muonSeededTracksOutInClassifier4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.muonSeededSeedsInOut4 = process.muonSeededSeedsInOut.clone()
process.muonSeededSeedsInOut4.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesInOut4 = process.muonSeededTrackCandidatesInOut.clone()
process.muonSeededTrackCandidatesInOut4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesInOut4.src = cms.InputTag("muonSeededSeedsInOut"+layers)

process.muonSeededTracksInOut4 = process.muonSeededTracksInOut.clone()
process.muonSeededTracksInOut4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksInOut4.src = cms.InputTag("muonSeededTrackCandidatesInOut"+layers)

process.muonSeededSeedsOutIn4 = process.muonSeededSeedsOutIn.clone()
process.muonSeededSeedsOutIn4.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesOutIn4 = process.muonSeededTrackCandidatesOutIn.clone()
process.muonSeededTrackCandidatesOutIn4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesOutIn4.src = cms.InputTag("muonSeededSeedsOutIn"+layers)

process.muonSeededTracksOutIn4 = process.muonSeededTracksOutIn.clone()
process.muonSeededTracksOutIn4.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksOutIn4.src = cms.InputTag("muonSeededTrackCandidatesOutIn"+layers)

process.muonSeededTracksInOutClassifier4 = process.muonSeededTracksInOutClassifier.clone()
process.muonSeededTracksInOutClassifier4.src = cms.InputTag("muonSeededTracksInOut"+layers)
process.muonSeededTracksInOutClassifier4.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.clusterSummaryProducer4 = process.clusterSummaryProducer.clone()
process.clusterSummaryProducer4.stripClusters = cms.InputTag("rCluster"+layers)

process.siStripMatchedRecHits4 = process.siStripMatchedRecHits.clone()
process.siStripMatchedRecHits4.ClusterProducer = cms.InputTag("rCluster"+layers)

process.reconstruction_trackingOnly_4layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.trackExtrapolator,process.trackExtrapolator4)
process.reconstruction_trackingOnly_4layers.replace(process.generalV0Candidates,process.generalV0Candidates4)
process.reconstruction_trackingOnly_4layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices4)
process.reconstruction_trackingOnly_4layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS4)
process.reconstruction_trackingOnly_4layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting4)
process.reconstruction_trackingOnly_4layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting4)
process.reconstruction_trackingOnly_4layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices4)
process.reconstruction_trackingOnly_4layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk4)
process.reconstruction_trackingOnly_4layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices4)
process.reconstruction_trackingOnly_4layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder4)
process.reconstruction_trackingOnly_4layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator4)
process.reconstruction_trackingOnly_4layers.replace(process.vertexMerger,process.vertexMerger4)
process.reconstruction_trackingOnly_4layers.replace(process.dedxHarmonic2,process.dedxHarmonic24)
process.reconstruction_trackingOnly_4layers.replace(process.dedxHitInfo,process.dedxHitInfo4)
process.reconstruction_trackingOnly_4layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0854)
process.reconstruction_trackingOnly_4layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic24)
process.reconstruction_trackingOnly_4layers.replace(process.dedxTruncated40,process.dedxTruncated404)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask4)
process.reconstruction_trackingOnly_4layers.replace(process.newCombinedSeeds,process.newCombinedSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions4)
process.reconstruction_trackingOnly_4layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask4)
process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets4)
process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.conversionStepTracks,process.conversionStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.trackerClusterCheck,process.trackerClusterCheck4)
process.reconstruction_trackingOnly_4layers.replace(process.convClusters,process.convClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.convLayerPairs,process.convLayerPairs4)
process.reconstruction_trackingOnly_4layers.replace(process.convStepSelector,process.convStepSelector4)
process.reconstruction_trackingOnly_4layers.replace(process.convStepTracks,process.convStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.convTrackCandidates,process.convTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg4)
process.reconstruction_trackingOnly_4layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent4)
process.reconstruction_trackingOnly_4layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits4)
process.reconstruction_trackingOnly_4layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache4)
process.reconstruction_trackingOnly_4layers.replace(process.siPixelClusters,process.siPixelClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.siPixelRecHits,process.siPixelRecHits4)
process.reconstruction_trackingOnly_4layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting4)
process.reconstruction_trackingOnly_4layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier4)
process.reconstruction_trackingOnly_4layers.replace(process.generalTracks,process.generalTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.earlyMuons,process.earlyMuons4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStep,process.detachedQuadStep4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStep,process.detachedTripletStep4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier14)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier24)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStep,process.highPtTripletStep4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices4)
process.reconstruction_trackingOnly_4layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStep,process.initialStep4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepClassifier1,process.initialStepClassifier14)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeeds,process.initialStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets4)
process.reconstruction_trackingOnly_4layers.replace(process.initialStepTracks,process.initialStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits4)
process.reconstruction_trackingOnly_4layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits4)
process.reconstruction_trackingOnly_4layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices4)
process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep4)
process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions4)
process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStep,process.lowPtQuadStep4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStep,process.lowPtTripletStep4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStep,process.mixedTripletStep4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier14)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier24)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStep,process.pixelLessStep4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier14)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier24)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTrackCandidatesMkFitConfig,process.pixelLessStepTrackCandidatesMkFitConfig4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStep,process.pixelPairStep4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB4)
process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStep,process.tobTecStep4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier14)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier24)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepClusters,process.tobTecStepClusters4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates4)
process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepTracks,process.tobTecStepTracks4)
process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier4)
process.reconstruction_trackingOnly_4layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut4)
process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut4)
process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut4)
process.reconstruction_trackingOnly_4layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn4)
process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn4)
process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn4)
process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier4)
process.reconstruction_trackingOnly_4layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer4)
process.reconstruction_trackingOnly_4layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits4)

####################################################################################################

layers = "5"

process.MeasurementTrackerEventPreSplitting5 = process.MeasurementTrackerEventPreSplitting.clone()
process.MeasurementTrackerEventPreSplitting5.stripClusterProducer = cms.string('rCluster'+layers)

process.trackExtrapolator5 = process.trackExtrapolator.clone()
process.trackExtrapolator5.trackSrc = cms.InputTag("generalTracks"+layers)

process.generalV0Candidates5 = process.generalV0Candidates.clone()
process.generalV0Candidates5.trackRecoAlgorithm = cms.InputTag("generalTracks"+layers)
process.generalV0Candidates5.vertices = cms.InputTag("offlinePrimaryVertices"+layers)

process.offlinePrimaryVertices5 = process.offlinePrimaryVertices.clone()
process.offlinePrimaryVertices5.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVertices5.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVertices5.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.offlinePrimaryVerticesWithBS5 = process.offlinePrimaryVerticesWithBS.clone()
process.offlinePrimaryVerticesWithBS5.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVerticesWithBS5.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVerticesWithBS5.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers,"WithBS")

process.trackRefsForJetsBeforeSorting5 = process.trackRefsForJetsBeforeSorting.clone()
process.trackRefsForJetsBeforeSorting5.src = cms.InputTag("trackWithVertexRefSelectorBeforeSorting"+layers)

process.trackWithVertexRefSelectorBeforeSorting5 = process.trackWithVertexRefSelectorBeforeSorting.clone()
process.trackWithVertexRefSelectorBeforeSorting5.src = cms.InputTag("generalTracks"+layers)
process.trackWithVertexRefSelectorBeforeSorting5.vertexTag = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.unsortedOfflinePrimaryVertices5 = process.unsortedOfflinePrimaryVertices.clone()
process.unsortedOfflinePrimaryVertices5.TrackLabel = cms.InputTag("generalTracks"+layers)

process.ak4CaloJetsForTrk5 = process.ak4CaloJetsForTrk.clone()
process.ak4CaloJetsForTrk5.srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.inclusiveSecondaryVertices5 = process.inclusiveSecondaryVertices.clone()
process.inclusiveSecondaryVertices5.secondaryVertices = cms.InputTag("trackVertexArbitrator"+layers)

process.inclusiveVertexFinder5 = process.inclusiveVertexFinder.clone() 
process.inclusiveVertexFinder5.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.inclusiveVertexFinder5.tracks = cms.InputTag("generalTracks"+layers)

process.trackVertexArbitrator5 = process.trackVertexArbitrator.clone() 
process.trackVertexArbitrator5.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.trackVertexArbitrator5.secondaryVertices = cms.InputTag("vertexMerger"+layers)
process.trackVertexArbitrator5.tracks = cms.InputTag("generalTracks"+layers)

process.vertexMerger5 = process.vertexMerger.clone()
process.vertexMerger5.secondaryVertices = cms.InputTag("inclusiveVertexFinder"+layers)

process.dedxHarmonic25 = process.dedxHarmonic2.clone()
process.dedxHarmonic25.tracks = cms.InputTag("generalTracks"+layers)

process.dedxHitInfo5 = process.dedxHitInfo.clone() 
process.dedxHitInfo5.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelAndStripHarmonic2T0855 = process.dedxPixelAndStripHarmonic2T085.clone() 
process.dedxPixelAndStripHarmonic2T0855.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelHarmonic25 = process.dedxPixelHarmonic2.clone() 
process.dedxPixelHarmonic25.tracks = cms.InputTag("generalTracks"+layers)

process.dedxTruncated405 = process.dedxTruncated40.clone()
process.dedxTruncated405.tracks = cms.InputTag("generalTracks"+layers)

process.detachedTripletStepSeedClusterMask5 = process.detachedTripletStepSeedClusterMask.clone() 
process.detachedTripletStepSeedClusterMask5.oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+layers)
process.detachedTripletStepSeedClusterMask5.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask5.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask5.trajectories = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.initialStepSeedClusterMask5 = process.initialStepSeedClusterMask.clone() 
process.initialStepSeedClusterMask5.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.initialStepSeedClusterMask5.pixelClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask5.stripClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask5.trajectories = cms.InputTag("initialStepSeeds"+layers)

process.mixedTripletStepSeedClusterMask5 = process.mixedTripletStepSeedClusterMask.clone() 
process.mixedTripletStepSeedClusterMask5.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+layers)
process.mixedTripletStepSeedClusterMask5.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask5.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask5.trajectories = cms.InputTag("mixedTripletStepSeeds"+layers)

process.newCombinedSeeds5 = process.newCombinedSeeds.clone()
process.newCombinedSeeds5.seedCollections = cms.VInputTag(
        "initialStepSeeds"+layers, "highPtTripletStepSeeds"+layers, "mixedTripletStepSeeds"+layers, "pixelLessStepSeeds"+layers, "tripletElectronSeeds"+layers,
        "pixelPairElectronSeeds"+layers, "stripPairElectronSeeds"+layers, "lowPtTripletStepSeeds"+layers, "lowPtQuadStepSeeds"+layers, "detachedTripletStepSeeds"+layers,
        "detachedQuadStepSeeds"+layers, "pixelPairStepSeeds"+layers
    )

process.pixelLessStepSeedClusterMask5 = process.pixelLessStepSeedClusterMask.clone() 
process.pixelLessStepSeedClusterMask5.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+layers)
process.pixelLessStepSeedClusterMask5.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask5.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask5.trajectories = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelPairElectronHitDoublets5 = process.pixelPairElectronHitDoublets.clone() 
process.pixelPairElectronHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairElectronHitDoublets5.seedingLayers = cms.InputTag("pixelPairElectronSeedLayers"+layers)
process.pixelPairElectronHitDoublets5.trackingRegions = cms.InputTag("pixelPairElectronTrackingRegions"+layers)

process.pixelPairElectronSeedLayers5 = process.pixelPairElectronSeedLayers.clone()
process.pixelPairElectronSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers5.BPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.pixelPairElectronSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers5.FPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.pixelPairElectronSeeds5 = process.pixelPairElectronSeeds.clone()
process.pixelPairElectronSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairElectronHitDoublets'+layers+'__reRECO')
process.pixelPairElectronSeeds5.seedingHitSets = cms.InputTag("pixelPairElectronHitDoublets"+layers)

process.pixelPairElectronTrackingRegions5 = process.pixelPairElectronTrackingRegions.clone() 
process.pixelPairElectronTrackingRegions5.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairElectronTrackingRegions5.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.stripPairElectronHitDoublets5 = process.stripPairElectronHitDoublets.clone() 
process.stripPairElectronHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.stripPairElectronHitDoublets5.seedingLayers = cms.InputTag("stripPairElectronSeedLayers"+layers)

process.stripPairElectronSeedLayers5 = process.stripPairElectronSeedLayers.clone() 
process.stripPairElectronSeedLayers5.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers5.TEC.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers5.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers5.TIB.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers5.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers5.TID.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.stripPairElectronSeeds5 = process.stripPairElectronSeeds.clone() 
process.stripPairElectronSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_stripPairElectronHitDoublets'+layers+'__reRECO')
process.stripPairElectronSeeds5.seedingHitSets = cms.InputTag("stripPairElectronHitDoublets"+layers)

process.tripletElectronClusterMask5 = process.tripletElectronClusterMask.clone()
process.tripletElectronClusterMask5.oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronClusterMask5.pixelClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask5.stripClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask5.trajectories = cms.InputTag("tripletElectronSeeds"+layers)

process.tripletElectronHitDoublets5 = process.tripletElectronHitDoublets.clone() 
process.tripletElectronHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tripletElectronHitDoublets5.seedingLayers = cms.InputTag("tripletElectronSeedLayers"+layers)

process.tripletElectronHitTriplets5 = process.tripletElectronHitTriplets.clone()
process.tripletElectronHitTriplets5.doublets = cms.InputTag("tripletElectronHitDoublets"+layers)
process.tripletElectronHitTriplets5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO')

process.tripletElectronSeedLayers5 = process.tripletElectronSeedLayers.clone()
process.tripletElectronSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers5.BPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers5.FPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)

process.tripletElectronSeeds5 = process.tripletElectronSeeds.clone()
process.tripletElectronSeeds5.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tripletElectronHitTriplets'+layers+'__reRECO',
        'IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO'
    )
process.tripletElectronSeeds5.seedingHitSets = cms.InputTag("tripletElectronHitTriplets"+layers)

process.conversionStepTracks5 = process.conversionStepTracks.clone()
process.conversionStepTracks5.TrackProducers = cms.VInputTag("convStepTracks"+layers)
process.conversionStepTracks5.selectedTrackQuals = cms.VInputTag("convStepSelector"+layers+":convStep"+layers)

process.earlyGeneralTracks5 = process.earlyGeneralTracks.clone()
process.earlyGeneralTracks5.inputClassifiers = cms.vstring(
        'initialStep'+layers,
        'highPtTripletStep'+layers,
        'jetCoreRegionalStep'+layers,
        'lowPtQuadStep'+layers,
        'lowPtTripletStep'+layers,
        'detachedQuadStep'+layers,
        'detachedTripletStep'+layers,
        'pixelPairStep'+layers,
        'mixedTripletStep'+layers,
        'pixelLessStep'+layers,
        'tobTecStep'+layers
    )
process.earlyGeneralTracks5.trackProducers = cms.VInputTag(
        "initialStepTracks"+layers, "highPtTripletStepTracks"+layers, "jetCoreRegionalStepTracks"+layers, "lowPtQuadStepTracks"+layers, "lowPtTripletStepTracks"+layers,
        "detachedQuadStepTracks"+layers, "detachedTripletStepTracks"+layers, "pixelPairStepTracks"+layers, "mixedTripletStepTracks"+layers, "pixelLessStepTracks"+layers,
        "tobTecStepTracks"+layers
    )

process.preDuplicateMergingGeneralTracks5 = process.preDuplicateMergingGeneralTracks.clone()
process.preDuplicateMergingGeneralTracks5.inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+layers,
        'muonSeededTracksInOutClassifier'+layers,
        'muonSeededTracksOutInClassifier'+layers
    )
process.preDuplicateMergingGeneralTracks5.trackProducers = cms.VInputTag("earlyGeneralTracks"+layers, "muonSeededTracksInOut"+layers, "muonSeededTracksOutIn"+layers)

process.trackerClusterCheck5 = process.trackerClusterCheck.clone()
process.trackerClusterCheck5.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.trackerClusterCheck5.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.convClusters5 = process.convClusters.clone()
process.convClusters5.oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"+layers)
process.convClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.convClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.convClusters5.trackClassifier = cms.InputTag("tobTecStep"+layers,"QualityMasks")
process.convClusters5.trajectories = cms.InputTag("tobTecStepTracks"+layers)

process.convLayerPairs5 = process.convLayerPairs.clone()
process.convLayerPairs5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs5.BPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs5.FPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs5.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs5.MTIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs5.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs5.MTOB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs5.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs5.TEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHitUnmatched")
process.convLayerPairs5.TEC.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs5.TEC.stereoRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHitUnmatched")
process.convLayerPairs5.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs5.TIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs5.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs5.TID.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs5.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs5.TOB.skipClusters = cms.InputTag("convClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.convStepSelector5 = process.convStepSelector.clone()
process.convStepSelector5.src = cms.InputTag("convStepTracks"+layers)
#process.convStepSelector5.trackSelectors.name = cms.string('convStep'+layers)
process.convStepSelector5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.convStepTracks5 = process.convStepTracks.clone()
process.convStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convStepTracks5.src = cms.InputTag("convTrackCandidates"+layers)

process.convTrackCandidates5 = process.convTrackCandidates.clone()
process.convTrackCandidates5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convTrackCandidates5.clustersToSkip = cms.InputTag("convClusters"+layers)
process.convTrackCandidates5.src = cms.InputTag("photonConvTrajSeedFromSingleLeg"+layers,"convSeedCandidates")

process.photonConvTrajSeedFromSingleLeg5 = process.photonConvTrajSeedFromSingleLeg.clone()
process.photonConvTrajSeedFromSingleLeg5.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg5.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg5.OrderedHitsFactoryPSet.SeedingLayers = cms.InputTag("convLayerPairs"+layers)
process.photonConvTrajSeedFromSingleLeg5.TrackRefitter = cms.InputTag("generalTracks"+layers)
process.photonConvTrajSeedFromSingleLeg5.primaryVerticesTag = cms.InputTag("firstStepPrimaryVertices"+layers)

process.MeasurementTrackerEvent5 = process.MeasurementTrackerEvent.clone()
process.MeasurementTrackerEvent5.pixelClusterProducer = cms.string('rCluster'+layers)
process.MeasurementTrackerEvent5.stripClusterProducer = cms.string('rCluster'+layers)

process.ak4CaloJetsForTrkPreSplitting5 = process.ak4CaloJetsForTrkPreSplitting.clone()
process.ak4CaloJetsForTrkPreSplitting5.srcPVs = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.firstStepPrimaryVerticesPreSplitting5 = process.firstStepPrimaryVerticesPreSplitting.clone()
process.firstStepPrimaryVerticesPreSplitting5.TrackLabel = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepHitDoubletsPreSplitting5 = process.initialStepHitDoubletsPreSplitting.clone()
process.initialStepHitDoubletsPreSplitting5.clusterCheck = cms.InputTag("trackerClusterCheckPreSplitting"+layers)

process.initialStepHitQuadrupletsPreSplitting5 = process.initialStepHitQuadrupletsPreSplitting.clone()
process.initialStepHitQuadrupletsPreSplitting5.doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"+layers)
process.initialStepHitQuadrupletsPreSplitting5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoubletsPreSplitting'+layers+'__reRECO')

process.initialStepSeedsPreSplitting5 = process.initialStepSeedsPreSplitting.clone()
process.initialStepSeedsPreSplitting5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadrupletsPreSplitting'+layers+'__reRECO')
process.initialStepSeedsPreSplitting5.seedingHitSets = cms.InputTag("initialStepHitQuadrupletsPreSplitting"+layers)

process.initialStepTrackCandidatesMkFitConfigPreSplitting5 = process.initialStepTrackCandidatesMkFitConfigPreSplitting.clone()
process.initialStepTrackCandidatesMkFitConfigPreSplitting5.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfigPreSplitting'+layers)

process.initialStepTrackCandidatesMkFitPreSplitting5 = process.initialStepTrackCandidatesMkFitPreSplitting.clone()
process.initialStepTrackCandidatesMkFitPreSplitting5.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfigPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting5.eventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting5.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFitPreSplitting5.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting5.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitSeedsPreSplitting5 = process.initialStepTrackCandidatesMkFitSeedsPreSplitting.clone()
process.initialStepTrackCandidatesMkFitSeedsPreSplitting5.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)

process.initialStepTrackCandidatesPreSplitting5 = process.initialStepTrackCandidatesPreSplitting.clone()
process.initialStepTrackCandidatesPreSplitting5.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFitPreSplitting'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesPreSplitting5.mkFitEventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting5.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting5.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidatesPreSplitting5.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting5.tracks = cms.InputTag("initialStepTrackCandidatesMkFitPreSplitting"+layers)

process.initialStepTrackRefsForJetsPreSplitting5 = process.initialStepTrackRefsForJetsPreSplitting.clone()
process.initialStepTrackRefsForJetsPreSplitting5.src = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepTracksPreSplitting5 = process.initialStepTracksPreSplitting.clone()
process.initialStepTracksPreSplitting5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"+layers)
process.initialStepTracksPreSplitting5.src = cms.InputTag("initialStepTrackCandidatesPreSplitting"+layers)

process.jetsForCoreTrackingPreSplitting5 = process.jetsForCoreTrackingPreSplitting.clone()
process.jetsForCoreTrackingPreSplitting5.src = cms.InputTag("ak4CaloJetsForTrkPreSplitting"+layers)

process.mkFitEventOfHitsPreSplitting5 = process.mkFitEventOfHitsPreSplitting.clone()
process.mkFitEventOfHitsPreSplitting5.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHitsPreSplitting5.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiStripHits5 = process.mkFitSiStripHits.clone()
process.mkFitSiStripHits5.rphiHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.mkFitSiStripHits5.stereoHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHit")

process.siPixelClusterShapeCache5 = process.siPixelClusterShapeCache.clone()
process.siPixelClusterShapeCache5.src = cms.InputTag("rCluster"+layers)

process.siPixelClusters5 = process.siPixelClusters.clone()
process.siPixelClusters5.cores = cms.InputTag("jetsForCoreTrackingPreSplitting"+layers)
process.siPixelClusters5.vertices = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.siPixelRecHits5 = process.siPixelRecHits.clone()
process.siPixelRecHits5.src = cms.InputTag("rCluster"+layers)

process.trackerClusterCheckPreSplitting5 = process.trackerClusterCheckPreSplitting.clone()
process.trackerClusterCheckPreSplitting5.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.duplicateTrackCandidates5 = process.duplicateTrackCandidates.clone()
process.duplicateTrackCandidates5.source = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.duplicateTrackClassifier5 = process.duplicateTrackClassifier.clone()
process.duplicateTrackClassifier5.src = cms.InputTag("mergedDuplicateTracks"+layers)
process.duplicateTrackClassifier5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.generalTracks5 = process.generalTracks.clone()
process.generalTracks5.candidateComponents = cms.InputTag("duplicateTrackCandidates"+layers,"candidateMap")
process.generalTracks5.candidateSource = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")
process.generalTracks5.mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+layers,"MVAValues")
process.generalTracks5.mergedSource = cms.InputTag("mergedDuplicateTracks"+layers)
process.generalTracks5.originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+layers,"MVAValues")
process.generalTracks5.originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.mergedDuplicateTracks5 = process.mergedDuplicateTracks.clone()
process.mergedDuplicateTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mergedDuplicateTracks5.src = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")

process.earlyMuons5 = process.earlyMuons.clone()
process.earlyMuons5.TrackExtractorPSet.inputTrackCollection = cms.InputTag("generalTracks"+layers)
process.earlyMuons5.inputCollectionLabels = cms.VInputTag("earlyGeneralTracks"+layers, "standAloneMuons:UpdatedAtVtx")
process.earlyMuons5.pvInputTag = cms.InputTag("offlinePrimaryVertices"+layers)

process.detachedQuadStep5 = process.detachedQuadStep.clone()
process.detachedQuadStep5.src = cms.InputTag("detachedQuadStepTracks"+layers)
process.detachedQuadStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedQuadStepClusters5 = process.detachedQuadStepClusters.clone()
process.detachedQuadStepClusters5.oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+layers)
process.detachedQuadStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters5.trackClassifier = cms.InputTag("lowPtTripletStep"+layers,"QualityMasks")
process.detachedQuadStepClusters5.trajectories = cms.InputTag("lowPtTripletStepTracks"+layers)

process.detachedQuadStepHitDoublets5 = process.detachedQuadStepHitDoublets.clone()
process.detachedQuadStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedQuadStepHitDoublets5.seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+layers)

process.detachedQuadStepHitQuadruplets5 = process.detachedQuadStepHitQuadruplets.clone()
process.detachedQuadStepHitQuadruplets5.doublets = cms.InputTag("detachedQuadStepHitDoublets"+layers)
process.detachedQuadStepHitQuadruplets5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+layers+'__reRECO')

process.detachedQuadStepSeedLayers5 = process.detachedQuadStepSeedLayers.clone()
process.detachedQuadStepSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers5.BPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers5.FPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)

process.detachedQuadStepSeeds5 = process.detachedQuadStepSeeds.clone()
process.detachedQuadStepSeeds5.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedQuadStepSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+layers+'__reRECO')
process.detachedQuadStepSeeds5.seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+layers)

process.detachedQuadStepTrackCandidates5 = process.detachedQuadStepTrackCandidates.clone()
process.detachedQuadStepTrackCandidates5.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedQuadStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidates5.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidates5.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidates5.mkFitSeeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidates5.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedQuadStepTrackCandidates5.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)
process.detachedQuadStepTrackCandidates5.tracks = cms.InputTag("detachedQuadStepTrackCandidatesMkFit"+layers)

process.detachedQuadStepTrackCandidatesMkFit5 = process.detachedQuadStepTrackCandidatesMkFit.clone()
process.detachedQuadStepTrackCandidatesMkFit5.clustersToSkip = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepTrackCandidatesMkFit5.config = cms.ESInputTag("","detachedQuadStepTrackCandidatesMkFitConfig"+layers)
process.detachedQuadStepTrackCandidatesMkFit5.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit5.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidatesMkFit5.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit5.seeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidatesMkFit5.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedQuadStepTrackCandidatesMkFitConfig5 = process.detachedQuadStepTrackCandidatesMkFitConfig.clone()
process.detachedQuadStepTrackCandidatesMkFitConfig5.ComponentName = cms.string('detachedQuadStepTrackCandidatesMkFitConfig'+layers)

process.detachedQuadStepTrackCandidatesMkFitSeeds5 = process.detachedQuadStepTrackCandidatesMkFitSeeds.clone()
process.detachedQuadStepTrackCandidatesMkFitSeeds5.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)

process.detachedQuadStepTracks5 = process.detachedQuadStepTracks.clone()
process.detachedQuadStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedQuadStepTracks5.src = cms.InputTag("detachedQuadStepTrackCandidates"+layers)

process.detachedTripletStep5 = process.detachedTripletStep.clone()
process.detachedTripletStep5.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier15 = process.detachedTripletStepClassifier1.clone()
process.detachedTripletStepClassifier15.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier15.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier25 = process.detachedTripletStepClassifier2.clone()
process.detachedTripletStepClassifier25.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier25.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClusters5 = process.detachedTripletStepClusters.clone()
process.detachedTripletStepClusters5.oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedTripletStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters5.trackClassifier = cms.InputTag("detachedQuadStep"+layers,"QualityMasks")
process.detachedTripletStepClusters5.trajectories = cms.InputTag("detachedQuadStepTracks"+layers)

process.detachedTripletStepHitDoublets5 = process.detachedTripletStepHitDoublets.clone()
process.detachedTripletStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedTripletStepHitDoublets5.seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+layers)

process.detachedTripletStepHitTriplets5 = process.detachedTripletStepHitTriplets.clone()
process.detachedTripletStepHitTriplets5.doublets = cms.InputTag("detachedTripletStepHitDoublets"+layers)
process.detachedTripletStepHitTriplets5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+layers+'__reRECO')

process.detachedTripletStepSeedLayers5 = process.detachedTripletStepSeedLayers.clone()
process.detachedTripletStepSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers5.BPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers5.FPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)

process.detachedTripletStepSeeds5 = process.detachedTripletStepSeeds.clone()
process.detachedTripletStepSeeds5.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedTripletStepSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+layers+'__reRECO')
process.detachedTripletStepSeeds5.seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+layers)

process.detachedTripletStepTrackCandidates5 = process.detachedTripletStepTrackCandidates.clone()
process.detachedTripletStepTrackCandidates5.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidates5.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidates5.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidates5.mkFitSeeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidates5.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedTripletStepTrackCandidates5.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)
process.detachedTripletStepTrackCandidates5.tracks = cms.InputTag("detachedTripletStepTrackCandidatesMkFit"+layers)

process.detachedTripletStepTrackCandidatesMkFit5 = process.detachedTripletStepTrackCandidatesMkFit.clone()
process.detachedTripletStepTrackCandidatesMkFit5.clustersToSkip = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepTrackCandidatesMkFit5.config = cms.ESInputTag("","detachedTripletStepTrackCandidatesMkFitConfig"+layers)
process.detachedTripletStepTrackCandidatesMkFit5.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit5.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidatesMkFit5.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit5.seeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidatesMkFit5.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedTripletStepTrackCandidatesMkFitConfig5 = process.detachedTripletStepTrackCandidatesMkFitConfig.clone()
process.detachedTripletStepTrackCandidatesMkFitConfig5.ComponentName = cms.string('detachedTripletStepTrackCandidatesMkFitConfig'+layers)

process.detachedTripletStepTrackCandidatesMkFitSeeds5 = process.detachedTripletStepTrackCandidatesMkFitSeeds.clone()
process.detachedTripletStepTrackCandidatesMkFitSeeds5.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)

process.detachedTripletStepTracks5 = process.detachedTripletStepTracks.clone()
process.detachedTripletStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedTripletStepTracks5.src = cms.InputTag("detachedTripletStepTrackCandidates"+layers)

process.highPtTripletStep5 = process.highPtTripletStep.clone()
process.highPtTripletStep5.src = cms.InputTag("highPtTripletStepTracks"+layers)
process.highPtTripletStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.highPtTripletStepClusters5 = process.highPtTripletStepClusters.clone()
process.highPtTripletStepClusters5.oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+layers)
process.highPtTripletStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters5.trackClassifier = cms.InputTag("lowPtQuadStep"+layers,"QualityMasks")
process.highPtTripletStepClusters5.trajectories = cms.InputTag("lowPtQuadStepTracks"+layers)

process.highPtTripletStepHitDoublets5 = process.highPtTripletStepHitDoublets.clone()
process.highPtTripletStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.highPtTripletStepHitDoublets5.seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+layers)

process.highPtTripletStepHitTriplets5 = process.highPtTripletStepHitTriplets.clone()
process.highPtTripletStepHitTriplets5.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.highPtTripletStepHitTriplets5.doublets = cms.InputTag("highPtTripletStepHitDoublets"+layers)
process.highPtTripletStepHitTriplets5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+layers+'__reRECO')

process.highPtTripletStepSeedLayers5 = process.highPtTripletStepSeedLayers.clone()
process.highPtTripletStepSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers5.BPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers5.FPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)

process.highPtTripletStepSeeds5 = process.highPtTripletStepSeeds.clone()
process.highPtTripletStepSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+layers+'__reRECO')
process.highPtTripletStepSeeds5.seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+layers)

process.highPtTripletStepTrackCandidates5 = process.highPtTripletStepTrackCandidates.clone()
process.highPtTripletStepTrackCandidates5.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_highPtTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidates5.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidates5.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidates5.mkFitSeeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidates5.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.highPtTripletStepTrackCandidates5.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)
process.highPtTripletStepTrackCandidates5.tracks = cms.InputTag("highPtTripletStepTrackCandidatesMkFit"+layers)

process.highPtTripletStepTrackCandidatesMkFit5 = process.highPtTripletStepTrackCandidatesMkFit.clone()
process.highPtTripletStepTrackCandidatesMkFit5.clustersToSkip = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepTrackCandidatesMkFit5.config = cms.ESInputTag("","highPtTripletStepTrackCandidatesMkFitConfig"+layers)
process.highPtTripletStepTrackCandidatesMkFit5.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit5.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidatesMkFit5.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit5.seeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidatesMkFit5.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.highPtTripletStepTrackCandidatesMkFitConfig5 = process.highPtTripletStepTrackCandidatesMkFitConfig.clone()
process.highPtTripletStepTrackCandidatesMkFitConfig5.ComponentName = cms.string('highPtTripletStepTrackCandidatesMkFitConfig'+layers)

process.highPtTripletStepTrackCandidatesMkFitSeeds5 = process.highPtTripletStepTrackCandidatesMkFitSeeds.clone()
process.highPtTripletStepTrackCandidatesMkFitSeeds5.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)

process.highPtTripletStepTracks5 = process.highPtTripletStepTracks.clone()
process.highPtTripletStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.highPtTripletStepTracks5.src = cms.InputTag("highPtTripletStepTrackCandidates"+layers)

process.firstStepPrimaryVertices5 = process.firstStepPrimaryVertices.clone()
process.firstStepPrimaryVertices5.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.firstStepPrimaryVertices5.particles = cms.InputTag("initialStepTrackRefsForJets"+layers)
process.firstStepPrimaryVertices5.vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.firstStepPrimaryVerticesUnsorted5 = process.firstStepPrimaryVerticesUnsorted.clone()
process.firstStepPrimaryVerticesUnsorted5.TrackLabel = cms.InputTag("initialStepTracks"+layers)

process.initialStep5 = process.initialStep.clone()
process.initialStep5.src = cms.InputTag("initialStepTracks"+layers)
process.initialStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepClassifier15 = process.initialStepClassifier1.clone()
process.initialStepClassifier15.src = cms.InputTag("initialStepTracks"+layers)
process.initialStepClassifier15.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepHitDoublets5 = process.initialStepHitDoublets.clone()
process.initialStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.initialStepHitDoublets5.seedingLayers = cms.InputTag("initialStepSeedLayers"+layers)

process.initialStepHitQuadruplets5 = process.initialStepHitQuadruplets.clone()
process.initialStepHitQuadruplets5.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepHitQuadruplets5.doublets = cms.InputTag("initialStepHitDoublets"+layers)
process.initialStepHitQuadruplets5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+layers+'__reRECO')

process.initialStepSeedLayers5 = process.initialStepSeedLayers.clone()
process.initialStepSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.initialStepSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)

process.initialStepSeeds5 = process.initialStepSeeds.clone()
process.initialStepSeeds5.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+layers+'__reRECO')
process.initialStepSeeds5.seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+layers)

process.initialStepTrackCandidates5 = process.initialStepTrackCandidates.clone()
process.initialStepTrackCandidates5.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidates5.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidates5.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidates5.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidates5.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidates5.seeds = cms.InputTag("initialStepSeeds"+layers)
process.initialStepTrackCandidates5.tracks = cms.InputTag("initialStepTrackCandidatesMkFit"+layers)

process.initialStepTrackCandidatesMkFit5 = process.initialStepTrackCandidatesMkFit.clone()
process.initialStepTrackCandidatesMkFit5.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfig"+layers)
process.initialStepTrackCandidatesMkFit5.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidatesMkFit5.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFit5.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidatesMkFit5.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidatesMkFit5.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitConfig5 = process.initialStepTrackCandidatesMkFitConfig.clone()
process.initialStepTrackCandidatesMkFitConfig5.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfig'+layers)

process.initialStepTrackCandidatesMkFitSeeds5 = process.initialStepTrackCandidatesMkFitSeeds.clone()
process.initialStepTrackCandidatesMkFitSeeds5.seeds = cms.InputTag("initialStepSeeds"+layers)

process.initialStepTrackRefsForJets5 = process.initialStepTrackRefsForJets.clone()
process.initialStepTrackRefsForJets5.src = cms.InputTag("initialStepTracks"+layers)

process.initialStepTracks5 = process.initialStepTracks.clone()
process.initialStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.initialStepTracks5.src = cms.InputTag("initialStepTrackCandidates"+layers)

process.mkFitEventOfHits5 = process.mkFitEventOfHits.clone()
process.mkFitEventOfHits5.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHits5.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.mkFitEventOfHits5.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiPixelHits5 = process.mkFitSiPixelHits.clone()
process.mkFitSiPixelHits5.hits = cms.InputTag("siPixelRecHits"+layers)

process.firstStepGoodPrimaryVertices5 = process.firstStepGoodPrimaryVertices.clone()
process.firstStepGoodPrimaryVertices5.src = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStep5 = process.jetCoreRegionalStep.clone()
process.jetCoreRegionalStep5.src = cms.InputTag("jetCoreRegionalStepTracks"+layers)
process.jetCoreRegionalStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStepHitDoublets5 = process.jetCoreRegionalStepHitDoublets.clone()
process.jetCoreRegionalStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.jetCoreRegionalStepHitDoublets5.seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"+layers)
process.jetCoreRegionalStepHitDoublets5.trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"+layers)

process.jetCoreRegionalStepSeedLayers5 = process.jetCoreRegionalStepSeedLayers.clone()
process.jetCoreRegionalStepSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers5.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")

process.jetCoreRegionalStepSeeds5 = process.jetCoreRegionalStepSeeds.clone()
process.jetCoreRegionalStepSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_jetCoreRegionalStepHitDoublets'+layers+'__reRECO')
process.jetCoreRegionalStepSeeds5.seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets"+layers)

process.jetCoreRegionalStepTrackCandidates5 = process.jetCoreRegionalStepTrackCandidates.clone()
process.jetCoreRegionalStepTrackCandidates5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackCandidates5.src = cms.InputTag("jetCoreRegionalStepSeeds"+layers)

process.jetCoreRegionalStepTrackingRegions5 = process.jetCoreRegionalStepTrackingRegions.clone()
process.jetCoreRegionalStepTrackingRegions5.RegionPSet.JetSrc = cms.InputTag("jetsForCoreTracking"+layers)
process.jetCoreRegionalStepTrackingRegions5.RegionPSet.measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackingRegions5.RegionPSet.vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices"+layers)

process.jetCoreRegionalStepTracks5 = process.jetCoreRegionalStepTracks.clone()
process.jetCoreRegionalStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTracks5.src = cms.InputTag("jetCoreRegionalStepTrackCandidates"+layers)

process.jetsForCoreTracking5 = process.jetsForCoreTracking.clone()
process.jetsForCoreTracking5.src = cms.InputTag("ak4CaloJetsForTrk"+layers)

process.lowPtQuadStep5 = process.lowPtQuadStep.clone()
process.lowPtQuadStep5.src = cms.InputTag("lowPtQuadStepTracks"+layers)
process.lowPtQuadStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtQuadStepClusters5 = process.lowPtQuadStepClusters.clone()
process.lowPtQuadStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters5.trackClassifier = cms.InputTag("initialStep"+layers,"QualityMasks")
process.lowPtQuadStepClusters5.trajectories = cms.InputTag("initialStepTracks"+layers)

process.lowPtQuadStepHitDoublets5 = process.lowPtQuadStepHitDoublets.clone()
process.lowPtQuadStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtQuadStepHitDoublets5.seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+layers)

process.lowPtQuadStepHitQuadruplets5 = process.lowPtQuadStepHitQuadruplets.clone()
process.lowPtQuadStepHitQuadruplets5.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtQuadStepHitQuadruplets5.doublets = cms.InputTag("lowPtQuadStepHitDoublets"+layers)
process.lowPtQuadStepHitQuadruplets5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+layers+'__reRECO')

process.lowPtQuadStepSeedLayers5 = process.lowPtQuadStepSeedLayers.clone()
process.lowPtQuadStepSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers5.BPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers5.FPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)

process.lowPtQuadStepSeeds5 = process.lowPtQuadStepSeeds.clone()
process.lowPtQuadStepSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+layers+'__reRECO')
process.lowPtQuadStepSeeds5.seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+layers)

process.lowPtQuadStepTrackCandidates5 = process.lowPtQuadStepTrackCandidates.clone()
process.lowPtQuadStepTrackCandidates5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTrackCandidates5.clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepTrackCandidates5.src = cms.InputTag("lowPtQuadStepSeeds"+layers)

process.lowPtQuadStepTracks5 = process.lowPtQuadStepTracks.clone()
process.lowPtQuadStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTracks5.src = cms.InputTag("lowPtQuadStepTrackCandidates"+layers)

process.lowPtTripletStep5 = process.lowPtTripletStep.clone()
process.lowPtTripletStep5.src = cms.InputTag("lowPtTripletStepTracks"+layers)
process.lowPtTripletStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtTripletStepClusters5 = process.lowPtTripletStepClusters.clone()
process.lowPtTripletStepClusters5.oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+layers)
process.lowPtTripletStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters5.trackClassifier = cms.InputTag("highPtTripletStep"+layers,"QualityMasks")
process.lowPtTripletStepClusters5.trajectories = cms.InputTag("highPtTripletStepTracks"+layers)

process.lowPtTripletStepHitDoublets5 = process.lowPtTripletStepHitDoublets.clone()
process.lowPtTripletStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtTripletStepHitDoublets5.seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+layers)

process.lowPtTripletStepHitTriplets5 = process.lowPtTripletStepHitTriplets.clone()
process.lowPtTripletStepHitTriplets5.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtTripletStepHitTriplets5.doublets = cms.InputTag("lowPtTripletStepHitDoublets"+layers)
process.lowPtTripletStepHitTriplets5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+layers+'__reRECO')

process.lowPtTripletStepSeedLayers5 = process.lowPtTripletStepSeedLayers.clone()
process.lowPtTripletStepSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers5.BPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers5.FPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)

process.lowPtTripletStepSeeds5 = process.lowPtTripletStepSeeds.clone()
process.lowPtTripletStepSeeds5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+layers+'__reRECO')
process.lowPtTripletStepSeeds5.seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+layers)

process.lowPtTripletStepTrackCandidates5 = process.lowPtTripletStepTrackCandidates.clone()
process.lowPtTripletStepTrackCandidates5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTrackCandidates5.clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepTrackCandidates5.src = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.lowPtTripletStepTracks5 = process.lowPtTripletStepTracks.clone()
process.lowPtTripletStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTracks5.src = cms.InputTag("lowPtTripletStepTrackCandidates"+layers)

process.chargeCut2069Clusters5 = process.chargeCut2069Clusters.clone()
process.chargeCut2069Clusters5.oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+layers)
process.chargeCut2069Clusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.chargeCut2069Clusters5.stripClusters = cms.InputTag("rCluster"+layers)

process.mixedTripletStep5 = process.mixedTripletStep.clone()
process.mixedTripletStep5.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier15 = process.mixedTripletStepClassifier1.clone()
process.mixedTripletStepClassifier15.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier15.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier25 = process.mixedTripletStepClassifier2.clone()
process.mixedTripletStepClassifier25.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier25.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClusters5 = process.mixedTripletStepClusters.clone()
process.mixedTripletStepClusters5.oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+layers)
process.mixedTripletStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters5.trackClassifier = cms.InputTag("pixelPairStep"+layers,"QualityMasks")
process.mixedTripletStepClusters5.trajectories = cms.InputTag("pixelPairStepTracks"+layers)

process.mixedTripletStepHitDoubletsA5 = process.mixedTripletStepHitDoubletsA.clone()
process.mixedTripletStepHitDoubletsA5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsA5.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+layers)

process.mixedTripletStepHitDoubletsB5 = process.mixedTripletStepHitDoubletsB.clone()
process.mixedTripletStepHitDoubletsB5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsB5.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+layers)

process.mixedTripletStepHitTripletsA5 = process.mixedTripletStepHitTripletsA.clone()
process.mixedTripletStepHitTripletsA5.doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+layers)
process.mixedTripletStepHitTripletsA5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO')

process.mixedTripletStepHitTripletsB5 = process.mixedTripletStepHitTripletsB.clone()
process.mixedTripletStepHitTripletsB5.doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+layers)
process.mixedTripletStepHitTripletsB5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO')

process.mixedTripletStepSeedLayersA5 = process.mixedTripletStepSeedLayersA.clone()
process.mixedTripletStepSeedLayersA5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA5.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA5.FPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA5.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersA5.TEC.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeedLayersB5 = process.mixedTripletStepSeedLayersB.clone()
process.mixedTripletStepSeedLayersB5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersB5.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersB5.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersB5.TIB.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeeds5 = process.mixedTripletStepSeeds.clone()
process.mixedTripletStepSeeds5.seedCollections = cms.VInputTag("mixedTripletStepSeedsA"+layers, "mixedTripletStepSeedsB"+layers)

process.mixedTripletStepSeedsA5 = process.mixedTripletStepSeedsA.clone()
process.mixedTripletStepSeedsA5.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsA5.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsA5.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+layers)

process.mixedTripletStepSeedsB5 = process.mixedTripletStepSeedsB.clone()
process.mixedTripletStepSeedsB5.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsB5.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsB5.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+layers)

process.mixedTripletStepTrackCandidates5 = process.mixedTripletStepTrackCandidates.clone()
process.mixedTripletStepTrackCandidates5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTrackCandidates5.clustersToSkip = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepTrackCandidates5.src = cms.InputTag("mixedTripletStepSeeds"+layers)

process.mixedTripletStepTracks5 = process.mixedTripletStepTracks.clone()
process.mixedTripletStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTracks5.src = cms.InputTag("mixedTripletStepTrackCandidates"+layers)

process.pixelLessStep5 = process.pixelLessStep.clone()
process.pixelLessStep5.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier15 = process.pixelLessStepClassifier1.clone()
process.pixelLessStepClassifier15.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier15.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier25 = process.pixelLessStepClassifier2.clone()
process.pixelLessStepClassifier25.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier25.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClusters5 = process.pixelLessStepClusters.clone()
process.pixelLessStepClusters5.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+layers)
process.pixelLessStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters5.trackClassifier = cms.InputTag("mixedTripletStep"+layers,"QualityMasks")
process.pixelLessStepClusters5.trajectories = cms.InputTag("mixedTripletStepTracks"+layers)

process.pixelLessStepHitDoublets5 = process.pixelLessStepHitDoublets.clone()
process.pixelLessStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelLessStepHitDoublets5.seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+layers)

process.pixelLessStepHitTriplets5 = process.pixelLessStepHitTriplets.clone()
process.pixelLessStepHitTriplets5.doublets = cms.InputTag("pixelLessStepHitDoublets"+layers)
process.pixelLessStepHitTriplets5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+layers+'__reRECO')

process.pixelLessStepSeedLayers5 = process.pixelLessStepSeedLayers.clone()
process.pixelLessStepSeedLayers5.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers5.MTEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers5.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers5.MTIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers5.MTID.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers5.MTID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers5.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers5.TEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers5.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers5.TIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers5.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers5.TID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.pixelLessStepSeeds5 = process.pixelLessStepSeeds.clone()
process.pixelLessStepSeeds5.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.pixelLessStepSeeds5.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+layers+'__reRECO'
    )
process.pixelLessStepSeeds5.seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+layers)

process.pixelLessStepTrackCandidates5 = process.pixelLessStepTrackCandidates.clone()
process.pixelLessStepTrackCandidates5.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitOutputWrapper_pixelLessStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidates5.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidates5.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidates5.mkFitSeeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidates5.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.pixelLessStepTrackCandidates5.seeds = cms.InputTag("pixelLessStepSeeds"+layers)
process.pixelLessStepTrackCandidates5.tracks = cms.InputTag("pixelLessStepTrackCandidatesMkFit"+layers)

process.pixelLessStepTrackCandidatesMkFit5 = process.pixelLessStepTrackCandidatesMkFit.clone()
process.pixelLessStepTrackCandidatesMkFit5.clustersToSkip = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepTrackCandidatesMkFit5.config = cms.ESInputTag("","pixelLessStepTrackCandidatesMkFitConfig"+layers)
process.pixelLessStepTrackCandidatesMkFit5.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidatesMkFit5.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidatesMkFit5.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidatesMkFit5.seeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidatesMkFit5.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.pixelLessStepTrackCandidatesMkFitSeeds5 = process.pixelLessStepTrackCandidatesMkFitSeeds.clone()
process.pixelLessStepTrackCandidatesMkFitSeeds5.seeds = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelLessStepTrackCandidatesMkFitConfig5 = process.pixelLessStepTrackCandidatesMkFitConfig.clone()
process.pixelLessStepTrackCandidatesMkFitConfig5.ComponentName = cms.string('pixelLessStepTrackCandidatesMkFitConfig'+layers)

process.pixelLessStepTracks5 = process.pixelLessStepTracks.clone()
process.pixelLessStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelLessStepTracks5.src = cms.InputTag("pixelLessStepTrackCandidates"+layers)

process.pixelPairStep5 = process.pixelPairStep.clone()
process.pixelPairStep5.src = cms.InputTag("pixelPairStepTracks"+layers)
process.pixelPairStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepClusters5 = process.pixelPairStepClusters.clone()
process.pixelPairStepClusters5.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+layers)
process.pixelPairStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters5.trackClassifier = cms.InputTag("detachedTripletStep"+layers,"QualityMasks")
process.pixelPairStepClusters5.trajectories = cms.InputTag("detachedTripletStepTracks"+layers)

process.pixelPairStepHitDoublets5 = process.pixelPairStepHitDoublets.clone()
process.pixelPairStepHitDoublets5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoublets5.seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+layers)
process.pixelPairStepHitDoublets5.trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+layers)

process.pixelPairStepHitDoubletsB5 = process.pixelPairStepHitDoubletsB.clone()
process.pixelPairStepHitDoubletsB5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoubletsB5.trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+layers)

process.pixelPairStepSeedLayers5 = process.pixelPairStepSeedLayers.clone()
process.pixelPairStepSeedLayers5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers5.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepSeedLayers5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers5.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)

process.pixelPairStepSeeds5 = process.pixelPairStepSeeds.clone()
process.pixelPairStepSeeds5.seedCollections = cms.VInputTag("pixelPairStepSeedsA"+layers, "pixelPairStepSeedsB"+layers)

process.pixelPairStepSeedsA5 = process.pixelPairStepSeedsA.clone()
process.pixelPairStepSeedsA5.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsA5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+layers+'__reRECO')
process.pixelPairStepSeedsA5.seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+layers)

process.pixelPairStepSeedsB5 = process.pixelPairStepSeedsB.clone()
process.pixelPairStepSeedsB5.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsB5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+layers+'__reRECO')
process.pixelPairStepSeedsB5.seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+layers)

process.pixelPairStepTrackCandidates5 = process.pixelPairStepTrackCandidates.clone()
process.pixelPairStepTrackCandidates5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTrackCandidates5.clustersToSkip = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackCandidates5.src = cms.InputTag("pixelPairStepSeeds"+layers)

process.pixelPairStepTrackingRegions5 = process.pixelPairStepTrackingRegions.clone()
process.pixelPairStepTrackingRegions5.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairStepTrackingRegions5.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.pixelPairStepTrackingRegionsSeedLayersB5 = process.pixelPairStepTrackingRegionsSeedLayersB.clone()
process.pixelPairStepTrackingRegionsSeedLayersB5.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB5.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB5.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB5.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB5.RegionPSet.vertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepTracks5 = process.pixelPairStepTracks.clone()
process.pixelPairStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTracks5.src = cms.InputTag("pixelPairStepTrackCandidates"+layers)

process.tobTecStep5 = process.tobTecStep.clone()
process.tobTecStep5.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStep5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier15 = process.tobTecStepClassifier1.clone()
process.tobTecStepClassifier15.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier15.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier25 = process.tobTecStepClassifier2.clone()
process.tobTecStepClassifier25.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier25.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClusters5 = process.tobTecStepClusters.clone()
process.tobTecStepClusters5.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.tobTecStepClusters5.pixelClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters5.stripClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters5.trackClassifier = cms.InputTag("pixelLessStep"+layers,"QualityMasks")
process.tobTecStepClusters5.trajectories = cms.InputTag("pixelLessStepTracks"+layers)

process.tobTecStepHitDoubletsPair5 = process.tobTecStepHitDoubletsPair.clone()
process.tobTecStepHitDoubletsPair5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsPair5.seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+layers)

process.tobTecStepHitDoubletsTripl5 = process.tobTecStepHitDoubletsTripl.clone()
process.tobTecStepHitDoubletsTripl5.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsTripl5.seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+layers)

process.tobTecStepHitTripletsTripl5 = process.tobTecStepHitTripletsTripl.clone()
process.tobTecStepHitTripletsTripl5.doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+layers)
process.tobTecStepHitTripletsTripl5.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+layers+'__reRECO')

process.tobTecStepSeedLayersPair5 = process.tobTecStepSeedLayersPair.clone()
process.tobTecStepSeedLayersPair5.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair5.TEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersPair5.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair5.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeedLayersTripl5 = process.tobTecStepSeedLayersTripl.clone()
process.tobTecStepSeedLayersTripl5.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl5.MTEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl5.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl5.MTOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl5.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersTripl5.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeeds5 = process.tobTecStepSeeds.clone()
process.tobTecStepSeeds5.seedCollections = cms.VInputTag("tobTecStepSeedsTripl"+layers, "tobTecStepSeedsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsPair5 = process.tobTecStepSeedsPair.clone()
process.tobTecStepSeedsPair5.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsPair5.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+layers+'__reRECO')
process.tobTecStepSeedsPair5.seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsTripl5 = process.tobTecStepSeedsTripl.clone()
process.tobTecStepSeedsTripl5.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsTripl5.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+layers+'__reRECO'
    )
process.tobTecStepSeedsTripl5.seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+layers)

process.tobTecStepTrackCandidates5 = process.tobTecStepTrackCandidates.clone()
process.tobTecStepTrackCandidates5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTrackCandidates5.clustersToSkip = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepTrackCandidates5.src = cms.InputTag("tobTecStepSeeds"+layers)

process.tobTecStepTracks5 = process.tobTecStepTracks.clone()
process.tobTecStepTracks5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTracks5.src = cms.InputTag("tobTecStepTrackCandidates"+layers)

process.muonSeededTracksOutInClassifier5 = process.muonSeededTracksOutInClassifier.clone()
process.muonSeededTracksOutInClassifier5.src = cms.InputTag("muonSeededTracksOutIn"+layers)
process.muonSeededTracksOutInClassifier5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.muonSeededSeedsInOut5 = process.muonSeededSeedsInOut.clone()
process.muonSeededSeedsInOut5.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesInOut5 = process.muonSeededTrackCandidatesInOut.clone()
process.muonSeededTrackCandidatesInOut5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesInOut5.src = cms.InputTag("muonSeededSeedsInOut"+layers)

process.muonSeededTracksInOut5 = process.muonSeededTracksInOut.clone()
process.muonSeededTracksInOut5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksInOut5.src = cms.InputTag("muonSeededTrackCandidatesInOut"+layers)

process.muonSeededSeedsOutIn5 = process.muonSeededSeedsOutIn.clone()
process.muonSeededSeedsOutIn5.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesOutIn5 = process.muonSeededTrackCandidatesOutIn.clone()
process.muonSeededTrackCandidatesOutIn5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesOutIn5.src = cms.InputTag("muonSeededSeedsOutIn"+layers)

process.muonSeededTracksOutIn5 = process.muonSeededTracksOutIn.clone()
process.muonSeededTracksOutIn5.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksOutIn5.src = cms.InputTag("muonSeededTrackCandidatesOutIn"+layers)

process.muonSeededTracksInOutClassifier5 = process.muonSeededTracksInOutClassifier.clone()
process.muonSeededTracksInOutClassifier5.src = cms.InputTag("muonSeededTracksInOut"+layers)
process.muonSeededTracksInOutClassifier5.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.clusterSummaryProducer5 = process.clusterSummaryProducer.clone()
process.clusterSummaryProducer5.stripClusters = cms.InputTag("rCluster"+layers)

process.siStripMatchedRecHits5 = process.siStripMatchedRecHits.clone()
process.siStripMatchedRecHits5.ClusterProducer = cms.InputTag("rCluster"+layers)

process.reconstruction_trackingOnly_5layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.trackExtrapolator,process.trackExtrapolator5)
process.reconstruction_trackingOnly_5layers.replace(process.generalV0Candidates,process.generalV0Candidates5)
process.reconstruction_trackingOnly_5layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices5)
process.reconstruction_trackingOnly_5layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS5)
process.reconstruction_trackingOnly_5layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting5)
process.reconstruction_trackingOnly_5layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting5)
process.reconstruction_trackingOnly_5layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices5)
process.reconstruction_trackingOnly_5layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk5)
process.reconstruction_trackingOnly_5layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices5)
process.reconstruction_trackingOnly_5layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder5)
process.reconstruction_trackingOnly_5layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator5)
process.reconstruction_trackingOnly_5layers.replace(process.vertexMerger,process.vertexMerger5)
process.reconstruction_trackingOnly_5layers.replace(process.dedxHarmonic2,process.dedxHarmonic25)
process.reconstruction_trackingOnly_5layers.replace(process.dedxHitInfo,process.dedxHitInfo5)
process.reconstruction_trackingOnly_5layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0855)
process.reconstruction_trackingOnly_5layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic25)
process.reconstruction_trackingOnly_5layers.replace(process.dedxTruncated40,process.dedxTruncated405)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask5)
process.reconstruction_trackingOnly_5layers.replace(process.newCombinedSeeds,process.newCombinedSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions5)
process.reconstruction_trackingOnly_5layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask5)
process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets5)
process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.conversionStepTracks,process.conversionStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.trackerClusterCheck,process.trackerClusterCheck5)
process.reconstruction_trackingOnly_5layers.replace(process.convClusters,process.convClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.convLayerPairs,process.convLayerPairs5)
process.reconstruction_trackingOnly_5layers.replace(process.convStepSelector,process.convStepSelector5)
process.reconstruction_trackingOnly_5layers.replace(process.convStepTracks,process.convStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.convTrackCandidates,process.convTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg5)
process.reconstruction_trackingOnly_5layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent5)
process.reconstruction_trackingOnly_5layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits5)
process.reconstruction_trackingOnly_5layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache5)
process.reconstruction_trackingOnly_5layers.replace(process.siPixelClusters,process.siPixelClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.siPixelRecHits,process.siPixelRecHits5)
process.reconstruction_trackingOnly_5layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting5)
process.reconstruction_trackingOnly_5layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier5)
process.reconstruction_trackingOnly_5layers.replace(process.generalTracks,process.generalTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.earlyMuons,process.earlyMuons5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStep,process.detachedQuadStep5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStep,process.detachedTripletStep5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier15)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier25)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStep,process.highPtTripletStep5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices5)
process.reconstruction_trackingOnly_5layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStep,process.initialStep5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepClassifier1,process.initialStepClassifier15)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeeds,process.initialStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets5)
process.reconstruction_trackingOnly_5layers.replace(process.initialStepTracks,process.initialStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits5)
process.reconstruction_trackingOnly_5layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits5)
process.reconstruction_trackingOnly_5layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices5)
process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep5)
process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions5)
process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStep,process.lowPtQuadStep5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStep,process.lowPtTripletStep5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStep,process.mixedTripletStep5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier15)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier25)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStep,process.pixelLessStep5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier15)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier25)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTrackCandidatesMkFitConfig,process.pixelLessStepTrackCandidatesMkFitConfig5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStep,process.pixelPairStep5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB5)
process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStep,process.tobTecStep5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier15)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier25)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepClusters,process.tobTecStepClusters5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates5)
process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepTracks,process.tobTecStepTracks5)
process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier5)
process.reconstruction_trackingOnly_5layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut5)
process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut5)
process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut5)
process.reconstruction_trackingOnly_5layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn5)
process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn5)
process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn5)
process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier5)
process.reconstruction_trackingOnly_5layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer5)
process.reconstruction_trackingOnly_5layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits5)

####################################################################################################

layers = "6"

process.MeasurementTrackerEventPreSplitting6 = process.MeasurementTrackerEventPreSplitting.clone()
process.MeasurementTrackerEventPreSplitting6.stripClusterProducer = cms.string('rCluster'+layers)

process.trackExtrapolator6 = process.trackExtrapolator.clone()
process.trackExtrapolator6.trackSrc = cms.InputTag("generalTracks"+layers)

process.generalV0Candidates6 = process.generalV0Candidates.clone()
process.generalV0Candidates6.trackRecoAlgorithm = cms.InputTag("generalTracks"+layers)
process.generalV0Candidates6.vertices = cms.InputTag("offlinePrimaryVertices"+layers)

process.offlinePrimaryVertices6 = process.offlinePrimaryVertices.clone()
process.offlinePrimaryVertices6.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVertices6.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVertices6.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.offlinePrimaryVerticesWithBS6 = process.offlinePrimaryVerticesWithBS.clone()
process.offlinePrimaryVerticesWithBS6.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVerticesWithBS6.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVerticesWithBS6.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers,"WithBS")

process.trackRefsForJetsBeforeSorting6 = process.trackRefsForJetsBeforeSorting.clone()
process.trackRefsForJetsBeforeSorting6.src = cms.InputTag("trackWithVertexRefSelectorBeforeSorting"+layers)

process.trackWithVertexRefSelectorBeforeSorting6 = process.trackWithVertexRefSelectorBeforeSorting.clone()
process.trackWithVertexRefSelectorBeforeSorting6.src = cms.InputTag("generalTracks"+layers)
process.trackWithVertexRefSelectorBeforeSorting6.vertexTag = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.unsortedOfflinePrimaryVertices6 = process.unsortedOfflinePrimaryVertices.clone()
process.unsortedOfflinePrimaryVertices6.TrackLabel = cms.InputTag("generalTracks"+layers)

process.ak4CaloJetsForTrk6 = process.ak4CaloJetsForTrk.clone()
process.ak4CaloJetsForTrk6.srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.inclusiveSecondaryVertices6 = process.inclusiveSecondaryVertices.clone()
process.inclusiveSecondaryVertices6.secondaryVertices = cms.InputTag("trackVertexArbitrator"+layers)

process.inclusiveVertexFinder6 = process.inclusiveVertexFinder.clone() 
process.inclusiveVertexFinder6.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.inclusiveVertexFinder6.tracks = cms.InputTag("generalTracks"+layers)

process.trackVertexArbitrator6 = process.trackVertexArbitrator.clone() 
process.trackVertexArbitrator6.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.trackVertexArbitrator6.secondaryVertices = cms.InputTag("vertexMerger"+layers)
process.trackVertexArbitrator6.tracks = cms.InputTag("generalTracks"+layers)

process.vertexMerger6 = process.vertexMerger.clone()
process.vertexMerger6.secondaryVertices = cms.InputTag("inclusiveVertexFinder"+layers)

process.dedxHarmonic26 = process.dedxHarmonic2.clone()
process.dedxHarmonic26.tracks = cms.InputTag("generalTracks"+layers)

process.dedxHitInfo6 = process.dedxHitInfo.clone() 
process.dedxHitInfo6.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelAndStripHarmonic2T0856 = process.dedxPixelAndStripHarmonic2T085.clone() 
process.dedxPixelAndStripHarmonic2T0856.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelHarmonic26 = process.dedxPixelHarmonic2.clone() 
process.dedxPixelHarmonic26.tracks = cms.InputTag("generalTracks"+layers)

process.dedxTruncated406 = process.dedxTruncated40.clone()
process.dedxTruncated406.tracks = cms.InputTag("generalTracks"+layers)

process.detachedTripletStepSeedClusterMask6 = process.detachedTripletStepSeedClusterMask.clone() 
process.detachedTripletStepSeedClusterMask6.oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+layers)
process.detachedTripletStepSeedClusterMask6.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask6.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask6.trajectories = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.initialStepSeedClusterMask6 = process.initialStepSeedClusterMask.clone() 
process.initialStepSeedClusterMask6.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.initialStepSeedClusterMask6.pixelClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask6.stripClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask6.trajectories = cms.InputTag("initialStepSeeds"+layers)

process.mixedTripletStepSeedClusterMask6 = process.mixedTripletStepSeedClusterMask.clone() 
process.mixedTripletStepSeedClusterMask6.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+layers)
process.mixedTripletStepSeedClusterMask6.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask6.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask6.trajectories = cms.InputTag("mixedTripletStepSeeds"+layers)

process.newCombinedSeeds6 = process.newCombinedSeeds.clone()
process.newCombinedSeeds6.seedCollections = cms.VInputTag(
        "initialStepSeeds"+layers, "highPtTripletStepSeeds"+layers, "mixedTripletStepSeeds"+layers, "pixelLessStepSeeds"+layers, "tripletElectronSeeds"+layers,
        "pixelPairElectronSeeds"+layers, "stripPairElectronSeeds"+layers, "lowPtTripletStepSeeds"+layers, "lowPtQuadStepSeeds"+layers, "detachedTripletStepSeeds"+layers,
        "detachedQuadStepSeeds"+layers, "pixelPairStepSeeds"+layers
    )

process.pixelLessStepSeedClusterMask6 = process.pixelLessStepSeedClusterMask.clone() 
process.pixelLessStepSeedClusterMask6.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+layers)
process.pixelLessStepSeedClusterMask6.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask6.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask6.trajectories = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelPairElectronHitDoublets6 = process.pixelPairElectronHitDoublets.clone() 
process.pixelPairElectronHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairElectronHitDoublets6.seedingLayers = cms.InputTag("pixelPairElectronSeedLayers"+layers)
process.pixelPairElectronHitDoublets6.trackingRegions = cms.InputTag("pixelPairElectronTrackingRegions"+layers)

process.pixelPairElectronSeedLayers6 = process.pixelPairElectronSeedLayers.clone()
process.pixelPairElectronSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers6.BPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.pixelPairElectronSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers6.FPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.pixelPairElectronSeeds6 = process.pixelPairElectronSeeds.clone()
process.pixelPairElectronSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairElectronHitDoublets'+layers+'__reRECO')
process.pixelPairElectronSeeds6.seedingHitSets = cms.InputTag("pixelPairElectronHitDoublets"+layers)

process.pixelPairElectronTrackingRegions6 = process.pixelPairElectronTrackingRegions.clone() 
process.pixelPairElectronTrackingRegions6.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairElectronTrackingRegions6.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.stripPairElectronHitDoublets6 = process.stripPairElectronHitDoublets.clone() 
process.stripPairElectronHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.stripPairElectronHitDoublets6.seedingLayers = cms.InputTag("stripPairElectronSeedLayers"+layers)

process.stripPairElectronSeedLayers6 = process.stripPairElectronSeedLayers.clone() 
process.stripPairElectronSeedLayers6.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers6.TEC.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers6.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers6.TIB.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers6.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers6.TID.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.stripPairElectronSeeds6 = process.stripPairElectronSeeds.clone() 
process.stripPairElectronSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_stripPairElectronHitDoublets'+layers+'__reRECO')
process.stripPairElectronSeeds6.seedingHitSets = cms.InputTag("stripPairElectronHitDoublets"+layers)

process.tripletElectronClusterMask6 = process.tripletElectronClusterMask.clone()
process.tripletElectronClusterMask6.oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronClusterMask6.pixelClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask6.stripClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask6.trajectories = cms.InputTag("tripletElectronSeeds"+layers)

process.tripletElectronHitDoublets6 = process.tripletElectronHitDoublets.clone() 
process.tripletElectronHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tripletElectronHitDoublets6.seedingLayers = cms.InputTag("tripletElectronSeedLayers"+layers)

process.tripletElectronHitTriplets6 = process.tripletElectronHitTriplets.clone()
process.tripletElectronHitTriplets6.doublets = cms.InputTag("tripletElectronHitDoublets"+layers)
process.tripletElectronHitTriplets6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO')

process.tripletElectronSeedLayers6 = process.tripletElectronSeedLayers.clone()
process.tripletElectronSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers6.BPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers6.FPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)

process.tripletElectronSeeds6 = process.tripletElectronSeeds.clone()
process.tripletElectronSeeds6.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tripletElectronHitTriplets'+layers+'__reRECO',
        'IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO'
    )
process.tripletElectronSeeds6.seedingHitSets = cms.InputTag("tripletElectronHitTriplets"+layers)

process.conversionStepTracks6 = process.conversionStepTracks.clone()
process.conversionStepTracks6.TrackProducers = cms.VInputTag("convStepTracks"+layers)
process.conversionStepTracks6.selectedTrackQuals = cms.VInputTag("convStepSelector"+layers+":convStep"+layers)

process.earlyGeneralTracks6 = process.earlyGeneralTracks.clone()
process.earlyGeneralTracks6.inputClassifiers = cms.vstring(
        'initialStep'+layers,
        'highPtTripletStep'+layers,
        'jetCoreRegionalStep'+layers,
        'lowPtQuadStep'+layers,
        'lowPtTripletStep'+layers,
        'detachedQuadStep'+layers,
        'detachedTripletStep'+layers,
        'pixelPairStep'+layers,
        'mixedTripletStep'+layers,
        'pixelLessStep'+layers,
        'tobTecStep'+layers
    )
process.earlyGeneralTracks6.trackProducers = cms.VInputTag(
        "initialStepTracks"+layers, "highPtTripletStepTracks"+layers, "jetCoreRegionalStepTracks"+layers, "lowPtQuadStepTracks"+layers, "lowPtTripletStepTracks"+layers,
        "detachedQuadStepTracks"+layers, "detachedTripletStepTracks"+layers, "pixelPairStepTracks"+layers, "mixedTripletStepTracks"+layers, "pixelLessStepTracks"+layers,
        "tobTecStepTracks"+layers
    )

process.preDuplicateMergingGeneralTracks6 = process.preDuplicateMergingGeneralTracks.clone()
process.preDuplicateMergingGeneralTracks6.inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+layers,
        'muonSeededTracksInOutClassifier'+layers,
        'muonSeededTracksOutInClassifier'+layers
    )
process.preDuplicateMergingGeneralTracks6.trackProducers = cms.VInputTag("earlyGeneralTracks"+layers, "muonSeededTracksInOut"+layers, "muonSeededTracksOutIn"+layers)

process.trackerClusterCheck6 = process.trackerClusterCheck.clone()
process.trackerClusterCheck6.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.trackerClusterCheck6.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.convClusters6 = process.convClusters.clone()
process.convClusters6.oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"+layers)
process.convClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.convClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.convClusters6.trackClassifier = cms.InputTag("tobTecStep"+layers,"QualityMasks")
process.convClusters6.trajectories = cms.InputTag("tobTecStepTracks"+layers)

process.convLayerPairs6 = process.convLayerPairs.clone()
process.convLayerPairs6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs6.BPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs6.FPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs6.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs6.MTIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs6.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs6.MTOB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs6.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs6.TEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHitUnmatched")
process.convLayerPairs6.TEC.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs6.TEC.stereoRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHitUnmatched")
process.convLayerPairs6.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs6.TIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs6.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs6.TID.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs6.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs6.TOB.skipClusters = cms.InputTag("convClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.convStepSelector6 = process.convStepSelector.clone()
process.convStepSelector6.src = cms.InputTag("convStepTracks"+layers)
#process.convStepSelector6.trackSelectors.name = cms.string('convStep'+layers)
process.convStepSelector6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.convStepTracks6 = process.convStepTracks.clone()
process.convStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convStepTracks6.src = cms.InputTag("convTrackCandidates"+layers)

process.convTrackCandidates6 = process.convTrackCandidates.clone()
process.convTrackCandidates6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convTrackCandidates6.clustersToSkip = cms.InputTag("convClusters"+layers)
process.convTrackCandidates6.src = cms.InputTag("photonConvTrajSeedFromSingleLeg"+layers,"convSeedCandidates")

process.photonConvTrajSeedFromSingleLeg6 = process.photonConvTrajSeedFromSingleLeg.clone()
process.photonConvTrajSeedFromSingleLeg6.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg6.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg6.OrderedHitsFactoryPSet.SeedingLayers = cms.InputTag("convLayerPairs"+layers)
process.photonConvTrajSeedFromSingleLeg6.TrackRefitter = cms.InputTag("generalTracks"+layers)
process.photonConvTrajSeedFromSingleLeg6.primaryVerticesTag = cms.InputTag("firstStepPrimaryVertices"+layers)

process.MeasurementTrackerEvent6 = process.MeasurementTrackerEvent.clone()
process.MeasurementTrackerEvent6.pixelClusterProducer = cms.string('rCluster'+layers)
process.MeasurementTrackerEvent6.stripClusterProducer = cms.string('rCluster'+layers)

process.ak4CaloJetsForTrkPreSplitting6 = process.ak4CaloJetsForTrkPreSplitting.clone()
process.ak4CaloJetsForTrkPreSplitting6.srcPVs = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.firstStepPrimaryVerticesPreSplitting6 = process.firstStepPrimaryVerticesPreSplitting.clone()
process.firstStepPrimaryVerticesPreSplitting6.TrackLabel = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepHitDoubletsPreSplitting6 = process.initialStepHitDoubletsPreSplitting.clone()
process.initialStepHitDoubletsPreSplitting6.clusterCheck = cms.InputTag("trackerClusterCheckPreSplitting"+layers)

process.initialStepHitQuadrupletsPreSplitting6 = process.initialStepHitQuadrupletsPreSplitting.clone()
process.initialStepHitQuadrupletsPreSplitting6.doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"+layers)
process.initialStepHitQuadrupletsPreSplitting6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoubletsPreSplitting'+layers+'__reRECO')

process.initialStepSeedsPreSplitting6 = process.initialStepSeedsPreSplitting.clone()
process.initialStepSeedsPreSplitting6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadrupletsPreSplitting'+layers+'__reRECO')
process.initialStepSeedsPreSplitting6.seedingHitSets = cms.InputTag("initialStepHitQuadrupletsPreSplitting"+layers)

process.initialStepTrackCandidatesMkFitConfigPreSplitting6 = process.initialStepTrackCandidatesMkFitConfigPreSplitting.clone()
process.initialStepTrackCandidatesMkFitConfigPreSplitting6.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfigPreSplitting'+layers)

process.initialStepTrackCandidatesMkFitPreSplitting6 = process.initialStepTrackCandidatesMkFitPreSplitting.clone()
process.initialStepTrackCandidatesMkFitPreSplitting6.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfigPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting6.eventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting6.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFitPreSplitting6.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting6.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitSeedsPreSplitting6 = process.initialStepTrackCandidatesMkFitSeedsPreSplitting.clone()
process.initialStepTrackCandidatesMkFitSeedsPreSplitting6.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)

process.initialStepTrackCandidatesPreSplitting6 = process.initialStepTrackCandidatesPreSplitting.clone()
process.initialStepTrackCandidatesPreSplitting6.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFitPreSplitting'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesPreSplitting6.mkFitEventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting6.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting6.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidatesPreSplitting6.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting6.tracks = cms.InputTag("initialStepTrackCandidatesMkFitPreSplitting"+layers)

process.initialStepTrackRefsForJetsPreSplitting6 = process.initialStepTrackRefsForJetsPreSplitting.clone()
process.initialStepTrackRefsForJetsPreSplitting6.src = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepTracksPreSplitting6 = process.initialStepTracksPreSplitting.clone()
process.initialStepTracksPreSplitting6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"+layers)
process.initialStepTracksPreSplitting6.src = cms.InputTag("initialStepTrackCandidatesPreSplitting"+layers)

process.jetsForCoreTrackingPreSplitting6 = process.jetsForCoreTrackingPreSplitting.clone()
process.jetsForCoreTrackingPreSplitting6.src = cms.InputTag("ak4CaloJetsForTrkPreSplitting"+layers)

process.mkFitEventOfHitsPreSplitting6 = process.mkFitEventOfHitsPreSplitting.clone()
process.mkFitEventOfHitsPreSplitting6.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHitsPreSplitting6.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiStripHits6 = process.mkFitSiStripHits.clone()
process.mkFitSiStripHits6.rphiHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.mkFitSiStripHits6.stereoHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHit")

process.siPixelClusterShapeCache6 = process.siPixelClusterShapeCache.clone()
process.siPixelClusterShapeCache6.src = cms.InputTag("rCluster"+layers)

process.siPixelClusters6 = process.siPixelClusters.clone()
process.siPixelClusters6.cores = cms.InputTag("jetsForCoreTrackingPreSplitting"+layers)
process.siPixelClusters6.vertices = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.siPixelRecHits6 = process.siPixelRecHits.clone()
process.siPixelRecHits6.src = cms.InputTag("rCluster"+layers)

process.trackerClusterCheckPreSplitting6 = process.trackerClusterCheckPreSplitting.clone()
process.trackerClusterCheckPreSplitting6.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.duplicateTrackCandidates6 = process.duplicateTrackCandidates.clone()
process.duplicateTrackCandidates6.source = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.duplicateTrackClassifier6 = process.duplicateTrackClassifier.clone()
process.duplicateTrackClassifier6.src = cms.InputTag("mergedDuplicateTracks"+layers)
process.duplicateTrackClassifier6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.generalTracks6 = process.generalTracks.clone()
process.generalTracks6.candidateComponents = cms.InputTag("duplicateTrackCandidates"+layers,"candidateMap")
process.generalTracks6.candidateSource = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")
process.generalTracks6.mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+layers,"MVAValues")
process.generalTracks6.mergedSource = cms.InputTag("mergedDuplicateTracks"+layers)
process.generalTracks6.originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+layers,"MVAValues")
process.generalTracks6.originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.mergedDuplicateTracks6 = process.mergedDuplicateTracks.clone()
process.mergedDuplicateTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mergedDuplicateTracks6.src = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")

process.earlyMuons6 = process.earlyMuons.clone()
process.earlyMuons6.TrackExtractorPSet.inputTrackCollection = cms.InputTag("generalTracks"+layers)
process.earlyMuons6.inputCollectionLabels = cms.VInputTag("earlyGeneralTracks"+layers, "standAloneMuons:UpdatedAtVtx")
process.earlyMuons6.pvInputTag = cms.InputTag("offlinePrimaryVertices"+layers)

process.detachedQuadStep6 = process.detachedQuadStep.clone()
process.detachedQuadStep6.src = cms.InputTag("detachedQuadStepTracks"+layers)
process.detachedQuadStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedQuadStepClusters6 = process.detachedQuadStepClusters.clone()
process.detachedQuadStepClusters6.oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+layers)
process.detachedQuadStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters6.trackClassifier = cms.InputTag("lowPtTripletStep"+layers,"QualityMasks")
process.detachedQuadStepClusters6.trajectories = cms.InputTag("lowPtTripletStepTracks"+layers)

process.detachedQuadStepHitDoublets6 = process.detachedQuadStepHitDoublets.clone()
process.detachedQuadStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedQuadStepHitDoublets6.seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+layers)

process.detachedQuadStepHitQuadruplets6 = process.detachedQuadStepHitQuadruplets.clone()
process.detachedQuadStepHitQuadruplets6.doublets = cms.InputTag("detachedQuadStepHitDoublets"+layers)
process.detachedQuadStepHitQuadruplets6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+layers+'__reRECO')

process.detachedQuadStepSeedLayers6 = process.detachedQuadStepSeedLayers.clone()
process.detachedQuadStepSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers6.BPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers6.FPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)

process.detachedQuadStepSeeds6 = process.detachedQuadStepSeeds.clone()
process.detachedQuadStepSeeds6.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedQuadStepSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+layers+'__reRECO')
process.detachedQuadStepSeeds6.seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+layers)

process.detachedQuadStepTrackCandidates6 = process.detachedQuadStepTrackCandidates.clone()
process.detachedQuadStepTrackCandidates6.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedQuadStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidates6.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidates6.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidates6.mkFitSeeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidates6.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedQuadStepTrackCandidates6.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)
process.detachedQuadStepTrackCandidates6.tracks = cms.InputTag("detachedQuadStepTrackCandidatesMkFit"+layers)

process.detachedQuadStepTrackCandidatesMkFit6 = process.detachedQuadStepTrackCandidatesMkFit.clone()
process.detachedQuadStepTrackCandidatesMkFit6.clustersToSkip = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepTrackCandidatesMkFit6.config = cms.ESInputTag("","detachedQuadStepTrackCandidatesMkFitConfig"+layers)
process.detachedQuadStepTrackCandidatesMkFit6.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit6.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidatesMkFit6.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit6.seeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidatesMkFit6.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedQuadStepTrackCandidatesMkFitConfig6 = process.detachedQuadStepTrackCandidatesMkFitConfig.clone()
process.detachedQuadStepTrackCandidatesMkFitConfig6.ComponentName = cms.string('detachedQuadStepTrackCandidatesMkFitConfig'+layers)

process.detachedQuadStepTrackCandidatesMkFitSeeds6 = process.detachedQuadStepTrackCandidatesMkFitSeeds.clone()
process.detachedQuadStepTrackCandidatesMkFitSeeds6.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)

process.detachedQuadStepTracks6 = process.detachedQuadStepTracks.clone()
process.detachedQuadStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedQuadStepTracks6.src = cms.InputTag("detachedQuadStepTrackCandidates"+layers)

process.detachedTripletStep6 = process.detachedTripletStep.clone()
process.detachedTripletStep6.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier16 = process.detachedTripletStepClassifier1.clone()
process.detachedTripletStepClassifier16.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier16.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier26 = process.detachedTripletStepClassifier2.clone()
process.detachedTripletStepClassifier26.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier26.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClusters6 = process.detachedTripletStepClusters.clone()
process.detachedTripletStepClusters6.oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedTripletStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters6.trackClassifier = cms.InputTag("detachedQuadStep"+layers,"QualityMasks")
process.detachedTripletStepClusters6.trajectories = cms.InputTag("detachedQuadStepTracks"+layers)

process.detachedTripletStepHitDoublets6 = process.detachedTripletStepHitDoublets.clone()
process.detachedTripletStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedTripletStepHitDoublets6.seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+layers)

process.detachedTripletStepHitTriplets6 = process.detachedTripletStepHitTriplets.clone()
process.detachedTripletStepHitTriplets6.doublets = cms.InputTag("detachedTripletStepHitDoublets"+layers)
process.detachedTripletStepHitTriplets6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+layers+'__reRECO')

process.detachedTripletStepSeedLayers6 = process.detachedTripletStepSeedLayers.clone()
process.detachedTripletStepSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers6.BPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers6.FPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)

process.detachedTripletStepSeeds6 = process.detachedTripletStepSeeds.clone()
process.detachedTripletStepSeeds6.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedTripletStepSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+layers+'__reRECO')
process.detachedTripletStepSeeds6.seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+layers)

process.detachedTripletStepTrackCandidates6 = process.detachedTripletStepTrackCandidates.clone()
process.detachedTripletStepTrackCandidates6.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidates6.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidates6.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidates6.mkFitSeeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidates6.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedTripletStepTrackCandidates6.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)
process.detachedTripletStepTrackCandidates6.tracks = cms.InputTag("detachedTripletStepTrackCandidatesMkFit"+layers)

process.detachedTripletStepTrackCandidatesMkFit6 = process.detachedTripletStepTrackCandidatesMkFit.clone()
process.detachedTripletStepTrackCandidatesMkFit6.clustersToSkip = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepTrackCandidatesMkFit6.config = cms.ESInputTag("","detachedTripletStepTrackCandidatesMkFitConfig"+layers)
process.detachedTripletStepTrackCandidatesMkFit6.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit6.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidatesMkFit6.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit6.seeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidatesMkFit6.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedTripletStepTrackCandidatesMkFitConfig6 = process.detachedTripletStepTrackCandidatesMkFitConfig.clone()
process.detachedTripletStepTrackCandidatesMkFitConfig6.ComponentName = cms.string('detachedTripletStepTrackCandidatesMkFitConfig'+layers)

process.detachedTripletStepTrackCandidatesMkFitSeeds6 = process.detachedTripletStepTrackCandidatesMkFitSeeds.clone()
process.detachedTripletStepTrackCandidatesMkFitSeeds6.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)

process.detachedTripletStepTracks6 = process.detachedTripletStepTracks.clone()
process.detachedTripletStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedTripletStepTracks6.src = cms.InputTag("detachedTripletStepTrackCandidates"+layers)

process.highPtTripletStep6 = process.highPtTripletStep.clone()
process.highPtTripletStep6.src = cms.InputTag("highPtTripletStepTracks"+layers)
process.highPtTripletStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.highPtTripletStepClusters6 = process.highPtTripletStepClusters.clone()
process.highPtTripletStepClusters6.oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+layers)
process.highPtTripletStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters6.trackClassifier = cms.InputTag("lowPtQuadStep"+layers,"QualityMasks")
process.highPtTripletStepClusters6.trajectories = cms.InputTag("lowPtQuadStepTracks"+layers)

process.highPtTripletStepHitDoublets6 = process.highPtTripletStepHitDoublets.clone()
process.highPtTripletStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.highPtTripletStepHitDoublets6.seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+layers)

process.highPtTripletStepHitTriplets6 = process.highPtTripletStepHitTriplets.clone()
process.highPtTripletStepHitTriplets6.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.highPtTripletStepHitTriplets6.doublets = cms.InputTag("highPtTripletStepHitDoublets"+layers)
process.highPtTripletStepHitTriplets6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+layers+'__reRECO')

process.highPtTripletStepSeedLayers6 = process.highPtTripletStepSeedLayers.clone()
process.highPtTripletStepSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers6.BPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers6.FPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)

process.highPtTripletStepSeeds6 = process.highPtTripletStepSeeds.clone()
process.highPtTripletStepSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+layers+'__reRECO')
process.highPtTripletStepSeeds6.seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+layers)

process.highPtTripletStepTrackCandidates6 = process.highPtTripletStepTrackCandidates.clone()
process.highPtTripletStepTrackCandidates6.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_highPtTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidates6.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidates6.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidates6.mkFitSeeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidates6.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.highPtTripletStepTrackCandidates6.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)
process.highPtTripletStepTrackCandidates6.tracks = cms.InputTag("highPtTripletStepTrackCandidatesMkFit"+layers)

process.highPtTripletStepTrackCandidatesMkFit6 = process.highPtTripletStepTrackCandidatesMkFit.clone()
process.highPtTripletStepTrackCandidatesMkFit6.clustersToSkip = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepTrackCandidatesMkFit6.config = cms.ESInputTag("","highPtTripletStepTrackCandidatesMkFitConfig"+layers)
process.highPtTripletStepTrackCandidatesMkFit6.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit6.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidatesMkFit6.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit6.seeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidatesMkFit6.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.highPtTripletStepTrackCandidatesMkFitConfig6 = process.highPtTripletStepTrackCandidatesMkFitConfig.clone()
process.highPtTripletStepTrackCandidatesMkFitConfig6.ComponentName = cms.string('highPtTripletStepTrackCandidatesMkFitConfig'+layers)

process.highPtTripletStepTrackCandidatesMkFitSeeds6 = process.highPtTripletStepTrackCandidatesMkFitSeeds.clone()
process.highPtTripletStepTrackCandidatesMkFitSeeds6.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)

process.highPtTripletStepTracks6 = process.highPtTripletStepTracks.clone()
process.highPtTripletStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.highPtTripletStepTracks6.src = cms.InputTag("highPtTripletStepTrackCandidates"+layers)

process.firstStepPrimaryVertices6 = process.firstStepPrimaryVertices.clone()
process.firstStepPrimaryVertices6.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.firstStepPrimaryVertices6.particles = cms.InputTag("initialStepTrackRefsForJets"+layers)
process.firstStepPrimaryVertices6.vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.firstStepPrimaryVerticesUnsorted6 = process.firstStepPrimaryVerticesUnsorted.clone()
process.firstStepPrimaryVerticesUnsorted6.TrackLabel = cms.InputTag("initialStepTracks"+layers)

process.initialStep6 = process.initialStep.clone()
process.initialStep6.src = cms.InputTag("initialStepTracks"+layers)
process.initialStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepClassifier16 = process.initialStepClassifier1.clone()
process.initialStepClassifier16.src = cms.InputTag("initialStepTracks"+layers)
process.initialStepClassifier16.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepHitDoublets6 = process.initialStepHitDoublets.clone()
process.initialStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.initialStepHitDoublets6.seedingLayers = cms.InputTag("initialStepSeedLayers"+layers)

process.initialStepHitQuadruplets6 = process.initialStepHitQuadruplets.clone()
process.initialStepHitQuadruplets6.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepHitQuadruplets6.doublets = cms.InputTag("initialStepHitDoublets"+layers)
process.initialStepHitQuadruplets6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+layers+'__reRECO')

process.initialStepSeedLayers6 = process.initialStepSeedLayers.clone()
process.initialStepSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.initialStepSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)

process.initialStepSeeds6 = process.initialStepSeeds.clone()
process.initialStepSeeds6.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+layers+'__reRECO')
process.initialStepSeeds6.seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+layers)

process.initialStepTrackCandidates6 = process.initialStepTrackCandidates.clone()
process.initialStepTrackCandidates6.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidates6.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidates6.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidates6.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidates6.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidates6.seeds = cms.InputTag("initialStepSeeds"+layers)
process.initialStepTrackCandidates6.tracks = cms.InputTag("initialStepTrackCandidatesMkFit"+layers)

process.initialStepTrackCandidatesMkFit6 = process.initialStepTrackCandidatesMkFit.clone()
process.initialStepTrackCandidatesMkFit6.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfig"+layers)
process.initialStepTrackCandidatesMkFit6.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidatesMkFit6.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFit6.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidatesMkFit6.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidatesMkFit6.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitConfig6 = process.initialStepTrackCandidatesMkFitConfig.clone()
process.initialStepTrackCandidatesMkFitConfig6.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfig'+layers)

process.initialStepTrackCandidatesMkFitSeeds6 = process.initialStepTrackCandidatesMkFitSeeds.clone()
process.initialStepTrackCandidatesMkFitSeeds6.seeds = cms.InputTag("initialStepSeeds"+layers)

process.initialStepTrackRefsForJets6 = process.initialStepTrackRefsForJets.clone()
process.initialStepTrackRefsForJets6.src = cms.InputTag("initialStepTracks"+layers)

process.initialStepTracks6 = process.initialStepTracks.clone()
process.initialStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.initialStepTracks6.src = cms.InputTag("initialStepTrackCandidates"+layers)

process.mkFitEventOfHits6 = process.mkFitEventOfHits.clone()
process.mkFitEventOfHits6.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHits6.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.mkFitEventOfHits6.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiPixelHits6 = process.mkFitSiPixelHits.clone()
process.mkFitSiPixelHits6.hits = cms.InputTag("siPixelRecHits"+layers)

process.firstStepGoodPrimaryVertices6 = process.firstStepGoodPrimaryVertices.clone()
process.firstStepGoodPrimaryVertices6.src = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStep6 = process.jetCoreRegionalStep.clone()
process.jetCoreRegionalStep6.src = cms.InputTag("jetCoreRegionalStepTracks"+layers)
process.jetCoreRegionalStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStepHitDoublets6 = process.jetCoreRegionalStepHitDoublets.clone()
process.jetCoreRegionalStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.jetCoreRegionalStepHitDoublets6.seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"+layers)
process.jetCoreRegionalStepHitDoublets6.trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"+layers)

process.jetCoreRegionalStepSeedLayers6 = process.jetCoreRegionalStepSeedLayers.clone()
process.jetCoreRegionalStepSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers6.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")

process.jetCoreRegionalStepSeeds6 = process.jetCoreRegionalStepSeeds.clone()
process.jetCoreRegionalStepSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_jetCoreRegionalStepHitDoublets'+layers+'__reRECO')
process.jetCoreRegionalStepSeeds6.seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets"+layers)

process.jetCoreRegionalStepTrackCandidates6 = process.jetCoreRegionalStepTrackCandidates.clone()
process.jetCoreRegionalStepTrackCandidates6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackCandidates6.src = cms.InputTag("jetCoreRegionalStepSeeds"+layers)

process.jetCoreRegionalStepTrackingRegions6 = process.jetCoreRegionalStepTrackingRegions.clone()
process.jetCoreRegionalStepTrackingRegions6.RegionPSet.JetSrc = cms.InputTag("jetsForCoreTracking"+layers)
process.jetCoreRegionalStepTrackingRegions6.RegionPSet.measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackingRegions6.RegionPSet.vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices"+layers)

process.jetCoreRegionalStepTracks6 = process.jetCoreRegionalStepTracks.clone()
process.jetCoreRegionalStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTracks6.src = cms.InputTag("jetCoreRegionalStepTrackCandidates"+layers)

process.jetsForCoreTracking6 = process.jetsForCoreTracking.clone()
process.jetsForCoreTracking6.src = cms.InputTag("ak4CaloJetsForTrk"+layers)

process.lowPtQuadStep6 = process.lowPtQuadStep.clone()
process.lowPtQuadStep6.src = cms.InputTag("lowPtQuadStepTracks"+layers)
process.lowPtQuadStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtQuadStepClusters6 = process.lowPtQuadStepClusters.clone()
process.lowPtQuadStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters6.trackClassifier = cms.InputTag("initialStep"+layers,"QualityMasks")
process.lowPtQuadStepClusters6.trajectories = cms.InputTag("initialStepTracks"+layers)

process.lowPtQuadStepHitDoublets6 = process.lowPtQuadStepHitDoublets.clone()
process.lowPtQuadStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtQuadStepHitDoublets6.seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+layers)

process.lowPtQuadStepHitQuadruplets6 = process.lowPtQuadStepHitQuadruplets.clone()
process.lowPtQuadStepHitQuadruplets6.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtQuadStepHitQuadruplets6.doublets = cms.InputTag("lowPtQuadStepHitDoublets"+layers)
process.lowPtQuadStepHitQuadruplets6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+layers+'__reRECO')

process.lowPtQuadStepSeedLayers6 = process.lowPtQuadStepSeedLayers.clone()
process.lowPtQuadStepSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers6.BPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers6.FPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)

process.lowPtQuadStepSeeds6 = process.lowPtQuadStepSeeds.clone()
process.lowPtQuadStepSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+layers+'__reRECO')
process.lowPtQuadStepSeeds6.seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+layers)

process.lowPtQuadStepTrackCandidates6 = process.lowPtQuadStepTrackCandidates.clone()
process.lowPtQuadStepTrackCandidates6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTrackCandidates6.clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepTrackCandidates6.src = cms.InputTag("lowPtQuadStepSeeds"+layers)

process.lowPtQuadStepTracks6 = process.lowPtQuadStepTracks.clone()
process.lowPtQuadStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTracks6.src = cms.InputTag("lowPtQuadStepTrackCandidates"+layers)

process.lowPtTripletStep6 = process.lowPtTripletStep.clone()
process.lowPtTripletStep6.src = cms.InputTag("lowPtTripletStepTracks"+layers)
process.lowPtTripletStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtTripletStepClusters6 = process.lowPtTripletStepClusters.clone()
process.lowPtTripletStepClusters6.oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+layers)
process.lowPtTripletStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters6.trackClassifier = cms.InputTag("highPtTripletStep"+layers,"QualityMasks")
process.lowPtTripletStepClusters6.trajectories = cms.InputTag("highPtTripletStepTracks"+layers)

process.lowPtTripletStepHitDoublets6 = process.lowPtTripletStepHitDoublets.clone()
process.lowPtTripletStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtTripletStepHitDoublets6.seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+layers)

process.lowPtTripletStepHitTriplets6 = process.lowPtTripletStepHitTriplets.clone()
process.lowPtTripletStepHitTriplets6.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtTripletStepHitTriplets6.doublets = cms.InputTag("lowPtTripletStepHitDoublets"+layers)
process.lowPtTripletStepHitTriplets6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+layers+'__reRECO')

process.lowPtTripletStepSeedLayers6 = process.lowPtTripletStepSeedLayers.clone()
process.lowPtTripletStepSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers6.BPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers6.FPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)

process.lowPtTripletStepSeeds6 = process.lowPtTripletStepSeeds.clone()
process.lowPtTripletStepSeeds6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+layers+'__reRECO')
process.lowPtTripletStepSeeds6.seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+layers)

process.lowPtTripletStepTrackCandidates6 = process.lowPtTripletStepTrackCandidates.clone()
process.lowPtTripletStepTrackCandidates6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTrackCandidates6.clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepTrackCandidates6.src = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.lowPtTripletStepTracks6 = process.lowPtTripletStepTracks.clone()
process.lowPtTripletStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTracks6.src = cms.InputTag("lowPtTripletStepTrackCandidates"+layers)

process.chargeCut2069Clusters6 = process.chargeCut2069Clusters.clone()
process.chargeCut2069Clusters6.oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+layers)
process.chargeCut2069Clusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.chargeCut2069Clusters6.stripClusters = cms.InputTag("rCluster"+layers)

process.mixedTripletStep6 = process.mixedTripletStep.clone()
process.mixedTripletStep6.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier16 = process.mixedTripletStepClassifier1.clone()
process.mixedTripletStepClassifier16.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier16.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier26 = process.mixedTripletStepClassifier2.clone()
process.mixedTripletStepClassifier26.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier26.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClusters6 = process.mixedTripletStepClusters.clone()
process.mixedTripletStepClusters6.oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+layers)
process.mixedTripletStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters6.trackClassifier = cms.InputTag("pixelPairStep"+layers,"QualityMasks")
process.mixedTripletStepClusters6.trajectories = cms.InputTag("pixelPairStepTracks"+layers)

process.mixedTripletStepHitDoubletsA6 = process.mixedTripletStepHitDoubletsA.clone()
process.mixedTripletStepHitDoubletsA6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsA6.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+layers)

process.mixedTripletStepHitDoubletsB6 = process.mixedTripletStepHitDoubletsB.clone()
process.mixedTripletStepHitDoubletsB6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsB6.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+layers)

process.mixedTripletStepHitTripletsA6 = process.mixedTripletStepHitTripletsA.clone()
process.mixedTripletStepHitTripletsA6.doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+layers)
process.mixedTripletStepHitTripletsA6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO')

process.mixedTripletStepHitTripletsB6 = process.mixedTripletStepHitTripletsB.clone()
process.mixedTripletStepHitTripletsB6.doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+layers)
process.mixedTripletStepHitTripletsB6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO')

process.mixedTripletStepSeedLayersA6 = process.mixedTripletStepSeedLayersA.clone()
process.mixedTripletStepSeedLayersA6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA6.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA6.FPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA6.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersA6.TEC.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeedLayersB6 = process.mixedTripletStepSeedLayersB.clone()
process.mixedTripletStepSeedLayersB6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersB6.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersB6.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersB6.TIB.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeeds6 = process.mixedTripletStepSeeds.clone()
process.mixedTripletStepSeeds6.seedCollections = cms.VInputTag("mixedTripletStepSeedsA"+layers, "mixedTripletStepSeedsB"+layers)

process.mixedTripletStepSeedsA6 = process.mixedTripletStepSeedsA.clone()
process.mixedTripletStepSeedsA6.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsA6.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsA6.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+layers)

process.mixedTripletStepSeedsB6 = process.mixedTripletStepSeedsB.clone()
process.mixedTripletStepSeedsB6.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsB6.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsB6.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+layers)

process.mixedTripletStepTrackCandidates6 = process.mixedTripletStepTrackCandidates.clone()
process.mixedTripletStepTrackCandidates6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTrackCandidates6.clustersToSkip = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepTrackCandidates6.src = cms.InputTag("mixedTripletStepSeeds"+layers)

process.mixedTripletStepTracks6 = process.mixedTripletStepTracks.clone()
process.mixedTripletStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTracks6.src = cms.InputTag("mixedTripletStepTrackCandidates"+layers)

process.pixelLessStep6 = process.pixelLessStep.clone()
process.pixelLessStep6.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier16 = process.pixelLessStepClassifier1.clone()
process.pixelLessStepClassifier16.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier16.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier26 = process.pixelLessStepClassifier2.clone()
process.pixelLessStepClassifier26.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier26.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClusters6 = process.pixelLessStepClusters.clone()
process.pixelLessStepClusters6.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+layers)
process.pixelLessStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters6.trackClassifier = cms.InputTag("mixedTripletStep"+layers,"QualityMasks")
process.pixelLessStepClusters6.trajectories = cms.InputTag("mixedTripletStepTracks"+layers)

process.pixelLessStepHitDoublets6 = process.pixelLessStepHitDoublets.clone()
process.pixelLessStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelLessStepHitDoublets6.seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+layers)

process.pixelLessStepHitTriplets6 = process.pixelLessStepHitTriplets.clone()
process.pixelLessStepHitTriplets6.doublets = cms.InputTag("pixelLessStepHitDoublets"+layers)
process.pixelLessStepHitTriplets6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+layers+'__reRECO')

process.pixelLessStepSeedLayers6 = process.pixelLessStepSeedLayers.clone()
process.pixelLessStepSeedLayers6.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers6.MTEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers6.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers6.MTIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers6.MTID.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers6.MTID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers6.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers6.TEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers6.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers6.TIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers6.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers6.TID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.pixelLessStepSeeds6 = process.pixelLessStepSeeds.clone()
process.pixelLessStepSeeds6.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.pixelLessStepSeeds6.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+layers+'__reRECO'
    )
process.pixelLessStepSeeds6.seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+layers)

process.pixelLessStepTrackCandidates6 = process.pixelLessStepTrackCandidates.clone()
process.pixelLessStepTrackCandidates6.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitOutputWrapper_pixelLessStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidates6.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidates6.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidates6.mkFitSeeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidates6.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.pixelLessStepTrackCandidates6.seeds = cms.InputTag("pixelLessStepSeeds"+layers)
process.pixelLessStepTrackCandidates6.tracks = cms.InputTag("pixelLessStepTrackCandidatesMkFit"+layers)

process.pixelLessStepTrackCandidatesMkFit6 = process.pixelLessStepTrackCandidatesMkFit.clone()
process.pixelLessStepTrackCandidatesMkFit6.clustersToSkip = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepTrackCandidatesMkFit6.config = cms.ESInputTag("","pixelLessStepTrackCandidatesMkFitConfig"+layers)
process.pixelLessStepTrackCandidatesMkFit6.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidatesMkFit6.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidatesMkFit6.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidatesMkFit6.seeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidatesMkFit6.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.pixelLessStepTrackCandidatesMkFitSeeds6 = process.pixelLessStepTrackCandidatesMkFitSeeds.clone()
process.pixelLessStepTrackCandidatesMkFitSeeds6.seeds = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelLessStepTrackCandidatesMkFitConfig6 = process.pixelLessStepTrackCandidatesMkFitConfig.clone()
process.pixelLessStepTrackCandidatesMkFitConfig6.ComponentName = cms.string('pixelLessStepTrackCandidatesMkFitConfig'+layers)

process.pixelLessStepTracks6 = process.pixelLessStepTracks.clone()
process.pixelLessStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelLessStepTracks6.src = cms.InputTag("pixelLessStepTrackCandidates"+layers)

process.pixelPairStep6 = process.pixelPairStep.clone()
process.pixelPairStep6.src = cms.InputTag("pixelPairStepTracks"+layers)
process.pixelPairStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepClusters6 = process.pixelPairStepClusters.clone()
process.pixelPairStepClusters6.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+layers)
process.pixelPairStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters6.trackClassifier = cms.InputTag("detachedTripletStep"+layers,"QualityMasks")
process.pixelPairStepClusters6.trajectories = cms.InputTag("detachedTripletStepTracks"+layers)

process.pixelPairStepHitDoublets6 = process.pixelPairStepHitDoublets.clone()
process.pixelPairStepHitDoublets6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoublets6.seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+layers)
process.pixelPairStepHitDoublets6.trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+layers)

process.pixelPairStepHitDoubletsB6 = process.pixelPairStepHitDoubletsB.clone()
process.pixelPairStepHitDoubletsB6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoubletsB6.trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+layers)

process.pixelPairStepSeedLayers6 = process.pixelPairStepSeedLayers.clone()
process.pixelPairStepSeedLayers6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers6.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepSeedLayers6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers6.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)

process.pixelPairStepSeeds6 = process.pixelPairStepSeeds.clone()
process.pixelPairStepSeeds6.seedCollections = cms.VInputTag("pixelPairStepSeedsA"+layers, "pixelPairStepSeedsB"+layers)

process.pixelPairStepSeedsA6 = process.pixelPairStepSeedsA.clone()
process.pixelPairStepSeedsA6.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsA6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+layers+'__reRECO')
process.pixelPairStepSeedsA6.seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+layers)

process.pixelPairStepSeedsB6 = process.pixelPairStepSeedsB.clone()
process.pixelPairStepSeedsB6.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsB6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+layers+'__reRECO')
process.pixelPairStepSeedsB6.seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+layers)

process.pixelPairStepTrackCandidates6 = process.pixelPairStepTrackCandidates.clone()
process.pixelPairStepTrackCandidates6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTrackCandidates6.clustersToSkip = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackCandidates6.src = cms.InputTag("pixelPairStepSeeds"+layers)

process.pixelPairStepTrackingRegions6 = process.pixelPairStepTrackingRegions.clone()
process.pixelPairStepTrackingRegions6.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairStepTrackingRegions6.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.pixelPairStepTrackingRegionsSeedLayersB6 = process.pixelPairStepTrackingRegionsSeedLayersB.clone()
process.pixelPairStepTrackingRegionsSeedLayersB6.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB6.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB6.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB6.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB6.RegionPSet.vertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepTracks6 = process.pixelPairStepTracks.clone()
process.pixelPairStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTracks6.src = cms.InputTag("pixelPairStepTrackCandidates"+layers)

process.tobTecStep6 = process.tobTecStep.clone()
process.tobTecStep6.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStep6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier16 = process.tobTecStepClassifier1.clone()
process.tobTecStepClassifier16.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier16.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier26 = process.tobTecStepClassifier2.clone()
process.tobTecStepClassifier26.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier26.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClusters6 = process.tobTecStepClusters.clone()
process.tobTecStepClusters6.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.tobTecStepClusters6.pixelClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters6.stripClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters6.trackClassifier = cms.InputTag("pixelLessStep"+layers,"QualityMasks")
process.tobTecStepClusters6.trajectories = cms.InputTag("pixelLessStepTracks"+layers)

process.tobTecStepHitDoubletsPair6 = process.tobTecStepHitDoubletsPair.clone()
process.tobTecStepHitDoubletsPair6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsPair6.seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+layers)

process.tobTecStepHitDoubletsTripl6 = process.tobTecStepHitDoubletsTripl.clone()
process.tobTecStepHitDoubletsTripl6.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsTripl6.seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+layers)

process.tobTecStepHitTripletsTripl6 = process.tobTecStepHitTripletsTripl.clone()
process.tobTecStepHitTripletsTripl6.doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+layers)
process.tobTecStepHitTripletsTripl6.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+layers+'__reRECO')

process.tobTecStepSeedLayersPair6 = process.tobTecStepSeedLayersPair.clone()
process.tobTecStepSeedLayersPair6.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair6.TEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersPair6.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair6.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeedLayersTripl6 = process.tobTecStepSeedLayersTripl.clone()
process.tobTecStepSeedLayersTripl6.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl6.MTEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl6.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl6.MTOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl6.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersTripl6.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeeds6 = process.tobTecStepSeeds.clone()
process.tobTecStepSeeds6.seedCollections = cms.VInputTag("tobTecStepSeedsTripl"+layers, "tobTecStepSeedsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsPair6 = process.tobTecStepSeedsPair.clone()
process.tobTecStepSeedsPair6.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsPair6.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+layers+'__reRECO')
process.tobTecStepSeedsPair6.seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsTripl6 = process.tobTecStepSeedsTripl.clone()
process.tobTecStepSeedsTripl6.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsTripl6.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+layers+'__reRECO'
    )
process.tobTecStepSeedsTripl6.seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+layers)

process.tobTecStepTrackCandidates6 = process.tobTecStepTrackCandidates.clone()
process.tobTecStepTrackCandidates6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTrackCandidates6.clustersToSkip = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepTrackCandidates6.src = cms.InputTag("tobTecStepSeeds"+layers)

process.tobTecStepTracks6 = process.tobTecStepTracks.clone()
process.tobTecStepTracks6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTracks6.src = cms.InputTag("tobTecStepTrackCandidates"+layers)

process.muonSeededTracksOutInClassifier6 = process.muonSeededTracksOutInClassifier.clone()
process.muonSeededTracksOutInClassifier6.src = cms.InputTag("muonSeededTracksOutIn"+layers)
process.muonSeededTracksOutInClassifier6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.muonSeededSeedsInOut6 = process.muonSeededSeedsInOut.clone()
process.muonSeededSeedsInOut6.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesInOut6 = process.muonSeededTrackCandidatesInOut.clone()
process.muonSeededTrackCandidatesInOut6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesInOut6.src = cms.InputTag("muonSeededSeedsInOut"+layers)

process.muonSeededTracksInOut6 = process.muonSeededTracksInOut.clone()
process.muonSeededTracksInOut6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksInOut6.src = cms.InputTag("muonSeededTrackCandidatesInOut"+layers)

process.muonSeededSeedsOutIn6 = process.muonSeededSeedsOutIn.clone()
process.muonSeededSeedsOutIn6.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesOutIn6 = process.muonSeededTrackCandidatesOutIn.clone()
process.muonSeededTrackCandidatesOutIn6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesOutIn6.src = cms.InputTag("muonSeededSeedsOutIn"+layers)

process.muonSeededTracksOutIn6 = process.muonSeededTracksOutIn.clone()
process.muonSeededTracksOutIn6.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksOutIn6.src = cms.InputTag("muonSeededTrackCandidatesOutIn"+layers)

process.muonSeededTracksInOutClassifier6 = process.muonSeededTracksInOutClassifier.clone()
process.muonSeededTracksInOutClassifier6.src = cms.InputTag("muonSeededTracksInOut"+layers)
process.muonSeededTracksInOutClassifier6.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.clusterSummaryProducer6 = process.clusterSummaryProducer.clone()
process.clusterSummaryProducer6.stripClusters = cms.InputTag("rCluster"+layers)

process.siStripMatchedRecHits6 = process.siStripMatchedRecHits.clone()
process.siStripMatchedRecHits6.ClusterProducer = cms.InputTag("rCluster"+layers)

process.reconstruction_trackingOnly_6layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.trackExtrapolator,process.trackExtrapolator6)
process.reconstruction_trackingOnly_6layers.replace(process.generalV0Candidates,process.generalV0Candidates6)
process.reconstruction_trackingOnly_6layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices6)
process.reconstruction_trackingOnly_6layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS6)
process.reconstruction_trackingOnly_6layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting6)
process.reconstruction_trackingOnly_6layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting6)
process.reconstruction_trackingOnly_6layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices6)
process.reconstruction_trackingOnly_6layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk6)
process.reconstruction_trackingOnly_6layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices6)
process.reconstruction_trackingOnly_6layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder6)
process.reconstruction_trackingOnly_6layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator6)
process.reconstruction_trackingOnly_6layers.replace(process.vertexMerger,process.vertexMerger6)
process.reconstruction_trackingOnly_6layers.replace(process.dedxHarmonic2,process.dedxHarmonic26)
process.reconstruction_trackingOnly_6layers.replace(process.dedxHitInfo,process.dedxHitInfo6)
process.reconstruction_trackingOnly_6layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0856)
process.reconstruction_trackingOnly_6layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic26)
process.reconstruction_trackingOnly_6layers.replace(process.dedxTruncated40,process.dedxTruncated406)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask6)
process.reconstruction_trackingOnly_6layers.replace(process.newCombinedSeeds,process.newCombinedSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions6)
process.reconstruction_trackingOnly_6layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask6)
process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets6)
process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.conversionStepTracks,process.conversionStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.trackerClusterCheck,process.trackerClusterCheck6)
process.reconstruction_trackingOnly_6layers.replace(process.convClusters,process.convClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.convLayerPairs,process.convLayerPairs6)
process.reconstruction_trackingOnly_6layers.replace(process.convStepSelector,process.convStepSelector6)
process.reconstruction_trackingOnly_6layers.replace(process.convStepTracks,process.convStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.convTrackCandidates,process.convTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg6)
process.reconstruction_trackingOnly_6layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent6)
process.reconstruction_trackingOnly_6layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits6)
process.reconstruction_trackingOnly_6layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache6)
process.reconstruction_trackingOnly_6layers.replace(process.siPixelClusters,process.siPixelClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.siPixelRecHits,process.siPixelRecHits6)
process.reconstruction_trackingOnly_6layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting6)
process.reconstruction_trackingOnly_6layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier6)
process.reconstruction_trackingOnly_6layers.replace(process.generalTracks,process.generalTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.earlyMuons,process.earlyMuons6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStep,process.detachedQuadStep6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStep,process.detachedTripletStep6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier16)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier26)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStep,process.highPtTripletStep6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices6)
process.reconstruction_trackingOnly_6layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStep,process.initialStep6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepClassifier1,process.initialStepClassifier16)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeeds,process.initialStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets6)
process.reconstruction_trackingOnly_6layers.replace(process.initialStepTracks,process.initialStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits6)
process.reconstruction_trackingOnly_6layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits6)
process.reconstruction_trackingOnly_6layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices6)
process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep6)
process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions6)
process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStep,process.lowPtQuadStep6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStep,process.lowPtTripletStep6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStep,process.mixedTripletStep6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier16)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier26)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStep,process.pixelLessStep6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier16)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier26)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTrackCandidatesMkFitConfig,process.pixelLessStepTrackCandidatesMkFitConfig6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStep,process.pixelPairStep6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB6)
process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStep,process.tobTecStep6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier16)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier26)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepClusters,process.tobTecStepClusters6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates6)
process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepTracks,process.tobTecStepTracks6)
process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier6)
process.reconstruction_trackingOnly_6layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut6)
process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut6)
process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut6)
process.reconstruction_trackingOnly_6layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn6)
process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn6)
process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn6)
process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier6)
process.reconstruction_trackingOnly_6layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer6)
process.reconstruction_trackingOnly_6layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits6)

####################################################################################################

layers = "7"

process.MeasurementTrackerEventPreSplitting7 = process.MeasurementTrackerEventPreSplitting.clone()
process.MeasurementTrackerEventPreSplitting7.stripClusterProducer = cms.string('rCluster'+layers)

process.trackExtrapolator7 = process.trackExtrapolator.clone()
process.trackExtrapolator7.trackSrc = cms.InputTag("generalTracks"+layers)

process.generalV0Candidates7 = process.generalV0Candidates.clone()
process.generalV0Candidates7.trackRecoAlgorithm = cms.InputTag("generalTracks"+layers)
process.generalV0Candidates7.vertices = cms.InputTag("offlinePrimaryVertices"+layers)

process.offlinePrimaryVertices7 = process.offlinePrimaryVertices.clone()
process.offlinePrimaryVertices7.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVertices7.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVertices7.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.offlinePrimaryVerticesWithBS7 = process.offlinePrimaryVerticesWithBS.clone()
process.offlinePrimaryVerticesWithBS7.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVerticesWithBS7.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVerticesWithBS7.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers,"WithBS")

process.trackRefsForJetsBeforeSorting7 = process.trackRefsForJetsBeforeSorting.clone()
process.trackRefsForJetsBeforeSorting7.src = cms.InputTag("trackWithVertexRefSelectorBeforeSorting"+layers)

process.trackWithVertexRefSelectorBeforeSorting7 = process.trackWithVertexRefSelectorBeforeSorting.clone()
process.trackWithVertexRefSelectorBeforeSorting7.src = cms.InputTag("generalTracks"+layers)
process.trackWithVertexRefSelectorBeforeSorting7.vertexTag = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.unsortedOfflinePrimaryVertices7 = process.unsortedOfflinePrimaryVertices.clone()
process.unsortedOfflinePrimaryVertices7.TrackLabel = cms.InputTag("generalTracks"+layers)

process.ak4CaloJetsForTrk7 = process.ak4CaloJetsForTrk.clone()
process.ak4CaloJetsForTrk7.srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.inclusiveSecondaryVertices7 = process.inclusiveSecondaryVertices.clone()
process.inclusiveSecondaryVertices7.secondaryVertices = cms.InputTag("trackVertexArbitrator"+layers)

process.inclusiveVertexFinder7 = process.inclusiveVertexFinder.clone() 
process.inclusiveVertexFinder7.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.inclusiveVertexFinder7.tracks = cms.InputTag("generalTracks"+layers)

process.trackVertexArbitrator7 = process.trackVertexArbitrator.clone() 
process.trackVertexArbitrator7.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.trackVertexArbitrator7.secondaryVertices = cms.InputTag("vertexMerger"+layers)
process.trackVertexArbitrator7.tracks = cms.InputTag("generalTracks"+layers)

process.vertexMerger7 = process.vertexMerger.clone()
process.vertexMerger7.secondaryVertices = cms.InputTag("inclusiveVertexFinder"+layers)

process.dedxHarmonic27 = process.dedxHarmonic2.clone()
process.dedxHarmonic27.tracks = cms.InputTag("generalTracks"+layers)

process.dedxHitInfo7 = process.dedxHitInfo.clone() 
process.dedxHitInfo7.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelAndStripHarmonic2T0857 = process.dedxPixelAndStripHarmonic2T085.clone() 
process.dedxPixelAndStripHarmonic2T0857.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelHarmonic27 = process.dedxPixelHarmonic2.clone() 
process.dedxPixelHarmonic27.tracks = cms.InputTag("generalTracks"+layers)

process.dedxTruncated407 = process.dedxTruncated40.clone()
process.dedxTruncated407.tracks = cms.InputTag("generalTracks"+layers)

process.detachedTripletStepSeedClusterMask7 = process.detachedTripletStepSeedClusterMask.clone() 
process.detachedTripletStepSeedClusterMask7.oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+layers)
process.detachedTripletStepSeedClusterMask7.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask7.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask7.trajectories = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.initialStepSeedClusterMask7 = process.initialStepSeedClusterMask.clone() 
process.initialStepSeedClusterMask7.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.initialStepSeedClusterMask7.pixelClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask7.stripClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask7.trajectories = cms.InputTag("initialStepSeeds"+layers)

process.mixedTripletStepSeedClusterMask7 = process.mixedTripletStepSeedClusterMask.clone() 
process.mixedTripletStepSeedClusterMask7.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+layers)
process.mixedTripletStepSeedClusterMask7.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask7.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask7.trajectories = cms.InputTag("mixedTripletStepSeeds"+layers)

process.newCombinedSeeds7 = process.newCombinedSeeds.clone()
process.newCombinedSeeds7.seedCollections = cms.VInputTag(
        "initialStepSeeds"+layers, "highPtTripletStepSeeds"+layers, "mixedTripletStepSeeds"+layers, "pixelLessStepSeeds"+layers, "tripletElectronSeeds"+layers,
        "pixelPairElectronSeeds"+layers, "stripPairElectronSeeds"+layers, "lowPtTripletStepSeeds"+layers, "lowPtQuadStepSeeds"+layers, "detachedTripletStepSeeds"+layers,
        "detachedQuadStepSeeds"+layers, "pixelPairStepSeeds"+layers
    )

process.pixelLessStepSeedClusterMask7 = process.pixelLessStepSeedClusterMask.clone() 
process.pixelLessStepSeedClusterMask7.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+layers)
process.pixelLessStepSeedClusterMask7.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask7.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask7.trajectories = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelPairElectronHitDoublets7 = process.pixelPairElectronHitDoublets.clone() 
process.pixelPairElectronHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairElectronHitDoublets7.seedingLayers = cms.InputTag("pixelPairElectronSeedLayers"+layers)
process.pixelPairElectronHitDoublets7.trackingRegions = cms.InputTag("pixelPairElectronTrackingRegions"+layers)

process.pixelPairElectronSeedLayers7 = process.pixelPairElectronSeedLayers.clone()
process.pixelPairElectronSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers7.BPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.pixelPairElectronSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers7.FPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.pixelPairElectronSeeds7 = process.pixelPairElectronSeeds.clone()
process.pixelPairElectronSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairElectronHitDoublets'+layers+'__reRECO')
process.pixelPairElectronSeeds7.seedingHitSets = cms.InputTag("pixelPairElectronHitDoublets"+layers)

process.pixelPairElectronTrackingRegions7 = process.pixelPairElectronTrackingRegions.clone() 
process.pixelPairElectronTrackingRegions7.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairElectronTrackingRegions7.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.stripPairElectronHitDoublets7 = process.stripPairElectronHitDoublets.clone() 
process.stripPairElectronHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.stripPairElectronHitDoublets7.seedingLayers = cms.InputTag("stripPairElectronSeedLayers"+layers)

process.stripPairElectronSeedLayers7 = process.stripPairElectronSeedLayers.clone() 
process.stripPairElectronSeedLayers7.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers7.TEC.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers7.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers7.TIB.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers7.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers7.TID.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.stripPairElectronSeeds7 = process.stripPairElectronSeeds.clone() 
process.stripPairElectronSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_stripPairElectronHitDoublets'+layers+'__reRECO')
process.stripPairElectronSeeds7.seedingHitSets = cms.InputTag("stripPairElectronHitDoublets"+layers)

process.tripletElectronClusterMask7 = process.tripletElectronClusterMask.clone()
process.tripletElectronClusterMask7.oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronClusterMask7.pixelClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask7.stripClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask7.trajectories = cms.InputTag("tripletElectronSeeds"+layers)

process.tripletElectronHitDoublets7 = process.tripletElectronHitDoublets.clone() 
process.tripletElectronHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tripletElectronHitDoublets7.seedingLayers = cms.InputTag("tripletElectronSeedLayers"+layers)

process.tripletElectronHitTriplets7 = process.tripletElectronHitTriplets.clone()
process.tripletElectronHitTriplets7.doublets = cms.InputTag("tripletElectronHitDoublets"+layers)
process.tripletElectronHitTriplets7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO')

process.tripletElectronSeedLayers7 = process.tripletElectronSeedLayers.clone()
process.tripletElectronSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers7.BPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers7.FPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)

process.tripletElectronSeeds7 = process.tripletElectronSeeds.clone()
process.tripletElectronSeeds7.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tripletElectronHitTriplets'+layers+'__reRECO',
        'IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO'
    )
process.tripletElectronSeeds7.seedingHitSets = cms.InputTag("tripletElectronHitTriplets"+layers)

process.conversionStepTracks7 = process.conversionStepTracks.clone()
process.conversionStepTracks7.TrackProducers = cms.VInputTag("convStepTracks"+layers)
process.conversionStepTracks7.selectedTrackQuals = cms.VInputTag("convStepSelector"+layers+":convStep"+layers)

process.earlyGeneralTracks7 = process.earlyGeneralTracks.clone()
process.earlyGeneralTracks7.inputClassifiers = cms.vstring(
        'initialStep'+layers,
        'highPtTripletStep'+layers,
        'jetCoreRegionalStep'+layers,
        'lowPtQuadStep'+layers,
        'lowPtTripletStep'+layers,
        'detachedQuadStep'+layers,
        'detachedTripletStep'+layers,
        'pixelPairStep'+layers,
        'mixedTripletStep'+layers,
        'pixelLessStep'+layers,
        'tobTecStep'+layers
    )
process.earlyGeneralTracks7.trackProducers = cms.VInputTag(
        "initialStepTracks"+layers, "highPtTripletStepTracks"+layers, "jetCoreRegionalStepTracks"+layers, "lowPtQuadStepTracks"+layers, "lowPtTripletStepTracks"+layers,
        "detachedQuadStepTracks"+layers, "detachedTripletStepTracks"+layers, "pixelPairStepTracks"+layers, "mixedTripletStepTracks"+layers, "pixelLessStepTracks"+layers,
        "tobTecStepTracks"+layers
    )

process.preDuplicateMergingGeneralTracks7 = process.preDuplicateMergingGeneralTracks.clone()
process.preDuplicateMergingGeneralTracks7.inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+layers,
        'muonSeededTracksInOutClassifier'+layers,
        'muonSeededTracksOutInClassifier'+layers
    )
process.preDuplicateMergingGeneralTracks7.trackProducers = cms.VInputTag("earlyGeneralTracks"+layers, "muonSeededTracksInOut"+layers, "muonSeededTracksOutIn"+layers)

process.trackerClusterCheck7 = process.trackerClusterCheck.clone()
process.trackerClusterCheck7.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.trackerClusterCheck7.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.convClusters7 = process.convClusters.clone()
process.convClusters7.oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"+layers)
process.convClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.convClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.convClusters7.trackClassifier = cms.InputTag("tobTecStep"+layers,"QualityMasks")
process.convClusters7.trajectories = cms.InputTag("tobTecStepTracks"+layers)

process.convLayerPairs7 = process.convLayerPairs.clone()
process.convLayerPairs7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs7.BPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs7.FPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs7.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs7.MTIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs7.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs7.MTOB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs7.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs7.TEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHitUnmatched")
process.convLayerPairs7.TEC.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs7.TEC.stereoRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHitUnmatched")
process.convLayerPairs7.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs7.TIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs7.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs7.TID.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs7.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs7.TOB.skipClusters = cms.InputTag("convClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.convStepSelector7 = process.convStepSelector.clone()
process.convStepSelector7.src = cms.InputTag("convStepTracks"+layers)
#process.convStepSelector7.trackSelectors.name = cms.string('convStep'+layers)
process.convStepSelector7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.convStepTracks7 = process.convStepTracks.clone()
process.convStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convStepTracks7.src = cms.InputTag("convTrackCandidates"+layers)

process.convTrackCandidates7 = process.convTrackCandidates.clone()
process.convTrackCandidates7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convTrackCandidates7.clustersToSkip = cms.InputTag("convClusters"+layers)
process.convTrackCandidates7.src = cms.InputTag("photonConvTrajSeedFromSingleLeg"+layers,"convSeedCandidates")

process.photonConvTrajSeedFromSingleLeg7 = process.photonConvTrajSeedFromSingleLeg.clone()
process.photonConvTrajSeedFromSingleLeg7.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg7.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg7.OrderedHitsFactoryPSet.SeedingLayers = cms.InputTag("convLayerPairs"+layers)
process.photonConvTrajSeedFromSingleLeg7.TrackRefitter = cms.InputTag("generalTracks"+layers)
process.photonConvTrajSeedFromSingleLeg7.primaryVerticesTag = cms.InputTag("firstStepPrimaryVertices"+layers)

process.MeasurementTrackerEvent7 = process.MeasurementTrackerEvent.clone()
process.MeasurementTrackerEvent7.pixelClusterProducer = cms.string('rCluster'+layers)
process.MeasurementTrackerEvent7.stripClusterProducer = cms.string('rCluster'+layers)

process.ak4CaloJetsForTrkPreSplitting7 = process.ak4CaloJetsForTrkPreSplitting.clone()
process.ak4CaloJetsForTrkPreSplitting7.srcPVs = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.firstStepPrimaryVerticesPreSplitting7 = process.firstStepPrimaryVerticesPreSplitting.clone()
process.firstStepPrimaryVerticesPreSplitting7.TrackLabel = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepHitDoubletsPreSplitting7 = process.initialStepHitDoubletsPreSplitting.clone()
process.initialStepHitDoubletsPreSplitting7.clusterCheck = cms.InputTag("trackerClusterCheckPreSplitting"+layers)

process.initialStepHitQuadrupletsPreSplitting7 = process.initialStepHitQuadrupletsPreSplitting.clone()
process.initialStepHitQuadrupletsPreSplitting7.doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"+layers)
process.initialStepHitQuadrupletsPreSplitting7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoubletsPreSplitting'+layers+'__reRECO')

process.initialStepSeedsPreSplitting7 = process.initialStepSeedsPreSplitting.clone()
process.initialStepSeedsPreSplitting7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadrupletsPreSplitting'+layers+'__reRECO')
process.initialStepSeedsPreSplitting7.seedingHitSets = cms.InputTag("initialStepHitQuadrupletsPreSplitting"+layers)

process.initialStepTrackCandidatesMkFitConfigPreSplitting7 = process.initialStepTrackCandidatesMkFitConfigPreSplitting.clone()
process.initialStepTrackCandidatesMkFitConfigPreSplitting7.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfigPreSplitting'+layers)

process.initialStepTrackCandidatesMkFitPreSplitting7 = process.initialStepTrackCandidatesMkFitPreSplitting.clone()
process.initialStepTrackCandidatesMkFitPreSplitting7.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfigPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting7.eventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting7.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFitPreSplitting7.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting7.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitSeedsPreSplitting7 = process.initialStepTrackCandidatesMkFitSeedsPreSplitting.clone()
process.initialStepTrackCandidatesMkFitSeedsPreSplitting7.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)

process.initialStepTrackCandidatesPreSplitting7 = process.initialStepTrackCandidatesPreSplitting.clone()
process.initialStepTrackCandidatesPreSplitting7.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFitPreSplitting'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesPreSplitting7.mkFitEventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting7.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting7.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidatesPreSplitting7.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting7.tracks = cms.InputTag("initialStepTrackCandidatesMkFitPreSplitting"+layers)

process.initialStepTrackRefsForJetsPreSplitting7 = process.initialStepTrackRefsForJetsPreSplitting.clone()
process.initialStepTrackRefsForJetsPreSplitting7.src = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepTracksPreSplitting7 = process.initialStepTracksPreSplitting.clone()
process.initialStepTracksPreSplitting7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"+layers)
process.initialStepTracksPreSplitting7.src = cms.InputTag("initialStepTrackCandidatesPreSplitting"+layers)

process.jetsForCoreTrackingPreSplitting7 = process.jetsForCoreTrackingPreSplitting.clone()
process.jetsForCoreTrackingPreSplitting7.src = cms.InputTag("ak4CaloJetsForTrkPreSplitting"+layers)

process.mkFitEventOfHitsPreSplitting7 = process.mkFitEventOfHitsPreSplitting.clone()
process.mkFitEventOfHitsPreSplitting7.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHitsPreSplitting7.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiStripHits7 = process.mkFitSiStripHits.clone()
process.mkFitSiStripHits7.rphiHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.mkFitSiStripHits7.stereoHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHit")

process.siPixelClusterShapeCache7 = process.siPixelClusterShapeCache.clone()
process.siPixelClusterShapeCache7.src = cms.InputTag("rCluster"+layers)

process.siPixelClusters7 = process.siPixelClusters.clone()
process.siPixelClusters7.cores = cms.InputTag("jetsForCoreTrackingPreSplitting"+layers)
process.siPixelClusters7.vertices = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.siPixelRecHits7 = process.siPixelRecHits.clone()
process.siPixelRecHits7.src = cms.InputTag("rCluster"+layers)

process.trackerClusterCheckPreSplitting7 = process.trackerClusterCheckPreSplitting.clone()
process.trackerClusterCheckPreSplitting7.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.duplicateTrackCandidates7 = process.duplicateTrackCandidates.clone()
process.duplicateTrackCandidates7.source = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.duplicateTrackClassifier7 = process.duplicateTrackClassifier.clone()
process.duplicateTrackClassifier7.src = cms.InputTag("mergedDuplicateTracks"+layers)
process.duplicateTrackClassifier7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.generalTracks7 = process.generalTracks.clone()
process.generalTracks7.candidateComponents = cms.InputTag("duplicateTrackCandidates"+layers,"candidateMap")
process.generalTracks7.candidateSource = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")
process.generalTracks7.mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+layers,"MVAValues")
process.generalTracks7.mergedSource = cms.InputTag("mergedDuplicateTracks"+layers)
process.generalTracks7.originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+layers,"MVAValues")
process.generalTracks7.originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.mergedDuplicateTracks7 = process.mergedDuplicateTracks.clone()
process.mergedDuplicateTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mergedDuplicateTracks7.src = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")

process.earlyMuons7 = process.earlyMuons.clone()
process.earlyMuons7.TrackExtractorPSet.inputTrackCollection = cms.InputTag("generalTracks"+layers)
process.earlyMuons7.inputCollectionLabels = cms.VInputTag("earlyGeneralTracks"+layers, "standAloneMuons:UpdatedAtVtx")
process.earlyMuons7.pvInputTag = cms.InputTag("offlinePrimaryVertices"+layers)

process.detachedQuadStep7 = process.detachedQuadStep.clone()
process.detachedQuadStep7.src = cms.InputTag("detachedQuadStepTracks"+layers)
process.detachedQuadStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedQuadStepClusters7 = process.detachedQuadStepClusters.clone()
process.detachedQuadStepClusters7.oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+layers)
process.detachedQuadStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters7.trackClassifier = cms.InputTag("lowPtTripletStep"+layers,"QualityMasks")
process.detachedQuadStepClusters7.trajectories = cms.InputTag("lowPtTripletStepTracks"+layers)

process.detachedQuadStepHitDoublets7 = process.detachedQuadStepHitDoublets.clone()
process.detachedQuadStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedQuadStepHitDoublets7.seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+layers)

process.detachedQuadStepHitQuadruplets7 = process.detachedQuadStepHitQuadruplets.clone()
process.detachedQuadStepHitQuadruplets7.doublets = cms.InputTag("detachedQuadStepHitDoublets"+layers)
process.detachedQuadStepHitQuadruplets7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+layers+'__reRECO')

process.detachedQuadStepSeedLayers7 = process.detachedQuadStepSeedLayers.clone()
process.detachedQuadStepSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers7.BPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers7.FPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)

process.detachedQuadStepSeeds7 = process.detachedQuadStepSeeds.clone()
process.detachedQuadStepSeeds7.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedQuadStepSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+layers+'__reRECO')
process.detachedQuadStepSeeds7.seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+layers)

process.detachedQuadStepTrackCandidates7 = process.detachedQuadStepTrackCandidates.clone()
process.detachedQuadStepTrackCandidates7.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedQuadStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidates7.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidates7.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidates7.mkFitSeeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidates7.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedQuadStepTrackCandidates7.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)
process.detachedQuadStepTrackCandidates7.tracks = cms.InputTag("detachedQuadStepTrackCandidatesMkFit"+layers)

process.detachedQuadStepTrackCandidatesMkFit7 = process.detachedQuadStepTrackCandidatesMkFit.clone()
process.detachedQuadStepTrackCandidatesMkFit7.clustersToSkip = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepTrackCandidatesMkFit7.config = cms.ESInputTag("","detachedQuadStepTrackCandidatesMkFitConfig"+layers)
process.detachedQuadStepTrackCandidatesMkFit7.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit7.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidatesMkFit7.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit7.seeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidatesMkFit7.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedQuadStepTrackCandidatesMkFitConfig7 = process.detachedQuadStepTrackCandidatesMkFitConfig.clone()
process.detachedQuadStepTrackCandidatesMkFitConfig7.ComponentName = cms.string('detachedQuadStepTrackCandidatesMkFitConfig'+layers)

process.detachedQuadStepTrackCandidatesMkFitSeeds7 = process.detachedQuadStepTrackCandidatesMkFitSeeds.clone()
process.detachedQuadStepTrackCandidatesMkFitSeeds7.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)

process.detachedQuadStepTracks7 = process.detachedQuadStepTracks.clone()
process.detachedQuadStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedQuadStepTracks7.src = cms.InputTag("detachedQuadStepTrackCandidates"+layers)

process.detachedTripletStep7 = process.detachedTripletStep.clone()
process.detachedTripletStep7.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier17 = process.detachedTripletStepClassifier1.clone()
process.detachedTripletStepClassifier17.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier17.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier27 = process.detachedTripletStepClassifier2.clone()
process.detachedTripletStepClassifier27.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier27.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClusters7 = process.detachedTripletStepClusters.clone()
process.detachedTripletStepClusters7.oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedTripletStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters7.trackClassifier = cms.InputTag("detachedQuadStep"+layers,"QualityMasks")
process.detachedTripletStepClusters7.trajectories = cms.InputTag("detachedQuadStepTracks"+layers)

process.detachedTripletStepHitDoublets7 = process.detachedTripletStepHitDoublets.clone()
process.detachedTripletStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedTripletStepHitDoublets7.seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+layers)

process.detachedTripletStepHitTriplets7 = process.detachedTripletStepHitTriplets.clone()
process.detachedTripletStepHitTriplets7.doublets = cms.InputTag("detachedTripletStepHitDoublets"+layers)
process.detachedTripletStepHitTriplets7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+layers+'__reRECO')

process.detachedTripletStepSeedLayers7 = process.detachedTripletStepSeedLayers.clone()
process.detachedTripletStepSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers7.BPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers7.FPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)

process.detachedTripletStepSeeds7 = process.detachedTripletStepSeeds.clone()
process.detachedTripletStepSeeds7.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedTripletStepSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+layers+'__reRECO')
process.detachedTripletStepSeeds7.seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+layers)

process.detachedTripletStepTrackCandidates7 = process.detachedTripletStepTrackCandidates.clone()
process.detachedTripletStepTrackCandidates7.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidates7.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidates7.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidates7.mkFitSeeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidates7.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedTripletStepTrackCandidates7.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)
process.detachedTripletStepTrackCandidates7.tracks = cms.InputTag("detachedTripletStepTrackCandidatesMkFit"+layers)

process.detachedTripletStepTrackCandidatesMkFit7 = process.detachedTripletStepTrackCandidatesMkFit.clone()
process.detachedTripletStepTrackCandidatesMkFit7.clustersToSkip = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepTrackCandidatesMkFit7.config = cms.ESInputTag("","detachedTripletStepTrackCandidatesMkFitConfig"+layers)
process.detachedTripletStepTrackCandidatesMkFit7.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit7.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidatesMkFit7.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit7.seeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidatesMkFit7.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedTripletStepTrackCandidatesMkFitConfig7 = process.detachedTripletStepTrackCandidatesMkFitConfig.clone()
process.detachedTripletStepTrackCandidatesMkFitConfig7.ComponentName = cms.string('detachedTripletStepTrackCandidatesMkFitConfig'+layers)

process.detachedTripletStepTrackCandidatesMkFitSeeds7 = process.detachedTripletStepTrackCandidatesMkFitSeeds.clone()
process.detachedTripletStepTrackCandidatesMkFitSeeds7.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)

process.detachedTripletStepTracks7 = process.detachedTripletStepTracks.clone()
process.detachedTripletStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedTripletStepTracks7.src = cms.InputTag("detachedTripletStepTrackCandidates"+layers)

process.highPtTripletStep7 = process.highPtTripletStep.clone()
process.highPtTripletStep7.src = cms.InputTag("highPtTripletStepTracks"+layers)
process.highPtTripletStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.highPtTripletStepClusters7 = process.highPtTripletStepClusters.clone()
process.highPtTripletStepClusters7.oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+layers)
process.highPtTripletStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters7.trackClassifier = cms.InputTag("lowPtQuadStep"+layers,"QualityMasks")
process.highPtTripletStepClusters7.trajectories = cms.InputTag("lowPtQuadStepTracks"+layers)

process.highPtTripletStepHitDoublets7 = process.highPtTripletStepHitDoublets.clone()
process.highPtTripletStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.highPtTripletStepHitDoublets7.seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+layers)

process.highPtTripletStepHitTriplets7 = process.highPtTripletStepHitTriplets.clone()
process.highPtTripletStepHitTriplets7.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.highPtTripletStepHitTriplets7.doublets = cms.InputTag("highPtTripletStepHitDoublets"+layers)
process.highPtTripletStepHitTriplets7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+layers+'__reRECO')

process.highPtTripletStepSeedLayers7 = process.highPtTripletStepSeedLayers.clone()
process.highPtTripletStepSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers7.BPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers7.FPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)

process.highPtTripletStepSeeds7 = process.highPtTripletStepSeeds.clone()
process.highPtTripletStepSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+layers+'__reRECO')
process.highPtTripletStepSeeds7.seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+layers)

process.highPtTripletStepTrackCandidates7 = process.highPtTripletStepTrackCandidates.clone()
process.highPtTripletStepTrackCandidates7.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_highPtTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidates7.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidates7.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidates7.mkFitSeeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidates7.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.highPtTripletStepTrackCandidates7.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)
process.highPtTripletStepTrackCandidates7.tracks = cms.InputTag("highPtTripletStepTrackCandidatesMkFit"+layers)

process.highPtTripletStepTrackCandidatesMkFit7 = process.highPtTripletStepTrackCandidatesMkFit.clone()
process.highPtTripletStepTrackCandidatesMkFit7.clustersToSkip = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepTrackCandidatesMkFit7.config = cms.ESInputTag("","highPtTripletStepTrackCandidatesMkFitConfig"+layers)
process.highPtTripletStepTrackCandidatesMkFit7.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit7.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidatesMkFit7.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit7.seeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidatesMkFit7.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.highPtTripletStepTrackCandidatesMkFitConfig7 = process.highPtTripletStepTrackCandidatesMkFitConfig.clone()
process.highPtTripletStepTrackCandidatesMkFitConfig7.ComponentName = cms.string('highPtTripletStepTrackCandidatesMkFitConfig'+layers)

process.highPtTripletStepTrackCandidatesMkFitSeeds7 = process.highPtTripletStepTrackCandidatesMkFitSeeds.clone()
process.highPtTripletStepTrackCandidatesMkFitSeeds7.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)

process.highPtTripletStepTracks7 = process.highPtTripletStepTracks.clone()
process.highPtTripletStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.highPtTripletStepTracks7.src = cms.InputTag("highPtTripletStepTrackCandidates"+layers)

process.firstStepPrimaryVertices7 = process.firstStepPrimaryVertices.clone()
process.firstStepPrimaryVertices7.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.firstStepPrimaryVertices7.particles = cms.InputTag("initialStepTrackRefsForJets"+layers)
process.firstStepPrimaryVertices7.vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.firstStepPrimaryVerticesUnsorted7 = process.firstStepPrimaryVerticesUnsorted.clone()
process.firstStepPrimaryVerticesUnsorted7.TrackLabel = cms.InputTag("initialStepTracks"+layers)

process.initialStep7 = process.initialStep.clone()
process.initialStep7.src = cms.InputTag("initialStepTracks"+layers)
process.initialStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepClassifier17 = process.initialStepClassifier1.clone()
process.initialStepClassifier17.src = cms.InputTag("initialStepTracks"+layers)
process.initialStepClassifier17.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepHitDoublets7 = process.initialStepHitDoublets.clone()
process.initialStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.initialStepHitDoublets7.seedingLayers = cms.InputTag("initialStepSeedLayers"+layers)

process.initialStepHitQuadruplets7 = process.initialStepHitQuadruplets.clone()
process.initialStepHitQuadruplets7.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepHitQuadruplets7.doublets = cms.InputTag("initialStepHitDoublets"+layers)
process.initialStepHitQuadruplets7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+layers+'__reRECO')

process.initialStepSeedLayers7 = process.initialStepSeedLayers.clone()
process.initialStepSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.initialStepSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)

process.initialStepSeeds7 = process.initialStepSeeds.clone()
process.initialStepSeeds7.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+layers+'__reRECO')
process.initialStepSeeds7.seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+layers)

process.initialStepTrackCandidates7 = process.initialStepTrackCandidates.clone()
process.initialStepTrackCandidates7.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidates7.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidates7.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidates7.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidates7.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidates7.seeds = cms.InputTag("initialStepSeeds"+layers)
process.initialStepTrackCandidates7.tracks = cms.InputTag("initialStepTrackCandidatesMkFit"+layers)

process.initialStepTrackCandidatesMkFit7 = process.initialStepTrackCandidatesMkFit.clone()
process.initialStepTrackCandidatesMkFit7.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfig"+layers)
process.initialStepTrackCandidatesMkFit7.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidatesMkFit7.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFit7.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidatesMkFit7.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidatesMkFit7.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitConfig7 = process.initialStepTrackCandidatesMkFitConfig.clone()
process.initialStepTrackCandidatesMkFitConfig7.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfig'+layers)

process.initialStepTrackCandidatesMkFitSeeds7 = process.initialStepTrackCandidatesMkFitSeeds.clone()
process.initialStepTrackCandidatesMkFitSeeds7.seeds = cms.InputTag("initialStepSeeds"+layers)

process.initialStepTrackRefsForJets7 = process.initialStepTrackRefsForJets.clone()
process.initialStepTrackRefsForJets7.src = cms.InputTag("initialStepTracks"+layers)

process.initialStepTracks7 = process.initialStepTracks.clone()
process.initialStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.initialStepTracks7.src = cms.InputTag("initialStepTrackCandidates"+layers)

process.mkFitEventOfHits7 = process.mkFitEventOfHits.clone()
process.mkFitEventOfHits7.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHits7.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.mkFitEventOfHits7.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiPixelHits7 = process.mkFitSiPixelHits.clone()
process.mkFitSiPixelHits7.hits = cms.InputTag("siPixelRecHits"+layers)

process.firstStepGoodPrimaryVertices7 = process.firstStepGoodPrimaryVertices.clone()
process.firstStepGoodPrimaryVertices7.src = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStep7 = process.jetCoreRegionalStep.clone()
process.jetCoreRegionalStep7.src = cms.InputTag("jetCoreRegionalStepTracks"+layers)
process.jetCoreRegionalStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStepHitDoublets7 = process.jetCoreRegionalStepHitDoublets.clone()
process.jetCoreRegionalStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.jetCoreRegionalStepHitDoublets7.seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"+layers)
process.jetCoreRegionalStepHitDoublets7.trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"+layers)

process.jetCoreRegionalStepSeedLayers7 = process.jetCoreRegionalStepSeedLayers.clone()
process.jetCoreRegionalStepSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers7.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")

process.jetCoreRegionalStepSeeds7 = process.jetCoreRegionalStepSeeds.clone()
process.jetCoreRegionalStepSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_jetCoreRegionalStepHitDoublets'+layers+'__reRECO')
process.jetCoreRegionalStepSeeds7.seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets"+layers)

process.jetCoreRegionalStepTrackCandidates7 = process.jetCoreRegionalStepTrackCandidates.clone()
process.jetCoreRegionalStepTrackCandidates7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackCandidates7.src = cms.InputTag("jetCoreRegionalStepSeeds"+layers)

process.jetCoreRegionalStepTrackingRegions7 = process.jetCoreRegionalStepTrackingRegions.clone()
process.jetCoreRegionalStepTrackingRegions7.RegionPSet.JetSrc = cms.InputTag("jetsForCoreTracking"+layers)
process.jetCoreRegionalStepTrackingRegions7.RegionPSet.measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackingRegions7.RegionPSet.vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices"+layers)

process.jetCoreRegionalStepTracks7 = process.jetCoreRegionalStepTracks.clone()
process.jetCoreRegionalStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTracks7.src = cms.InputTag("jetCoreRegionalStepTrackCandidates"+layers)

process.jetsForCoreTracking7 = process.jetsForCoreTracking.clone()
process.jetsForCoreTracking7.src = cms.InputTag("ak4CaloJetsForTrk"+layers)

process.lowPtQuadStep7 = process.lowPtQuadStep.clone()
process.lowPtQuadStep7.src = cms.InputTag("lowPtQuadStepTracks"+layers)
process.lowPtQuadStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtQuadStepClusters7 = process.lowPtQuadStepClusters.clone()
process.lowPtQuadStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters7.trackClassifier = cms.InputTag("initialStep"+layers,"QualityMasks")
process.lowPtQuadStepClusters7.trajectories = cms.InputTag("initialStepTracks"+layers)

process.lowPtQuadStepHitDoublets7 = process.lowPtQuadStepHitDoublets.clone()
process.lowPtQuadStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtQuadStepHitDoublets7.seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+layers)

process.lowPtQuadStepHitQuadruplets7 = process.lowPtQuadStepHitQuadruplets.clone()
process.lowPtQuadStepHitQuadruplets7.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtQuadStepHitQuadruplets7.doublets = cms.InputTag("lowPtQuadStepHitDoublets"+layers)
process.lowPtQuadStepHitQuadruplets7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+layers+'__reRECO')

process.lowPtQuadStepSeedLayers7 = process.lowPtQuadStepSeedLayers.clone()
process.lowPtQuadStepSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers7.BPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers7.FPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)

process.lowPtQuadStepSeeds7 = process.lowPtQuadStepSeeds.clone()
process.lowPtQuadStepSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+layers+'__reRECO')
process.lowPtQuadStepSeeds7.seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+layers)

process.lowPtQuadStepTrackCandidates7 = process.lowPtQuadStepTrackCandidates.clone()
process.lowPtQuadStepTrackCandidates7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTrackCandidates7.clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepTrackCandidates7.src = cms.InputTag("lowPtQuadStepSeeds"+layers)

process.lowPtQuadStepTracks7 = process.lowPtQuadStepTracks.clone()
process.lowPtQuadStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTracks7.src = cms.InputTag("lowPtQuadStepTrackCandidates"+layers)

process.lowPtTripletStep7 = process.lowPtTripletStep.clone()
process.lowPtTripletStep7.src = cms.InputTag("lowPtTripletStepTracks"+layers)
process.lowPtTripletStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtTripletStepClusters7 = process.lowPtTripletStepClusters.clone()
process.lowPtTripletStepClusters7.oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+layers)
process.lowPtTripletStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters7.trackClassifier = cms.InputTag("highPtTripletStep"+layers,"QualityMasks")
process.lowPtTripletStepClusters7.trajectories = cms.InputTag("highPtTripletStepTracks"+layers)

process.lowPtTripletStepHitDoublets7 = process.lowPtTripletStepHitDoublets.clone()
process.lowPtTripletStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtTripletStepHitDoublets7.seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+layers)

process.lowPtTripletStepHitTriplets7 = process.lowPtTripletStepHitTriplets.clone()
process.lowPtTripletStepHitTriplets7.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtTripletStepHitTriplets7.doublets = cms.InputTag("lowPtTripletStepHitDoublets"+layers)
process.lowPtTripletStepHitTriplets7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+layers+'__reRECO')

process.lowPtTripletStepSeedLayers7 = process.lowPtTripletStepSeedLayers.clone()
process.lowPtTripletStepSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers7.BPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers7.FPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)

process.lowPtTripletStepSeeds7 = process.lowPtTripletStepSeeds.clone()
process.lowPtTripletStepSeeds7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+layers+'__reRECO')
process.lowPtTripletStepSeeds7.seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+layers)

process.lowPtTripletStepTrackCandidates7 = process.lowPtTripletStepTrackCandidates.clone()
process.lowPtTripletStepTrackCandidates7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTrackCandidates7.clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepTrackCandidates7.src = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.lowPtTripletStepTracks7 = process.lowPtTripletStepTracks.clone()
process.lowPtTripletStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTracks7.src = cms.InputTag("lowPtTripletStepTrackCandidates"+layers)

process.chargeCut2069Clusters7 = process.chargeCut2069Clusters.clone()
process.chargeCut2069Clusters7.oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+layers)
process.chargeCut2069Clusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.chargeCut2069Clusters7.stripClusters = cms.InputTag("rCluster"+layers)

process.mixedTripletStep7 = process.mixedTripletStep.clone()
process.mixedTripletStep7.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier17 = process.mixedTripletStepClassifier1.clone()
process.mixedTripletStepClassifier17.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier17.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier27 = process.mixedTripletStepClassifier2.clone()
process.mixedTripletStepClassifier27.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier27.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClusters7 = process.mixedTripletStepClusters.clone()
process.mixedTripletStepClusters7.oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+layers)
process.mixedTripletStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters7.trackClassifier = cms.InputTag("pixelPairStep"+layers,"QualityMasks")
process.mixedTripletStepClusters7.trajectories = cms.InputTag("pixelPairStepTracks"+layers)

process.mixedTripletStepHitDoubletsA7 = process.mixedTripletStepHitDoubletsA.clone()
process.mixedTripletStepHitDoubletsA7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsA7.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+layers)

process.mixedTripletStepHitDoubletsB7 = process.mixedTripletStepHitDoubletsB.clone()
process.mixedTripletStepHitDoubletsB7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsB7.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+layers)

process.mixedTripletStepHitTripletsA7 = process.mixedTripletStepHitTripletsA.clone()
process.mixedTripletStepHitTripletsA7.doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+layers)
process.mixedTripletStepHitTripletsA7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO')

process.mixedTripletStepHitTripletsB7 = process.mixedTripletStepHitTripletsB.clone()
process.mixedTripletStepHitTripletsB7.doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+layers)
process.mixedTripletStepHitTripletsB7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO')

process.mixedTripletStepSeedLayersA7 = process.mixedTripletStepSeedLayersA.clone()
process.mixedTripletStepSeedLayersA7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA7.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA7.FPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA7.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersA7.TEC.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeedLayersB7 = process.mixedTripletStepSeedLayersB.clone()
process.mixedTripletStepSeedLayersB7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersB7.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersB7.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersB7.TIB.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeeds7 = process.mixedTripletStepSeeds.clone()
process.mixedTripletStepSeeds7.seedCollections = cms.VInputTag("mixedTripletStepSeedsA"+layers, "mixedTripletStepSeedsB"+layers)

process.mixedTripletStepSeedsA7 = process.mixedTripletStepSeedsA.clone()
process.mixedTripletStepSeedsA7.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsA7.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsA7.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+layers)

process.mixedTripletStepSeedsB7 = process.mixedTripletStepSeedsB.clone()
process.mixedTripletStepSeedsB7.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsB7.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsB7.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+layers)

process.mixedTripletStepTrackCandidates7 = process.mixedTripletStepTrackCandidates.clone()
process.mixedTripletStepTrackCandidates7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTrackCandidates7.clustersToSkip = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepTrackCandidates7.src = cms.InputTag("mixedTripletStepSeeds"+layers)

process.mixedTripletStepTracks7 = process.mixedTripletStepTracks.clone()
process.mixedTripletStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTracks7.src = cms.InputTag("mixedTripletStepTrackCandidates"+layers)

process.pixelLessStep7 = process.pixelLessStep.clone()
process.pixelLessStep7.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier17 = process.pixelLessStepClassifier1.clone()
process.pixelLessStepClassifier17.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier17.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier27 = process.pixelLessStepClassifier2.clone()
process.pixelLessStepClassifier27.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier27.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClusters7 = process.pixelLessStepClusters.clone()
process.pixelLessStepClusters7.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+layers)
process.pixelLessStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters7.trackClassifier = cms.InputTag("mixedTripletStep"+layers,"QualityMasks")
process.pixelLessStepClusters7.trajectories = cms.InputTag("mixedTripletStepTracks"+layers)

process.pixelLessStepHitDoublets7 = process.pixelLessStepHitDoublets.clone()
process.pixelLessStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelLessStepHitDoublets7.seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+layers)

process.pixelLessStepHitTriplets7 = process.pixelLessStepHitTriplets.clone()
process.pixelLessStepHitTriplets7.doublets = cms.InputTag("pixelLessStepHitDoublets"+layers)
process.pixelLessStepHitTriplets7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+layers+'__reRECO')

process.pixelLessStepSeedLayers7 = process.pixelLessStepSeedLayers.clone()
process.pixelLessStepSeedLayers7.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers7.MTEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers7.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers7.MTIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers7.MTID.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers7.MTID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers7.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers7.TEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers7.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers7.TIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers7.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers7.TID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.pixelLessStepSeeds7 = process.pixelLessStepSeeds.clone()
process.pixelLessStepSeeds7.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.pixelLessStepSeeds7.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+layers+'__reRECO'
    )
process.pixelLessStepSeeds7.seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+layers)

process.pixelLessStepTrackCandidates7 = process.pixelLessStepTrackCandidates.clone()
process.pixelLessStepTrackCandidates7.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitOutputWrapper_pixelLessStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidates7.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidates7.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidates7.mkFitSeeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidates7.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.pixelLessStepTrackCandidates7.seeds = cms.InputTag("pixelLessStepSeeds"+layers)
process.pixelLessStepTrackCandidates7.tracks = cms.InputTag("pixelLessStepTrackCandidatesMkFit"+layers)

process.pixelLessStepTrackCandidatesMkFit7 = process.pixelLessStepTrackCandidatesMkFit.clone()
process.pixelLessStepTrackCandidatesMkFit7.clustersToSkip = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepTrackCandidatesMkFit7.config = cms.ESInputTag("","pixelLessStepTrackCandidatesMkFitConfig"+layers)
process.pixelLessStepTrackCandidatesMkFit7.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidatesMkFit7.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidatesMkFit7.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidatesMkFit7.seeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidatesMkFit7.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.pixelLessStepTrackCandidatesMkFitSeeds7 = process.pixelLessStepTrackCandidatesMkFitSeeds.clone()
process.pixelLessStepTrackCandidatesMkFitSeeds7.seeds = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelLessStepTrackCandidatesMkFitConfig7 = process.pixelLessStepTrackCandidatesMkFitConfig.clone()
process.pixelLessStepTrackCandidatesMkFitConfig7.ComponentName = cms.string('pixelLessStepTrackCandidatesMkFitConfig'+layers)

process.pixelLessStepTracks7 = process.pixelLessStepTracks.clone()
process.pixelLessStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelLessStepTracks7.src = cms.InputTag("pixelLessStepTrackCandidates"+layers)

process.pixelPairStep7 = process.pixelPairStep.clone()
process.pixelPairStep7.src = cms.InputTag("pixelPairStepTracks"+layers)
process.pixelPairStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepClusters7 = process.pixelPairStepClusters.clone()
process.pixelPairStepClusters7.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+layers)
process.pixelPairStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters7.trackClassifier = cms.InputTag("detachedTripletStep"+layers,"QualityMasks")
process.pixelPairStepClusters7.trajectories = cms.InputTag("detachedTripletStepTracks"+layers)

process.pixelPairStepHitDoublets7 = process.pixelPairStepHitDoublets.clone()
process.pixelPairStepHitDoublets7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoublets7.seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+layers)
process.pixelPairStepHitDoublets7.trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+layers)

process.pixelPairStepHitDoubletsB7 = process.pixelPairStepHitDoubletsB.clone()
process.pixelPairStepHitDoubletsB7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoubletsB7.trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+layers)

process.pixelPairStepSeedLayers7 = process.pixelPairStepSeedLayers.clone()
process.pixelPairStepSeedLayers7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers7.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepSeedLayers7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers7.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)

process.pixelPairStepSeeds7 = process.pixelPairStepSeeds.clone()
process.pixelPairStepSeeds7.seedCollections = cms.VInputTag("pixelPairStepSeedsA"+layers, "pixelPairStepSeedsB"+layers)

process.pixelPairStepSeedsA7 = process.pixelPairStepSeedsA.clone()
process.pixelPairStepSeedsA7.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsA7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+layers+'__reRECO')
process.pixelPairStepSeedsA7.seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+layers)

process.pixelPairStepSeedsB7 = process.pixelPairStepSeedsB.clone()
process.pixelPairStepSeedsB7.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsB7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+layers+'__reRECO')
process.pixelPairStepSeedsB7.seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+layers)

process.pixelPairStepTrackCandidates7 = process.pixelPairStepTrackCandidates.clone()
process.pixelPairStepTrackCandidates7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTrackCandidates7.clustersToSkip = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackCandidates7.src = cms.InputTag("pixelPairStepSeeds"+layers)

process.pixelPairStepTrackingRegions7 = process.pixelPairStepTrackingRegions.clone()
process.pixelPairStepTrackingRegions7.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairStepTrackingRegions7.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.pixelPairStepTrackingRegionsSeedLayersB7 = process.pixelPairStepTrackingRegionsSeedLayersB.clone()
process.pixelPairStepTrackingRegionsSeedLayersB7.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB7.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB7.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB7.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB7.RegionPSet.vertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepTracks7 = process.pixelPairStepTracks.clone()
process.pixelPairStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTracks7.src = cms.InputTag("pixelPairStepTrackCandidates"+layers)

process.tobTecStep7 = process.tobTecStep.clone()
process.tobTecStep7.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStep7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier17 = process.tobTecStepClassifier1.clone()
process.tobTecStepClassifier17.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier17.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier27 = process.tobTecStepClassifier2.clone()
process.tobTecStepClassifier27.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier27.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClusters7 = process.tobTecStepClusters.clone()
process.tobTecStepClusters7.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.tobTecStepClusters7.pixelClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters7.stripClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters7.trackClassifier = cms.InputTag("pixelLessStep"+layers,"QualityMasks")
process.tobTecStepClusters7.trajectories = cms.InputTag("pixelLessStepTracks"+layers)

process.tobTecStepHitDoubletsPair7 = process.tobTecStepHitDoubletsPair.clone()
process.tobTecStepHitDoubletsPair7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsPair7.seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+layers)

process.tobTecStepHitDoubletsTripl7 = process.tobTecStepHitDoubletsTripl.clone()
process.tobTecStepHitDoubletsTripl7.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsTripl7.seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+layers)

process.tobTecStepHitTripletsTripl7 = process.tobTecStepHitTripletsTripl.clone()
process.tobTecStepHitTripletsTripl7.doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+layers)
process.tobTecStepHitTripletsTripl7.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+layers+'__reRECO')

process.tobTecStepSeedLayersPair7 = process.tobTecStepSeedLayersPair.clone()
process.tobTecStepSeedLayersPair7.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair7.TEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersPair7.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair7.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeedLayersTripl7 = process.tobTecStepSeedLayersTripl.clone()
process.tobTecStepSeedLayersTripl7.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl7.MTEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl7.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl7.MTOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl7.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersTripl7.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeeds7 = process.tobTecStepSeeds.clone()
process.tobTecStepSeeds7.seedCollections = cms.VInputTag("tobTecStepSeedsTripl"+layers, "tobTecStepSeedsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsPair7 = process.tobTecStepSeedsPair.clone()
process.tobTecStepSeedsPair7.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsPair7.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+layers+'__reRECO')
process.tobTecStepSeedsPair7.seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsTripl7 = process.tobTecStepSeedsTripl.clone()
process.tobTecStepSeedsTripl7.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsTripl7.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+layers+'__reRECO'
    )
process.tobTecStepSeedsTripl7.seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+layers)

process.tobTecStepTrackCandidates7 = process.tobTecStepTrackCandidates.clone()
process.tobTecStepTrackCandidates7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTrackCandidates7.clustersToSkip = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepTrackCandidates7.src = cms.InputTag("tobTecStepSeeds"+layers)

process.tobTecStepTracks7 = process.tobTecStepTracks.clone()
process.tobTecStepTracks7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTracks7.src = cms.InputTag("tobTecStepTrackCandidates"+layers)

process.muonSeededTracksOutInClassifier7 = process.muonSeededTracksOutInClassifier.clone()
process.muonSeededTracksOutInClassifier7.src = cms.InputTag("muonSeededTracksOutIn"+layers)
process.muonSeededTracksOutInClassifier7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.muonSeededSeedsInOut7 = process.muonSeededSeedsInOut.clone()
process.muonSeededSeedsInOut7.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesInOut7 = process.muonSeededTrackCandidatesInOut.clone()
process.muonSeededTrackCandidatesInOut7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesInOut7.src = cms.InputTag("muonSeededSeedsInOut"+layers)

process.muonSeededTracksInOut7 = process.muonSeededTracksInOut.clone()
process.muonSeededTracksInOut7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksInOut7.src = cms.InputTag("muonSeededTrackCandidatesInOut"+layers)

process.muonSeededSeedsOutIn7 = process.muonSeededSeedsOutIn.clone()
process.muonSeededSeedsOutIn7.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesOutIn7 = process.muonSeededTrackCandidatesOutIn.clone()
process.muonSeededTrackCandidatesOutIn7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesOutIn7.src = cms.InputTag("muonSeededSeedsOutIn"+layers)

process.muonSeededTracksOutIn7 = process.muonSeededTracksOutIn.clone()
process.muonSeededTracksOutIn7.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksOutIn7.src = cms.InputTag("muonSeededTrackCandidatesOutIn"+layers)

process.muonSeededTracksInOutClassifier7 = process.muonSeededTracksInOutClassifier.clone()
process.muonSeededTracksInOutClassifier7.src = cms.InputTag("muonSeededTracksInOut"+layers)
process.muonSeededTracksInOutClassifier7.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.clusterSummaryProducer7 = process.clusterSummaryProducer.clone()
process.clusterSummaryProducer7.stripClusters = cms.InputTag("rCluster"+layers)

process.siStripMatchedRecHits7 = process.siStripMatchedRecHits.clone()
process.siStripMatchedRecHits7.ClusterProducer = cms.InputTag("rCluster"+layers)

process.reconstruction_trackingOnly_7layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.trackExtrapolator,process.trackExtrapolator7)
process.reconstruction_trackingOnly_7layers.replace(process.generalV0Candidates,process.generalV0Candidates7)
process.reconstruction_trackingOnly_7layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices7)
process.reconstruction_trackingOnly_7layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS7)
process.reconstruction_trackingOnly_7layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting7)
process.reconstruction_trackingOnly_7layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting7)
process.reconstruction_trackingOnly_7layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices7)
process.reconstruction_trackingOnly_7layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk7)
process.reconstruction_trackingOnly_7layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices7)
process.reconstruction_trackingOnly_7layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder7)
process.reconstruction_trackingOnly_7layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator7)
process.reconstruction_trackingOnly_7layers.replace(process.vertexMerger,process.vertexMerger7)
process.reconstruction_trackingOnly_7layers.replace(process.dedxHarmonic2,process.dedxHarmonic27)
process.reconstruction_trackingOnly_7layers.replace(process.dedxHitInfo,process.dedxHitInfo7)
process.reconstruction_trackingOnly_7layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0857)
process.reconstruction_trackingOnly_7layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic27)
process.reconstruction_trackingOnly_7layers.replace(process.dedxTruncated40,process.dedxTruncated407)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask7)
process.reconstruction_trackingOnly_7layers.replace(process.newCombinedSeeds,process.newCombinedSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions7)
process.reconstruction_trackingOnly_7layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask7)
process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets7)
process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.conversionStepTracks,process.conversionStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.trackerClusterCheck,process.trackerClusterCheck7)
process.reconstruction_trackingOnly_7layers.replace(process.convClusters,process.convClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.convLayerPairs,process.convLayerPairs7)
process.reconstruction_trackingOnly_7layers.replace(process.convStepSelector,process.convStepSelector7)
process.reconstruction_trackingOnly_7layers.replace(process.convStepTracks,process.convStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.convTrackCandidates,process.convTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg7)
process.reconstruction_trackingOnly_7layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent7)
process.reconstruction_trackingOnly_7layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits7)
process.reconstruction_trackingOnly_7layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache7)
process.reconstruction_trackingOnly_7layers.replace(process.siPixelClusters,process.siPixelClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.siPixelRecHits,process.siPixelRecHits7)
process.reconstruction_trackingOnly_7layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting7)
process.reconstruction_trackingOnly_7layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier7)
process.reconstruction_trackingOnly_7layers.replace(process.generalTracks,process.generalTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.earlyMuons,process.earlyMuons7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStep,process.detachedQuadStep7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStep,process.detachedTripletStep7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier17)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier27)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStep,process.highPtTripletStep7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices7)
process.reconstruction_trackingOnly_7layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStep,process.initialStep7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepClassifier1,process.initialStepClassifier17)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeeds,process.initialStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets7)
process.reconstruction_trackingOnly_7layers.replace(process.initialStepTracks,process.initialStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits7)
process.reconstruction_trackingOnly_7layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits7)
process.reconstruction_trackingOnly_7layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices7)
process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep7)
process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions7)
process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStep,process.lowPtQuadStep7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStep,process.lowPtTripletStep7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStep,process.mixedTripletStep7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier17)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier27)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStep,process.pixelLessStep7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier17)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier27)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTrackCandidatesMkFitConfig,process.pixelLessStepTrackCandidatesMkFitConfig7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStep,process.pixelPairStep7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB7)
process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStep,process.tobTecStep7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier17)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier27)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepClusters,process.tobTecStepClusters7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates7)
process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepTracks,process.tobTecStepTracks7)
process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier7)
process.reconstruction_trackingOnly_7layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut7)
process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut7)
process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut7)
process.reconstruction_trackingOnly_7layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn7)
process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn7)
process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn7)
process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier7)
process.reconstruction_trackingOnly_7layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer7)
process.reconstruction_trackingOnly_7layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits7)

####################################################################################################

layers = "8"

process.MeasurementTrackerEventPreSplitting8 = process.MeasurementTrackerEventPreSplitting.clone()
process.MeasurementTrackerEventPreSplitting8.stripClusterProducer = cms.string('rCluster'+layers)

process.trackExtrapolator8 = process.trackExtrapolator.clone()
process.trackExtrapolator8.trackSrc = cms.InputTag("generalTracks"+layers)

process.generalV0Candidates8 = process.generalV0Candidates.clone()
process.generalV0Candidates8.trackRecoAlgorithm = cms.InputTag("generalTracks"+layers)
process.generalV0Candidates8.vertices = cms.InputTag("offlinePrimaryVertices"+layers)

process.offlinePrimaryVertices8 = process.offlinePrimaryVertices.clone()
process.offlinePrimaryVertices8.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVertices8.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVertices8.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.offlinePrimaryVerticesWithBS8 = process.offlinePrimaryVerticesWithBS.clone()
process.offlinePrimaryVerticesWithBS8.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.offlinePrimaryVerticesWithBS8.particles = cms.InputTag("trackRefsForJetsBeforeSorting"+layers)
process.offlinePrimaryVerticesWithBS8.vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+layers,"WithBS")

process.trackRefsForJetsBeforeSorting8 = process.trackRefsForJetsBeforeSorting.clone()
process.trackRefsForJetsBeforeSorting8.src = cms.InputTag("trackWithVertexRefSelectorBeforeSorting"+layers)

process.trackWithVertexRefSelectorBeforeSorting8 = process.trackWithVertexRefSelectorBeforeSorting.clone()
process.trackWithVertexRefSelectorBeforeSorting8.src = cms.InputTag("generalTracks"+layers)
process.trackWithVertexRefSelectorBeforeSorting8.vertexTag = cms.InputTag("unsortedOfflinePrimaryVertices"+layers)

process.unsortedOfflinePrimaryVertices8 = process.unsortedOfflinePrimaryVertices.clone()
process.unsortedOfflinePrimaryVertices8.TrackLabel = cms.InputTag("generalTracks"+layers)

process.ak4CaloJetsForTrk8 = process.ak4CaloJetsForTrk.clone()
process.ak4CaloJetsForTrk8.srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.inclusiveSecondaryVertices8 = process.inclusiveSecondaryVertices.clone()
process.inclusiveSecondaryVertices8.secondaryVertices = cms.InputTag("trackVertexArbitrator"+layers)

process.inclusiveVertexFinder8 = process.inclusiveVertexFinder.clone() 
process.inclusiveVertexFinder8.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.inclusiveVertexFinder8.tracks = cms.InputTag("generalTracks"+layers)

process.trackVertexArbitrator8 = process.trackVertexArbitrator.clone() 
process.trackVertexArbitrator8.primaryVertices = cms.InputTag("offlinePrimaryVertices"+layers)
process.trackVertexArbitrator8.secondaryVertices = cms.InputTag("vertexMerger"+layers)
process.trackVertexArbitrator8.tracks = cms.InputTag("generalTracks"+layers)

process.vertexMerger8 = process.vertexMerger.clone()
process.vertexMerger8.secondaryVertices = cms.InputTag("inclusiveVertexFinder"+layers)

process.dedxHarmonic28 = process.dedxHarmonic2.clone()
process.dedxHarmonic28.tracks = cms.InputTag("generalTracks"+layers)

process.dedxHitInfo8 = process.dedxHitInfo.clone() 
process.dedxHitInfo8.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelAndStripHarmonic2T0858 = process.dedxPixelAndStripHarmonic2T085.clone() 
process.dedxPixelAndStripHarmonic2T0858.tracks = cms.InputTag("generalTracks"+layers)

process.dedxPixelHarmonic28 = process.dedxPixelHarmonic2.clone() 
process.dedxPixelHarmonic28.tracks = cms.InputTag("generalTracks"+layers)

process.dedxTruncated408 = process.dedxTruncated40.clone()
process.dedxTruncated408.tracks = cms.InputTag("generalTracks"+layers)

process.detachedTripletStepSeedClusterMask8 = process.detachedTripletStepSeedClusterMask.clone() 
process.detachedTripletStepSeedClusterMask8.oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+layers)
process.detachedTripletStepSeedClusterMask8.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask8.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepSeedClusterMask8.trajectories = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.initialStepSeedClusterMask8 = process.initialStepSeedClusterMask.clone() 
process.initialStepSeedClusterMask8.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.initialStepSeedClusterMask8.pixelClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask8.stripClusters = cms.InputTag("rCluster"+layers)
process.initialStepSeedClusterMask8.trajectories = cms.InputTag("initialStepSeeds"+layers)

process.mixedTripletStepSeedClusterMask8 = process.mixedTripletStepSeedClusterMask.clone() 
process.mixedTripletStepSeedClusterMask8.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+layers)
process.mixedTripletStepSeedClusterMask8.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask8.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepSeedClusterMask8.trajectories = cms.InputTag("mixedTripletStepSeeds"+layers)

process.newCombinedSeeds8 = process.newCombinedSeeds.clone()
process.newCombinedSeeds8.seedCollections = cms.VInputTag(
        "initialStepSeeds"+layers, "highPtTripletStepSeeds"+layers, "mixedTripletStepSeeds"+layers, "pixelLessStepSeeds"+layers, "tripletElectronSeeds"+layers,
        "pixelPairElectronSeeds"+layers, "stripPairElectronSeeds"+layers, "lowPtTripletStepSeeds"+layers, "lowPtQuadStepSeeds"+layers, "detachedTripletStepSeeds"+layers,
        "detachedQuadStepSeeds"+layers, "pixelPairStepSeeds"+layers
    )

process.pixelLessStepSeedClusterMask8 = process.pixelLessStepSeedClusterMask.clone() 
process.pixelLessStepSeedClusterMask8.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+layers)
process.pixelLessStepSeedClusterMask8.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask8.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepSeedClusterMask8.trajectories = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelPairElectronHitDoublets8 = process.pixelPairElectronHitDoublets.clone() 
process.pixelPairElectronHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairElectronHitDoublets8.seedingLayers = cms.InputTag("pixelPairElectronSeedLayers"+layers)
process.pixelPairElectronHitDoublets8.trackingRegions = cms.InputTag("pixelPairElectronTrackingRegions"+layers)

process.pixelPairElectronSeedLayers8 = process.pixelPairElectronSeedLayers.clone()
process.pixelPairElectronSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers8.BPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.pixelPairElectronSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairElectronSeedLayers8.FPix.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.pixelPairElectronSeeds8 = process.pixelPairElectronSeeds.clone()
process.pixelPairElectronSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairElectronHitDoublets'+layers+'__reRECO')
process.pixelPairElectronSeeds8.seedingHitSets = cms.InputTag("pixelPairElectronHitDoublets"+layers)

process.pixelPairElectronTrackingRegions8 = process.pixelPairElectronTrackingRegions.clone() 
process.pixelPairElectronTrackingRegions8.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairElectronTrackingRegions8.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.stripPairElectronHitDoublets8 = process.stripPairElectronHitDoublets.clone() 
process.stripPairElectronHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.stripPairElectronHitDoublets8.seedingLayers = cms.InputTag("stripPairElectronSeedLayers"+layers)

process.stripPairElectronSeedLayers8 = process.stripPairElectronSeedLayers.clone() 
process.stripPairElectronSeedLayers8.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers8.TEC.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers8.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers8.TIB.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)
process.stripPairElectronSeedLayers8.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.stripPairElectronSeedLayers8.TID.skipClusters = cms.InputTag("tripletElectronClusterMask"+layers)

process.stripPairElectronSeeds8 = process.stripPairElectronSeeds.clone() 
process.stripPairElectronSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_stripPairElectronHitDoublets'+layers+'__reRECO')
process.stripPairElectronSeeds8.seedingHitSets = cms.InputTag("stripPairElectronHitDoublets"+layers)

process.tripletElectronClusterMask8 = process.tripletElectronClusterMask.clone()
process.tripletElectronClusterMask8.oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronClusterMask8.pixelClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask8.stripClusters = cms.InputTag("rCluster"+layers)
process.tripletElectronClusterMask8.trajectories = cms.InputTag("tripletElectronSeeds"+layers)

process.tripletElectronHitDoublets8 = process.tripletElectronHitDoublets.clone() 
process.tripletElectronHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tripletElectronHitDoublets8.seedingLayers = cms.InputTag("tripletElectronSeedLayers"+layers)

process.tripletElectronHitTriplets8 = process.tripletElectronHitTriplets.clone()
process.tripletElectronHitTriplets8.doublets = cms.InputTag("tripletElectronHitDoublets"+layers)
process.tripletElectronHitTriplets8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO')

process.tripletElectronSeedLayers8 = process.tripletElectronSeedLayers.clone()
process.tripletElectronSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers8.BPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)
process.tripletElectronSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.tripletElectronSeedLayers8.FPix.skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+layers)

process.tripletElectronSeeds8 = process.tripletElectronSeeds.clone()
process.tripletElectronSeeds8.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tripletElectronHitTriplets'+layers+'__reRECO',
        'IntermediateHitDoublets_tripletElectronHitDoublets'+layers+'__reRECO'
    )
process.tripletElectronSeeds8.seedingHitSets = cms.InputTag("tripletElectronHitTriplets"+layers)

process.conversionStepTracks8 = process.conversionStepTracks.clone()
process.conversionStepTracks8.TrackProducers = cms.VInputTag("convStepTracks"+layers)
process.conversionStepTracks8.selectedTrackQuals = cms.VInputTag("convStepSelector"+layers+":convStep"+layers)

process.earlyGeneralTracks8 = process.earlyGeneralTracks.clone()
process.earlyGeneralTracks8.inputClassifiers = cms.vstring(
        'initialStep'+layers,
        'highPtTripletStep'+layers,
        'jetCoreRegionalStep'+layers,
        'lowPtQuadStep'+layers,
        'lowPtTripletStep'+layers,
        'detachedQuadStep'+layers,
        'detachedTripletStep'+layers,
        'pixelPairStep'+layers,
        'mixedTripletStep'+layers,
        'pixelLessStep'+layers,
        'tobTecStep'+layers
    )
process.earlyGeneralTracks8.trackProducers = cms.VInputTag(
        "initialStepTracks"+layers, "highPtTripletStepTracks"+layers, "jetCoreRegionalStepTracks"+layers, "lowPtQuadStepTracks"+layers, "lowPtTripletStepTracks"+layers,
        "detachedQuadStepTracks"+layers, "detachedTripletStepTracks"+layers, "pixelPairStepTracks"+layers, "mixedTripletStepTracks"+layers, "pixelLessStepTracks"+layers,
        "tobTecStepTracks"+layers
    )

process.preDuplicateMergingGeneralTracks8 = process.preDuplicateMergingGeneralTracks.clone()
process.preDuplicateMergingGeneralTracks8.inputClassifiers = cms.vstring(
        'earlyGeneralTracks'+layers,
        'muonSeededTracksInOutClassifier'+layers,
        'muonSeededTracksOutInClassifier'+layers
    )
process.preDuplicateMergingGeneralTracks8.trackProducers = cms.VInputTag("earlyGeneralTracks"+layers, "muonSeededTracksInOut"+layers, "muonSeededTracksOutIn"+layers)

process.trackerClusterCheck8 = process.trackerClusterCheck.clone()
process.trackerClusterCheck8.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.trackerClusterCheck8.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.convClusters8 = process.convClusters.clone()
process.convClusters8.oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"+layers)
process.convClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.convClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.convClusters8.trackClassifier = cms.InputTag("tobTecStep"+layers,"QualityMasks")
process.convClusters8.trajectories = cms.InputTag("tobTecStepTracks"+layers)

process.convLayerPairs8 = process.convLayerPairs.clone()
process.convLayerPairs8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs8.BPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.convLayerPairs8.FPix.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs8.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs8.MTIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs8.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.convLayerPairs8.MTOB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs8.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs8.TEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHitUnmatched")
process.convLayerPairs8.TEC.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs8.TEC.stereoRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHitUnmatched")
process.convLayerPairs8.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs8.TIB.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs8.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs8.TID.skipClusters = cms.InputTag("convClusters"+layers)
process.convLayerPairs8.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.convLayerPairs8.TOB.skipClusters = cms.InputTag("convClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.convStepSelector8 = process.convStepSelector.clone()
process.convStepSelector8.src = cms.InputTag("convStepTracks"+layers)
#process.convStepSelector8.trackSelectors.name = cms.string('convStep'+layers)
process.convStepSelector8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.convStepTracks8 = process.convStepTracks.clone()
process.convStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convStepTracks8.src = cms.InputTag("convTrackCandidates"+layers)

process.convTrackCandidates8 = process.convTrackCandidates.clone()
process.convTrackCandidates8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.convTrackCandidates8.clustersToSkip = cms.InputTag("convClusters"+layers)
process.convTrackCandidates8.src = cms.InputTag("photonConvTrajSeedFromSingleLeg"+layers,"convSeedCandidates")

process.photonConvTrajSeedFromSingleLeg8 = process.photonConvTrajSeedFromSingleLeg.clone()
process.photonConvTrajSeedFromSingleLeg8.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg8.ClusterCheckPSet.PixelClusterCollectionLabel = cms.InputTag("rCluster"+layers)
process.photonConvTrajSeedFromSingleLeg8.OrderedHitsFactoryPSet.SeedingLayers = cms.InputTag("convLayerPairs"+layers)
process.photonConvTrajSeedFromSingleLeg8.TrackRefitter = cms.InputTag("generalTracks"+layers)
process.photonConvTrajSeedFromSingleLeg8.primaryVerticesTag = cms.InputTag("firstStepPrimaryVertices"+layers)

process.MeasurementTrackerEvent8 = process.MeasurementTrackerEvent.clone()
process.MeasurementTrackerEvent8.pixelClusterProducer = cms.string('rCluster'+layers)
process.MeasurementTrackerEvent8.stripClusterProducer = cms.string('rCluster'+layers)

process.ak4CaloJetsForTrkPreSplitting8 = process.ak4CaloJetsForTrkPreSplitting.clone()
process.ak4CaloJetsForTrkPreSplitting8.srcPVs = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.firstStepPrimaryVerticesPreSplitting8 = process.firstStepPrimaryVerticesPreSplitting.clone()
process.firstStepPrimaryVerticesPreSplitting8.TrackLabel = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepHitDoubletsPreSplitting8 = process.initialStepHitDoubletsPreSplitting.clone()
process.initialStepHitDoubletsPreSplitting8.clusterCheck = cms.InputTag("trackerClusterCheckPreSplitting"+layers)

process.initialStepHitQuadrupletsPreSplitting8 = process.initialStepHitQuadrupletsPreSplitting.clone()
process.initialStepHitQuadrupletsPreSplitting8.doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"+layers)
process.initialStepHitQuadrupletsPreSplitting8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoubletsPreSplitting'+layers+'__reRECO')

process.initialStepSeedsPreSplitting8 = process.initialStepSeedsPreSplitting.clone()
process.initialStepSeedsPreSplitting8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadrupletsPreSplitting'+layers+'__reRECO')
process.initialStepSeedsPreSplitting8.seedingHitSets = cms.InputTag("initialStepHitQuadrupletsPreSplitting"+layers)

process.initialStepTrackCandidatesMkFitConfigPreSplitting8 = process.initialStepTrackCandidatesMkFitConfigPreSplitting.clone()
process.initialStepTrackCandidatesMkFitConfigPreSplitting8.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfigPreSplitting'+layers)

process.initialStepTrackCandidatesMkFitPreSplitting8 = process.initialStepTrackCandidatesMkFitPreSplitting.clone()
process.initialStepTrackCandidatesMkFitPreSplitting8.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfigPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting8.eventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting8.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFitPreSplitting8.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesMkFitPreSplitting8.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitSeedsPreSplitting8 = process.initialStepTrackCandidatesMkFitSeedsPreSplitting.clone()
process.initialStepTrackCandidatesMkFitSeedsPreSplitting8.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)

process.initialStepTrackCandidatesPreSplitting8 = process.initialStepTrackCandidatesPreSplitting.clone()
process.initialStepTrackCandidatesPreSplitting8.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFitPreSplitting'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesPreSplitting8.mkFitEventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting8.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting8.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidatesPreSplitting8.seeds = cms.InputTag("initialStepSeedsPreSplitting"+layers)
process.initialStepTrackCandidatesPreSplitting8.tracks = cms.InputTag("initialStepTrackCandidatesMkFitPreSplitting"+layers)

process.initialStepTrackRefsForJetsPreSplitting8 = process.initialStepTrackRefsForJetsPreSplitting.clone()
process.initialStepTrackRefsForJetsPreSplitting8.src = cms.InputTag("initialStepTracksPreSplitting"+layers)

process.initialStepTracksPreSplitting8 = process.initialStepTracksPreSplitting.clone()
process.initialStepTracksPreSplitting8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"+layers)
process.initialStepTracksPreSplitting8.src = cms.InputTag("initialStepTrackCandidatesPreSplitting"+layers)

process.jetsForCoreTrackingPreSplitting8 = process.jetsForCoreTrackingPreSplitting.clone()
process.jetsForCoreTrackingPreSplitting8.src = cms.InputTag("ak4CaloJetsForTrkPreSplitting"+layers)

process.mkFitEventOfHitsPreSplitting8 = process.mkFitEventOfHitsPreSplitting.clone()
process.mkFitEventOfHitsPreSplitting8.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHitsPreSplitting8.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiStripHits8 = process.mkFitSiStripHits.clone()
process.mkFitSiStripHits8.rphiHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.mkFitSiStripHits8.stereoHits = cms.InputTag("siStripMatchedRecHits"+layers,"stereoRecHit")

process.siPixelClusterShapeCache8 = process.siPixelClusterShapeCache.clone()
process.siPixelClusterShapeCache8.src = cms.InputTag("rCluster"+layers)

process.siPixelClusters8 = process.siPixelClusters.clone()
process.siPixelClusters8.cores = cms.InputTag("jetsForCoreTrackingPreSplitting"+layers)
process.siPixelClusters8.vertices = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+layers)

process.siPixelRecHits8 = process.siPixelRecHits.clone()
process.siPixelRecHits8.src = cms.InputTag("rCluster"+layers)

process.trackerClusterCheckPreSplitting8 = process.trackerClusterCheckPreSplitting.clone()
process.trackerClusterCheckPreSplitting8.ClusterCollectionLabel = cms.InputTag("rCluster"+layers)

process.duplicateTrackCandidates8 = process.duplicateTrackCandidates.clone()
process.duplicateTrackCandidates8.source = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.duplicateTrackClassifier8 = process.duplicateTrackClassifier.clone()
process.duplicateTrackClassifier8.src = cms.InputTag("mergedDuplicateTracks"+layers)
process.duplicateTrackClassifier8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.generalTracks8 = process.generalTracks.clone()
process.generalTracks8.candidateComponents = cms.InputTag("duplicateTrackCandidates"+layers,"candidateMap")
process.generalTracks8.candidateSource = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")
process.generalTracks8.mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+layers,"MVAValues")
process.generalTracks8.mergedSource = cms.InputTag("mergedDuplicateTracks"+layers)
process.generalTracks8.originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+layers,"MVAValues")
process.generalTracks8.originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+layers)

process.mergedDuplicateTracks8 = process.mergedDuplicateTracks.clone()
process.mergedDuplicateTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mergedDuplicateTracks8.src = cms.InputTag("duplicateTrackCandidates"+layers,"candidates")

process.earlyMuons8 = process.earlyMuons.clone()
process.earlyMuons8.TrackExtractorPSet.inputTrackCollection = cms.InputTag("generalTracks"+layers)
process.earlyMuons8.inputCollectionLabels = cms.VInputTag("earlyGeneralTracks"+layers, "standAloneMuons:UpdatedAtVtx")
process.earlyMuons8.pvInputTag = cms.InputTag("offlinePrimaryVertices"+layers)

process.detachedQuadStep8 = process.detachedQuadStep.clone()
process.detachedQuadStep8.src = cms.InputTag("detachedQuadStepTracks"+layers)
process.detachedQuadStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedQuadStepClusters8 = process.detachedQuadStepClusters.clone()
process.detachedQuadStepClusters8.oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+layers)
process.detachedQuadStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedQuadStepClusters8.trackClassifier = cms.InputTag("lowPtTripletStep"+layers,"QualityMasks")
process.detachedQuadStepClusters8.trajectories = cms.InputTag("lowPtTripletStepTracks"+layers)

process.detachedQuadStepHitDoublets8 = process.detachedQuadStepHitDoublets.clone()
process.detachedQuadStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedQuadStepHitDoublets8.seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+layers)

process.detachedQuadStepHitQuadruplets8 = process.detachedQuadStepHitQuadruplets.clone()
process.detachedQuadStepHitQuadruplets8.doublets = cms.InputTag("detachedQuadStepHitDoublets"+layers)
process.detachedQuadStepHitQuadruplets8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+layers+'__reRECO')

process.detachedQuadStepSeedLayers8 = process.detachedQuadStepSeedLayers.clone()
process.detachedQuadStepSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers8.BPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedQuadStepSeedLayers8.FPix.skipClusters = cms.InputTag("detachedQuadStepClusters"+layers)

process.detachedQuadStepSeeds8 = process.detachedQuadStepSeeds.clone()
process.detachedQuadStepSeeds8.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedQuadStepSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+layers+'__reRECO')
process.detachedQuadStepSeeds8.seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+layers)

process.detachedQuadStepTrackCandidates8 = process.detachedQuadStepTrackCandidates.clone()
process.detachedQuadStepTrackCandidates8.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedQuadStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidates8.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidates8.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidates8.mkFitSeeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidates8.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedQuadStepTrackCandidates8.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)
process.detachedQuadStepTrackCandidates8.tracks = cms.InputTag("detachedQuadStepTrackCandidatesMkFit"+layers)

process.detachedQuadStepTrackCandidatesMkFit8 = process.detachedQuadStepTrackCandidatesMkFit.clone()
process.detachedQuadStepTrackCandidatesMkFit8.clustersToSkip = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedQuadStepTrackCandidatesMkFit8.config = cms.ESInputTag("","detachedQuadStepTrackCandidatesMkFitConfig"+layers)
process.detachedQuadStepTrackCandidatesMkFit8.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit8.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedQuadStepTrackCandidatesMkFit8.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedQuadStepTrackCandidatesMkFit8.seeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+layers)
process.detachedQuadStepTrackCandidatesMkFit8.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedQuadStepTrackCandidatesMkFitConfig8 = process.detachedQuadStepTrackCandidatesMkFitConfig.clone()
process.detachedQuadStepTrackCandidatesMkFitConfig8.ComponentName = cms.string('detachedQuadStepTrackCandidatesMkFitConfig'+layers)

process.detachedQuadStepTrackCandidatesMkFitSeeds8 = process.detachedQuadStepTrackCandidatesMkFitSeeds.clone()
process.detachedQuadStepTrackCandidatesMkFitSeeds8.seeds = cms.InputTag("detachedQuadStepSeeds"+layers)

process.detachedQuadStepTracks8 = process.detachedQuadStepTracks.clone()
process.detachedQuadStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedQuadStepTracks8.src = cms.InputTag("detachedQuadStepTrackCandidates"+layers)

process.detachedTripletStep8 = process.detachedTripletStep.clone()
process.detachedTripletStep8.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier18 = process.detachedTripletStepClassifier1.clone()
process.detachedTripletStepClassifier18.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier18.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClassifier28 = process.detachedTripletStepClassifier2.clone()
process.detachedTripletStepClassifier28.src = cms.InputTag("detachedTripletStepTracks"+layers)
process.detachedTripletStepClassifier28.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.detachedTripletStepClusters8 = process.detachedTripletStepClusters.clone()
process.detachedTripletStepClusters8.oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+layers)
process.detachedTripletStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.detachedTripletStepClusters8.trackClassifier = cms.InputTag("detachedQuadStep"+layers,"QualityMasks")
process.detachedTripletStepClusters8.trajectories = cms.InputTag("detachedQuadStepTracks"+layers)

process.detachedTripletStepHitDoublets8 = process.detachedTripletStepHitDoublets.clone()
process.detachedTripletStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.detachedTripletStepHitDoublets8.seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+layers)

process.detachedTripletStepHitTriplets8 = process.detachedTripletStepHitTriplets.clone()
process.detachedTripletStepHitTriplets8.doublets = cms.InputTag("detachedTripletStepHitDoublets"+layers)
process.detachedTripletStepHitTriplets8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+layers+'__reRECO')

process.detachedTripletStepSeedLayers8 = process.detachedTripletStepSeedLayers.clone()
process.detachedTripletStepSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers8.BPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.detachedTripletStepSeedLayers8.FPix.skipClusters = cms.InputTag("detachedTripletStepClusters"+layers)

process.detachedTripletStepSeeds8 = process.detachedTripletStepSeeds.clone()
process.detachedTripletStepSeeds8.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.detachedTripletStepSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+layers+'__reRECO')
process.detachedTripletStepSeeds8.seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+layers)

process.detachedTripletStepTrackCandidates8 = process.detachedTripletStepTrackCandidates.clone()
process.detachedTripletStepTrackCandidates8.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_detachedTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidates8.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidates8.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidates8.mkFitSeeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidates8.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.detachedTripletStepTrackCandidates8.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)
process.detachedTripletStepTrackCandidates8.tracks = cms.InputTag("detachedTripletStepTrackCandidatesMkFit"+layers)

process.detachedTripletStepTrackCandidatesMkFit8 = process.detachedTripletStepTrackCandidatesMkFit.clone()
process.detachedTripletStepTrackCandidatesMkFit8.clustersToSkip = cms.InputTag("detachedTripletStepClusters"+layers)
process.detachedTripletStepTrackCandidatesMkFit8.config = cms.ESInputTag("","detachedTripletStepTrackCandidatesMkFitConfig"+layers)
process.detachedTripletStepTrackCandidatesMkFit8.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit8.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.detachedTripletStepTrackCandidatesMkFit8.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.detachedTripletStepTrackCandidatesMkFit8.seeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+layers)
process.detachedTripletStepTrackCandidatesMkFit8.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.detachedTripletStepTrackCandidatesMkFitConfig8 = process.detachedTripletStepTrackCandidatesMkFitConfig.clone()
process.detachedTripletStepTrackCandidatesMkFitConfig8.ComponentName = cms.string('detachedTripletStepTrackCandidatesMkFitConfig'+layers)

process.detachedTripletStepTrackCandidatesMkFitSeeds8 = process.detachedTripletStepTrackCandidatesMkFitSeeds.clone()
process.detachedTripletStepTrackCandidatesMkFitSeeds8.seeds = cms.InputTag("detachedTripletStepSeeds"+layers)

process.detachedTripletStepTracks8 = process.detachedTripletStepTracks.clone()
process.detachedTripletStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.detachedTripletStepTracks8.src = cms.InputTag("detachedTripletStepTrackCandidates"+layers)

process.highPtTripletStep8 = process.highPtTripletStep.clone()
process.highPtTripletStep8.src = cms.InputTag("highPtTripletStepTracks"+layers)
process.highPtTripletStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.highPtTripletStepClusters8 = process.highPtTripletStepClusters.clone()
process.highPtTripletStepClusters8.oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+layers)
process.highPtTripletStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.highPtTripletStepClusters8.trackClassifier = cms.InputTag("lowPtQuadStep"+layers,"QualityMasks")
process.highPtTripletStepClusters8.trajectories = cms.InputTag("lowPtQuadStepTracks"+layers)

process.highPtTripletStepHitDoublets8 = process.highPtTripletStepHitDoublets.clone()
process.highPtTripletStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.highPtTripletStepHitDoublets8.seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+layers)

process.highPtTripletStepHitTriplets8 = process.highPtTripletStepHitTriplets.clone()
process.highPtTripletStepHitTriplets8.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.highPtTripletStepHitTriplets8.doublets = cms.InputTag("highPtTripletStepHitDoublets"+layers)
process.highPtTripletStepHitTriplets8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+layers+'__reRECO')

process.highPtTripletStepSeedLayers8 = process.highPtTripletStepSeedLayers.clone()
process.highPtTripletStepSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers8.BPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.highPtTripletStepSeedLayers8.FPix.skipClusters = cms.InputTag("highPtTripletStepClusters"+layers)

process.highPtTripletStepSeeds8 = process.highPtTripletStepSeeds.clone()
process.highPtTripletStepSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+layers+'__reRECO')
process.highPtTripletStepSeeds8.seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+layers)

process.highPtTripletStepTrackCandidates8 = process.highPtTripletStepTrackCandidates.clone()
process.highPtTripletStepTrackCandidates8.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_highPtTripletStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidates8.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidates8.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidates8.mkFitSeeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidates8.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.highPtTripletStepTrackCandidates8.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)
process.highPtTripletStepTrackCandidates8.tracks = cms.InputTag("highPtTripletStepTrackCandidatesMkFit"+layers)

process.highPtTripletStepTrackCandidatesMkFit8 = process.highPtTripletStepTrackCandidatesMkFit.clone()
process.highPtTripletStepTrackCandidatesMkFit8.clustersToSkip = cms.InputTag("highPtTripletStepClusters"+layers)
process.highPtTripletStepTrackCandidatesMkFit8.config = cms.ESInputTag("","highPtTripletStepTrackCandidatesMkFitConfig"+layers)
process.highPtTripletStepTrackCandidatesMkFit8.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit8.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.highPtTripletStepTrackCandidatesMkFit8.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.highPtTripletStepTrackCandidatesMkFit8.seeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+layers)
process.highPtTripletStepTrackCandidatesMkFit8.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.highPtTripletStepTrackCandidatesMkFitConfig8 = process.highPtTripletStepTrackCandidatesMkFitConfig.clone()
process.highPtTripletStepTrackCandidatesMkFitConfig8.ComponentName = cms.string('highPtTripletStepTrackCandidatesMkFitConfig'+layers)

process.highPtTripletStepTrackCandidatesMkFitSeeds8 = process.highPtTripletStepTrackCandidatesMkFitSeeds.clone()
process.highPtTripletStepTrackCandidatesMkFitSeeds8.seeds = cms.InputTag("highPtTripletStepSeeds"+layers)

process.highPtTripletStepTracks8 = process.highPtTripletStepTracks.clone()
process.highPtTripletStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.highPtTripletStepTracks8.src = cms.InputTag("highPtTripletStepTrackCandidates"+layers)

process.firstStepPrimaryVertices8 = process.firstStepPrimaryVertices.clone()
process.firstStepPrimaryVertices8.jets = cms.InputTag("ak4CaloJetsForTrk"+layers)
process.firstStepPrimaryVertices8.particles = cms.InputTag("initialStepTrackRefsForJets"+layers)
process.firstStepPrimaryVertices8.vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+layers)

process.firstStepPrimaryVerticesUnsorted8 = process.firstStepPrimaryVerticesUnsorted.clone()
process.firstStepPrimaryVerticesUnsorted8.TrackLabel = cms.InputTag("initialStepTracks"+layers)

process.initialStep8 = process.initialStep.clone()
process.initialStep8.src = cms.InputTag("initialStepTracks"+layers)
process.initialStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepClassifier18 = process.initialStepClassifier1.clone()
process.initialStepClassifier18.src = cms.InputTag("initialStepTracks"+layers)
process.initialStepClassifier18.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.initialStepHitDoublets8 = process.initialStepHitDoublets.clone()
process.initialStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.initialStepHitDoublets8.seedingLayers = cms.InputTag("initialStepSeedLayers"+layers)

process.initialStepHitQuadruplets8 = process.initialStepHitQuadruplets.clone()
process.initialStepHitQuadruplets8.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepHitQuadruplets8.doublets = cms.InputTag("initialStepHitDoublets"+layers)
process.initialStepHitQuadruplets8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+layers+'__reRECO')

process.initialStepSeedLayers8 = process.initialStepSeedLayers.clone()
process.initialStepSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.initialStepSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)

process.initialStepSeeds8 = process.initialStepSeeds.clone()
process.initialStepSeeds8.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.initialStepSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+layers+'__reRECO')
process.initialStepSeeds8.seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+layers)

process.initialStepTrackCandidates8 = process.initialStepTrackCandidates.clone()
process.initialStepTrackCandidates8.mightGet = cms.untracked.vstring(
        'MkFitOutputWrapper_initialStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidates8.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidates8.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidates8.mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidates8.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.initialStepTrackCandidates8.seeds = cms.InputTag("initialStepSeeds"+layers)
process.initialStepTrackCandidates8.tracks = cms.InputTag("initialStepTrackCandidatesMkFit"+layers)

process.initialStepTrackCandidatesMkFit8 = process.initialStepTrackCandidatesMkFit.clone()
process.initialStepTrackCandidatesMkFit8.config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfig"+layers)
process.initialStepTrackCandidatesMkFit8.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.initialStepTrackCandidatesMkFit8.mightGet = cms.untracked.vstring(
        'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+layers+'__reRECO',
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.initialStepTrackCandidatesMkFit8.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.initialStepTrackCandidatesMkFit8.seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+layers)
process.initialStepTrackCandidatesMkFit8.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.initialStepTrackCandidatesMkFitConfig8 = process.initialStepTrackCandidatesMkFitConfig.clone()
process.initialStepTrackCandidatesMkFitConfig8.ComponentName = cms.string('initialStepTrackCandidatesMkFitConfig'+layers)

process.initialStepTrackCandidatesMkFitSeeds8 = process.initialStepTrackCandidatesMkFitSeeds.clone()
process.initialStepTrackCandidatesMkFitSeeds8.seeds = cms.InputTag("initialStepSeeds"+layers)

process.initialStepTrackRefsForJets8 = process.initialStepTrackRefsForJets.clone()
process.initialStepTrackRefsForJets8.src = cms.InputTag("initialStepTracks"+layers)

process.initialStepTracks8 = process.initialStepTracks.clone()
process.initialStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.initialStepTracks8.src = cms.InputTag("initialStepTrackCandidates"+layers)

process.mkFitEventOfHits8 = process.mkFitEventOfHits.clone()
process.mkFitEventOfHits8.mightGet = cms.untracked.vstring(
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO'
    )
process.mkFitEventOfHits8.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.mkFitEventOfHits8.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.mkFitSiPixelHits8 = process.mkFitSiPixelHits.clone()
process.mkFitSiPixelHits8.hits = cms.InputTag("siPixelRecHits"+layers)

process.firstStepGoodPrimaryVertices8 = process.firstStepGoodPrimaryVertices.clone()
process.firstStepGoodPrimaryVertices8.src = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStep8 = process.jetCoreRegionalStep.clone()
process.jetCoreRegionalStep8.src = cms.InputTag("jetCoreRegionalStepTracks"+layers)
process.jetCoreRegionalStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.jetCoreRegionalStepHitDoublets8 = process.jetCoreRegionalStepHitDoublets.clone()
process.jetCoreRegionalStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.jetCoreRegionalStepHitDoublets8.seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"+layers)
process.jetCoreRegionalStepHitDoublets8.trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"+layers)

process.jetCoreRegionalStepSeedLayers8 = process.jetCoreRegionalStepSeedLayers.clone()
process.jetCoreRegionalStepSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.jetCoreRegionalStepSeedLayers8.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")

process.jetCoreRegionalStepSeeds8 = process.jetCoreRegionalStepSeeds.clone()
process.jetCoreRegionalStepSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_jetCoreRegionalStepHitDoublets'+layers+'__reRECO')
process.jetCoreRegionalStepSeeds8.seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets"+layers)

process.jetCoreRegionalStepTrackCandidates8 = process.jetCoreRegionalStepTrackCandidates.clone()
process.jetCoreRegionalStepTrackCandidates8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackCandidates8.src = cms.InputTag("jetCoreRegionalStepSeeds"+layers)

process.jetCoreRegionalStepTrackingRegions8 = process.jetCoreRegionalStepTrackingRegions.clone()
process.jetCoreRegionalStepTrackingRegions8.RegionPSet.JetSrc = cms.InputTag("jetsForCoreTracking"+layers)
process.jetCoreRegionalStepTrackingRegions8.RegionPSet.measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTrackingRegions8.RegionPSet.vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices"+layers)

process.jetCoreRegionalStepTracks8 = process.jetCoreRegionalStepTracks.clone()
process.jetCoreRegionalStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.jetCoreRegionalStepTracks8.src = cms.InputTag("jetCoreRegionalStepTrackCandidates"+layers)

process.jetsForCoreTracking8 = process.jetsForCoreTracking.clone()
process.jetsForCoreTracking8.src = cms.InputTag("ak4CaloJetsForTrk"+layers)

process.lowPtQuadStep8 = process.lowPtQuadStep.clone()
process.lowPtQuadStep8.src = cms.InputTag("lowPtQuadStepTracks"+layers)
process.lowPtQuadStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtQuadStepClusters8 = process.lowPtQuadStepClusters.clone()
process.lowPtQuadStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtQuadStepClusters8.trackClassifier = cms.InputTag("initialStep"+layers,"QualityMasks")
process.lowPtQuadStepClusters8.trajectories = cms.InputTag("initialStepTracks"+layers)

process.lowPtQuadStepHitDoublets8 = process.lowPtQuadStepHitDoublets.clone()
process.lowPtQuadStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtQuadStepHitDoublets8.seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+layers)

process.lowPtQuadStepHitQuadruplets8 = process.lowPtQuadStepHitQuadruplets.clone()
process.lowPtQuadStepHitQuadruplets8.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtQuadStepHitQuadruplets8.doublets = cms.InputTag("lowPtQuadStepHitDoublets"+layers)
process.lowPtQuadStepHitQuadruplets8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+layers+'__reRECO')

process.lowPtQuadStepSeedLayers8 = process.lowPtQuadStepSeedLayers.clone()
process.lowPtQuadStepSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers8.BPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtQuadStepSeedLayers8.FPix.skipClusters = cms.InputTag("lowPtQuadStepClusters"+layers)

process.lowPtQuadStepSeeds8 = process.lowPtQuadStepSeeds.clone()
process.lowPtQuadStepSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+layers+'__reRECO')
process.lowPtQuadStepSeeds8.seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+layers)

process.lowPtQuadStepTrackCandidates8 = process.lowPtQuadStepTrackCandidates.clone()
process.lowPtQuadStepTrackCandidates8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTrackCandidates8.clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+layers)
process.lowPtQuadStepTrackCandidates8.src = cms.InputTag("lowPtQuadStepSeeds"+layers)

process.lowPtQuadStepTracks8 = process.lowPtQuadStepTracks.clone()
process.lowPtQuadStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtQuadStepTracks8.src = cms.InputTag("lowPtQuadStepTrackCandidates"+layers)

process.lowPtTripletStep8 = process.lowPtTripletStep.clone()
process.lowPtTripletStep8.src = cms.InputTag("lowPtTripletStepTracks"+layers)
process.lowPtTripletStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.lowPtTripletStepClusters8 = process.lowPtTripletStepClusters.clone()
process.lowPtTripletStepClusters8.oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+layers)
process.lowPtTripletStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.lowPtTripletStepClusters8.trackClassifier = cms.InputTag("highPtTripletStep"+layers,"QualityMasks")
process.lowPtTripletStepClusters8.trajectories = cms.InputTag("highPtTripletStepTracks"+layers)

process.lowPtTripletStepHitDoublets8 = process.lowPtTripletStepHitDoublets.clone()
process.lowPtTripletStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.lowPtTripletStepHitDoublets8.seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+layers)

process.lowPtTripletStepHitTriplets8 = process.lowPtTripletStepHitTriplets.clone()
process.lowPtTripletStepHitTriplets8.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.lowPtTripletStepHitTriplets8.doublets = cms.InputTag("lowPtTripletStepHitDoublets"+layers)
process.lowPtTripletStepHitTriplets8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+layers+'__reRECO')

process.lowPtTripletStepSeedLayers8 = process.lowPtTripletStepSeedLayers.clone()
process.lowPtTripletStepSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers8.BPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.lowPtTripletStepSeedLayers8.FPix.skipClusters = cms.InputTag("lowPtTripletStepClusters"+layers)

process.lowPtTripletStepSeeds8 = process.lowPtTripletStepSeeds.clone()
process.lowPtTripletStepSeeds8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+layers+'__reRECO')
process.lowPtTripletStepSeeds8.seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+layers)

process.lowPtTripletStepTrackCandidates8 = process.lowPtTripletStepTrackCandidates.clone()
process.lowPtTripletStepTrackCandidates8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTrackCandidates8.clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+layers)
process.lowPtTripletStepTrackCandidates8.src = cms.InputTag("lowPtTripletStepSeeds"+layers)

process.lowPtTripletStepTracks8 = process.lowPtTripletStepTracks.clone()
process.lowPtTripletStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.lowPtTripletStepTracks8.src = cms.InputTag("lowPtTripletStepTrackCandidates"+layers)

process.chargeCut2069Clusters8 = process.chargeCut2069Clusters.clone()
process.chargeCut2069Clusters8.oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+layers)
process.chargeCut2069Clusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.chargeCut2069Clusters8.stripClusters = cms.InputTag("rCluster"+layers)

process.mixedTripletStep8 = process.mixedTripletStep.clone()
process.mixedTripletStep8.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier18 = process.mixedTripletStepClassifier1.clone()
process.mixedTripletStepClassifier18.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier18.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClassifier28 = process.mixedTripletStepClassifier2.clone()
process.mixedTripletStepClassifier28.src = cms.InputTag("mixedTripletStepTracks"+layers)
process.mixedTripletStepClassifier28.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.mixedTripletStepClusters8 = process.mixedTripletStepClusters.clone()
process.mixedTripletStepClusters8.oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+layers)
process.mixedTripletStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.mixedTripletStepClusters8.trackClassifier = cms.InputTag("pixelPairStep"+layers,"QualityMasks")
process.mixedTripletStepClusters8.trajectories = cms.InputTag("pixelPairStepTracks"+layers)

process.mixedTripletStepHitDoubletsA8 = process.mixedTripletStepHitDoubletsA.clone()
process.mixedTripletStepHitDoubletsA8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsA8.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+layers)

process.mixedTripletStepHitDoubletsB8 = process.mixedTripletStepHitDoubletsB.clone()
process.mixedTripletStepHitDoubletsB8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.mixedTripletStepHitDoubletsB8.seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+layers)

process.mixedTripletStepHitTripletsA8 = process.mixedTripletStepHitTripletsA.clone()
process.mixedTripletStepHitTripletsA8.doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+layers)
process.mixedTripletStepHitTripletsA8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO')

process.mixedTripletStepHitTripletsB8 = process.mixedTripletStepHitTripletsB.clone()
process.mixedTripletStepHitTripletsB8.doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+layers)
process.mixedTripletStepHitTripletsB8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO')

process.mixedTripletStepSeedLayersA8 = process.mixedTripletStepSeedLayersA.clone()
process.mixedTripletStepSeedLayersA8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA8.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersA8.FPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersA8.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersA8.TEC.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeedLayersB8 = process.mixedTripletStepSeedLayersB.clone()
process.mixedTripletStepSeedLayersB8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.mixedTripletStepSeedLayersB8.BPix.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepSeedLayersB8.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.mixedTripletStepSeedLayersB8.TIB.skipClusters = cms.InputTag("mixedTripletStepClusters"+layers)

process.mixedTripletStepSeeds8 = process.mixedTripletStepSeeds.clone()
process.mixedTripletStepSeeds8.seedCollections = cms.VInputTag("mixedTripletStepSeedsA"+layers, "mixedTripletStepSeedsB"+layers)

process.mixedTripletStepSeedsA8 = process.mixedTripletStepSeedsA.clone()
process.mixedTripletStepSeedsA8.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsA8.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsA8.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+layers)

process.mixedTripletStepSeedsB8 = process.mixedTripletStepSeedsB.clone()
process.mixedTripletStepSeedsB8.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.mixedTripletStepSeedsB8.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+layers+'__reRECO',
        'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+layers+'__reRECO'
    )
process.mixedTripletStepSeedsB8.seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+layers)

process.mixedTripletStepTrackCandidates8 = process.mixedTripletStepTrackCandidates.clone()
process.mixedTripletStepTrackCandidates8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTrackCandidates8.clustersToSkip = cms.InputTag("mixedTripletStepClusters"+layers)
process.mixedTripletStepTrackCandidates8.src = cms.InputTag("mixedTripletStepSeeds"+layers)

process.mixedTripletStepTracks8 = process.mixedTripletStepTracks.clone()
process.mixedTripletStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.mixedTripletStepTracks8.src = cms.InputTag("mixedTripletStepTrackCandidates"+layers)

process.pixelLessStep8 = process.pixelLessStep.clone()
process.pixelLessStep8.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier18 = process.pixelLessStepClassifier1.clone()
process.pixelLessStepClassifier18.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier18.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClassifier28 = process.pixelLessStepClassifier2.clone()
process.pixelLessStepClassifier28.src = cms.InputTag("pixelLessStepTracks"+layers)
process.pixelLessStepClassifier28.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelLessStepClusters8 = process.pixelLessStepClusters.clone()
process.pixelLessStepClusters8.oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+layers)
process.pixelLessStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelLessStepClusters8.trackClassifier = cms.InputTag("mixedTripletStep"+layers,"QualityMasks")
process.pixelLessStepClusters8.trajectories = cms.InputTag("mixedTripletStepTracks"+layers)

process.pixelLessStepHitDoublets8 = process.pixelLessStepHitDoublets.clone()
process.pixelLessStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelLessStepHitDoublets8.seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+layers)

process.pixelLessStepHitTriplets8 = process.pixelLessStepHitTriplets.clone()
process.pixelLessStepHitTriplets8.doublets = cms.InputTag("pixelLessStepHitDoublets"+layers)
process.pixelLessStepHitTriplets8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+layers+'__reRECO')

process.pixelLessStepSeedLayers8 = process.pixelLessStepSeedLayers.clone()
process.pixelLessStepSeedLayers8.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers8.MTEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers8.MTIB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers8.MTIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers8.MTID.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.pixelLessStepSeedLayers8.MTID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers8.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers8.TEC.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers8.TIB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers8.TIB.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepSeedLayers8.TID.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.pixelLessStepSeedLayers8.TID.skipClusters = cms.InputTag("pixelLessStepClusters"+layers)

# Maybe check this guy in output_reRECO.txt
process.pixelLessStepSeeds8 = process.pixelLessStepSeeds.clone()
process.pixelLessStepSeeds8.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.pixelLessStepSeeds8.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_pixelLessStepHitTriplets'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+layers+'__reRECO'
    )
process.pixelLessStepSeeds8.seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+layers)

process.pixelLessStepTrackCandidates8 = process.pixelLessStepTrackCandidates.clone()
process.pixelLessStepTrackCandidates8.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitOutputWrapper_pixelLessStepTrackCandidatesMkFit'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidates8.mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidates8.mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidates8.mkFitSeeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidates8.mkFitStripHits = cms.InputTag("mkFitSiStripHits"+layers)
process.pixelLessStepTrackCandidates8.seeds = cms.InputTag("pixelLessStepSeeds"+layers)
process.pixelLessStepTrackCandidates8.tracks = cms.InputTag("pixelLessStepTrackCandidatesMkFit"+layers)

process.pixelLessStepTrackCandidatesMkFit8 = process.pixelLessStepTrackCandidatesMkFit.clone()
process.pixelLessStepTrackCandidatesMkFit8.clustersToSkip = cms.InputTag("pixelLessStepClusters"+layers)
process.pixelLessStepTrackCandidatesMkFit8.config = cms.ESInputTag("","pixelLessStepTrackCandidatesMkFitConfig"+layers)
process.pixelLessStepTrackCandidatesMkFit8.eventOfHits = cms.InputTag("mkFitEventOfHits"+layers)
process.pixelLessStepTrackCandidatesMkFit8.mightGet = cms.untracked.vstring(
        'MkFitEventOfHits_mkFitEventOfHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiPixelHits'+layers+'__reRECO',
        'MkFitHitWrapper_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitClusterIndexToHit_mkFitSiStripHits'+layers+'__reRECO',
        'floats_mkFitSiStripHits'+layers+'__reRECO',
        'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+layers+'__reRECO'
    )
process.pixelLessStepTrackCandidatesMkFit8.pixelHits = cms.InputTag("mkFitSiPixelHits"+layers)
process.pixelLessStepTrackCandidatesMkFit8.seeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+layers)
process.pixelLessStepTrackCandidatesMkFit8.stripHits = cms.InputTag("mkFitSiStripHits"+layers)

process.pixelLessStepTrackCandidatesMkFitSeeds8 = process.pixelLessStepTrackCandidatesMkFitSeeds.clone()
process.pixelLessStepTrackCandidatesMkFitSeeds8.seeds = cms.InputTag("pixelLessStepSeeds"+layers)

process.pixelLessStepTrackCandidatesMkFitConfig8 = process.pixelLessStepTrackCandidatesMkFitConfig.clone()
process.pixelLessStepTrackCandidatesMkFitConfig8.ComponentName = cms.string('pixelLessStepTrackCandidatesMkFitConfig'+layers)

process.pixelLessStepTracks8 = process.pixelLessStepTracks.clone()
process.pixelLessStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelLessStepTracks8.src = cms.InputTag("pixelLessStepTrackCandidates"+layers)

process.pixelPairStep8 = process.pixelPairStep.clone()
process.pixelPairStep8.src = cms.InputTag("pixelPairStepTracks"+layers)
process.pixelPairStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepClusters8 = process.pixelPairStepClusters.clone()
process.pixelPairStepClusters8.oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+layers)
process.pixelPairStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.pixelPairStepClusters8.trackClassifier = cms.InputTag("detachedTripletStep"+layers,"QualityMasks")
process.pixelPairStepClusters8.trajectories = cms.InputTag("detachedTripletStepTracks"+layers)

process.pixelPairStepHitDoublets8 = process.pixelPairStepHitDoublets.clone()
process.pixelPairStepHitDoublets8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoublets8.seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+layers)
process.pixelPairStepHitDoublets8.trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+layers)

process.pixelPairStepHitDoubletsB8 = process.pixelPairStepHitDoubletsB.clone()
process.pixelPairStepHitDoubletsB8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.pixelPairStepHitDoubletsB8.trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+layers)

process.pixelPairStepSeedLayers8 = process.pixelPairStepSeedLayers.clone()
process.pixelPairStepSeedLayers8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers8.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepSeedLayers8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepSeedLayers8.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)

process.pixelPairStepSeeds8 = process.pixelPairStepSeeds.clone()
process.pixelPairStepSeeds8.seedCollections = cms.VInputTag("pixelPairStepSeedsA"+layers, "pixelPairStepSeedsB"+layers)

process.pixelPairStepSeedsA8 = process.pixelPairStepSeedsA.clone()
process.pixelPairStepSeedsA8.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsA8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+layers+'__reRECO')
process.pixelPairStepSeedsA8.seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+layers)

process.pixelPairStepSeedsB8 = process.pixelPairStepSeedsB.clone()
process.pixelPairStepSeedsB8.SeedComparitorPSet.ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers)
process.pixelPairStepSeedsB8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+layers+'__reRECO')
process.pixelPairStepSeedsB8.seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+layers)

process.pixelPairStepTrackCandidates8 = process.pixelPairStepTrackCandidates.clone()
process.pixelPairStepTrackCandidates8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTrackCandidates8.clustersToSkip = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackCandidates8.src = cms.InputTag("pixelPairStepSeeds"+layers)

process.pixelPairStepTrackingRegions8 = process.pixelPairStepTrackingRegions.clone()
process.pixelPairStepTrackingRegions8.RegionPSet.VertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)
process.pixelPairStepTrackingRegions8.RegionPSet.pixelClustersForScaling = cms.InputTag("rCluster"+layers)

process.pixelPairStepTrackingRegionsSeedLayersB8 = process.pixelPairStepTrackingRegionsSeedLayersB.clone()
process.pixelPairStepTrackingRegionsSeedLayersB8.BPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB8.BPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB8.FPix.HitProducer = cms.string('siPixelRecHits'+layers)
process.pixelPairStepTrackingRegionsSeedLayersB8.FPix.skipClusters = cms.InputTag("pixelPairStepClusters"+layers)
process.pixelPairStepTrackingRegionsSeedLayersB8.RegionPSet.vertexCollection = cms.InputTag("firstStepPrimaryVertices"+layers)

process.pixelPairStepTracks8 = process.pixelPairStepTracks.clone()
process.pixelPairStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.pixelPairStepTracks8.src = cms.InputTag("pixelPairStepTrackCandidates"+layers)

process.tobTecStep8 = process.tobTecStep.clone()
process.tobTecStep8.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStep8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier18 = process.tobTecStepClassifier1.clone()
process.tobTecStepClassifier18.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier18.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClassifier28 = process.tobTecStepClassifier2.clone()
process.tobTecStepClassifier28.src = cms.InputTag("tobTecStepTracks"+layers)
process.tobTecStepClassifier28.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.tobTecStepClusters8 = process.tobTecStepClusters.clone()
process.tobTecStepClusters8.oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+layers)
process.tobTecStepClusters8.pixelClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters8.stripClusters = cms.InputTag("rCluster"+layers)
process.tobTecStepClusters8.trackClassifier = cms.InputTag("pixelLessStep"+layers,"QualityMasks")
process.tobTecStepClusters8.trajectories = cms.InputTag("pixelLessStepTracks"+layers)

process.tobTecStepHitDoubletsPair8 = process.tobTecStepHitDoubletsPair.clone()
process.tobTecStepHitDoubletsPair8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsPair8.seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+layers)

process.tobTecStepHitDoubletsTripl8 = process.tobTecStepHitDoubletsTripl.clone()
process.tobTecStepHitDoubletsTripl8.clusterCheck = cms.InputTag("trackerClusterCheck"+layers)
process.tobTecStepHitDoubletsTripl8.seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+layers)

process.tobTecStepHitTripletsTripl8 = process.tobTecStepHitTripletsTripl.clone()
process.tobTecStepHitTripletsTripl8.doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+layers)
process.tobTecStepHitTripletsTripl8.mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+layers+'__reRECO')

process.tobTecStepSeedLayersPair8 = process.tobTecStepSeedLayersPair.clone()
process.tobTecStepSeedLayersPair8.TEC.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair8.TEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersPair8.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersPair8.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeedLayersTripl8 = process.tobTecStepSeedLayersTripl.clone()
process.tobTecStepSeedLayersTripl8.MTEC.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl8.MTEC.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl8.MTOB.rphiRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"rphiRecHit")
process.tobTecStepSeedLayersTripl8.MTOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepSeedLayersTripl8.TOB.matchedRecHits = cms.InputTag("siStripMatchedRecHits"+layers,"matchedRecHit")
process.tobTecStepSeedLayersTripl8.TOB.skipClusters = cms.InputTag("tobTecStepClusters"+layers)

process.tobTecStepSeeds8 = process.tobTecStepSeeds.clone()
process.tobTecStepSeeds8.seedCollections = cms.VInputTag("tobTecStepSeedsTripl"+layers, "tobTecStepSeedsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsPair8 = process.tobTecStepSeedsPair.clone()
process.tobTecStepSeedsPair8.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsPair8.mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+layers+'__reRECO')
process.tobTecStepSeedsPair8.seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+layers)

# Maybe check this guy in output_reRECO.txt
process.tobTecStepSeedsTripl8 = process.tobTecStepSeedsTripl.clone()
process.tobTecStepSeedsTripl8.SeedComparitorPSet.comparitors = cms.VPSet(
    cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+layers),
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
        layerMask = cms.PSet(

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
)
process.tobTecStepSeedsTripl8.mightGet = cms.untracked.vstring(
        'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+layers+'__reRECO',
        'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+layers+'__reRECO'
    )
process.tobTecStepSeedsTripl8.seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+layers)

process.tobTecStepTrackCandidates8 = process.tobTecStepTrackCandidates.clone()
process.tobTecStepTrackCandidates8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTrackCandidates8.clustersToSkip = cms.InputTag("tobTecStepClusters"+layers)
process.tobTecStepTrackCandidates8.src = cms.InputTag("tobTecStepSeeds"+layers)

process.tobTecStepTracks8 = process.tobTecStepTracks.clone()
process.tobTecStepTracks8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.tobTecStepTracks8.src = cms.InputTag("tobTecStepTrackCandidates"+layers)

process.muonSeededTracksOutInClassifier8 = process.muonSeededTracksOutInClassifier.clone()
process.muonSeededTracksOutInClassifier8.src = cms.InputTag("muonSeededTracksOutIn"+layers)
process.muonSeededTracksOutInClassifier8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.muonSeededSeedsInOut8 = process.muonSeededSeedsInOut.clone()
process.muonSeededSeedsInOut8.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesInOut8 = process.muonSeededTrackCandidatesInOut.clone()
process.muonSeededTrackCandidatesInOut8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesInOut8.src = cms.InputTag("muonSeededSeedsInOut"+layers)

process.muonSeededTracksInOut8 = process.muonSeededTracksInOut.clone()
process.muonSeededTracksInOut8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksInOut8.src = cms.InputTag("muonSeededTrackCandidatesInOut"+layers)

process.muonSeededSeedsOutIn8 = process.muonSeededSeedsOutIn.clone()
process.muonSeededSeedsOutIn8.src = cms.InputTag("earlyMuons"+layers)

process.muonSeededTrackCandidatesOutIn8 = process.muonSeededTrackCandidatesOutIn.clone()
process.muonSeededTrackCandidatesOutIn8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTrackCandidatesOutIn8.src = cms.InputTag("muonSeededSeedsOutIn"+layers)

process.muonSeededTracksOutIn8 = process.muonSeededTracksOutIn.clone()
process.muonSeededTracksOutIn8.MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+layers)
process.muonSeededTracksOutIn8.src = cms.InputTag("muonSeededTrackCandidatesOutIn"+layers)

process.muonSeededTracksInOutClassifier8 = process.muonSeededTracksInOutClassifier.clone()
process.muonSeededTracksInOutClassifier8.src = cms.InputTag("muonSeededTracksInOut"+layers)
process.muonSeededTracksInOutClassifier8.vertices = cms.InputTag("firstStepPrimaryVertices"+layers)

process.clusterSummaryProducer8 = process.clusterSummaryProducer.clone()
process.clusterSummaryProducer8.stripClusters = cms.InputTag("rCluster"+layers)

process.siStripMatchedRecHits8 = process.siStripMatchedRecHits.clone()
process.siStripMatchedRecHits8.ClusterProducer = cms.InputTag("rCluster"+layers)

process.reconstruction_trackingOnly_8layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.trackExtrapolator,process.trackExtrapolator8)
process.reconstruction_trackingOnly_8layers.replace(process.generalV0Candidates,process.generalV0Candidates8)
process.reconstruction_trackingOnly_8layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices8)
process.reconstruction_trackingOnly_8layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS8)
process.reconstruction_trackingOnly_8layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting8)
process.reconstruction_trackingOnly_8layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting8)
process.reconstruction_trackingOnly_8layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices8)
process.reconstruction_trackingOnly_8layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk8)
process.reconstruction_trackingOnly_8layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices8)
process.reconstruction_trackingOnly_8layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder8)
process.reconstruction_trackingOnly_8layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator8)
process.reconstruction_trackingOnly_8layers.replace(process.vertexMerger,process.vertexMerger8)
process.reconstruction_trackingOnly_8layers.replace(process.dedxHarmonic2,process.dedxHarmonic28)
process.reconstruction_trackingOnly_8layers.replace(process.dedxHitInfo,process.dedxHitInfo8)
process.reconstruction_trackingOnly_8layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0858)
process.reconstruction_trackingOnly_8layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic28)
process.reconstruction_trackingOnly_8layers.replace(process.dedxTruncated40,process.dedxTruncated408)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask8)
process.reconstruction_trackingOnly_8layers.replace(process.newCombinedSeeds,process.newCombinedSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions8)
process.reconstruction_trackingOnly_8layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask8)
process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets8)
process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.conversionStepTracks,process.conversionStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.trackerClusterCheck,process.trackerClusterCheck8)
process.reconstruction_trackingOnly_8layers.replace(process.convClusters,process.convClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.convLayerPairs,process.convLayerPairs8)
process.reconstruction_trackingOnly_8layers.replace(process.convStepSelector,process.convStepSelector8)
process.reconstruction_trackingOnly_8layers.replace(process.convStepTracks,process.convStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.convTrackCandidates,process.convTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg8)
process.reconstruction_trackingOnly_8layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent8)
process.reconstruction_trackingOnly_8layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits8)
process.reconstruction_trackingOnly_8layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache8)
process.reconstruction_trackingOnly_8layers.replace(process.siPixelClusters,process.siPixelClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.siPixelRecHits,process.siPixelRecHits8)
process.reconstruction_trackingOnly_8layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting8)
process.reconstruction_trackingOnly_8layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier8)
process.reconstruction_trackingOnly_8layers.replace(process.generalTracks,process.generalTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.earlyMuons,process.earlyMuons8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStep,process.detachedQuadStep8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStep,process.detachedTripletStep8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier18)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier28)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStep,process.highPtTripletStep8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices8)
process.reconstruction_trackingOnly_8layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStep,process.initialStep8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepClassifier1,process.initialStepClassifier18)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeeds,process.initialStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets8)
process.reconstruction_trackingOnly_8layers.replace(process.initialStepTracks,process.initialStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits8)
process.reconstruction_trackingOnly_8layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits8)
process.reconstruction_trackingOnly_8layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices8)
process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep8)
process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions8)
process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStep,process.lowPtQuadStep8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStep,process.lowPtTripletStep8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStep,process.mixedTripletStep8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier18)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier28)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStep,process.pixelLessStep8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier18)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier28)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTrackCandidatesMkFitConfig,process.pixelLessStepTrackCandidatesMkFitConfig8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStep,process.pixelPairStep8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB8)
process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStep,process.tobTecStep8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier18)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier28)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepClusters,process.tobTecStepClusters8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates8)
process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepTracks,process.tobTecStepTracks8)
process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier8)
process.reconstruction_trackingOnly_8layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut8)
process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut8)
process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut8)
process.reconstruction_trackingOnly_8layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn8)
process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn8)
process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn8)
process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier8)
process.reconstruction_trackingOnly_8layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer8)
process.reconstruction_trackingOnly_8layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits8)

####################################################################################################

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
process.reconstruction_step3 = cms.Path(process.reconstruction_trackingOnly_3layers)
process.reconstruction_step4 = cms.Path(process.reconstruction_trackingOnly_4layers)
process.reconstruction_step5 = cms.Path(process.reconstruction_trackingOnly_5layers)
process.reconstruction_step6 = cms.Path(process.reconstruction_trackingOnly_6layers)
process.reconstruction_step7 = cms.Path(process.reconstruction_trackingOnly_7layers)
process.reconstruction_step8 = cms.Path(process.reconstruction_trackingOnly_8layers)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
if options.layersThreshold==3: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.reconstruction_step3,process.endjob_step,process.RECOSIMoutput_step)
if options.layersThreshold==4: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.reconstruction_step4,process.endjob_step,process.RECOSIMoutput_step)
if options.layersThreshold==5: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.reconstruction_step5,process.endjob_step,process.RECOSIMoutput_step)
if options.layersThreshold==6: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.reconstruction_step6,process.endjob_step,process.RECOSIMoutput_step)
if options.layersThreshold==7: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.reconstruction_step7,process.endjob_step,process.RECOSIMoutput_step)
if options.layersThreshold==8: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.reconstruction_step8,process.endjob_step,process.RECOSIMoutput_step)
if options.layersThreshold<3 or options.layersThreshold>8: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.reconstruction_step3,process.reconstruction_step4,process.reconstruction_step5,process.reconstruction_step6,process.reconstruction_step7,process.reconstruction_step8,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

process.options.numberOfThreads = 8
process.options.numberOfStreams = 0
process.options.numberOfConcurrentLuminosityBlocks = 2
process.options.eventSetup.numberOfConcurrentIOVs = 1

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
