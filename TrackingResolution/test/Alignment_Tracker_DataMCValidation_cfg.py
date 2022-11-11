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
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

filenames = []

for i in range(1):
    #filenames.append('file:/eos/user/b/borzari/TrackingRootFile/RelValZMM_1260_GEN_SIM_RECO.root')
    filenames.append('/store/relval/CMSSW_12_6_0_pre3/RelValZMM_14/GEN-SIM-RECO/125X_mcRun3_2022_realistic_v3-v1/2580000/7dd1dbfc-90c2-46c9-a57e-1fa715218c26.root')
    filenames.append('/store/relval/CMSSW_12_6_0_pre3/RelValZMM_14/GEN-SIM-RECO/125X_mcRun3_2022_realistic_v3-v1/2580000/ac18f277-3b03-4b5d-b3d7-e81fb1608715.root')

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
    fileName = cms.untracked.string('file:test_alignmentReRECO_definitive_allRECO_DQMAlignment_'+str(options.layersThreshold)+'layers_'+options.outputFile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:/eos/user/b/borzari/TrackingRootFile/test_alignmentReRECO_definitive_allRECO_Alignment_'+str(options.layersThreshold)+'layers_'+options.outputFile),
    outputCommands = cms.untracked.vstring( (
    'keep *'
         ) ),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic', '')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

###################################################################
## Load and Configure TrackRefitter
##First refit with applying geometry set above
##Second refit after the track selection
###################################################################
# refitting
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

process.TrackRefitter = process.TrackRefitter.clone(
    src = 'rCluster',
    TrajectoryInEvent = True,
    TTRHBuilder = "WithAngleAndTemplate", #"WithTrackAngle"
    NavigationSchool = ''
)

process.load("RecoTracker.FinalTrackSelectors.TrackerTrackHitFilter_cff")
process.TrackerTrackHitFilter.src = 'TrackRefitter'
#process.TrackerTrackHitFilter.src = 'generalTracks'
process.TrackerTrackHitFilter.useTrajectories= True  # this is needed only if you require some selections; but it will work even if you don't ask for them
process.TrackerTrackHitFilter.minimumHits = 8
process.TrackerTrackHitFilter.commands = cms.vstring("keep PXB","keep PXE","keep TIB","keep TID","keep TOB","keep TEC")
process.TrackerTrackHitFilter.detsToIgnore = []
process.TrackerTrackHitFilter.replaceWithInactiveHits = True
process.TrackerTrackHitFilter.stripAllInvalidHits = False
process.TrackerTrackHitFilter.rejectBadStoNHits = True
process.TrackerTrackHitFilter.StoNcommands = cms.vstring("ALL 14.0")
process.TrackerTrackHitFilter.rejectLowAngleHits= True
process.TrackerTrackHitFilter.TrackAngleCut= 0.35 # in rads, starting from the module surface
process.TrackerTrackHitFilter.usePixelQualityFlag= True

process.TrackerTrackHitFilter3 = process.TrackerTrackHitFilter.clone()
process.TrackerTrackHitFilter3.minimumHits = 3
process.TrackerTrackHitFilter3.commands = cms.vstring("keep PXB","keep PXE","drop TIB","drop TID","drop TOB","drop TEC")

process.TrackerTrackHitFilter4 = process.TrackerTrackHitFilter.clone()
process.TrackerTrackHitFilter4.minimumHits = 4
process.TrackerTrackHitFilter4.commands = cms.vstring("keep PXB","keep PXE","keep TIB","keep TID","drop TOB","drop TEC")

process.TrackerTrackHitFilter5 = process.TrackerTrackHitFilter.clone()
process.TrackerTrackHitFilter5.minimumHits = 5
process.TrackerTrackHitFilter5.commands = cms.vstring("keep PXB","keep PXE","keep TIB","keep TID","drop TOB","drop TEC")

process.TrackerTrackHitFilter6 = process.TrackerTrackHitFilter.clone()
process.TrackerTrackHitFilter6.minimumHits = 6
process.TrackerTrackHitFilter6.commands = cms.vstring("keep PXB","keep PXE","keep TIB","keep TID","drop TOB","drop TEC")

process.TrackerTrackHitFilter7 = process.TrackerTrackHitFilter.clone()
process.TrackerTrackHitFilter7.minimumHits = 7
process.TrackerTrackHitFilter7.commands = cms.vstring("keep PXB","keep PXE","keep TIB","keep TID","drop TOB","drop TEC")

process.TrackerTrackHitFilter8 = process.TrackerTrackHitFilter.clone()
process.TrackerTrackHitFilter8.minimumHits = 8
process.TrackerTrackHitFilter8.commands = cms.vstring("keep PXB","keep PXE","keep TIB","keep TID","drop TOB","drop TEC")

import RecoTracker.TrackProducer.CTFFinalFitWithMaterial_cff   #TrackRefitters_cff
process.HitFilteredTracks = RecoTracker.TrackProducer.CTFFinalFitWithMaterial_cff.ctfWithMaterialTracks.clone(
    src = 'TrackerTrackHitFilter',
    TrajectoryInEvent = True,
    TTRHBuilder = "WithAngleAndTemplate"
)

process.HitFilteredTracks3 = process.HitFilteredTracks.clone()
process.HitFilteredTracks3.src = 'TrackerTrackHitFilter3'

process.HitFilteredTracks4 = process.HitFilteredTracks.clone()
process.HitFilteredTracks4.src = 'TrackerTrackHitFilter4'

process.HitFilteredTracks5 = process.HitFilteredTracks.clone()
process.HitFilteredTracks5.src = 'TrackerTrackHitFilter5'

process.HitFilteredTracks6 = process.HitFilteredTracks.clone()
process.HitFilteredTracks6.src = 'TrackerTrackHitFilter6'

process.HitFilteredTracks7 = process.HitFilteredTracks.clone()
process.HitFilteredTracks7.src = 'TrackerTrackHitFilter7'

process.HitFilteredTracks8 = process.HitFilteredTracks.clone()
process.HitFilteredTracks8.src = 'TrackerTrackHitFilter8'

# Tracker Data MC validation suite
process.trackingResolution = DQMEDAnalyzer("TrackingResolutionAlignment",
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
    tracksInputTag     = cms.untracked.InputTag("generalTracks", "", "RECO"),
    primVertexInputTag = cms.untracked.InputTag("offlinePrimaryVertices", "", "RECO"),
    tracksRerecoInputTag     = cms.untracked.InputTag("HitFilteredTracks", "", "DQM")
)

process.trackingResolution3 = process.trackingResolution.clone()
process.trackingResolution3.tracksInputTag=cms.untracked.InputTag("rCluster", "", "DQM")
process.trackingResolution3.tracksRerecoInputTag=cms.untracked.InputTag("HitFilteredTracks3", "", "DQM")
process.trackingResolution3.hitsRemainInput=cms.untracked.string("3")

process.trackingResolution4 = process.trackingResolution3.clone()
process.trackingResolution4.tracksInputTag=cms.untracked.InputTag("rCluster", "", "DQM")
process.trackingResolution4.tracksRerecoInputTag=cms.untracked.InputTag("HitFilteredTracks4", "", "DQM")
process.trackingResolution4.hitsRemainInput=cms.untracked.string("4")

process.trackingResolution5 = process.trackingResolution3.clone()
process.trackingResolution5.tracksInputTag=cms.untracked.InputTag("rCluster", "", "DQM")
process.trackingResolution5.tracksRerecoInputTag=cms.untracked.InputTag("HitFilteredTracks5", "", "DQM")
process.trackingResolution5.hitsRemainInput=cms.untracked.string("5")

process.trackingResolution6 = process.trackingResolution3.clone()
process.trackingResolution6.tracksInputTag=cms.untracked.InputTag("rCluster", "", "DQM")
process.trackingResolution6.tracksRerecoInputTag=cms.untracked.InputTag("HitFilteredTracks6", "", "DQM")
process.trackingResolution6.hitsRemainInput=cms.untracked.string("6")

process.trackingResolution7 = process.trackingResolution3.clone()
process.trackingResolution7.tracksInputTag=cms.untracked.InputTag("rCluster", "", "DQM")
process.trackingResolution7.tracksRerecoInputTag=cms.untracked.InputTag("HitFilteredTracks7", "", "DQM")
process.trackingResolution7.hitsRemainInput=cms.untracked.string("7")

process.trackingResolution8 = process.trackingResolution3.clone()
process.trackingResolution8.tracksInputTag=cms.untracked.InputTag("rCluster", "", "DQM")
process.trackingResolution8.tracksRerecoInputTag=cms.untracked.InputTag("HitFilteredTracks8", "", "DQM")
process.trackingResolution8.hitsRemainInput=cms.untracked.string("8")

# Path and EndPath definitions
process.load("TrackingResolution.TrackingResolution.RClusterSeq_Alignment_cff")

process.p = cms.Path(process.RClusterSeq)

if options.layersThreshold==3: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter3*process.HitFilteredTracks3*process.trackingResolution3)
if options.layersThreshold==4: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter4*process.HitFilteredTracks4*process.trackingResolution4)
if options.layersThreshold==5: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter5*process.HitFilteredTracks5*process.trackingResolution5)
if options.layersThreshold==6: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter6*process.HitFilteredTracks6*process.trackingResolution6)
if options.layersThreshold==7: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter7*process.HitFilteredTracks7*process.trackingResolution7)
if options.layersThreshold==8: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter8*process.HitFilteredTracks8*process.trackingResolution8)
if options.layersThreshold<3 or options.layersThreshold>8: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter3*process.TrackerTrackHitFilter4*process.TrackerTrackHitFilter5*process.TrackerTrackHitFilter6*process.TrackerTrackHitFilter7*process.TrackerTrackHitFilter8*process.HitFilteredTracks3*process.HitFilteredTracks4*process.HitFilteredTracks5*process.HitFilteredTracks6*process.HitFilteredTracks7*process.HitFilteredTracks8*process.trackingResolution3*process.trackingResolution4*process.trackingResolution5*process.trackingResolution6*process.trackingResolution7*process.trackingResolution8)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.p,process.analysis_step, process.endjob_step, process.DQMoutput_step)

print(process.analysis_step)
print(process.schedule)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)
