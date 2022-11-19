import sys, os
import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')

options.register ('layersThreshold',
                  3, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.int,          # string, int, or float
                  "Number of threshold layers (from 3 to 8 so far)")

options.parseArguments()

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

filenames = []

for i in range(1):
    filenames.append('file:/eos/user/b/borzari/TrackingRootFile/test_usualReRECO_definitive_allRECO_reRECO_'+str(options.layersThreshold)+'layers_'+options.inputFiles[i]+'.root')

# Input source
process.source = cms.Source("PoolSource",
  secondaryFileNames = cms.untracked.vstring(),
  fileNames = cms.untracked.vstring(
    filenames
  )
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
    fileName = cms.untracked.string('file:test_usualReRECO_definitive_allRECO_DQM_'+str(options.layersThreshold)+'layers_'+options.outputFile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic', '')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

layers = 0
if options.layersThreshold<3 or options.layersThreshold>8: layers = 8
else: layers = options.layersThreshold

myCollection = "rCluster"+str(layers)

# Tracker Data MC validation suite
process.trackingResolution = DQMEDAnalyzer("TrackingResolutionMod",
    moduleName        = cms.untracked.string("testTrackingResolution"),
    folderName        = cms.untracked.string("TrackRefitting"),
    hitsRemainInput        = cms.untracked.string(str(layers)),
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
    tracksInputTag     = cms.untracked.InputTag(myCollection, "", "RECO"),
    primVertexInputTag = cms.untracked.InputTag("offlinePrimaryVertices", "", "RECO"),
    tracksRerecoInputTag     = cms.untracked.InputTag("generalTracks", "", "reRECO"),
    initialStepRerecoInputTag     = cms.untracked.InputTag("initialStepTracks", "", "reRECO"),
    highPtTripletStepRerecoInputTag     = cms.untracked.InputTag("highPtTripletStepTracks", "", "reRECO"),
    jetCoreRegionalStepRerecoInputTag     = cms.untracked.InputTag("jetCoreRegionalStepTracks", "", "reRECO"),
    lowPtQuadStepRerecoInputTag     = cms.untracked.InputTag("lowPtQuadStepTracks", "", "reRECO"),
    lowPtTripletStepRerecoInputTag     = cms.untracked.InputTag("lowPtTripletStepTracks", "", "reRECO"),
    detachedQuadStepRerecoInputTag     = cms.untracked.InputTag("detachedQuadStepTracks", "", "reRECO"),
    detachedTripletStepRerecoInputTag     = cms.untracked.InputTag("detachedTripletStepTracks", "", "reRECO"),
    pixelPairStepRerecoInputTag     = cms.untracked.InputTag("pixelPairStepTracks", "", "reRECO"),
    mixedTripletStepRerecoInputTag     = cms.untracked.InputTag("mixedTripletStepTracks", "", "reRECO"),
    pixelLessStepRerecoInputTag     = cms.untracked.InputTag("pixelLessStepTracks", "", "reRECO"),
    tobTecStepRerecoInputTag     = cms.untracked.InputTag("tobTecStepTracks", "", "reRECO"),
    muonSeededTracksInOutRerecoInputTag     = cms.untracked.InputTag("muonSeededTracksInOut", "", "reRECO"),
    muonSeededTracksOutInRerecoInputTag     = cms.untracked.InputTag("muonSeededTracksOutIn", "", "reRECO"),
    earlyGeneralTracksRerecoInputTag     = cms.untracked.InputTag("earlyGeneralTracks", "", "reRECO"),
    preDuplicateMergingGeneralTracksRerecoInputTag     = cms.untracked.InputTag("preDuplicateMergingGeneralTracks", "", "reRECO"),
    mergedDuplicateTracksRerecoInputTag     = cms.untracked.InputTag("mergedDuplicateTracks", "", "reRECO")
)

process.trackingResolution3 = process.trackingResolution.clone()
process.trackingResolution3.tracksInputTag=cms.untracked.InputTag("rCluster3", "", "RECO")
process.trackingResolution3.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks3", "", "reRECO")
process.trackingResolution3.hitsRemainInput=cms.untracked.string("3")
process.trackingResolution3.initialStepRerecoInputTag=cms.untracked.InputTag("initialStepTracks3", "", "reRECO")
process.trackingResolution3.highPtTripletStepRerecoInputTag=cms.untracked.InputTag("highPtTripletStepTracks3", "", "reRECO")
process.trackingResolution3.jetCoreRegionalStepRerecoInputTag=cms.untracked.InputTag("jetCoreRegionalStepTracks3", "", "reRECO")
process.trackingResolution3.lowPtQuadStepRerecoInputTag=cms.untracked.InputTag("lowPtQuadStepTracks3", "", "reRECO")
process.trackingResolution3.lowPtTripletStepRerecoInputTag=cms.untracked.InputTag("lowPtTripletStepTracks3", "", "reRECO")
process.trackingResolution3.detachedQuadStepRerecoInputTag=cms.untracked.InputTag("detachedQuadStepTracks3", "", "reRECO")
process.trackingResolution3.detachedTripletStepRerecoInputTag=cms.untracked.InputTag("detachedTripletStepTracks3", "", "reRECO")
process.trackingResolution3.pixelPairStepRerecoInputTag=cms.untracked.InputTag("pixelPairStepTracks3", "", "reRECO")
process.trackingResolution3.mixedTripletStepRerecoInputTag=cms.untracked.InputTag("mixedTripletStepTracks3", "", "reRECO")
process.trackingResolution3.pixelLessStepRerecoInputTag=cms.untracked.InputTag("pixelLessStepTracks3", "", "reRECO")
process.trackingResolution3.tobTecStepRerecoInputTag=cms.untracked.InputTag("tobTecStepTracks3", "", "reRECO")
process.trackingResolution3.muonSeededTracksInOutRerecoInputTag=cms.untracked.InputTag("muonSeededTracksInOut3", "", "reRECO")
process.trackingResolution3.muonSeededTracksOutInRerecoInputTag=cms.untracked.InputTag("muonSeededTracksOutIn3", "", "reRECO")
process.trackingResolution3.earlyGeneralTracksRerecoInputTag=cms.untracked.InputTag("earlyGeneralTracks3", "", "reRECO")
process.trackingResolution3.preDuplicateMergingGeneralTracksRerecoInputTag=cms.untracked.InputTag("preDuplicateMergingGeneralTracks3", "", "reRECO")
process.trackingResolution3.mergedDuplicateTracksRerecoInputTag=cms.untracked.InputTag("mergedDuplicateTracks3", "", "reRECO")

process.trackingResolution4 = process.trackingResolution3.clone()
process.trackingResolution4.tracksInputTag=cms.untracked.InputTag("rCluster4", "", "RECO")
process.trackingResolution4.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks4", "", "reRECO")
process.trackingResolution4.hitsRemainInput=cms.untracked.string("4")
process.trackingResolution4.initialStepRerecoInputTag=cms.untracked.InputTag("initialStepTracks4", "", "reRECO")
process.trackingResolution4.highPtTripletStepRerecoInputTag=cms.untracked.InputTag("highPtTripletStepTracks4", "", "reRECO")
process.trackingResolution4.jetCoreRegionalStepRerecoInputTag=cms.untracked.InputTag("jetCoreRegionalStepTracks4", "", "reRECO")
process.trackingResolution4.lowPtQuadStepRerecoInputTag=cms.untracked.InputTag("lowPtQuadStepTracks4", "", "reRECO")
process.trackingResolution4.lowPtTripletStepRerecoInputTag=cms.untracked.InputTag("lowPtTripletStepTracks4", "", "reRECO")
process.trackingResolution4.detachedQuadStepRerecoInputTag=cms.untracked.InputTag("detachedQuadStepTracks4", "", "reRECO")
process.trackingResolution4.detachedTripletStepRerecoInputTag=cms.untracked.InputTag("detachedTripletStepTracks4", "", "reRECO")
process.trackingResolution4.pixelPairStepRerecoInputTag=cms.untracked.InputTag("pixelPairStepTracks4", "", "reRECO")
process.trackingResolution4.mixedTripletStepRerecoInputTag=cms.untracked.InputTag("mixedTripletStepTracks4", "", "reRECO")
process.trackingResolution4.pixelLessStepRerecoInputTag=cms.untracked.InputTag("pixelLessStepTracks4", "", "reRECO")
process.trackingResolution4.tobTecStepRerecoInputTag=cms.untracked.InputTag("tobTecStepTracks4", "", "reRECO")
process.trackingResolution4.muonSeededTracksInOutRerecoInputTag=cms.untracked.InputTag("muonSeededTracksInOut4", "", "reRECO")
process.trackingResolution4.muonSeededTracksOutInRerecoInputTag=cms.untracked.InputTag("muonSeededTracksOutIn4", "", "reRECO")
process.trackingResolution4.earlyGeneralTracksRerecoInputTag=cms.untracked.InputTag("earlyGeneralTracks4", "", "reRECO")
process.trackingResolution4.preDuplicateMergingGeneralTracksRerecoInputTag=cms.untracked.InputTag("preDuplicateMergingGeneralTracks4", "", "reRECO")
process.trackingResolution4.mergedDuplicateTracksRerecoInputTag=cms.untracked.InputTag("mergedDuplicateTracks4", "", "reRECO")

process.trackingResolution5 = process.trackingResolution3.clone()
process.trackingResolution5.tracksInputTag=cms.untracked.InputTag("rCluster5", "", "RECO")
process.trackingResolution5.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks5", "", "reRECO")
process.trackingResolution5.hitsRemainInput=cms.untracked.string("5")
process.trackingResolution5.initialStepRerecoInputTag=cms.untracked.InputTag("initialStepTracks5", "", "reRECO")
process.trackingResolution5.highPtTripletStepRerecoInputTag=cms.untracked.InputTag("highPtTripletStepTracks5", "", "reRECO")
process.trackingResolution5.jetCoreRegionalStepRerecoInputTag=cms.untracked.InputTag("jetCoreRegionalStepTracks5", "", "reRECO")
process.trackingResolution5.lowPtQuadStepRerecoInputTag=cms.untracked.InputTag("lowPtQuadStepTracks5", "", "reRECO")
process.trackingResolution5.lowPtTripletStepRerecoInputTag=cms.untracked.InputTag("lowPtTripletStepTracks5", "", "reRECO")
process.trackingResolution5.detachedQuadStepRerecoInputTag=cms.untracked.InputTag("detachedQuadStepTracks5", "", "reRECO")
process.trackingResolution5.detachedTripletStepRerecoInputTag=cms.untracked.InputTag("detachedTripletStepTracks5", "", "reRECO")
process.trackingResolution5.pixelPairStepRerecoInputTag=cms.untracked.InputTag("pixelPairStepTracks5", "", "reRECO")
process.trackingResolution5.mixedTripletStepRerecoInputTag=cms.untracked.InputTag("mixedTripletStepTracks5", "", "reRECO")
process.trackingResolution5.pixelLessStepRerecoInputTag=cms.untracked.InputTag("pixelLessStepTracks5", "", "reRECO")
process.trackingResolution5.tobTecStepRerecoInputTag=cms.untracked.InputTag("tobTecStepTracks5", "", "reRECO")
process.trackingResolution5.muonSeededTracksInOutRerecoInputTag=cms.untracked.InputTag("muonSeededTracksInOut5", "", "reRECO")
process.trackingResolution5.muonSeededTracksOutInRerecoInputTag=cms.untracked.InputTag("muonSeededTracksOutIn5", "", "reRECO")
process.trackingResolution5.earlyGeneralTracksRerecoInputTag=cms.untracked.InputTag("earlyGeneralTracks5", "", "reRECO")
process.trackingResolution5.preDuplicateMergingGeneralTracksRerecoInputTag=cms.untracked.InputTag("preDuplicateMergingGeneralTracks5", "", "reRECO")
process.trackingResolution5.mergedDuplicateTracksRerecoInputTag=cms.untracked.InputTag("mergedDuplicateTracks5", "", "reRECO")

process.trackingResolution6 = process.trackingResolution3.clone()
process.trackingResolution6.tracksInputTag=cms.untracked.InputTag("rCluster6", "", "RECO")
process.trackingResolution6.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks6", "", "reRECO")
process.trackingResolution6.hitsRemainInput=cms.untracked.string("6")
process.trackingResolution6.initialStepRerecoInputTag=cms.untracked.InputTag("initialStepTracks6", "", "reRECO")
process.trackingResolution6.highPtTripletStepRerecoInputTag=cms.untracked.InputTag("highPtTripletStepTracks6", "", "reRECO")
process.trackingResolution6.jetCoreRegionalStepRerecoInputTag=cms.untracked.InputTag("jetCoreRegionalStepTracks6", "", "reRECO")
process.trackingResolution6.lowPtQuadStepRerecoInputTag=cms.untracked.InputTag("lowPtQuadStepTracks6", "", "reRECO")
process.trackingResolution6.lowPtTripletStepRerecoInputTag=cms.untracked.InputTag("lowPtTripletStepTracks6", "", "reRECO")
process.trackingResolution6.detachedQuadStepRerecoInputTag=cms.untracked.InputTag("detachedQuadStepTracks6", "", "reRECO")
process.trackingResolution6.detachedTripletStepRerecoInputTag=cms.untracked.InputTag("detachedTripletStepTracks6", "", "reRECO")
process.trackingResolution6.pixelPairStepRerecoInputTag=cms.untracked.InputTag("pixelPairStepTracks6", "", "reRECO")
process.trackingResolution6.mixedTripletStepRerecoInputTag=cms.untracked.InputTag("mixedTripletStepTracks6", "", "reRECO")
process.trackingResolution6.pixelLessStepRerecoInputTag=cms.untracked.InputTag("pixelLessStepTracks6", "", "reRECO")
process.trackingResolution6.tobTecStepRerecoInputTag=cms.untracked.InputTag("tobTecStepTracks6", "", "reRECO")
process.trackingResolution6.muonSeededTracksInOutRerecoInputTag=cms.untracked.InputTag("muonSeededTracksInOut6", "", "reRECO")
process.trackingResolution6.muonSeededTracksOutInRerecoInputTag=cms.untracked.InputTag("muonSeededTracksOutIn6", "", "reRECO")
process.trackingResolution6.earlyGeneralTracksRerecoInputTag=cms.untracked.InputTag("earlyGeneralTracks6", "", "reRECO")
process.trackingResolution6.preDuplicateMergingGeneralTracksRerecoInputTag=cms.untracked.InputTag("preDuplicateMergingGeneralTracks6", "", "reRECO")
process.trackingResolution6.mergedDuplicateTracksRerecoInputTag=cms.untracked.InputTag("mergedDuplicateTracks6", "", "reRECO")

process.trackingResolution7 = process.trackingResolution3.clone()
process.trackingResolution7.tracksInputTag=cms.untracked.InputTag("rCluster7", "", "RECO")
process.trackingResolution7.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks7", "", "reRECO")
process.trackingResolution7.hitsRemainInput=cms.untracked.string("7")
process.trackingResolution7.initialStepRerecoInputTag=cms.untracked.InputTag("initialStepTracks7", "", "reRECO")
process.trackingResolution7.highPtTripletStepRerecoInputTag=cms.untracked.InputTag("highPtTripletStepTracks7", "", "reRECO")
process.trackingResolution7.jetCoreRegionalStepRerecoInputTag=cms.untracked.InputTag("jetCoreRegionalStepTracks7", "", "reRECO")
process.trackingResolution7.lowPtQuadStepRerecoInputTag=cms.untracked.InputTag("lowPtQuadStepTracks7", "", "reRECO")
process.trackingResolution7.lowPtTripletStepRerecoInputTag=cms.untracked.InputTag("lowPtTripletStepTracks7", "", "reRECO")
process.trackingResolution7.detachedQuadStepRerecoInputTag=cms.untracked.InputTag("detachedQuadStepTracks7", "", "reRECO")
process.trackingResolution7.detachedTripletStepRerecoInputTag=cms.untracked.InputTag("detachedTripletStepTracks7", "", "reRECO")
process.trackingResolution7.pixelPairStepRerecoInputTag=cms.untracked.InputTag("pixelPairStepTracks7", "", "reRECO")
process.trackingResolution7.mixedTripletStepRerecoInputTag=cms.untracked.InputTag("mixedTripletStepTracks7", "", "reRECO")
process.trackingResolution7.pixelLessStepRerecoInputTag=cms.untracked.InputTag("pixelLessStepTracks7", "", "reRECO")
process.trackingResolution7.tobTecStepRerecoInputTag=cms.untracked.InputTag("tobTecStepTracks7", "", "reRECO")
process.trackingResolution7.muonSeededTracksInOutRerecoInputTag=cms.untracked.InputTag("muonSeededTracksInOut7", "", "reRECO")
process.trackingResolution7.muonSeededTracksOutInRerecoInputTag=cms.untracked.InputTag("muonSeededTracksOutIn7", "", "reRECO")
process.trackingResolution7.earlyGeneralTracksRerecoInputTag=cms.untracked.InputTag("earlyGeneralTracks7", "", "reRECO")
process.trackingResolution7.preDuplicateMergingGeneralTracksRerecoInputTag=cms.untracked.InputTag("preDuplicateMergingGeneralTracks7", "", "reRECO")
process.trackingResolution7.mergedDuplicateTracksRerecoInputTag=cms.untracked.InputTag("mergedDuplicateTracks7", "", "reRECO")

process.trackingResolution8 = process.trackingResolution3.clone()
process.trackingResolution8.tracksInputTag=cms.untracked.InputTag("rCluster8", "", "RECO")
process.trackingResolution8.tracksRerecoInputTag=cms.untracked.InputTag("generalTracks8", "", "reRECO")
process.trackingResolution8.hitsRemainInput=cms.untracked.string("8")
process.trackingResolution8.initialStepRerecoInputTag=cms.untracked.InputTag("initialStepTracks8", "", "reRECO")
process.trackingResolution8.highPtTripletStepRerecoInputTag=cms.untracked.InputTag("highPtTripletStepTracks8", "", "reRECO")
process.trackingResolution8.jetCoreRegionalStepRerecoInputTag=cms.untracked.InputTag("jetCoreRegionalStepTracks8", "", "reRECO")
process.trackingResolution8.lowPtQuadStepRerecoInputTag=cms.untracked.InputTag("lowPtQuadStepTracks8", "", "reRECO")
process.trackingResolution8.lowPtTripletStepRerecoInputTag=cms.untracked.InputTag("lowPtTripletStepTracks8", "", "reRECO")
process.trackingResolution8.detachedQuadStepRerecoInputTag=cms.untracked.InputTag("detachedQuadStepTracks8", "", "reRECO")
process.trackingResolution8.detachedTripletStepRerecoInputTag=cms.untracked.InputTag("detachedTripletStepTracks8", "", "reRECO")
process.trackingResolution8.pixelPairStepRerecoInputTag=cms.untracked.InputTag("pixelPairStepTracks8", "", "reRECO")
process.trackingResolution8.mixedTripletStepRerecoInputTag=cms.untracked.InputTag("mixedTripletStepTracks8", "", "reRECO")
process.trackingResolution8.pixelLessStepRerecoInputTag=cms.untracked.InputTag("pixelLessStepTracks8", "", "reRECO")
process.trackingResolution8.tobTecStepRerecoInputTag=cms.untracked.InputTag("tobTecStepTracks8", "", "reRECO")
process.trackingResolution8.muonSeededTracksInOutRerecoInputTag=cms.untracked.InputTag("muonSeededTracksInOut8", "", "reRECO")
process.trackingResolution8.muonSeededTracksOutInRerecoInputTag=cms.untracked.InputTag("muonSeededTracksOutIn8", "", "reRECO")
process.trackingResolution8.earlyGeneralTracksRerecoInputTag=cms.untracked.InputTag("earlyGeneralTracks8", "", "reRECO")
process.trackingResolution8.preDuplicateMergingGeneralTracksRerecoInputTag=cms.untracked.InputTag("preDuplicateMergingGeneralTracks8", "", "reRECO")
process.trackingResolution8.mergedDuplicateTracksRerecoInputTag=cms.untracked.InputTag("mergedDuplicateTracks8", "", "reRECO")

# Path and EndPath definitions
# if options.layersThreshold==3: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution3)
# if options.layersThreshold==4: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution4)
# if options.layersThreshold==5: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution5)
# if options.layersThreshold==6: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution6)
# if options.layersThreshold==7: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution7)
# if options.layersThreshold==8: process.analysis_step = cms.Path(process.trackingResolution*process.trackingResolution8)

# if options.layersThreshold==3: process.analysis_step = cms.Path(process.trackingResolution3)
# if options.layersThreshold==4: process.analysis_step = cms.Path(process.trackingResolution4)
# if options.layersThreshold==5: process.analysis_step = cms.Path(process.trackingResolution5)
# if options.layersThreshold==6: process.analysis_step = cms.Path(process.trackingResolution6)
# if options.layersThreshold==7: process.analysis_step = cms.Path(process.trackingResolution7)
# if options.layersThreshold==8: process.analysis_step = cms.Path(process.trackingResolution8)

if options.layersThreshold<3 or options.layersThreshold>8: process.analysis_step = cms.Path(process.trackingResolution3*process.trackingResolution4*process.trackingResolution5*process.trackingResolution6*process.trackingResolution7*process.trackingResolution8)
else: process.analysis_step = cms.Path(process.trackingResolution)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.analysis_step, process.endjob_step, process.DQMoutput_step)
