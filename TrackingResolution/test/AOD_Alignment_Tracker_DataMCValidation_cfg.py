# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: RECO --data --eventcontent RECO --datatier RECO --conditions 124X_dataRun3_v15 --step RAW2DIGI,RECO --era Run3 --filein file:testin.root --fileout file:test.root --python_filename test_cfg.py --scenario pp --no_exec -n 100
import sys, os
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')

options.register ('layersThreshold',
                  3, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.int,          # string, int, or float
                  "Number of threshold layers (from 3 to 8 so far)")
options.register ('numEvents',
                  -1, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.int,          # string, int, or float
                  "Number of events to run")
options.register ('isPU',
                  'False', # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.string,          # string, int, or float
                  "Run MC events with or without PU")
options.register ('isMC',
                  'False', # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.string,          # string, int, or float
                  "Run MC or Data events")
options.register ('isAOD',
                  'False', # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.string,          # string, int, or float
                  "Run Data events that are AOD or RAW")

options.parseArguments()

process = cms.Process('DQM',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.numEvents),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

filenames = []

filepath = "filesMC.txt"
if options.isMC == 'True':
    if options.isPU == 'True': filepath = "filesMCPU.txt"
else: 
    if options.isAOD == 'True': filepath = "filesDataAOD.txt"
    else: filepath = "filesData.txt"

f = open(filepath,"r")
lines = f.readlines()

for line in lines:
    filenames.append(line.strip())

