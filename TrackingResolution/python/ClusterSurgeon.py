import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.parseArguments()

process = cms.Process("HITREMOVER")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.options  = cms.untracked.PSet( wantSummary = cms.untracked.bool(True),
                                       SkipEvent = cms.untracked.vstring('ProductNotFound') )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring('/store/relval/CMSSW_10_2_5/RelValZMM_13/GEN-SIM-RECO/102X_upgrade2018_realistic_v15_ECAL-v1/10000/1C0857D9-797E-644E-AE5B-EC1366030FAA.root','/store/relval/CMSSW_10_2_5/RelValZMM_13/GEN-SIM-RECO/102X_upgrade2018_realistic_v15_ECAL-v1/10000/79886AFC-3CB7-A746-9054-325FD1E5084E.root')
#  fileNames = cms.untracked.vstring('/store/relval/CMSSW_12_0_0_pre3/RelValZMM_14/GEN-SIM-RECO/120X_mcRun3_2021_realistic_v1-v1/00000/50637e56-d8d6-4919-a170-62f0a2d8a434.root','/store/relval/CMSSW_12_0_0_pre3/RelValZMM_14/GEN-SIM-RECO/120X_mcRun3_2021_realistic_v1-v1/00000/7c700839-ec7c-4fed-aacd-8cd6a67e6894.root','/store/relval/CMSSW_12_0_0_pre3/RelValZMM_14/GEN-SIM-RECO/120X_mcRun3_2021_realistic_v1-v1/00000/e2725ab2-b22d-40d9-964e-2609ef8a8879.root')
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

#process.GlobalTag = GlobalTag(process.GlobalTag, '120X_mcRun3_2021_realistic_v1', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15','')

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outputFile),
    outputCommands = cms.untracked.vstring(
        'keep *',
        ),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p"))
 )

process.load("TrackingResolution.TrackingResolution.RClusterSeq_cff")

process.p = cms.Path(process.RClusterSeq)
process.e = cms.EndPath(process.out)
