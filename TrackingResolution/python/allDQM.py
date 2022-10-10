# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase1_2022_realistic --datatier GEN-SIM-RECO --era Run3 --eventcontent RAW --filein file:step2.root --fileout file:RECO_OUTPUT_FILE_NAME.root --geometry DB:Extended --no_exec --number 100 --python_filename RECO.py --step RAW2DIGI,RECO --customise Configuration/DataProcessing/Utils.addMonitoring
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer

options = VarParsing('analysis')
options.parseArguments()

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('RECO',Run3)

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
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:file.root'),
    secondaryFileNames = cms.untracked.vstring()
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
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.DQMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('file:allDQM_'+options.outputFile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

process.load("TrackingResolution.TrackingResolution.RClusterSeq_cff")

process.p = cms.Path(process.RClusterSeq)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic', '')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

#################################################################################################################

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

#################################################################################################################

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.reconstruction_step3 = cms.Path(process.reconstruction_trackingOnly_3layers)
process.reconstruction_step4 = cms.Path(process.reconstruction_trackingOnly_4layers)
process.reconstruction_step5 = cms.Path(process.reconstruction_trackingOnly_5layers)
process.reconstruction_step6 = cms.Path(process.reconstruction_trackingOnly_6layers)
process.reconstruction_step7 = cms.Path(process.reconstruction_trackingOnly_7layers)
process.reconstruction_step8 = cms.Path(process.reconstruction_trackingOnly_8layers)
process.endjob_step = cms.EndPath(process.endOfProcess)

#################################################################################################################

# Tracker Data MC validation suite
process.trackingResolution = DQMEDAnalyzer("TrackingResolution",
    moduleName        = cms.untracked.string("testTrackingResolution"),
    folderName        = cms.untracked.string("TrackRefitting"),
    hitsRemainInput        = cms.untracked.string("0"),
    minTracksEtaInput      = cms.untracked.double(0.0),
    maxTracksEtaInput      = cms.untracked.double(2.2),
    minTracksPtInput      = cms.untracked.double(15.0),
    maxTracksPtInput      = cms.untracked.double(99999.9),
    lowPtRegionInput      = cms.untracked.double(15.0),
    medPtRegionInput      = cms.untracked.double(30.0),
    higPtRegionInput      = cms.untracked.double(100.0),
    maxDxyInput      = cms.untracked.double(0.2),
    maxDzInput      = cms.untracked.double(0.1),
    maxDrInput      = cms.untracked.double(0.01),
    minNumberOfLayersInput      = cms.untracked.int32(10),
    muonsInputTag     = cms.untracked.InputTag("muons", "", "RECO"),
    tracksInputTag     = cms.untracked.InputTag("rCluster3", "", "RECO"),
    primVertexInputTag = cms.untracked.InputTag("offlinePrimaryVertices", "", "RECO"),
    tracksRerecoInputTag     = cms.untracked.InputTag("generalTracks", "", "RECO")
)

process.trackingResolution3 = process.trackingResolution.clone()
process.trackingResolution3.tracksInputTag=cms.untracked.InputTag("rCluster3", "", "RECO")
process.trackingResolution3.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks3", "", "RECO")
process.trackingResolution3.hitsRemainInput=cms.untracked.string("3")

process.trackingResolution4 = process.trackingResolution3.clone()
process.trackingResolution4.tracksInputTag=cms.untracked.InputTag("rCluster4", "", "RECO")
process.trackingResolution4.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks4", "", "RECO")
process.trackingResolution4.hitsRemainInput=cms.untracked.string("4")

process.trackingResolution5 = process.trackingResolution3.clone()
process.trackingResolution5.tracksInputTag=cms.untracked.InputTag("rCluster5", "", "RECO")
process.trackingResolution5.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks5", "", "RECO")
process.trackingResolution5.hitsRemainInput=cms.untracked.string("5")

process.trackingResolution6 = process.trackingResolution3.clone()
process.trackingResolution6.tracksInputTag=cms.untracked.InputTag("rCluster6", "", "RECO")
process.trackingResolution6.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks6", "", "RECO")
process.trackingResolution6.hitsRemainInput=cms.untracked.string("6")

process.trackingResolution7 = process.trackingResolution3.clone()
process.trackingResolution7.tracksInputTag=cms.untracked.InputTag("rCluster7", "", "RECO")
process.trackingResolution7.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks7", "", "RECO")
process.trackingResolution7.hitsRemainInput=cms.untracked.string("7")

process.trackingResolution8 = process.trackingResolution3.clone()
process.trackingResolution8.tracksInputTag=cms.untracked.InputTag("rCluster8", "", "RECO")
process.trackingResolution8.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks8", "", "RECO")
process.trackingResolution8.hitsRemainInput=cms.untracked.string("8")

# Path and EndPath definitions
#if options.layersThreshold==3: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution3)
#if options.layersThreshold==4: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution4)
#if options.layersThreshold==5: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution5)
#if options.layersThreshold==6: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution6)
#if options.layersThreshold==7: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution7)
#if options.layersThreshold==8: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution8)
process.analysis_step = cms.Path(process.trackingResolution3*process.trackingResolution4*process.trackingResolution5*process.trackingResolution6*process.trackingResolution7*process.trackingResolution8)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

#################################################################################################################

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.p,process.reconstruction_step3,process.reconstruction_step4,process.reconstruction_step5,process.reconstruction_step6,process.reconstruction_step7,process.reconstruction_step8,process.analysis_step,process.endjob_step,process.DQMoutput_step)
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