# Input source
process.source = cms.Source("PoolSource",
  secondaryFileNames = cms.untracked.vstring(),
  fileNames = cms.untracked.vstring(
    filenames
  ),
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
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
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
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
    annotation = cms.untracked.string('DQM nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
eventType = "MC"
if options.isMC == 'True':
    if options.isPU == 'True': eventType = "MCPU"
else:
    if options.isAOD == 'True': eventType = "DataAOD"
    else: eventType = "Data"
process.DQMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('file:'+eventType+'_DQMAlignment_'+str(options.layersThreshold)+'layers_'+options.outputFile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
gtString = 'auto:phase1_2022_realistic'
if options.isMC == 'False': gtString = '124X_dataRun3_v15'
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, gtString, '')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
evtsToReport = 2000
if options.isMC == 'False' and options.isAOD == 'False': evtsToReport = 1
process.MessageLogger.cerr.FwkReport.reportEvery = evtsToReport

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

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

process.TrackerTrackHitFilter = cms.EDProducer("TrackerTrackHitFilterMod",
    src = cms.InputTag("TrackRefitter"),
    minimumHits = cms.uint32(options.layersThreshold),
    layersRemaining = cms.uint32(options.layersThreshold),
    truncateTracks = cms.bool(True),
    commands = cms.vstring("keep PXB","keep PXE","keep TIB","keep TID","keep TOB","keep TEC"),
    detsToIgnore = cms.vuint32( ),
    replaceWithInactiveHits =cms.bool(True),
    stripFrontInvalidHits   =cms.bool(False),
    stripBackInvalidHits    =cms.bool(False),
    stripAllInvalidHits = cms.bool(False),
    rejectBadStoNHits = cms.bool(True),
    CMNSubtractionMode = cms.string("Median"),
    StoNcommands = cms.vstring("ALL 14.0"),
    useTrajectories=cms.bool(False),
    rejectLowAngleHits=cms.bool(False),
    TrackAngleCut=cms.double(0.35),
    tagOverlaps=cms.bool(False),
    usePixelQualityFlag=cms.bool(True),
    PxlTemplateProbXYCut=cms.double(0.000125),
    PxlTemplateProbXYChargeCut=cms.double(-99.),
    PxlTemplateqBinCut =cms.vint32(0, 3),
    PxlCorrClusterChargeCut = cms.double(-999.0)
)

if options.layersThreshold<3 or options.layersThreshold>8:
    for i in range(3,9):
        setattr(process,"TrackerTrackHitFilter"+str(i),process.TrackerTrackHitFilter.clone(
                minimumHits = i,
                layersRemaining = i,
            )
        )

if options.isAOD == 'True':
    process.MeasurementTrackerEvent.pixelClusterProducer = cms.string('muonReducedTrackExtras')
    process.MeasurementTrackerEvent.stripClusterProducer = cms.string('muonReducedTrackExtras')
    process.MeasurementTrackerEvent.inactivePixelDetectorLabels = cms.VInputTag()
    process.MeasurementTrackerEvent.inactiveStripDetectorLabels = cms.VInputTag()

process.HitFilteredTracks = cms.EDProducer("TrackProducer",
    useSimpleMF = cms.bool(False),
    SimpleMagneticField = cms.string(""),
    src = cms.InputTag("TrackerTrackHitFilter"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    TrajectoryInEvent = cms.bool(False),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    GeometricInnerState = cms.bool(False),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
)

if options.layersThreshold<3 or options.layersThreshold>8:
    for i in range(3,9):
        setattr(process,"HitFilteredTracks"+str(i),process.HitFilteredTracks.clone(
                src = 'TrackerTrackHitFilter'+str(i),
            )
        )

offPVTag = "RECO"
if options.isMC == 'False' and options.isAOD == 'False': offPVTag = "DQM"
# Tracker Data MC validation suite
process.trackingResolution = DQMEDAnalyzer("TrackingResolutionAlignment",
    moduleName        = cms.untracked.string("testTrackingResolution"),
    folderName        = cms.untracked.string("TrackRefitting"),
    hitsRemainInput        = cms.untracked.string(str(options.layersThreshold)),
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
    tracksInputTag     = cms.untracked.InputTag("TrackRefitter", "", "DQM"),
    primVertexInputTag = cms.untracked.InputTag("offlinePrimaryVertices", "", offPVTag),
    tracksRerecoInputTag     = cms.untracked.InputTag("HitFilteredTracks", "", "DQM")
)

if options.layersThreshold<3 or options.layersThreshold>8:
    for i in range(3,9):
        setattr(process,"trackingResolution"+str(i),process.trackingResolution.clone(
                tracksRerecoInputTag = cms.untracked.InputTag("HitFilteredTracks"+str(i), "", "DQM"),
                hitsRemainInput = cms.untracked.string(str(i))
            )
        )

# Path and EndPath definitions
process.load("TrackingResolution.TrackingResolution.RClusterSeq_Alignment_cff")

process.p = cms.Path(process.RClusterSeq)

import RecoTracker.TrackProducer.trackExtraRekeyer_cfi
process.trackExtraRekeyer = RecoTracker.TrackProducer.trackExtraRekeyer_cfi.trackExtraRekeyer.clone(
    src = "generalTracks",
    association = "muonReducedTrackExtras"
)
if options.isAOD == 'True': process.rCluster.allTracks = cms.InputTag("trackExtraRekeyer")

if options.layersThreshold<3 or options.layersThreshold>8: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter3*process.TrackerTrackHitFilter4*process.TrackerTrackHitFilter5*process.TrackerTrackHitFilter6*process.TrackerTrackHitFilter7*process.TrackerTrackHitFilter8*process.HitFilteredTracks3*process.HitFilteredTracks4*process.HitFilteredTracks5*process.HitFilteredTracks6*process.HitFilteredTracks7*process.HitFilteredTracks8*process.trackingResolution3*process.trackingResolution4*process.trackingResolution5*process.trackingResolution6*process.trackingResolution7*process.trackingResolution8)
else: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter*process.HitFilteredTracks*process.trackingResolution)
process.rekeying = cms.Path(process.trackExtraRekeyer)

# Schedule definition
process.schedule = cms.Schedule(process.p,process.analysis_step,process.endjob_step,process.DQMoutput_step)
if options.isAOD == 'True': process.schedule = cms.Schedule(process.rekeying,process.p,process.analysis_step,process.endjob_step,process.DQMoutput_step)
if options.isMC == 'False' and options.isAOD == 'False': process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.p,process.analysis_step,process.endjob_step,process.DQMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#  Added: timing service (throughput measurement quite unreproduceable)
process.Timing = cms.Service("Timing",
    summaryOnly = cms.untracked.bool(True),
    useJobReport = cms.untracked.bool(False)
)

# Added: Throughput service (Andrea). Testing.
process.ThroughputService = cms.Service('ThroughputService',
    enableDQM = cms.untracked.bool(False),
    printEventSummary = cms.untracked.bool(True),
    eventResolution = cms.untracked.uint32(1000),
    eventRange = cms.untracked.uint32(100)    # this is just an optimisation for the initial memory allocation
)

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
