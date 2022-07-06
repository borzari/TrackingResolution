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

#############################################################################################

#layers = options.layersThreshold
layers = 0
if options.layersThreshold<3 or options.layersThreshold>8: layers = 8
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

process.reconstruction_trackingOnly_3layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_4layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_5layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_6layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_7layers = process.reconstruction_trackingOnly.copy()
process.reconstruction_trackingOnly_8layers = process.reconstruction_trackingOnly.copy()

from TrackingResolution.TrackingResolution.ShortTrack import *

shortTrackModules(process,3) # 3 layers
shortTrackModules(process,4) # 4 layers
shortTrackModules(process,5) # 5 layers
shortTrackModules(process,6) # 6 layers
shortTrackModules(process,7) # 7 layers
shortTrackModules(process,8) # 8 layers
shortTrackTask(process)

##############################################################################################

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
#if options.layersThreshold<3 or options.layersThreshold>8: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.reconstruction_step3,process.reconstruction_step4,process.reconstruction_step5,process.reconstruction_step6,process.reconstruction_step7,process.reconstruction_step8,process.endjob_step,process.RECOSIMoutput_step)
if options.layersThreshold<3 or options.layersThreshold>8: process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step3,process.reconstruction_step4,process.reconstruction_step5,process.reconstruction_step6,process.reconstruction_step7,process.reconstruction_step8,process.endjob_step,process.RECOSIMoutput_step)

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
