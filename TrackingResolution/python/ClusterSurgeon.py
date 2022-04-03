import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.parseArguments()

process = cms.Process("HITREMOVER")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.options  = cms.untracked.PSet( wantSummary = cms.untracked.bool(True),
                                       SkipEvent = cms.untracked.vstring('ProductNotFound') )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(options.inputFiles)
)

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag

process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

process.out = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:'+options.outputFile),
    outputCommands = cms.untracked.vstring(
        'keep *',
        ),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p")),
    splitLevel = cms.untracked.int32(0)
 )

process.load("TrackingResolution.TrackingResolution.RClusterSeq_cff")

process.p = cms.Path(process.RClusterSeq)
process.e = cms.EndPath(process.out)
