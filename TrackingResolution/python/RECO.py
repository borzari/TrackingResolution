# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase1_2021_realistic --datatier GEN-SIM-RECO --era Run3 --eventcontent RAW --filein file:step2.root --fileout file:RECO_OUTPUT_FILE_NAME.root --geometry DB:Extended --no_exec --number 100 --python_filename RECO.py --step RAW2DIGI,RECO --customise Configuration/DataProcessing/Utils.addMonitoring
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

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

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/123X_mcRun3_2021_realistic_v6-v1/10000/50b8cfdc-28dc-49b9-8946-c80591591409.root','/store/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/123X_mcRun3_2021_realistic_v6-v1/10000/66e32473-360e-44d8-b47d-312aaafd33bf.root','/store/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/123X_mcRun3_2021_realistic_v6-v1/10000/aafc1a81-5bbf-490a-aeba-4aaf1b984efc.root','/store/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/123X_mcRun3_2021_realistic_v6-v1/10000/c98b1e8c-bc95-41a5-bef2-858d64a8ebe2.root','/store/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/123X_mcRun3_2021_realistic_v6-v1/10000/c9ca5296-c83f-4e61-a5c1-bacafd198d9e.root','/store/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/123X_mcRun3_2021_realistic_v6-v1/10000/e0d81200-bf3c-4dd4-8d2a-e3dcd75f8a30.root','/store/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-DIGI-RAW/123X_mcRun3_2021_realistic_v6-v1/10000/ed0f8033-84ce-4834-a5db-c5326f5bfb20.root'),
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

process.RAWoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:RECO_'+options.outputFile),
    outputCommands = process.RAWEventContent.outputCommands+[
        'keep *_*_bunchSpacing_*',
        'keep *_*generalTracks*_*_RECO',
        'keep recoMuons_muons_*_RECO',
        'keep *_offlinePrimaryVertices*_*_RECO',
        'keep *_si*Clusters_*_RECO'
    ],
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWoutput_step = cms.EndPath(process.RAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RAWoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

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
