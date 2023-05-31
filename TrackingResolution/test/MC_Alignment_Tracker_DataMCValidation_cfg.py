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
    input = cms.untracked.int32(options.numEvents)
)

filenames = []

filepath = ""
if options.isPU == 'True': filepath = "filesMCPU.txt"
else: filepath = "filesMC.txt"

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
#   eventsToProcess = cms.untracked.VEventRange('1:17393'),#,'1:4543'),
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

PUorNot = "MC"
if options.isPU == 'True': PUorNot = "MCPU"
process.DQMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('file:'+PUorNot+'_TrajectoryFalse_alignmentReRECO_definitive_allRECO_DQMAlignment_'+str(options.layersThreshold)+'layers_'+options.outputFile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
gtString = 'auto:phase1_2022_realistic'
process.GlobalTag = GlobalTag(process.GlobalTag, gtString,'')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 2000

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
    primVertexInputTag = cms.untracked.InputTag("offlinePrimaryVertices", "", "RECO"),
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

if options.layersThreshold<3 or options.layersThreshold>8: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter3*process.TrackerTrackHitFilter4*process.TrackerTrackHitFilter5*process.TrackerTrackHitFilter6*process.TrackerTrackHitFilter7*process.TrackerTrackHitFilter8*process.HitFilteredTracks3*process.HitFilteredTracks4*process.HitFilteredTracks5*process.HitFilteredTracks6*process.HitFilteredTracks7*process.HitFilteredTracks8*process.trackingResolution3*process.trackingResolution4*process.trackingResolution5*process.trackingResolution6*process.trackingResolution7*process.trackingResolution8)
else: process.analysis_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.TrackerTrackHitFilter*process.HitFilteredTracks*process.trackingResolution)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.p, process.analysis_step, process.endjob_step, process.DQMoutput_step)

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
