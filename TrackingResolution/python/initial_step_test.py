import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
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

#myCollection = "rCluster3"
process = cms.Process("reRECO",eras.Run2_2018)

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

from PhysicsTools.PatAlgos.tools.helpers import *

process.load("RecoTracker.Configuration.RecoTracker_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('RecoLocalCalo.Configuration.RecoLocalCalo_cff')
process.load('RecoJets.Configuration.CaloTowersRec_cff')
process.load('RecoVertex.Configuration.RecoVertex_cff')
process.load('RecoTracker.FinalTrackSelectors.MergeTrackCollections_cff')

process.earlyGeneralTracks = process.earlyGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'initialStep',
        'highPtTripletStep',
        'lowPtQuadStep',
        'lowPtTripletStep'
    ),
    trackProducers = cms.VInputTag(
        "initialStepTracks", "highPtTripletStepTracks", "lowPtQuadStepTracks", "lowPtTripletStepTracks",
    )
)

process.preDuplicateMergingGeneralTracks = process.preDuplicateMergingGeneralTracks.clone(
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks'
    ),
    trackProducers = cms.VInputTag("earlyGeneralTracks")
)

process.GlobalTag = process.GlobalTag.clone(
    globaltag = cms.string('102X_upgrade2018_realistic_v15')
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

#process.reconstruction_step_track = cms.Path(cms.Task(process.LowPtQuadStepTask,process.HighPtTripletStepTask,process.LowPtTripletStepTask,process.InitialStepTask,process.generalTracksTask,process.earlyGeneralTracks,process.preDuplicateMergingGeneralTracks,process.trackerClusterCheck,process.siPixelRecHits,process.siPixelClusterShapeCache,process.MeasurementTrackerEvent))

#process.endjob_step = cms.EndPath(cms.Task(process.MEtoEDMConverter))

#process.RECOoutput_step = cms.EndPath(process.RECOoutput)

#process.schedule = cms.Schedule(*[ process.reconstruction_step_track, process.endjob_step, process.RECOoutput_step ])

cloneProcessingSnippet(process, process.trackingGlobalReco, "3")
cloneProcessingSnippet(process, process.InitialStep, "3")
cloneProcessingSnippet(process, process.HighPtTripletStep, "3")
cloneProcessingSnippet(process, process.LowPtTripletStep, "3")
cloneProcessingSnippet(process, process.LowPtQuadStep, "3")
cloneProcessingSnippet(process, process.generalTracksSequence, "3")

cloneProcessingSnippet(process, process.trackingGlobalReco, "4")
cloneProcessingSnippet(process, process.InitialStep, "4")
cloneProcessingSnippet(process, process.HighPtTripletStep, "4")
cloneProcessingSnippet(process, process.LowPtTripletStep, "4")
cloneProcessingSnippet(process, process.LowPtQuadStep, "4")
cloneProcessingSnippet(process, process.generalTracksSequence, "4")

cloneProcessingSnippet(process, process.trackingGlobalReco, "5")
cloneProcessingSnippet(process, process.InitialStep, "5")
cloneProcessingSnippet(process, process.HighPtTripletStep, "5")
cloneProcessingSnippet(process, process.LowPtTripletStep, "5")
cloneProcessingSnippet(process, process.LowPtQuadStep, "5")
cloneProcessingSnippet(process, process.generalTracksSequence, "5")

cloneProcessingSnippet(process, process.trackingGlobalReco, "6")
cloneProcessingSnippet(process, process.InitialStep, "6")
cloneProcessingSnippet(process, process.HighPtTripletStep, "6")
cloneProcessingSnippet(process, process.LowPtTripletStep, "6")
cloneProcessingSnippet(process, process.LowPtQuadStep, "6")
cloneProcessingSnippet(process, process.generalTracksSequence, "6")

cloneProcessingSnippet(process, process.trackingGlobalReco, "7")
cloneProcessingSnippet(process, process.InitialStep, "7")
cloneProcessingSnippet(process, process.HighPtTripletStep, "7")
cloneProcessingSnippet(process, process.LowPtTripletStep, "7")
cloneProcessingSnippet(process, process.LowPtQuadStep, "7")
cloneProcessingSnippet(process, process.generalTracksSequence, "7")

cloneProcessingSnippet(process, process.trackingGlobalReco, "8")
cloneProcessingSnippet(process, process.InitialStep, "8")
cloneProcessingSnippet(process, process.HighPtTripletStep, "8")
cloneProcessingSnippet(process, process.LowPtTripletStep, "8")
cloneProcessingSnippet(process, process.LowPtQuadStep, "8")
cloneProcessingSnippet(process, process.generalTracksSequence, "8")

#process.reconstruction_step_track3 = cms.Path(cms.Task(process.HighPtTripletStep3, process.InitialStep3, process.LowPtQuadStep3, process.LowPtTripletStep3, process.MeasurementTrackerEvent3, process.earlyGeneralTracks3, process.generalTracks3, process.preDuplicateMergingGeneralTracks3, process.siPixelClusterShapeCache3, process.siPixelRecHits3, process.trackerClusterCheck3))

#process.reconstruction_step_track4 = cms.Path(cms.Task(process.HighPtTripletStep4, process.InitialStep4, process.LowPtQuadStep4, process.LowPtTripletStep4, process.MeasurementTrackerEvent4, process.earlyGeneralTracks4, process.generalTracks4, process.preDuplicateMergingGeneralTracks4, process.siPixelClusterShapeCache4, process.siPixelRecHits4, process.trackerClusterCheck4))

#process.reconstruction_step_track5 = cms.Path(cms.Task(process.HighPtTripletStep5, process.InitialStep5, process.LowPtQuadStep5, process.LowPtTripletStep5, process.MeasurementTrackerEvent5, process.earlyGeneralTracks5, process.generalTracks5, process.preDuplicateMergingGeneralTracks5, process.siPixelClusterShapeCache5, process.siPixelRecHits5, process.trackerClusterCheck5))

#process.reconstruction_step_track6 = cms.Path(cms.Task(process.HighPtTripletStep6, process.InitialStep6, process.LowPtQuadStep6, process.LowPtTripletStep6, process.MeasurementTrackerEvent6, process.earlyGeneralTracks6, process.generalTracks6, process.preDuplicateMergingGeneralTracks6, process.siPixelClusterShapeCache6, process.siPixelRecHits6, process.trackerClusterCheck6))

#process.reconstruction_step_track7 = cms.Path(cms.Task(process.HighPtTripletStep7, process.InitialStep7, process.LowPtQuadStep7, process.LowPtTripletStep7, process.MeasurementTrackerEvent7, process.earlyGeneralTracks7, process.generalTracks7, process.preDuplicateMergingGeneralTracks7, process.siPixelClusterShapeCache7, process.siPixelRecHits7, process.trackerClusterCheck7))

#process.reconstruction_step_track8 = cms.Path(cms.Task(process.HighPtTripletStep8, process.InitialStep8, process.LowPtQuadStep8, process.LowPtTripletStep8, process.MeasurementTrackerEvent8, process.earlyGeneralTracks8, process.generalTracks8, process.preDuplicateMergingGeneralTracks8, process.siPixelClusterShapeCache8, process.siPixelRecHits8, process.trackerClusterCheck8))

#process.reconstruction_step_track3 = cms.Path(process.HighPtTripletStep3+ process.InitialStep3+ process.LowPtQuadStep3+ process.LowPtTripletStep3+ process.MeasurementTrackerEvent3+ process.earlyGeneralTracks3+ process.generalTracks3+ process.preDuplicateMergingGeneralTracks3+ process.siPixelClusterShapeCache3+ process.siPixelRecHits3+ process.trackerClusterCheck3)

process.reconstruction_step_track3 = cms.Path(process.siPixelRecHits3+process.siPixelClusterShapeCache3+process.InitialStep3+process.HighPtTripletStep3+process.LowPtQuadStep3+process.LowPtTripletStep3+process.earlyGeneralTracks3+process.preDuplicateMergingGeneralTracks3+process.generalTracks3+process.MeasurementTrackerEvent3+process.trackerClusterCheck3)

process.reconstruction_step_track4 = cms.Path(process.HighPtTripletStep4+ process.InitialStep4+ process.LowPtQuadStep4+ process.LowPtTripletStep4+ process.MeasurementTrackerEvent4+ process.earlyGeneralTracks4+ process.generalTracks4+ process.preDuplicateMergingGeneralTracks4+ process.siPixelClusterShapeCache4+ process.siPixelRecHits4+ process.trackerClusterCheck4)

process.reconstruction_step_track5 = cms.Path(process.HighPtTripletStep5+ process.InitialStep5+ process.LowPtQuadStep5+ process.LowPtTripletStep5+ process.MeasurementTrackerEvent5+ process.earlyGeneralTracks5+ process.generalTracks5+ process.preDuplicateMergingGeneralTracks5+ process.siPixelClusterShapeCache5+ process.siPixelRecHits5+ process.trackerClusterCheck5)

process.reconstruction_step_track6 = cms.Path(process.HighPtTripletStep6+ process.InitialStep6+ process.LowPtQuadStep6+ process.LowPtTripletStep6+ process.MeasurementTrackerEvent6+ process.earlyGeneralTracks6+ process.generalTracks6+ process.preDuplicateMergingGeneralTracks6+ process.siPixelClusterShapeCache6+ process.siPixelRecHits6+ process.trackerClusterCheck6)

process.reconstruction_step_track7 = cms.Path(process.HighPtTripletStep7+ process.InitialStep7+ process.LowPtQuadStep7+ process.LowPtTripletStep7+ process.MeasurementTrackerEvent7+ process.earlyGeneralTracks7+ process.generalTracks7+ process.preDuplicateMergingGeneralTracks7+ process.siPixelClusterShapeCache7+ process.siPixelRecHits7+ process.trackerClusterCheck7)

process.reconstruction_step_track8 = cms.Path(process.HighPtTripletStep8+ process.InitialStep8+ process.LowPtQuadStep8+ process.LowPtTripletStep8+ process.MeasurementTrackerEvent8+ process.earlyGeneralTracks8+ process.generalTracks8+ process.preDuplicateMergingGeneralTracks8+ process.siPixelClusterShapeCache8+ process.siPixelRecHits8+ process.trackerClusterCheck8)

process.endjob_step = cms.EndPath(cms.Task(process.MEtoEDMConverter))

process.RECOoutput_step = cms.EndPath(process.RECOoutput)

process.schedule = cms.Schedule(*[ process.reconstruction_step_track3, process.reconstruction_step_track4, process.reconstruction_step_track5, process.reconstruction_step_track6, process.reconstruction_step_track7, process.reconstruction_step_track8, process.endjob_step, process.RECOoutput_step ])

x = process.dumpPython()
f = open("dumped.py","w")
f.write(x)
f.close()
