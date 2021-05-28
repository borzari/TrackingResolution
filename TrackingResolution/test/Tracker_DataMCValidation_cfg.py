import sys, os
import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer

process = cms.Process('DQM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
  secondaryFileNames = cms.untracked.vstring(),
  fileNames = cms.untracked.vstring([
    'file:/afs/cern.ch/work/b/borzari/CMSSW_10_2_7/src/TrackingResolution/TrackingResolution/rereco_output.root'
  ])
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step1 nevts:1'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.DQMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('diffreco_test_step1_DQM_only3layers.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15', '')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Tracker Data MC validation suite
process.trackingResolution3 = DQMEDAnalyzer("TrackingResolution",
    moduleName        = cms.untracked.string("testTrackingResolution"),
    folderName        = cms.untracked.string("TrackRefitting"),
    hitsRemainInput        = cms.untracked.string("3"),
    minTracksEtaInput      = cms.untracked.double(0.0),
    maxTracksEtaInput      = cms.untracked.double(2.2),
    minTracksPtInput      = cms.untracked.double(15.0),
    maxTracksPtInput      = cms.untracked.double(99999.9),
    lowPtRegionInput      = cms.untracked.double(15.0),
    medPtRegionInput      = cms.untracked.double(30.0),
    higPtRegionInput      = cms.untracked.double(100.0),
    muonsInputTag     = cms.untracked.InputTag("muons", "", "RECO"),
    pfcandsInputTag     = cms.untracked.InputTag("particleFlow", "", "RECO"),
    tracksInputTag     = cms.untracked.InputTag("rCluster3", "", "HITREMOVER"),
    tracksRerecoInputTag     = cms.untracked.InputTag("generalTracks3", "", "reRECO")
)

process.trackingResolution4 = process.trackingResolution3.clone()
process.trackingResolution4.tracksInputTag=cms.untracked.InputTag("rCluster4", "", "HITREMOVER")
process.trackingResolution4.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks4", "", "reRECO")
process.trackingResolution4.hitsRemainInput=cms.untracked.string("4")

process.trackingResolution5 = process.trackingResolution3.clone()
process.trackingResolution5.tracksInputTag=cms.untracked.InputTag("rCluster5", "", "HITREMOVER")
process.trackingResolution5.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks5", "", "reRECO")
process.trackingResolution5.hitsRemainInput=cms.untracked.string("5")

process.trackingResolution6 = process.trackingResolution3.clone()
process.trackingResolution6.tracksInputTag=cms.untracked.InputTag("rCluster6", "", "HITREMOVER")
process.trackingResolution6.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks6", "", "reRECO")
process.trackingResolution6.hitsRemainInput=cms.untracked.string("6")

process.trackingResolution7 = process.trackingResolution3.clone()
process.trackingResolution7.tracksInputTag=cms.untracked.InputTag("rCluster7", "", "HITREMOVER")
process.trackingResolution7.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks7", "", "reRECO")
process.trackingResolution7.hitsRemainInput=cms.untracked.string("7")

process.trackingResolution8 = process.trackingResolution3.clone()
process.trackingResolution8.tracksInputTag=cms.untracked.InputTag("rCluster8", "", "HITREMOVER")
process.trackingResolution8.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks8", "", "reRECO")
process.trackingResolution8.hitsRemainInput=cms.untracked.string("8")

# Path and EndPath definitions
process.analysis_step = cms.Path(process.trackingResolution3*process.trackingResolution4*process.trackingResolution5*process.trackingResolution6*process.trackingResolution7*process.trackingResolution8)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.analysis_step, process.endjob_step, process.DQMoutput_step)
