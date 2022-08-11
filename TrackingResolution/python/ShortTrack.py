import FWCore.ParameterSet.Config as cms

# Clone every module in reconstruction_trackingOnly and modify the pixel and strip
# clusters, as well as the modules names to fit each layerThreshold value

def shortTrackModules(process, layers=3):

    myCollection = "rCluster"+str(layers)
    
    setattr(process,"MeasurementTrackerEventPreSplitting"+str(layers),process.MeasurementTrackerEventPreSplitting.clone(
            Phase2TrackerCluster1DProducer = cms.string(''),
            badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
            inactivePixelDetectorLabels = cms.VInputTag("siPixelDigis"),
            inactiveStripDetectorLabels = cms.VInputTag("siStripDigis"),
            measurementTracker = cms.string(''),
            mightGet = cms.optional.untracked.vstring,
            pixelCablingMapLabel = cms.string(''),
            pixelClusterProducer = cms.string('siPixelClustersPreSplitting'+str(layers)),
            skipClusters = cms.InputTag(""),
            stripClusterProducer = cms.string(myCollection),
            switchOffPixelsIfEmpty = cms.bool(True),
            vectorHits = cms.InputTag(""),
            vectorHitsRej = cms.InputTag("")
        )
    )
    
    setattr(process,"siPixelClusterShapeCachePreSplitting"+str(layers),process.siPixelClusterShapeCachePreSplitting.clone(
            mightGet = cms.optional.untracked.vstring,
            onDemand = cms.bool(False),
            src = cms.InputTag("siPixelClustersPreSplitting"+str(layers))
        )
    )
    
    setattr(process,"hbhereco"+str(layers),process.hbhereco.clone(
            cpu = cms.EDProducer("HBHEPhase1Reconstructor",
                algoConfigClass = cms.string(''),
                algorithm = cms.PSet(
                    Class = cms.string('SimpleHBHEPhase1Algo'),
                    activeBXs = cms.vint32(
                        -3, -2, -1, 0, 1,
                        2, 3, 4
                    ),
                    applyFixPCC = cms.bool(True),
                    applyLegacyHBMCorrection = cms.bool(False),
                    applyPedConstraint = cms.bool(True),
                    applyPulseJitter = cms.bool(False),
                    applyTimeConstraint = cms.bool(True),
                    applyTimeSlew = cms.bool(True),
                    applyTimeSlewM3 = cms.bool(True),
                    calculateArrivalTime = cms.bool(True),
                    chiSqSwitch = cms.double(-1),
                    correctForPhaseContainment = cms.bool(True),
                    correctionPhaseNS = cms.double(6.0),
                    deltaChiSqThresh = cms.double(0.001),
                    dynamicPed = cms.bool(False),
                    firstSampleShift = cms.int32(0),
                    fitTimes = cms.int32(1),
                    meanPed = cms.double(0.0),
                    meanTime = cms.double(0.0),
                    nMaxItersMin = cms.int32(500),
                    nMaxItersNNLS = cms.int32(500),
                    nnlsThresh = cms.double(1e-11),
                    pulseJitter = cms.double(1.0),
                    respCorrM3 = cms.double(1.0),
                    samplesToAdd = cms.int32(2),
                    tdcTimeShift = cms.double(0.0),
                    timeMax = cms.double(12.5),
                    timeMin = cms.double(-12.5),
                    timeSigmaHPD = cms.double(5.0),
                    timeSigmaSiPM = cms.double(2.5),
                    timeSlewParsType = cms.int32(3),
                    ts4Max = cms.vdouble(100.0, 20000.0, 30000),
                    ts4Min = cms.double(0.0),
                    ts4Thresh = cms.double(0.0),
                    ts4chi2 = cms.vdouble(15.0, 15.0),
                    useM2 = cms.bool(False),
                    useM3 = cms.bool(False),
                    useMahi = cms.bool(True)
                ),
                digiLabelQIE11 = cms.InputTag("hcalDigis"),
                digiLabelQIE8 = cms.InputTag("hcalDigis"),
                dropZSmarkedPassed = cms.bool(True),
                flagParametersQIE11 = cms.PSet(
        
                ),
                flagParametersQIE8 = cms.PSet(
                    hitEnergyMinimum = cms.double(1.0),
                    hitMultiplicityThreshold = cms.int32(17),
                    nominalPedestal = cms.double(3.0),
                    pulseShapeParameterSets = cms.VPSet(
                        cms.PSet(
                            pulseShapeParameters = cms.vdouble(
                                0.0, 100.0, -50.0, 0.0, -15.0,
                                0.15
                            )
                        ),
                        cms.PSet(
                            pulseShapeParameters = cms.vdouble(
                                100.0, 2000.0, -50.0, 0.0, -5.0,
                                0.05
                            )
                        ),
                        cms.PSet(
                            pulseShapeParameters = cms.vdouble(
                                2000.0, 1000000.0, -50.0, 0.0, 95.0,
                                0.0
                            )
                        ),
                        cms.PSet(
                            pulseShapeParameters = cms.vdouble(
                                -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0,
                                0.0
                            )
                        )
                    )
                ),
                makeRecHits = cms.bool(True),
                processQIE11 = cms.bool(True),
                processQIE8 = cms.bool(True),
                pulseShapeParametersQIE11 = cms.PSet(
        
                ),
                pulseShapeParametersQIE8 = cms.PSet(
                    LeftSlopeCut = cms.vdouble(5, 2.55, 2.55),
                    LeftSlopeThreshold = cms.vdouble(250, 500, 100000),
                    LinearCut = cms.vdouble(-3, -0.054, -0.054),
                    LinearThreshold = cms.vdouble(20, 100, 100000),
                    MinimumChargeThreshold = cms.double(20),
                    MinimumTS4TS5Threshold = cms.double(100),
                    R45MinusOneRange = cms.double(0.2),
                    R45PlusOneRange = cms.double(0.2),
                    RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
                    RMS8MaxThreshold = cms.vdouble(20, 100, 100000),
                    RightSlopeCut = cms.vdouble(5, 4.15, 4.15),
                    RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
                    RightSlopeSmallThreshold = cms.vdouble(150, 200, 100000),
                    RightSlopeThreshold = cms.vdouble(250, 400, 100000),
                    TS3TS4ChargeThreshold = cms.double(70),
                    TS3TS4UpperChargeThreshold = cms.double(20),
                    TS4TS5ChargeThreshold = cms.double(70),
                    TS4TS5LowerCut = cms.vdouble(
                        -1, -0.7, -0.5, -0.4, -0.3,
                        0.1
                    ),
                    TS4TS5LowerThreshold = cms.vdouble(
                        100, 120, 160, 200, 300,
                        500
                    ),
                    TS4TS5UpperCut = cms.vdouble(1, 0.8, 0.75, 0.72),
                    TS4TS5UpperThreshold = cms.vdouble(70, 90, 100, 400),
                    TS5TS6ChargeThreshold = cms.double(70),
                    TS5TS6UpperChargeThreshold = cms.double(20),
                    TriangleIgnoreSlow = cms.bool(False),
                    TrianglePeakTS = cms.uint32(10000),
                    UseDualFit = cms.bool(True)
                ),
                recoParamsFromDB = cms.bool(True),
                saveDroppedInfos = cms.bool(False),
                saveEffectivePedestal = cms.bool(True),
                saveInfos = cms.bool(False),
                setLegacyFlagsQIE11 = cms.bool(False),
                setLegacyFlagsQIE8 = cms.bool(True),
                setNegativeFlagsQIE11 = cms.bool(False),
                setNegativeFlagsQIE8 = cms.bool(True),
                setNoiseFlagsQIE11 = cms.bool(False),
                setNoiseFlagsQIE8 = cms.bool(True),
                setPulseShapeFlagsQIE11 = cms.bool(False),
                setPulseShapeFlagsQIE8 = cms.bool(True),
                sipmQNTStoSum = cms.int32(3),
                sipmQTSShift = cms.int32(0),
                tsFromDB = cms.bool(False),
                use8ts = cms.bool(True)
            )
        )
    )
    
    setattr(process,"offlineBeamSpot"+str(layers),process.offlineBeamSpot.clone())
    
    setattr(process,"displacedMuonSeeds"+str(layers),process.displacedMuonSeeds.clone(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"+str(layers)),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"+str(layers)),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            ForcePointDown = cms.bool(False),
            MaxCSCChi2 = cms.double(300.0),
            MaxDTChi2 = cms.double(300.0),
            MaxSeeds = cms.int32(1000)
        )
    )
    
    setattr(process,"displacedStandAloneMuons"+str(layers),process.displacedStandAloneMuons.clone(
            InputObjects = cms.InputTag("displacedMuonSeeds"+str(layers)),
            MuonTrajectoryBuilder = cms.string('StandAloneMuonTrajectoryBuilder'),
            STATrajBuilderParameters = cms.PSet(
                BWFilterParameters = cms.PSet(
                    BWSeedType = cms.string('fromGenerator'),
                    CSCRecSegmentLabel = cms.InputTag("cscSegments"+str(layers)),
                    DTRecSegmentLabel = cms.InputTag("dt4DSegments"+str(layers)),
                    EnableCSCMeasurement = cms.bool(True),
                    EnableDTMeasurement = cms.bool(True),
                    EnableGEMMeasurement = cms.bool(True),
                    EnableME0Measurement = cms.bool(False),
                    EnableRPCMeasurement = cms.bool(True),
                    FitDirection = cms.string('outsideIn'),
                    GEMRecSegmentLabel = cms.InputTag("gemRecHits"+str(layers)),
                    ME0RecSegmentLabel = cms.InputTag("me0Segments"),
                    MaxChi2 = cms.double(100.0),
                    MuonTrajectoryUpdatorParameters = cms.PSet(
                        ExcludeRPCFromFit = cms.bool(False),
                        Granularity = cms.int32(0),
                        MaxChi2 = cms.double(25.0),
                        RescaleError = cms.bool(False),
                        RescaleErrorFactor = cms.double(100.0),
                        UseInvalidHits = cms.bool(True)
                    ),
                    NumberOfSigma = cms.double(3.0),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RPCRecSegmentLabel = cms.InputTag("rpcRecHits"+str(layers))
                ),
                DoBackwardFilter = cms.bool(True),
                DoRefit = cms.bool(False),
                DoSeedRefit = cms.bool(False),
                FilterParameters = cms.PSet(
                    CSCRecSegmentLabel = cms.InputTag("cscSegments"+str(layers)),
                    DTRecSegmentLabel = cms.InputTag("dt4DSegments"+str(layers)),
                    EnableCSCMeasurement = cms.bool(True),
                    EnableDTMeasurement = cms.bool(True),
                    EnableGEMMeasurement = cms.bool(True),
                    EnableME0Measurement = cms.bool(False),
                    EnableRPCMeasurement = cms.bool(True),
                    FitDirection = cms.string('insideOut'),
                    GEMRecSegmentLabel = cms.InputTag("gemRecHits"+str(layers)),
                    ME0RecSegmentLabel = cms.InputTag("me0Segments"),
                    MaxChi2 = cms.double(1000.0),
                    MuonTrajectoryUpdatorParameters = cms.PSet(
                        ExcludeRPCFromFit = cms.bool(False),
                        Granularity = cms.int32(0),
                        MaxChi2 = cms.double(25.0),
                        RescaleError = cms.bool(False),
                        RescaleErrorFactor = cms.double(100.0),
                        UseInvalidHits = cms.bool(True)
                    ),
                    NumberOfSigma = cms.double(3.0),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RPCRecSegmentLabel = cms.InputTag("rpcRecHits"+str(layers))
                ),
                NavigationType = cms.string('Standard'),
                RefitterParameters = cms.PSet(
                    FitterName = cms.string('KFFitterSmootherSTA'),
                    ForceAllIterations = cms.bool(False),
                    MaxFractionOfLostHits = cms.double(0.05),
                    NumberOfIterations = cms.uint32(3),
                    RescaleError = cms.double(100.0)
                ),
                SeedPosition = cms.string('in'),
                SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
                SeedTransformerParameters = cms.PSet(
                    Fitter = cms.string('KFFitterSmootherSTA'),
                    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
                    NMinRecHits = cms.uint32(2),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RescaleError = cms.double(100.0),
                    UseSubRecHits = cms.bool(False)
                )
            ),
            ServiceParameters = cms.PSet(
                CSCLayers = cms.untracked.bool(True),
                GEMLayers = cms.untracked.bool(True),
                ME0Layers = cms.bool(False),
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'SteppingHelixPropagatorAlong',
                    'SteppingHelixPropagatorOpposite',
                    'SteppingHelixPropagatorL2Any',
                    'SteppingHelixPropagatorL2Along',
                    'SteppingHelixPropagatorL2Opposite',
                    'SteppingHelixPropagatorAnyNoError',
                    'SteppingHelixPropagatorAlongNoError',
                    'SteppingHelixPropagatorOppositeNoError',
                    'SteppingHelixPropagatorL2AnyNoError',
                    'SteppingHelixPropagatorL2AlongNoError',
                    'SteppingHelixPropagatorL2OppositeNoError',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite',
                    'SmartPropagator',
                    'SmartPropagatorOpposite',
                    'SmartPropagatorAnyOpposite',
                    'SmartPropagatorAny',
                    'SmartPropagatorRK',
                    'SmartPropagatorAnyRK',
                    'StraightLinePropagator'
                ),
                RPCLayers = cms.bool(True),
                UseMuonNavigation = cms.untracked.bool(True)
            ),
            TrackLoaderParameters = cms.PSet(
                DoSmoothing = cms.bool(False),
                MuonUpdatorAtVertexParameters = cms.PSet(
                    BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
                    MaxChi2 = cms.double(1000000.0),
                    Propagator = cms.string('SteppingHelixPropagatorOpposite')
                ),
                Smoother = cms.string('KFSmootherForMuonTrackLoader'),
                TTRHBuilder = cms.string('WithAngleAndTemplate'),
                VertexConstraint = cms.bool(False),
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers))
            )
        )
    )
    
    setattr(process,"refittedStandAloneMuons"+str(layers),process.refittedStandAloneMuons.clone(
            InputObjects = cms.InputTag("ancientMuonSeed"+str(layers)),
            MuonTrajectoryBuilder = cms.string('Exhaustive'),
            STATrajBuilderParameters = cms.PSet(
                BWFilterParameters = cms.PSet(
                    BWSeedType = cms.string('fromGenerator'),
                    CSCRecSegmentLabel = cms.InputTag("cscSegments"+str(layers)),
                    DTRecSegmentLabel = cms.InputTag("dt4DSegments"+str(layers)),
                    EnableCSCMeasurement = cms.bool(True),
                    EnableDTMeasurement = cms.bool(True),
                    EnableGEMMeasurement = cms.bool(True),
                    EnableME0Measurement = cms.bool(False),
                    EnableRPCMeasurement = cms.bool(True),
                    FitDirection = cms.string('outsideIn'),
                    GEMRecSegmentLabel = cms.InputTag("gemRecHits"+str(layers)),
                    ME0RecSegmentLabel = cms.InputTag("me0Segments"),
                    MaxChi2 = cms.double(100.0),
                    MuonTrajectoryUpdatorParameters = cms.PSet(
                        ExcludeRPCFromFit = cms.bool(False),
                        Granularity = cms.int32(0),
                        MaxChi2 = cms.double(25.0),
                        RescaleError = cms.bool(False),
                        RescaleErrorFactor = cms.double(100.0),
                        UseInvalidHits = cms.bool(True)
                    ),
                    NumberOfSigma = cms.double(3.0),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RPCRecSegmentLabel = cms.InputTag("rpcRecHits"+str(layers))
                ),
                DoBackwardFilter = cms.bool(True),
                DoRefit = cms.bool(True),
                DoSeedRefit = cms.bool(False),
                FilterParameters = cms.PSet(
                    CSCRecSegmentLabel = cms.InputTag("cscSegments"+str(layers)),
                    DTRecSegmentLabel = cms.InputTag("dt4DSegments"+str(layers)),
                    EnableCSCMeasurement = cms.bool(True),
                    EnableDTMeasurement = cms.bool(True),
                    EnableGEMMeasurement = cms.bool(True),
                    EnableME0Measurement = cms.bool(False),
                    EnableRPCMeasurement = cms.bool(True),
                    FitDirection = cms.string('insideOut'),
                    GEMRecSegmentLabel = cms.InputTag("gemRecHits"+str(layers)),
                    ME0RecSegmentLabel = cms.InputTag("me0Segments"),
                    MaxChi2 = cms.double(1000.0),
                    MuonTrajectoryUpdatorParameters = cms.PSet(
                        ExcludeRPCFromFit = cms.bool(False),
                        Granularity = cms.int32(0),
                        MaxChi2 = cms.double(25.0),
                        RescaleError = cms.bool(False),
                        RescaleErrorFactor = cms.double(100.0),
                        UseInvalidHits = cms.bool(True)
                    ),
                    NumberOfSigma = cms.double(3.0),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RPCRecSegmentLabel = cms.InputTag("rpcRecHits"+str(layers))
                ),
                NavigationType = cms.string('Standard'),
                RefitterParameters = cms.PSet(
                    FitterName = cms.string('KFFitterSmootherSTA'),
                    ForceAllIterations = cms.bool(False),
                    MaxFractionOfLostHits = cms.double(0.05),
                    NumberOfIterations = cms.uint32(3),
                    RescaleError = cms.double(100.0)
                ),
                SeedPosition = cms.string('in'),
                SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
                SeedTransformerParameters = cms.PSet(
                    Fitter = cms.string('KFFitterSmootherSTA'),
                    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
                    NMinRecHits = cms.uint32(2),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RescaleError = cms.double(100.0),
                    UseSubRecHits = cms.bool(False)
                )
            ),
            ServiceParameters = cms.PSet(
                CSCLayers = cms.untracked.bool(True),
                GEMLayers = cms.untracked.bool(True),
                ME0Layers = cms.bool(False),
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'SteppingHelixPropagatorAlong',
                    'SteppingHelixPropagatorOpposite',
                    'SteppingHelixPropagatorL2Any',
                    'SteppingHelixPropagatorL2Along',
                    'SteppingHelixPropagatorL2Opposite',
                    'SteppingHelixPropagatorAnyNoError',
                    'SteppingHelixPropagatorAlongNoError',
                    'SteppingHelixPropagatorOppositeNoError',
                    'SteppingHelixPropagatorL2AnyNoError',
                    'SteppingHelixPropagatorL2AlongNoError',
                    'SteppingHelixPropagatorL2OppositeNoError',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite',
                    'SmartPropagator',
                    'SmartPropagatorOpposite',
                    'SmartPropagatorAnyOpposite',
                    'SmartPropagatorAny',
                    'SmartPropagatorRK',
                    'SmartPropagatorAnyRK',
                    'StraightLinePropagator'
                ),
                RPCLayers = cms.bool(True),
                UseMuonNavigation = cms.untracked.bool(True)
            ),
            TrackLoaderParameters = cms.PSet(
                DoSmoothing = cms.bool(False),
                MuonUpdatorAtVertexParameters = cms.PSet(
                    BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
                    MaxChi2 = cms.double(1000000.0),
                    Propagator = cms.string('SteppingHelixPropagatorOpposite')
                ),
                Smoother = cms.string('KFSmootherForMuonTrackLoader'),
                TTRHBuilder = cms.string('WithAngleAndTemplate'),
                VertexConstraint = cms.bool(True),
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers))
            )
        )
    )
    
    setattr(process,"standAloneMuons"+str(layers),process.standAloneMuons.clone(
            InputObjects = cms.InputTag("ancientMuonSeed"+str(layers)),
            MuonTrajectoryBuilder = cms.string('Exhaustive'),
            STATrajBuilderParameters = cms.PSet(
                BWFilterParameters = cms.PSet(
                    BWSeedType = cms.string('fromGenerator'),
                    CSCRecSegmentLabel = cms.InputTag("cscSegments"+str(layers)),
                    DTRecSegmentLabel = cms.InputTag("dt4DSegments"+str(layers)),
                    EnableCSCMeasurement = cms.bool(True),
                    EnableDTMeasurement = cms.bool(True),
                    EnableGEMMeasurement = cms.bool(True),
                    EnableME0Measurement = cms.bool(False),
                    EnableRPCMeasurement = cms.bool(True),
                    FitDirection = cms.string('outsideIn'),
                    GEMRecSegmentLabel = cms.InputTag("gemRecHits"+str(layers)),
                    ME0RecSegmentLabel = cms.InputTag("me0Segments"),
                    MaxChi2 = cms.double(100.0),
                    MuonTrajectoryUpdatorParameters = cms.PSet(
                        ExcludeRPCFromFit = cms.bool(False),
                        Granularity = cms.int32(0),
                        MaxChi2 = cms.double(25.0),
                        RescaleError = cms.bool(False),
                        RescaleErrorFactor = cms.double(100.0),
                        UseInvalidHits = cms.bool(True)
                    ),
                    NumberOfSigma = cms.double(3.0),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RPCRecSegmentLabel = cms.InputTag("rpcRecHits"+str(layers))
                ),
                DoBackwardFilter = cms.bool(True),
                DoRefit = cms.bool(False),
                DoSeedRefit = cms.bool(False),
                FilterParameters = cms.PSet(
                    CSCRecSegmentLabel = cms.InputTag("cscSegments"+str(layers)),
                    DTRecSegmentLabel = cms.InputTag("dt4DSegments"+str(layers)),
                    EnableCSCMeasurement = cms.bool(True),
                    EnableDTMeasurement = cms.bool(True),
                    EnableGEMMeasurement = cms.bool(True),
                    EnableME0Measurement = cms.bool(False),
                    EnableRPCMeasurement = cms.bool(True),
                    FitDirection = cms.string('insideOut'),
                    GEMRecSegmentLabel = cms.InputTag("gemRecHits"+str(layers)),
                    ME0RecSegmentLabel = cms.InputTag("me0Segments"),
                    MaxChi2 = cms.double(1000.0),
                    MuonTrajectoryUpdatorParameters = cms.PSet(
                        ExcludeRPCFromFit = cms.bool(False),
                        Granularity = cms.int32(0),
                        MaxChi2 = cms.double(25.0),
                        RescaleError = cms.bool(False),
                        RescaleErrorFactor = cms.double(100.0),
                        UseInvalidHits = cms.bool(True)
                    ),
                    NumberOfSigma = cms.double(3.0),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RPCRecSegmentLabel = cms.InputTag("rpcRecHits"+str(layers))
                ),
                NavigationType = cms.string('Standard'),
                RefitterParameters = cms.PSet(
                    FitterName = cms.string('KFFitterSmootherSTA'),
                    ForceAllIterations = cms.bool(False),
                    MaxFractionOfLostHits = cms.double(0.05),
                    NumberOfIterations = cms.uint32(3),
                    RescaleError = cms.double(100.0)
                ),
                SeedPosition = cms.string('in'),
                SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
                SeedTransformerParameters = cms.PSet(
                    Fitter = cms.string('KFFitterSmootherSTA'),
                    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
                    NMinRecHits = cms.uint32(2),
                    Propagator = cms.string('SteppingHelixPropagatorAny'),
                    RescaleError = cms.double(100.0),
                    UseSubRecHits = cms.bool(False)
                )
            ),
            ServiceParameters = cms.PSet(
                CSCLayers = cms.untracked.bool(True),
                GEMLayers = cms.untracked.bool(True),
                ME0Layers = cms.bool(False),
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny',
                    'SteppingHelixPropagatorAlong',
                    'SteppingHelixPropagatorOpposite',
                    'SteppingHelixPropagatorL2Any',
                    'SteppingHelixPropagatorL2Along',
                    'SteppingHelixPropagatorL2Opposite',
                    'SteppingHelixPropagatorAnyNoError',
                    'SteppingHelixPropagatorAlongNoError',
                    'SteppingHelixPropagatorOppositeNoError',
                    'SteppingHelixPropagatorL2AnyNoError',
                    'SteppingHelixPropagatorL2AlongNoError',
                    'SteppingHelixPropagatorL2OppositeNoError',
                    'PropagatorWithMaterial',
                    'PropagatorWithMaterialOpposite',
                    'SmartPropagator',
                    'SmartPropagatorOpposite',
                    'SmartPropagatorAnyOpposite',
                    'SmartPropagatorAny',
                    'SmartPropagatorRK',
                    'SmartPropagatorAnyRK',
                    'StraightLinePropagator'
                ),
                RPCLayers = cms.bool(True),
                UseMuonNavigation = cms.untracked.bool(True)
            ),
            TrackLoaderParameters = cms.PSet(
                DoSmoothing = cms.bool(False),
                MuonUpdatorAtVertexParameters = cms.PSet(
                    BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
                    MaxChi2 = cms.double(1000000.0),
                    Propagator = cms.string('SteppingHelixPropagatorOpposite')
                ),
                Smoother = cms.string('KFSmootherForMuonTrackLoader'),
                TTRHBuilder = cms.string('WithAngleAndTemplate'),
                VertexConstraint = cms.bool(True),
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers))
            )
        )
    )
    
    setattr(process,"trackExtrapolator"+str(layers),process.trackExtrapolator.clone(
            trackQuality = cms.string('goodIterative'),
            trackSrc = cms.InputTag("generalTracks"+str(layers))
        )
    )
    
    setattr(process,"generalV0Candidates"+str(layers),process.generalV0Candidates.clone(
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            cosThetaXYCut = cms.double(0.998),
            cosThetaXYZCut = cms.double(-2.0),
            doKShorts = cms.bool(True),
            doLambdas = cms.bool(True),
            innerHitPosCut = cms.double(4.0),
            kShortMassCut = cms.double(0.07),
            lambdaMassCut = cms.double(0.05),
            mPiPiCut = cms.double(0.6),
            tkChi2Cut = cms.double(10.0),
            tkDCACut = cms.double(1.0),
            tkIPSigXYCut = cms.double(2.0),
            tkIPSigZCut = cms.double(-1.0),
            tkNHitsCut = cms.int32(3),
            tkPtCut = cms.double(0.35),
            trackRecoAlgorithm = cms.InputTag("generalTracks"+str(layers)),
            useRefTracks = cms.bool(True),
            useVertex = cms.bool(False),
            vertexFitter = cms.bool(True),
            vertices = cms.InputTag("offlinePrimaryVertices"+str(layers)),
            vtxChi2Cut = cms.double(6.63),
            vtxDecaySigXYCut = cms.double(15.0),
            vtxDecaySigXYZCut = cms.double(-1.0)
        )
    )
    
    setattr(process,"offlinePrimaryVertices"+str(layers),process.offlinePrimaryVertices.clone(
            assignment = cms.PSet(
                DzCutForChargedFromPUVtxs = cms.double(0.2),
                EtaMinUseDz = cms.double(-1),
                NumOfPUVtxsForCharged = cms.uint32(0),
                OnlyUseFirstDz = cms.bool(False),
                PtMaxCharged = cms.double(-1),
                maxDistanceToJetAxis = cms.double(0.07),
                maxDtSigForPrimaryAssignment = cms.double(3),
                maxDxyForJetAxisAssigment = cms.double(0.1),
                maxDxyForNotReconstructedPrimary = cms.double(0.01),
                maxDxySigForNotReconstructedPrimary = cms.double(2),
                maxDzErrorForPrimaryAssignment = cms.double(0.05),
                maxDzForJetAxisAssigment = cms.double(0.1),
                maxDzForPrimaryAssignment = cms.double(0.1),
                maxDzSigForPrimaryAssignment = cms.double(5),
                maxJetDeltaR = cms.double(0.5),
                minJetPt = cms.double(25),
                preferHighRanked = cms.bool(False),
                useTiming = cms.bool(False),
                useVertexFit = cms.bool(True)
            ),
            jets = cms.InputTag("ak4CaloJetsForTrk"+str(layers)),
            mightGet = cms.optional.untracked.vstring,
            particles = cms.InputTag("trackRefsForJetsBeforeSorting"+str(layers)),
            produceAssociationToOriginalVertices = cms.bool(False),
            produceNoPileUpCollection = cms.bool(False),
            producePileUpCollection = cms.bool(False),
            produceSortedVertices = cms.bool(True),
            qualityForPrimary = cms.int32(3),
            sorting = cms.PSet(
        
            ),
            trackTimeResoTag = cms.InputTag(""),
            trackTimeTag = cms.InputTag(""),
            usePVMET = cms.bool(True),
            vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"offlinePrimaryVerticesWithBS"+str(layers),process.offlinePrimaryVerticesWithBS.clone(
            assignment = cms.PSet(
                DzCutForChargedFromPUVtxs = cms.double(0.2),
                EtaMinUseDz = cms.double(-1),
                NumOfPUVtxsForCharged = cms.uint32(0),
                OnlyUseFirstDz = cms.bool(False),
                PtMaxCharged = cms.double(-1),
                maxDistanceToJetAxis = cms.double(0.07),
                maxDtSigForPrimaryAssignment = cms.double(3),
                maxDxyForJetAxisAssigment = cms.double(0.1),
                maxDxyForNotReconstructedPrimary = cms.double(0.01),
                maxDxySigForNotReconstructedPrimary = cms.double(2),
                maxDzErrorForPrimaryAssignment = cms.double(0.05),
                maxDzForJetAxisAssigment = cms.double(0.1),
                maxDzForPrimaryAssignment = cms.double(0.1),
                maxDzSigForPrimaryAssignment = cms.double(5),
                maxJetDeltaR = cms.double(0.5),
                minJetPt = cms.double(25),
                preferHighRanked = cms.bool(False),
                useTiming = cms.bool(False),
                useVertexFit = cms.bool(True)
            ),
            jets = cms.InputTag("ak4CaloJetsForTrk"+str(layers)),
            mightGet = cms.optional.untracked.vstring,
            particles = cms.InputTag("trackRefsForJetsBeforeSorting"+str(layers)),
            produceAssociationToOriginalVertices = cms.bool(False),
            produceNoPileUpCollection = cms.bool(False),
            producePileUpCollection = cms.bool(False),
            produceSortedVertices = cms.bool(True),
            qualityForPrimary = cms.int32(3),
            sorting = cms.PSet(
        
            ),
            trackTimeResoTag = cms.InputTag(""),
            trackTimeTag = cms.InputTag(""),
            usePVMET = cms.bool(True),
            vertices = cms.InputTag("unsortedOfflinePrimaryVertices"+str(layers),"WithBS")
        )
    )
    
    setattr(process,"trackRefsForJetsBeforeSorting"+str(layers),process.trackRefsForJetsBeforeSorting.clone(
            particleType = cms.string('pi+'),
            src = cms.InputTag("trackWithVertexRefSelectorBeforeSorting"+str(layers))
        )
    )
    
    setattr(process,"trackWithVertexRefSelectorBeforeSorting"+str(layers),process.trackWithVertexRefSelectorBeforeSorting.clone(
            copyExtras = cms.untracked.bool(False),
            copyTrajectories = cms.untracked.bool(False),
            d0Max = cms.double(999.0),
            dzMax = cms.double(999.0),
            etaMax = cms.double(5.0),
            etaMin = cms.double(0.0),
            nSigmaDtVertex = cms.double(0),
            nVertices = cms.uint32(0),
            normalizedChi2 = cms.double(999999.0),
            numberOfLostHits = cms.uint32(999),
            numberOfValidHits = cms.uint32(0),
            numberOfValidPixelHits = cms.uint32(0),
            ptErrorCut = cms.double(9e+99),
            ptMax = cms.double(9e+99),
            ptMin = cms.double(0.3),
            quality = cms.string('highPurity'),
            rhoVtx = cms.double(0.2),
            src = cms.InputTag("generalTracks"+str(layers)),
            timeResosTag = cms.InputTag(""),
            timesTag = cms.InputTag(""),
            useVtx = cms.bool(True),
            vertexTag = cms.InputTag("unsortedOfflinePrimaryVertices"+str(layers)),
            vtxFallback = cms.bool(True),
            zetaVtx = cms.double(1.0)
        )
    )
    
    setattr(process,"unsortedOfflinePrimaryVertices"+str(layers),process.unsortedOfflinePrimaryVertices.clone(
            TkClusParameters = cms.PSet(
                TkDAClusParameters = cms.PSet(
                    Tmin = cms.double(2.0),
                    Tpurge = cms.double(2.0),
                    Tstop = cms.double(0.5),
                    convergence_mode = cms.int32(0),
                    coolingFactor = cms.double(0.6),
                    d0CutOff = cms.double(3.0),
                    delta_highT = cms.double(0.01),
                    delta_lowT = cms.double(0.001),
                    dzCutOff = cms.double(3.0),
                    uniquetrkminp = cms.double(0.0),
                    uniquetrkweight = cms.double(0.8),
                    vertexSize = cms.double(0.006),
                    zmerge = cms.double(0.01),
                    zrange = cms.double(4.0)
                ),
                algorithm = cms.string('DA_vect')
            ),
            TkFilterParameters = cms.PSet(
                algorithm = cms.string('filter'),
                maxD0Error = cms.double(1.0),
                maxD0Significance = cms.double(4.0),
                maxDzError = cms.double(1.0),
                maxEta = cms.double(2.4),
                maxNormalizedChi2 = cms.double(10.0),
                minPixelLayersWithHits = cms.int32(2),
                minPt = cms.double(0.0),
                minSiliconLayersWithHits = cms.int32(5),
                trackQuality = cms.string('any')
            ),
            TrackLabel = cms.InputTag("generalTracks"+str(layers)),
            beamSpotLabel = cms.InputTag("offlineBeamSpot"+str(layers)),
            isRecoveryIteration = cms.bool(False),
            recoveryVtxCollection = cms.InputTag(""),
            verbose = cms.untracked.bool(False),
            vertexCollections = cms.VPSet(
                cms.PSet(
                    algorithm = cms.string('AdaptiveVertexFitter'),
                    chi2cutoff = cms.double(2.5),
                    label = cms.string(''),
                    maxDistanceToBeam = cms.double(1.0),
                    minNdof = cms.double(0.0),
                    useBeamConstraint = cms.bool(False)
                ),
                cms.PSet(
                    algorithm = cms.string('AdaptiveVertexFitter'),
                    chi2cutoff = cms.double(2.5),
                    label = cms.string('WithBS'),
                    maxDistanceToBeam = cms.double(1.0),
                    minNdof = cms.double(2.0),
                    useBeamConstraint = cms.bool(True)
                )
            )
        )
    )
    
    setattr(process,"ancientMuonSeed"+str(layers),process.ancientMuonSeed.clone(
            CSCRecSegmentLabel = cms.InputTag("cscSegments"+str(layers)),
            CSC_01 = cms.vdouble(
                0.166, 0.0, 0.0, 0.031, 0.0,
                0.0
            ),
            CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
            CSC_02 = cms.vdouble(
                0.612, -0.207, -0.0, 0.067, -0.001,
                0.0
            ),
            CSC_03 = cms.vdouble(
                0.787, -0.338, 0.029, 0.101, -0.008,
                0.0
            ),
            CSC_12 = cms.vdouble(
                -0.161, 0.254, -0.047, 0.042, -0.007,
                0.0
            ),
            CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
            CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
            CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
            CSC_13 = cms.vdouble(
                0.901, -1.302, 0.533, 0.045, 0.005,
                0.0
            ),
            CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
            CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
            CSC_14 = cms.vdouble(
                0.606, -0.181, -0.002, 0.111, -0.003,
                0.0
            ),
            CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
            CSC_23 = cms.vdouble(
                -0.081, 0.113, -0.029, 0.015, 0.008,
                0.0
            ),
            CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
            CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
            CSC_24 = cms.vdouble(
                0.004, 0.021, -0.002, 0.053, 0.0,
                0.0
            ),
            CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
            CSC_34 = cms.vdouble(
                0.062, -0.067, 0.019, 0.021, 0.003,
                0.0
            ),
            CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"+str(layers)),
            DT_12 = cms.vdouble(
                0.183, 0.054, -0.087, 0.028, 0.002,
                0.0
            ),
            DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
            DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
            DT_13 = cms.vdouble(
                0.315, 0.068, -0.127, 0.051, -0.002,
                0.0
            ),
            DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
            DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
            DT_14 = cms.vdouble(
                0.359, 0.052, -0.107, 0.072, -0.004,
                0.0
            ),
            DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
            DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
            DT_23 = cms.vdouble(
                0.13, 0.023, -0.057, 0.028, 0.004,
                0.0
            ),
            DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
            DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
            DT_24 = cms.vdouble(
                0.176, 0.014, -0.051, 0.051, 0.003,
                0.0
            ),
            DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
            DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
            DT_34 = cms.vdouble(
                0.044, 0.004, -0.013, 0.029, 0.003,
                0.0
            ),
            DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
            DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableME0Measurement = cms.bool(False),
            ME0RecSegmentLabel = cms.InputTag("me0Segments"),
            OL_1213 = cms.vdouble(
                0.96, -0.737, 0.0, 0.052, 0.0,
                0.0
            ),
            OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
            OL_1222 = cms.vdouble(
                0.848, -0.591, 0.0, 0.062, 0.0,
                0.0
            ),
            OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
            OL_1232 = cms.vdouble(
                0.184, 0.0, 0.0, 0.066, 0.0,
                0.0
            ),
            OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
            OL_2213 = cms.vdouble(
                0.117, 0.0, 0.0, 0.044, 0.0,
                0.0
            ),
            OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
            OL_2222 = cms.vdouble(
                0.107, 0.0, 0.0, 0.04, 0.0,
                0.0
            ),
            OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
            SMB_10 = cms.vdouble(
                1.387, -0.038, 0.0, 0.19, 0.0,
                0.0
            ),
            SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
            SMB_11 = cms.vdouble(
                1.247, 0.72, -0.802, 0.229, -0.075,
                0.0
            ),
            SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
            SMB_12 = cms.vdouble(
                2.128, -0.956, 0.0, 0.199, 0.0,
                0.0
            ),
            SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
            SMB_20 = cms.vdouble(
                1.011, -0.052, 0.0, 0.188, 0.0,
                0.0
            ),
            SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
            SMB_21 = cms.vdouble(
                1.043, -0.124, 0.0, 0.183, 0.0,
                0.0
            ),
            SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
            SMB_22 = cms.vdouble(
                1.474, -0.758, 0.0, 0.185, 0.0,
                0.0
            ),
            SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
            SMB_30 = cms.vdouble(
                0.505, -0.022, 0.0, 0.215, 0.0,
                0.0
            ),
            SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
            SMB_31 = cms.vdouble(
                0.549, -0.145, 0.0, 0.207, 0.0,
                0.0
            ),
            SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
            SMB_32 = cms.vdouble(
                0.67, -0.327, 0.0, 0.22, 0.0,
                0.0
            ),
            SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
            SME_11 = cms.vdouble(
                3.295, -1.527, 0.112, 0.378, 0.02,
                0.0
            ),
            SME_11_0_scale = cms.vdouble(1.325085, 0.0),
            SME_12 = cms.vdouble(
                0.102, 0.599, 0.0, 0.38, 0.0,
                0.0
            ),
            SME_12_0_scale = cms.vdouble(2.279181, 0.0),
            SME_13 = cms.vdouble(
                -1.286, 1.711, 0.0, 0.356, 0.0,
                0.0
            ),
            SME_13_0_scale = cms.vdouble(0.104905, 0.0),
            SME_21 = cms.vdouble(
                -0.529, 1.194, -0.358, 0.472, 0.086,
                0.0
            ),
            SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
            SME_22 = cms.vdouble(
                -1.207, 1.491, -0.251, 0.189, 0.243,
                0.0
            ),
            SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
            SME_31 = cms.vdouble(
                -1.594, 1.482, -0.317, 0.487, 0.097,
                0.0
            ),
            SME_32 = cms.vdouble(
                -0.901, 1.333, -0.47, 0.41, 0.073,
                0.0
            ),
            SME_41 = cms.vdouble(
                -0.003, 0.005, 0.005, 0.608, 0.076,
                0.0
            ),
            SME_42 = cms.vdouble(
                -0.003, 0.005, 0.005, 0.608, 0.076,
                0.0
            ),
            beamSpotTag = cms.InputTag("offlineBeamSpot"+str(layers)),
            crackEtas = cms.vdouble(0.2, 1.6, 1.7),
            crackWindow = cms.double(0.04),
            deltaEtaCrackSearchWindow = cms.double(0.25),
            deltaEtaSearchWindow = cms.double(0.2),
            deltaPhiSearchWindow = cms.double(0.25),
            mightGet = cms.optional.untracked.vstring,
            scaleDT = cms.bool(True)
        )
    )
    
    setattr(process,"ak4CaloJetsForTrk"+str(layers),process.ak4CaloJetsForTrk.clone(
            Active_Area_Repeats = cms.int32(1),
            GhostArea = cms.double(0.01),
            Ghost_EtaMax = cms.double(5.0),
            Rho_EtaMax = cms.double(4.4),
            applyWeight = cms.bool(False),
            doAreaDiskApprox = cms.bool(False),
            doAreaFastjet = cms.bool(False),
            doPUOffsetCorr = cms.bool(False),
            doPVCorrection = cms.bool(True),
            doRhoFastjet = cms.bool(False),
            inputEMin = cms.double(0.0),
            inputEtMin = cms.double(0.3),
            jetAlgorithm = cms.string('AntiKt'),
            jetPtMin = cms.double(10.0),
            jetType = cms.string('CaloJet'),
            maxBadEcalCells = cms.uint32(9999999),
            maxBadHcalCells = cms.uint32(9999999),
            maxProblematicEcalCells = cms.uint32(9999999),
            maxProblematicHcalCells = cms.uint32(9999999),
            maxRecoveredEcalCells = cms.uint32(9999999),
            maxRecoveredHcalCells = cms.uint32(9999999),
            minSeed = cms.uint32(14327),
            nSigmaPU = cms.double(1.0),
            puPtMin = cms.double(10),
            rParam = cms.double(0.4),
            radiusPU = cms.double(0.5),
            src = cms.InputTag("caloTowerForTrk"+str(layers)),
            srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"+str(layers)),
            useDeterministicSeed = cms.bool(True),
            voronoiRfact = cms.double(-0.9)
        )
    )
    
    setattr(process,"caloTowerForTrk"+str(layers),process.caloTowerForTrk.clone(
            AllowMissingInputs = cms.bool(False),
            EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            EBSumThreshold = cms.double(0.2),
            EBThreshold = cms.double(0.07),
            EBWeight = cms.double(1.0),
            EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            EESumThreshold = cms.double(0.45),
            EEThreshold = cms.double(0.3),
            EEWeight = cms.double(1.0),
            EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            EcalRecHitSeveritiesToBeExcluded = cms.vstring(
                'kTime',
                'kWeird',
                'kBad'
            ),
            EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
            EcutTower = cms.double(-1000.0),
            HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HBThreshold = cms.double(0.3),
            HBThreshold1 = cms.double(0.1),
            HBThreshold2 = cms.double(0.2),
            HBWeight = cms.double(1.0),
            HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HEDThreshold = cms.double(0.2),
            HEDThreshold1 = cms.double(0.1),
            HEDWeight = cms.double(1.0),
            HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HESThreshold = cms.double(0.2),
            HESThreshold1 = cms.double(0.1),
            HESWeight = cms.double(1.0),
            HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HF1Threshold = cms.double(0.5),
            HF1Weight = cms.double(1.0),
            HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HF2Threshold = cms.double(0.85),
            HF2Weight = cms.double(1.0),
            HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HOThreshold0 = cms.double(1.1),
            HOThresholdMinus1 = cms.double(3.5),
            HOThresholdMinus2 = cms.double(3.5),
            HOThresholdPlus1 = cms.double(3.5),
            HOThresholdPlus2 = cms.double(3.5),
            HOWeight = cms.double(1.0),
            HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HcalAcceptSeverityLevel = cms.uint32(9),
            HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
            HcalPhase = cms.int32(1),
            HcalThreshold = cms.double(-1000.0),
            MomConstrMethod = cms.int32(1),
            MomEBDepth = cms.double(0.3),
            MomEEDepth = cms.double(0.0),
            MomHBDepth = cms.double(0.2),
            MomHEDepth = cms.double(0.4),
            UseEcalRecoveredHits = cms.bool(False),
            UseEtEBTreshold = cms.bool(False),
            UseEtEETreshold = cms.bool(False),
            UseHO = cms.bool(True),
            UseHcalRecoveredHits = cms.bool(True),
            UseRejectedHitsOnly = cms.bool(False),
            UseRejectedRecoveredEcalHits = cms.bool(False),
            UseRejectedRecoveredHcalHits = cms.bool(True),
            UseSymEBTreshold = cms.bool(True),
            UseSymEETreshold = cms.bool(True),
            ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEB"), cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEE")),
            hbheInput = cms.InputTag("hbhereco"+str(layers)),
            hfInput = cms.InputTag("hfreco"+str(layers)),
            hoInput = cms.InputTag("horeco"+str(layers)),
            missingHcalRescaleFactorForEcal = cms.double(1.0)
        )
    )
    
    setattr(process,"inclusiveSecondaryVertices"+str(layers),process.inclusiveSecondaryVertices.clone(
            maxFraction = cms.double(0.2),
            minSignificance = cms.double(10.0),
            secondaryVertices = cms.InputTag("trackVertexArbitrator"+str(layers))
        )
    )
    
    setattr(process,"inclusiveVertexFinder"+str(layers),process.inclusiveVertexFinder.clone(
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterizer = cms.PSet(
                clusterMaxDistance = cms.double(0.05),
                clusterMaxSignificance = cms.double(4.5),
                clusterMinAngleCosine = cms.double(0.5),
                distanceRatio = cms.double(20),
                maxTimeSignificance = cms.double(3.5),
                seedMax3DIPSignificance = cms.double(9999),
                seedMax3DIPValue = cms.double(9999),
                seedMin3DIPSignificance = cms.double(1.2),
                seedMin3DIPValue = cms.double(0.005)
            ),
            fitterRatio = cms.double(0.25),
            fitterSigmacut = cms.double(3),
            fitterTini = cms.double(256),
            maxNTracks = cms.uint32(30),
            maximumLongitudinalImpactParameter = cms.double(0.3),
            maximumTimeSignificance = cms.double(3),
            mightGet = cms.optional.untracked.vstring,
            minHits = cms.uint32(8),
            minPt = cms.double(0.8),
            primaryVertices = cms.InputTag("offlinePrimaryVertices"+str(layers)),
            tracks = cms.InputTag("generalTracks"+str(layers)),
            useDirectVertexFitter = cms.bool(True),
            useVertexReco = cms.bool(True),
            vertexMinAngleCosine = cms.double(0.95),
            vertexMinDLen2DSig = cms.double(2.5),
            vertexMinDLenSig = cms.double(0.5),
            vertexReco = cms.PSet(
                finder = cms.string('avr'),
                primcut = cms.double(1),
                seccut = cms.double(3),
                smoothing = cms.bool(True)
            )
        )
    )
    
    setattr(process,"trackVertexArbitrator"+str(layers),process.trackVertexArbitrator.clone(
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            dLenFraction = cms.double(0.333),
            dRCut = cms.double(0.4),
            distCut = cms.double(0.04),
            fitterRatio = cms.double(0.25),
            fitterSigmacut = cms.double(3),
            fitterTini = cms.double(256),
            maxTimeSignificance = cms.double(3.5),
            mightGet = cms.optional.untracked.vstring,
            primaryVertices = cms.InputTag("offlinePrimaryVertices"+str(layers)),
            secondaryVertices = cms.InputTag("vertexMerger"+str(layers)),
            sigCut = cms.double(5),
            trackMinLayers = cms.int32(4),
            trackMinPixels = cms.int32(1),
            trackMinPt = cms.double(0.4),
            tracks = cms.InputTag("generalTracks"+str(layers))
        )
    )
    
    setattr(process,"vertexMerger"+str(layers),process.vertexMerger.clone(
            maxFraction = cms.double(0.7),
            minSignificance = cms.double(2),
            secondaryVertices = cms.InputTag("inclusiveVertexFinder"+str(layers))
        )
    )
    
    setattr(process,"dedxHarmonic2"+str(layers),process.dedxHarmonic2.clone(
            MeVperADCPixel = cms.double(3.61e-06),
            MeVperADCStrip = cms.double(0.0009566500000000001),
            ProbabilityMode = cms.string('Accumulation'),
            Record = cms.string('SiStripDeDxMip_3D_Rcd'),
            ShapeTest = cms.bool(True),
            UseCalibration = cms.bool(False),
            UsePixel = cms.bool(False),
            UseStrip = cms.bool(True),
            calibrationPath = cms.string(''),
            estimator = cms.string('generic'),
            exponent = cms.double(-2),
            fraction = cms.double(0.4),
            mightGet = cms.optional.untracked.vstring,
            tracks = cms.InputTag("generalTracks"+str(layers))
        )
    )
    
    setattr(process,"dedxHitInfo"+str(layers),process.dedxHitInfo.clone(
            MeVperADCPixel = cms.double(3.61e-06),
            MeVperADCStrip = cms.double(0.0009566500000000001),
            calibrationPath = cms.string('file:Gains.root'),
            lowPtTracksDeDxThreshold = cms.double(3.5),
            lowPtTracksEstimatorParameters = cms.PSet(
                exponent = cms.double(-2.0),
                fraction = cms.double(-0.15),
                truncate = cms.bool(True),
            ),
            lowPtTracksPrescaleFail = cms.uint32(2000),
            lowPtTracksPrescalePass = cms.uint32(100),
            maxTrackEta = cms.double(5.0),
            minTrackHits = cms.uint32(0),
            minTrackPt = cms.double(10),
            minTrackPtPrescale = cms.double(0.5),
            shapeTest = cms.bool(True),
            tracks = cms.InputTag("generalTracks"+str(layers)),
            useCalibration = cms.bool(False),
            usePixel = cms.bool(True),
            useStrip = cms.bool(True)
        )
    )
    
    setattr(process,"dedxPixelAndStripHarmonic2T085"+str(layers),process.dedxPixelAndStripHarmonic2T085.clone(
            MeVperADCPixel = cms.double(3.61e-06),
            MeVperADCStrip = cms.double(0.0009566500000000001),
            ProbabilityMode = cms.string('Accumulation'),
            Record = cms.string('SiStripDeDxMip_3D_Rcd'),
            ShapeTest = cms.bool(True),
            UseCalibration = cms.bool(False),
            UsePixel = cms.bool(True),
            UseStrip = cms.bool(True),
            calibrationPath = cms.string(''),
            estimator = cms.string('genericTruncated'),
            exponent = cms.double(-2),
            fraction = cms.double(-0.15),
            mightGet = cms.optional.untracked.vstring,
            tracks = cms.InputTag("generalTracks"+str(layers))
        )
    )
    
    setattr(process,"dedxPixelHarmonic2"+str(layers),process.dedxPixelHarmonic2.clone(
            MeVperADCPixel = cms.double(3.61e-06),
            MeVperADCStrip = cms.double(0.0009566500000000001),
            ProbabilityMode = cms.string('Accumulation'),
            Record = cms.string('SiStripDeDxMip_3D_Rcd'),
            ShapeTest = cms.bool(True),
            UseCalibration = cms.bool(False),
            UsePixel = cms.bool(True),
            UseStrip = cms.bool(False),
            calibrationPath = cms.string(''),
            estimator = cms.string('generic'),
            exponent = cms.double(-2),
            fraction = cms.double(0.4),
            mightGet = cms.optional.untracked.vstring,
            tracks = cms.InputTag("generalTracks"+str(layers))
        )
    )
    
    setattr(process,"dedxTruncated40"+str(layers),process.dedxTruncated40.clone(
            MeVperADCPixel = cms.double(3.61e-06),
            MeVperADCStrip = cms.double(0.0009566500000000001),
            ProbabilityMode = cms.string('Accumulation'),
            Record = cms.string('SiStripDeDxMip_3D_Rcd'),
            ShapeTest = cms.bool(True),
            UseCalibration = cms.bool(False),
            UsePixel = cms.bool(False),
            UseStrip = cms.bool(True),
            calibrationPath = cms.string(''),
            estimator = cms.string('truncated'),
            exponent = cms.double(-2),
            fraction = cms.double(0.4),
            mightGet = cms.optional.untracked.vstring,
            tracks = cms.InputTag("generalTracks"+str(layers))
        )
    )
    
    setattr(process,"detachedTripletStepSeedClusterMask"+str(layers),process.detachedTripletStepSeedClusterMask.clone(
            Common = cms.PSet(
                maxChi2 = cms.double(9.0)
            ),
            oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("lowPtTripletStepSeeds"+str(layers))
        )
    )
    
    setattr(process,"initialStepSeedClusterMask"+str(layers),process.initialStepSeedClusterMask.clone(
            Common = cms.PSet(
                maxChi2 = cms.double(9.0)
            ),
            oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("initialStepSeeds"+str(layers))
        )
    )
    
    setattr(process,"mixedTripletStepSeedClusterMask"+str(layers),process.mixedTripletStepSeedClusterMask.clone(
            Common = cms.PSet(
                maxChi2 = cms.double(9.0)
            ),
            oldClusterRemovalInfo = cms.InputTag("detachedTripletStepSeedClusterMask"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("mixedTripletStepSeeds"+str(layers))
        )
    )
    
    setattr(process,"newCombinedSeeds"+str(layers),process.newCombinedSeeds.clone(
            seedCollections = cms.VInputTag(
                "initialStepSeeds"+str(layers), "highPtTripletStepSeeds"+str(layers), "mixedTripletStepSeeds"+str(layers), "pixelLessStepSeeds"+str(layers), "tripletElectronSeeds"+str(layers),
                "pixelPairElectronSeeds"+str(layers), "stripPairElectronSeeds"+str(layers), "lowPtTripletStepSeeds"+str(layers), "lowPtQuadStepSeeds"+str(layers), "detachedTripletStepSeeds"+str(layers),
                "detachedQuadStepSeeds"+str(layers), "pixelPairStepSeeds"+str(layers)
            )
        )
    )
    
    setattr(process,"pixelLessStepSeedClusterMask"+str(layers),process.pixelLessStepSeedClusterMask.clone(
            Common = cms.PSet(
                maxChi2 = cms.double(9.0)
            ),
            oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("pixelLessStepSeeds"+str(layers))
        )
    )
    
    setattr(process,"pixelPairElectronHitDoublets"+str(layers),process.pixelPairElectronHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(1000000),
            maxElementTotal = cms.uint32(12000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            seedingLayers = cms.InputTag("pixelPairElectronSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("pixelPairElectronTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"pixelPairElectronSeedLayers"+str(layers),process.pixelPairElectronSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("tripletElectronClusterMask"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("tripletElectronClusterMask"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2',
                'BPix1+BPix3',
                'BPix1+BPix4',
                'BPix2+BPix3',
                'BPix2+BPix4',
                'BPix3+BPix4',
                'BPix1+FPix1_pos',
                'BPix1+FPix1_neg',
                'BPix1+FPix2_pos',
                'BPix1+FPix2_neg',
                'BPix2+FPix1_pos',
                'BPix2+FPix1_neg',
                'FPix1_pos+FPix2_pos',
                'FPix1_neg+FPix2_neg',
                'FPix1_pos+FPix3_pos',
                'FPix1_neg+FPix3_neg',
                'FPix2_pos+FPix3_pos',
                'FPix2_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"pixelPairElectronSeeds"+str(layers),process.pixelPairElectronSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairElectronHitDoublets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("pixelPairElectronHitDoublets"+str(layers))
        )
    )
    
    setattr(process,"pixelPairElectronTrackingRegions"+str(layers),process.pixelPairElectronTrackingRegions.clone(
            RegionPSet = cms.PSet(
                VertexCollection = cms.InputTag("firstStepPrimaryVertices"+str(layers)),
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                fixedError = cms.double(0.03),
                halfLengthScaling4BigEvts = cms.bool(False),
                maxNVertices = cms.int32(-1),
                maxPtMin = cms.double(1000),
                minHalfLength = cms.double(0),
                minOriginR = cms.double(0),
                nSigmaZ = cms.double(4),
                originRScaling4BigEvts = cms.bool(False),
                originRadius = cms.double(0.015),
                pixelClustersForScaling = cms.InputTag(myCollection),
                precise = cms.bool(True),
                ptMin = cms.double(1.0),
                ptMinScaling4BigEvts = cms.bool(False),
                scalingEndNPix = cms.double(1),
                scalingStartNPix = cms.double(0),
                sigmaZVertex = cms.double(3),
                useFakeVertices = cms.bool(False),
                useFixedError = cms.bool(True),
                useFoundVertices = cms.bool(True),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"stripPairElectronHitDoublets"+str(layers),process.stripPairElectronHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(1000000),
            maxElementTotal = cms.uint32(12000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            seedingLayers = cms.InputTag("stripPairElectronSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("stripPairElectronTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"stripPairElectronSeedLayers"+str(layers),process.stripPairElectronSeedLayers.clone(
            BPix = cms.PSet(
        
            ),
            FPix = cms.PSet(
        
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutNone')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                maxRing = cms.int32(2),
                minRing = cms.int32(1),
                skipClusters = cms.InputTag("tripletElectronClusterMask"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            TIB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutNone')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                skipClusters = cms.InputTag("tripletElectronClusterMask"+str(layers))
            ),
            TID = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutNone')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                maxRing = cms.int32(2),
                minRing = cms.int32(1),
                skipClusters = cms.InputTag("tripletElectronClusterMask"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'TIB1+TIB2',
                'TIB1+TID1_pos',
                'TIB1+TID1_neg',
                'TID2_pos+TID3_pos',
                'TID2_neg+TID3_neg',
                'TEC1_pos+TEC2_pos',
                'TEC2_pos+TEC3_pos',
                'TEC3_pos+TEC4_pos',
                'TEC3_pos+TEC5_pos',
                'TEC1_neg+TEC2_neg',
                'TEC2_neg+TEC3_neg',
                'TEC3_neg+TEC4_neg',
                'TEC3_neg+TEC5_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"stripPairElectronSeeds"+str(layers),process.stripPairElectronSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_stripPairElectronHitDoublets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("stripPairElectronHitDoublets"+str(layers))
        )
    )
    
    setattr(process,"stripPairElectronTrackingRegions"+str(layers),process.stripPairElectronTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(0),
                originHalfLength = cms.double(12.0),
                originRadius = cms.double(0.4),
                precise = cms.bool(True),
                ptMin = cms.double(1.0),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"tripletElectronClusterMask"+str(layers),process.tripletElectronClusterMask.clone(
            Common = cms.PSet(
                maxChi2 = cms.double(9.0)
            ),
            oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("tripletElectronSeeds"+str(layers))
        )
    )
    
    setattr(process,"tripletElectronHitDoublets"+str(layers),process.tripletElectronHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("tripletElectronSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("tripletElectronTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"tripletElectronHitTriplets"+str(layers),process.tripletElectronHitTriplets.clone(
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            doublets = cms.InputTag("tripletElectronHitDoublets"+str(layers)),
            extraHitRPhitolerance = cms.double(0.032),
            extraHitRZtolerance = cms.double(0.037),
            maxElement = cms.uint32(1000000),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_tripletElectronHitDoublets'+str(layers)+'__reRECO'),
            phiPreFiltering = cms.double(0.3),
            produceIntermediateHitTriplets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            useMultScattering = cms.bool(True)
        )
    )
    
    setattr(process,"tripletElectronSeedLayers"+str(layers),process.tripletElectronSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
                skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
                skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2+BPix3',
                'BPix2+BPix3+BPix4',
                'BPix1+BPix3+BPix4',
                'BPix1+BPix2+BPix4',
                'BPix2+BPix3+FPix1_pos',
                'BPix2+BPix3+FPix1_neg',
                'BPix1+BPix2+FPix1_pos',
                'BPix1+BPix2+FPix1_neg',
                'BPix1+BPix3+FPix1_pos',
                'BPix1+BPix3+FPix1_neg',
                'BPix2+FPix1_pos+FPix2_pos',
                'BPix2+FPix1_neg+FPix2_neg',
                'BPix1+FPix1_pos+FPix2_pos',
                'BPix1+FPix1_neg+FPix2_neg',
                'BPix1+BPix2+FPix2_pos',
                'BPix1+BPix2+FPix2_neg',
                'FPix1_pos+FPix2_pos+FPix3_pos',
                'FPix1_neg+FPix2_neg+FPix3_neg',
                'BPix1+FPix2_pos+FPix3_pos',
                'BPix1+FPix2_neg+FPix3_neg',
                'BPix1+FPix1_pos+FPix3_pos',
                'BPix1+FPix1_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"tripletElectronSeeds"+str(layers),process.tripletElectronSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring(
                'RegionsSeedingHitSets_tripletElectronHitTriplets'+str(layers)+'__reRECO',
                'IntermediateHitDoublets_tripletElectronHitDoublets'+str(layers)+'__reRECO'
            ),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("tripletElectronHitTriplets"+str(layers))
        )
    )
    
    setattr(process,"tripletElectronTrackingRegions"+str(layers),process.tripletElectronTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(4),
                originHalfLength = cms.double(0),
                originRadius = cms.double(0.02),
                precise = cms.bool(True),
                ptMin = cms.double(1.0),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"conversionStepTracks"+str(layers),process.conversionStepTracks.clone(
            Epsilon = cms.double(-0.001),
            FoundHitBonus = cms.double(5.0),
            LostHitPenalty = cms.double(5.0),
            MaxNormalizedChisq = cms.double(1000.0),
            MinFound = cms.int32(3),
            MinPT = cms.double(0.05),
            ShareFrac = cms.double(0.19),
            TrackProducers = cms.VInputTag("convStepTracks"+str(layers)),
            allowFirstHitShare = cms.bool(True),
            copyExtras = cms.untracked.bool(True),
            copyMVA = cms.bool(True),
            hasSelector = cms.vint32(1),
            indivShareFrac = cms.vdouble(1.0, 1.0),
            makeReKeyedSeeds = cms.untracked.bool(False),
            newQuality = cms.string('confirmed'),
            selectedTrackQuals = cms.VInputTag("convStepSelector"+str(layers)+":convStep"+str(layers)),
            setsToMerge = cms.VPSet(cms.PSet(
                pQual = cms.bool(True),
                tLists = cms.vint32(1)
            )),
            trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
            writeOnlyTrkQuals = cms.bool(False)
        )
    )
    
    setattr(process,"earlyGeneralTracks"+str(layers),process.earlyGeneralTracks.clone(
            allowFirstHitShare = cms.bool(True),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            enableMerging = cms.bool(True),
            foundHitBonus = cms.double(10),
            inputClassifiers = cms.vstring(
                'initialStep'+str(layers),
                'highPtTripletStep'+str(layers),
                'jetCoreRegionalStep'+str(layers),
                'lowPtQuadStep'+str(layers),
                'lowPtTripletStep'+str(layers),
                'detachedQuadStep'+str(layers),
                'detachedTripletStep'+str(layers),
                'pixelPairStep'+str(layers),
                'mixedTripletStep'+str(layers),
                'pixelLessStep'+str(layers),
                'tobTecStep'+str(layers)
            ),
            lostHitPenalty = cms.double(5),
            mightGet = cms.optional.untracked.vstring,
            minQuality = cms.string('loose'),
            minShareHits = cms.uint32(2),
            shareFrac = cms.double(0.19),
            trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
            trackProducers = cms.VInputTag(
                "initialStepTracks"+str(layers), "highPtTripletStepTracks"+str(layers), "jetCoreRegionalStepTracks"+str(layers), "lowPtQuadStepTracks"+str(layers), "lowPtTripletStepTracks"+str(layers),
                "detachedQuadStepTracks"+str(layers), "detachedTripletStepTracks"+str(layers), "pixelPairStepTracks"+str(layers), "mixedTripletStepTracks"+str(layers), "pixelLessStepTracks"+str(layers),
                "tobTecStepTracks"+str(layers)
            )
        )
    )
    
    setattr(process,"preDuplicateMergingGeneralTracks"+str(layers),process.preDuplicateMergingGeneralTracks.clone(
            allowFirstHitShare = cms.bool(True),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            enableMerging = cms.bool(True),
            foundHitBonus = cms.double(100.0),
            inputClassifiers = cms.vstring(
                'earlyGeneralTracks'+str(layers),
                'muonSeededTracksInOutClassifier'+str(layers),
                'muonSeededTracksOutInClassifier'+str(layers)
            ),
            lostHitPenalty = cms.double(1.0),
            mightGet = cms.optional.untracked.vstring,
            minQuality = cms.string('loose'),
            minShareHits = cms.uint32(2),
            shareFrac = cms.double(0.19),
            trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
            trackProducers = cms.VInputTag("earlyGeneralTracks"+str(layers), "muonSeededTracksInOut"+str(layers), "muonSeededTracksOutIn"+str(layers))
        )
    )
    
    setattr(process,"trackdnn_source"+str(layers),process.trackdnn_source.clone(
            firstValid = cms.vuint32(1),
            iovIsRunNotTime = cms.bool(True),
            recordName = cms.string('TfGraphRecord')
        )
    )
    
    setattr(process,"trackerClusterCheck"+str(layers),process.trackerClusterCheck.clone(
            ClusterCollectionLabel = cms.InputTag(myCollection),
            MaxNumberOfCosmicClusters = cms.uint32(400000),
            MaxNumberOfPixelClusters = cms.uint32(40000),
            PixelClusterCollectionLabel = cms.InputTag(myCollection),
            cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
            doClusterCheck = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            silentClusterCheck = cms.untracked.bool(False)
        )
    )
    
    setattr(process,"convClusters"+str(layers),process.convClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(30),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("tobTecStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("tobTecStepTracks"+str(layers))
        )
    )
    
    setattr(process,"convLayerPairs"+str(layers),process.convLayerPairs.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("convClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("convClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHit"),
                skipClusters = cms.InputTag("convClusters"+str(layers))
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHit"),
                skipClusters = cms.InputTag("convClusters"+str(layers))
            ),
            TEC = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                maxRing = cms.int32(7),
                minRing = cms.int32(1),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHitUnmatched"),
                skipClusters = cms.InputTag("convClusters"+str(layers)),
                stereoRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"stereoRecHitUnmatched"),
                useRingSlector = cms.bool(True),
                useSimpleRphiHitsCleaner = cms.bool(False)
            ),
            TIB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                skipClusters = cms.InputTag("convClusters"+str(layers))
            ),
            TID = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                maxRing = cms.int32(2),
                minRing = cms.int32(1),
                skipClusters = cms.InputTag("convClusters"+str(layers)),
                useRingSlector = cms.bool(True),
                useSimpleRphiHitsCleaner = cms.bool(False)
            ),
            TOB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                skipClusters = cms.InputTag("convClusters"+str(layers))
            ),
            layerList = cms.vstring(
                'BPix1+BPix2',
                'BPix2+BPix3',
                'BPix3+BPix4',
                'BPix2+FPix1_pos',
                'BPix2+FPix1_neg',
                'BPix2+FPix2_pos',
                'BPix2+FPix2_neg',
                'BPix3+FPix1_pos',
                'BPix3+FPix1_neg',
                'FPix1_pos+FPix2_pos',
                'FPix1_neg+FPix2_neg',
                'FPix2_pos+FPix3_pos',
                'FPix2_neg+FPix3_neg',
                'BPix3+TIB1',
                'BPix4+TIB1',
                'BPix4+TIB2',
                'TIB1+TID1_pos',
                'TIB1+TID1_neg',
                'TIB1+TID2_pos',
                'TIB1+TID2_neg',
                'TIB1+TIB2',
                'TIB1+MTIB3',
                'TIB2+TID1_pos',
                'TIB2+TID1_neg',
                'TIB2+TID2_pos',
                'TIB2+TID2_neg',
                'TIB2+MTIB3',
                'TIB2+MTIB4',
                'MTIB3+MTIB4',
                'MTIB3+TOB1',
                'MTIB3+TID1_pos',
                'MTIB3+TID1_neg',
                'MTIB4+TOB1',
                'MTIB4+TOB2',
                'TOB1+TOB2',
                'TOB1+MTOB3',
                'TOB1+TEC1_pos',
                'TOB1+TEC1_neg',
                'TOB2+MTOB3',
                'TOB2+MTOB4',
                'TOB2+TEC1_pos',
                'TOB2+TEC1_neg',
                'TID1_pos+TID2_pos',
                'TID2_pos+TID3_pos',
                'TID3_pos+TEC1_pos',
                'TID1_neg+TID2_neg',
                'TID2_neg+TID3_neg',
                'TID3_neg+TEC1_neg',
                'TEC1_pos+TEC2_pos',
                'TEC2_pos+TEC3_pos',
                'TEC3_pos+TEC4_pos',
                'TEC4_pos+TEC5_pos',
                'TEC5_pos+TEC6_pos',
                'TEC6_pos+TEC7_pos',
                'TEC7_pos+TEC8_pos',
                'TEC1_neg+TEC2_neg',
                'TEC2_neg+TEC3_neg',
                'TEC3_neg+TEC4_neg',
                'TEC4_neg+TEC5_neg',
                'TEC5_neg+TEC6_neg',
                'TEC6_neg+TEC7_neg',
                'TEC7_neg+TEC8_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"convStepSelector"+str(layers),process.convStepSelector.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            src = cms.InputTag("convStepTracks"+str(layers)),
            trackSelectors = cms.VPSet(
                cms.PSet(
                    applyAbsCutsIfNoPV = cms.bool(False),
                    applyAdaptedPVCuts = cms.bool(False),
                    chi2n_no1Dmod_par = cms.double(9999),
                    chi2n_par = cms.double(3.0),
                    copyExtras = cms.untracked.bool(True),
                    copyTrajectories = cms.untracked.bool(False),
                    d0_par1 = cms.vdouble(5.0, 8.0),
                    d0_par2 = cms.vdouble(5.0, 8.0),
                    dz_par1 = cms.vdouble(5.0, 8.0),
                    dz_par2 = cms.vdouble(5.0, 8.0),
                    keepAllTracks = cms.bool(False),
                    maxNumberLostLayers = cms.uint32(1),
                    max_d0 = cms.double(100.0),
                    max_eta = cms.double(9999.0),
                    max_lostHitFraction = cms.double(1.0),
                    max_minMissHitOutOrIn = cms.int32(99),
                    max_relpterr = cms.double(9999.0),
                    max_z0 = cms.double(100.0),
                    minHitsToBypassChecks = cms.uint32(20),
                    minNumber3DLayers = cms.uint32(1),
                    minNumberLayers = cms.uint32(3),
                    min_eta = cms.double(-9999.0),
                    min_nhits = cms.uint32(0),
                    nSigmaZ = cms.double(4.0),
                    name = cms.string('convStepLoose'),
                    preFilterName = cms.string(''),
                    qualityBit = cms.string('loose'),
                    res_par = cms.vdouble(0.003, 0.001),
                    vertexCut = cms.string('ndof>=2&!isFake'),
                    vtxNumber = cms.int32(-1)
                ),
                cms.PSet(
                    applyAbsCutsIfNoPV = cms.bool(False),
                    applyAdaptedPVCuts = cms.bool(True),
                    chi2n_no1Dmod_par = cms.double(9999),
                    chi2n_par = cms.double(2.5),
                    copyExtras = cms.untracked.bool(True),
                    copyTrajectories = cms.untracked.bool(False),
                    d0_par1 = cms.vdouble(5.0, 8.0),
                    d0_par2 = cms.vdouble(5.0, 8.0),
                    dz_par1 = cms.vdouble(5.0, 8.0),
                    dz_par2 = cms.vdouble(5.0, 8.0),
                    keepAllTracks = cms.bool(True),
                    maxNumberLostLayers = cms.uint32(1),
                    max_d0 = cms.double(100.0),
                    max_eta = cms.double(9999.0),
                    max_lostHitFraction = cms.double(1.0),
                    max_minMissHitOutOrIn = cms.int32(99),
                    max_relpterr = cms.double(9999.0),
                    max_z0 = cms.double(100.0),
                    minHitsToBypassChecks = cms.uint32(20),
                    minNumber3DLayers = cms.uint32(1),
                    minNumberLayers = cms.uint32(3),
                    min_eta = cms.double(-9999.0),
                    min_nhits = cms.uint32(0),
                    nSigmaZ = cms.double(4.0),
                    name = cms.string('convStepTight'),
                    preFilterName = cms.string('convStepLoose'),
                    qualityBit = cms.string('tight'),
                    res_par = cms.vdouble(0.003, 0.001),
                    vertexCut = cms.string('ndof>=2&!isFake'),
                    vtxNumber = cms.int32(-1)
                ),
                cms.PSet(
                    applyAbsCutsIfNoPV = cms.bool(False),
                    applyAdaptedPVCuts = cms.bool(True),
                    chi2n_no1Dmod_par = cms.double(9999),
                    chi2n_par = cms.double(2.0),
                    copyExtras = cms.untracked.bool(True),
                    copyTrajectories = cms.untracked.bool(False),
                    d0_par1 = cms.vdouble(5.0, 8.0),
                    d0_par2 = cms.vdouble(5.0, 8.0),
                    dz_par1 = cms.vdouble(5.0, 8.0),
                    dz_par2 = cms.vdouble(5.0, 8.0),
                    keepAllTracks = cms.bool(True),
                    maxNumberLostLayers = cms.uint32(1),
                    max_d0 = cms.double(100.0),
                    max_eta = cms.double(9999.0),
                    max_lostHitFraction = cms.double(1.0),
                    max_minMissHitOutOrIn = cms.int32(99),
                    max_relpterr = cms.double(9999.0),
                    max_z0 = cms.double(100.0),
                    minHitsToBypassChecks = cms.uint32(20),
                    minNumber3DLayers = cms.uint32(1),
                    minNumberLayers = cms.uint32(3),
                    min_eta = cms.double(-9999.0),
                    min_nhits = cms.uint32(0),
                    nSigmaZ = cms.double(4.0),
                    name = cms.string('convStep'),
                    preFilterName = cms.string('convStepTight'),
                    qualityBit = cms.string('highPurity'),
                    res_par = cms.vdouble(0.003, 0.001),
                    vertexCut = cms.string('ndof>=2&!isFake'),
                    vtxNumber = cms.int32(-1)
                )
            ),
            useVertices = cms.bool(True),
            useVtxError = cms.bool(False),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"convStepTracks"+str(layers),process.convStepTracks.clone(
            AlgorithmName = cms.string('conversionStep'),
            Fitter = cms.string('convStepFitterSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("convTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"convTrackCandidates"+str(layers),process.convTrackCandidates.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('convCkfTrajectoryBuilder')
            ),
            TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag("convClusters"+str(layers)),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(5000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(4),
            onlyPixelHitsForSeedCleaner = cms.bool(False),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("photonConvTrajSeedFromSingleLeg"+str(layers),"convSeedCandidates"),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"photonConvTrajSeedFromSingleLeg"+str(layers),process.photonConvTrajSeedFromSingleLeg.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(400000),
                MaxNumberOfPixelClusters = cms.uint32(40000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
                doClusterCheck = cms.bool(False)
            ),
            DoxcheckSeedCandidates = cms.bool(False),
            OrderedHitsFactoryPSet = cms.PSet(
                SeedingLayers = cms.InputTag("convLayerPairs"+str(layers)),
                maxElement = cms.uint32(40000),
                maxHitPairsPerTrackAndGenerator = cms.uint32(10)
            ),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
                RegionPSet = cms.PSet(
                    beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                    originHalfLength = cms.double(12.0),
                    originRadius = cms.double(3.0),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.2)
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('SeedForPhotonConversion1Leg'),
                SeedMomentumForBOFF = cms.double(5.0),
                TTRHBuilder = cms.string('WithTrackAngle'),
                propagator = cms.string('PropagatorWithMaterial')
            ),
            TrackRefitter = cms.InputTag("generalTracks"+str(layers)),
            applyTkVtxConstraint = cms.bool(True),
            beamSpotInputTag = cms.InputTag("offlineBeamSpot"+str(layers)),
            maxDZSigmas = cms.double(10.0),
            maxNumSelVtx = cms.uint32(2),
            newSeedCandidates = cms.string('convSeedCandidates'),
            primaryVerticesTag = cms.InputTag("firstStepPrimaryVertices"+str(layers)),
            vtxMinDoF = cms.double(4),
            xcheckSeedCandidates = cms.string('xcheckSeedCandidates')
        )
    )
    
    setattr(process,"MeasurementTrackerEvent"+str(layers),process.MeasurementTrackerEvent.clone(
            Phase2TrackerCluster1DProducer = cms.string(''),
            badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
            inactivePixelDetectorLabels = cms.VInputTag("siPixelDigis"),
            inactiveStripDetectorLabels = cms.VInputTag("siStripDigis"),
            measurementTracker = cms.string(''),
            mightGet = cms.optional.untracked.vstring,
            pixelCablingMapLabel = cms.string(''),
            pixelClusterProducer = cms.string(myCollection),
            skipClusters = cms.InputTag(""),
            stripClusterProducer = cms.string(myCollection),
            switchOffPixelsIfEmpty = cms.bool(True),
            vectorHits = cms.InputTag(""),
            vectorHitsRej = cms.InputTag("")
        )
    )
    
    setattr(process,"ak4CaloJetsForTrkPreSplitting"+str(layers),process.ak4CaloJetsForTrkPreSplitting.clone(
            Active_Area_Repeats = cms.int32(1),
            GhostArea = cms.double(0.01),
            Ghost_EtaMax = cms.double(5.0),
            Rho_EtaMax = cms.double(4.4),
            applyWeight = cms.bool(False),
            doAreaDiskApprox = cms.bool(False),
            doAreaFastjet = cms.bool(False),
            doPUOffsetCorr = cms.bool(False),
            doPVCorrection = cms.bool(True),
            doRhoFastjet = cms.bool(False),
            inputEMin = cms.double(0.0),
            inputEtMin = cms.double(0.3),
            jetAlgorithm = cms.string('AntiKt'),
            jetPtMin = cms.double(10.0),
            jetType = cms.string('CaloJet'),
            maxBadEcalCells = cms.uint32(9999999),
            maxBadHcalCells = cms.uint32(9999999),
            maxProblematicEcalCells = cms.uint32(9999999),
            maxProblematicHcalCells = cms.uint32(9999999),
            maxRecoveredEcalCells = cms.uint32(9999999),
            maxRecoveredHcalCells = cms.uint32(9999999),
            minSeed = cms.uint32(14327),
            nSigmaPU = cms.double(1.0),
            puPtMin = cms.double(10),
            rParam = cms.double(0.4),
            radiusPU = cms.double(0.5),
            src = cms.InputTag("caloTowerForTrkPreSplitting"+str(layers)),
            srcPVs = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+str(layers)),
            useDeterministicSeed = cms.bool(True),
            voronoiRfact = cms.double(-0.9)
        )
    )
    
    setattr(process,"caloTowerForTrkPreSplitting"+str(layers),process.caloTowerForTrkPreSplitting.clone(
            AllowMissingInputs = cms.bool(False),
            EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            EBSumThreshold = cms.double(0.2),
            EBThreshold = cms.double(0.07),
            EBWeight = cms.double(1.0),
            EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            EESumThreshold = cms.double(0.45),
            EEThreshold = cms.double(0.3),
            EEWeight = cms.double(1.0),
            EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            EcalRecHitSeveritiesToBeExcluded = cms.vstring(
                'kTime',
                'kWeird',
                'kBad'
            ),
            EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
            EcutTower = cms.double(-1000.0),
            HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HBThreshold = cms.double(0.3),
            HBThreshold1 = cms.double(0.1),
            HBThreshold2 = cms.double(0.2),
            HBWeight = cms.double(1.0),
            HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HEDThreshold = cms.double(0.2),
            HEDThreshold1 = cms.double(0.1),
            HEDWeight = cms.double(1.0),
            HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HESThreshold = cms.double(0.2),
            HESThreshold1 = cms.double(0.1),
            HESWeight = cms.double(1.0),
            HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HF1Threshold = cms.double(0.5),
            HF1Weight = cms.double(1.0),
            HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HF2Threshold = cms.double(0.85),
            HF2Weight = cms.double(1.0),
            HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
            HOThreshold0 = cms.double(1.1),
            HOThresholdMinus1 = cms.double(3.5),
            HOThresholdMinus2 = cms.double(3.5),
            HOThresholdPlus1 = cms.double(3.5),
            HOThresholdPlus2 = cms.double(3.5),
            HOWeight = cms.double(1.0),
            HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
            HcalAcceptSeverityLevel = cms.uint32(9),
            HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
            HcalPhase = cms.int32(1),
            HcalThreshold = cms.double(-1000.0),
            MomConstrMethod = cms.int32(1),
            MomEBDepth = cms.double(0.3),
            MomEEDepth = cms.double(0.0),
            MomHBDepth = cms.double(0.2),
            MomHEDepth = cms.double(0.4),
            UseEcalRecoveredHits = cms.bool(False),
            UseEtEBTreshold = cms.bool(False),
            UseEtEETreshold = cms.bool(False),
            UseHO = cms.bool(True),
            UseHcalRecoveredHits = cms.bool(True),
            UseRejectedHitsOnly = cms.bool(False),
            UseRejectedRecoveredEcalHits = cms.bool(False),
            UseRejectedRecoveredHcalHits = cms.bool(True),
            UseSymEBTreshold = cms.bool(True),
            UseSymEETreshold = cms.bool(True),
            ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEB"), cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEE")),
            hbheInput = cms.InputTag("hbhereco"+str(layers)),
            hfInput = cms.InputTag("hfreco"+str(layers)),
            hoInput = cms.InputTag("horeco"+str(layers)),
            missingHcalRescaleFactorForEcal = cms.double(1.0)
        )
    )
    
    setattr(process,"firstStepPrimaryVerticesPreSplitting"+str(layers),process.firstStepPrimaryVerticesPreSplitting.clone(
            TkClusParameters = cms.PSet(
                TkDAClusParameters = cms.PSet(
                    Tmin = cms.double(2.0),
                    Tpurge = cms.double(2.0),
                    Tstop = cms.double(0.5),
                    convergence_mode = cms.int32(0),
                    coolingFactor = cms.double(0.6),
                    d0CutOff = cms.double(3.0),
                    delta_highT = cms.double(0.01),
                    delta_lowT = cms.double(0.001),
                    dzCutOff = cms.double(3.0),
                    uniquetrkminp = cms.double(0.0),
                    uniquetrkweight = cms.double(0.8),
                    vertexSize = cms.double(0.006),
                    zmerge = cms.double(0.01),
                    zrange = cms.double(4.0)
                ),
                algorithm = cms.string('DA_vect')
            ),
            TkFilterParameters = cms.PSet(
                algorithm = cms.string('filter'),
                maxD0Error = cms.double(1.0),
                maxD0Significance = cms.double(4.0),
                maxDzError = cms.double(1.0),
                maxEta = cms.double(2.4),
                maxNormalizedChi2 = cms.double(10.0),
                minPixelLayersWithHits = cms.int32(2),
                minPt = cms.double(0.0),
                minSiliconLayersWithHits = cms.int32(5),
                trackQuality = cms.string('any')
            ),
            TrackLabel = cms.InputTag("initialStepTracksPreSplitting"+str(layers)),
            beamSpotLabel = cms.InputTag("offlineBeamSpot"+str(layers)),
            isRecoveryIteration = cms.bool(False),
            recoveryVtxCollection = cms.InputTag(""),
            verbose = cms.untracked.bool(False),
            vertexCollections = cms.VPSet(cms.PSet(
                algorithm = cms.string('AdaptiveVertexFitter'),
                chi2cutoff = cms.double(2.5),
                label = cms.string(''),
                maxDistanceToBeam = cms.double(1.0),
                minNdof = cms.double(0.0),
                useBeamConstraint = cms.bool(False)
            ))
        )
    )
    
    setattr(process,"initialStepHitDoubletsPreSplitting"+str(layers),process.initialStepHitDoubletsPreSplitting.clone(
            clusterCheck = cms.InputTag("trackerClusterCheckPreSplitting"+str(layers)),
            layerPairs = cms.vuint32(0, 1, 2),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("initialStepSeedLayersPreSplitting"+str(layers)),
            trackingRegions = cms.InputTag("initialStepTrackingRegionsPreSplitting"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"initialStepHitQuadrupletsPreSplitting"+str(layers),process.initialStepHitQuadrupletsPreSplitting.clone(
            CAHardPtCut = cms.double(0),
            CAOnlyOneLastHitPerLayerFilter = cms.optional.bool,
            CAPhiCut = cms.double(0.2),
            CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            CAThetaCut = cms.double(0.0012),
            CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
                clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCachePreSplitting"+str(layers)),
                clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
            ),
            doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"+str(layers)),
            extraHitRPhitolerance = cms.double(0.032),
            fitFastCircle = cms.bool(True),
            fitFastCircleChi2Cut = cms.bool(True),
            maxChi2 = cms.PSet(
                enabled = cms.bool(True),
                pt1 = cms.double(0.7),
                pt2 = cms.double(2),
                value1 = cms.double(200),
                value2 = cms.double(50)
            ),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoubletsPreSplitting'+str(layers)+'__reRECO'),
            useBendingCorrection = cms.bool(True)
        )
    )
    
    setattr(process,"initialStepSeedLayersPreSplitting"+str(layers),process.initialStepSeedLayersPreSplitting.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHitsPreSplitting'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHitsPreSplitting'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2+BPix3+BPix4',
                'BPix1+BPix2+BPix3+FPix1_pos',
                'BPix1+BPix2+BPix3+FPix1_neg',
                'BPix1+BPix2+FPix1_pos+FPix2_pos',
                'BPix1+BPix2+FPix1_neg+FPix2_neg',
                'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
                'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"initialStepSeedsPreSplitting"+str(layers),process.initialStepSeedsPreSplitting.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadrupletsPreSplitting'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("initialStepHitQuadrupletsPreSplitting"+str(layers))
        )
    )
    
    setattr(process,"initialStepTrackCandidatesMkFitConfigPreSplitting"+str(layers),process.initialStepTrackCandidatesMkFitConfigPreSplitting.clone(
            ComponentName = cms.string('initialStepTrackCandidatesMkFitConfigPreSplitting'+str(layers)),
            appendToDataLabel = cms.string(''),
            config = cms.FileInPath('RecoTracker/MkFit/data/mkfit-phase1-initialStep.json')
        )
    )
    
    setattr(process,"initialStepTrackCandidatesMkFitPreSplitting"+str(layers),process.initialStepTrackCandidatesMkFitPreSplitting.clone(
            backwardFitInCMSSW = cms.bool(False),
            buildingRoutine = cms.string('cloneEngine'),
            clustersToSkip = cms.InputTag(""),
            config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfigPreSplitting"+str(layers)),
            eventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+str(layers)),
            limitConcurrency = cms.untracked.bool(False),
            mightGet = cms.untracked.vstring(
                'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHitsPreSplitting'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHitsPreSplitting'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            minGoodStripCharge = cms.PSet(
                refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
            ),
            mkFitSilent = cms.untracked.bool(True),
            pixelHits = cms.InputTag("mkFitSiPixelHitsPreSplitting"+str(layers)),
            removeDuplicates = cms.bool(True),
            seedCleaning = cms.bool(True),
            seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+str(layers)),
            stripHits = cms.InputTag("mkFitSiStripHits"+str(layers))
        )
    )
    
    setattr(process,"initialStepTrackCandidatesMkFitSeedsPreSplitting"+str(layers),process.initialStepTrackCandidatesMkFitSeedsPreSplitting.clone(
            mightGet = cms.optional.untracked.vstring,
            seeds = cms.InputTag("initialStepSeedsPreSplitting"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"initialStepTrackCandidatesPreSplitting"+str(layers),process.initialStepTrackCandidatesPreSplitting.clone(
            mightGet = cms.untracked.vstring(
                'MkFitOutputWrapper_initialStepTrackCandidatesMkFitPreSplitting'+str(layers)+'__reRECO',
                'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeedsPreSplitting'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHitsPreSplitting'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHitsPreSplitting'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHitsPreSplitting'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            mkFitEventOfHits = cms.InputTag("mkFitEventOfHitsPreSplitting"+str(layers)),
            mkFitPixelHits = cms.InputTag("mkFitSiPixelHitsPreSplitting"+str(layers)),
            mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeedsPreSplitting"+str(layers)),
            mkFitStripHits = cms.InputTag("mkFitSiStripHits"+str(layers)),
            propagatorAlong = cms.ESInputTag("","PropagatorWithMaterial"),
            propagatorOpposite = cms.ESInputTag("","PropagatorWithMaterialOpposite"),
            seeds = cms.InputTag("initialStepSeedsPreSplitting"+str(layers)),
            tracks = cms.InputTag("initialStepTrackCandidatesMkFitPreSplitting"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"initialStepTrackRefsForJetsPreSplitting"+str(layers),process.initialStepTrackRefsForJetsPreSplitting.clone(
            particleType = cms.string('pi+'),
            src = cms.InputTag("initialStepTracksPreSplitting"+str(layers))
        )
    )
    
    setattr(process,"initialStepTrackingRegionsPreSplitting"+str(layers),process.initialStepTrackingRegionsPreSplitting.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(4),
                originHalfLength = cms.double(0),
                originRadius = cms.double(0.02),
                precise = cms.bool(True),
                ptMin = cms.double(0.5),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"initialStepTracksPreSplitting"+str(layers),process.initialStepTracksPreSplitting.clone(
            AlgorithmName = cms.string('initialStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"+str(layers)),
            NavigationSchool = cms.string(''),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("initialStepTrackCandidatesPreSplitting"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"jetsForCoreTrackingPreSplitting"+str(layers),process.jetsForCoreTrackingPreSplitting.clone(
            cut = cms.string('pt > 100 && abs(eta) < 2.5'),
            filter = cms.bool(False),
            src = cms.InputTag("ak4CaloJetsForTrkPreSplitting"+str(layers))
        )
    )
    
    setattr(process,"mkFitEventOfHitsPreSplitting"+str(layers),process.mkFitEventOfHitsPreSplitting.clone(
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            mightGet = cms.untracked.vstring(
                'MkFitHitWrapper_mkFitSiPixelHitsPreSplitting'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHitsPreSplitting'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            pixelHits = cms.InputTag("mkFitSiPixelHitsPreSplitting"+str(layers)),
            stripHits = cms.InputTag("mkFitSiStripHits"+str(layers)),
            usePixelQualityDB = cms.bool(True),
            useStripStripQualityDB = cms.bool(True)
        )
    )
    
    setattr(process,"mkFitSiPixelHitsPreSplitting"+str(layers),process.mkFitSiPixelHitsPreSplitting.clone(
            hits = cms.InputTag("siPixelRecHitsPreSplitting"+str(layers)),
            mightGet = cms.optional.untracked.vstring,
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"mkFitSiStripHits"+str(layers),process.mkFitSiStripHits.clone(
            mightGet = cms.optional.untracked.vstring,
            minGoodStripCharge = cms.PSet(
                refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
            ),
            rphiHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHit"),
            stereoHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"stereoRecHit"),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"siPixelClusterShapeCache"+str(layers),process.siPixelClusterShapeCache.clone(
            mightGet = cms.optional.untracked.vstring,
            onDemand = cms.bool(False),
            src = cms.InputTag(myCollection)
        )
    )
    
    setattr(process,"siPixelClusters"+str(layers),process.siPixelClusters.clone(
            centralMIPCharge = cms.double(26000),
            chargeFractionMin = cms.double(2.0),
            chargePerUnit = cms.double(2000),
            cores = cms.InputTag("jetsForCoreTrackingPreSplitting"+str(layers)),
            deltaRmax = cms.double(0.05),
            forceXError = cms.double(100),
            forceYError = cms.double(150),
            fractionalWidth = cms.double(0.4),
            pixelCPE = cms.string('PixelCPEGeneric'),
            pixelClusters = cms.InputTag("siPixelClustersPreSplitting"+str(layers)),
            ptMin = cms.double(200),
            verbose = cms.bool(False),
            vertices = cms.InputTag("firstStepPrimaryVerticesPreSplitting"+str(layers))
        )
    )
    
    setattr(process,"siPixelRecHits"+str(layers),process.siPixelRecHits.clone(
            CPE = cms.string('PixelCPEGeneric'),
            VerboseLevel = cms.untracked.int32(0),
            src = cms.InputTag(myCollection)
        )
    )
    
    setattr(process,"trackerClusterCheckPreSplitting"+str(layers),process.trackerClusterCheckPreSplitting.clone(
            ClusterCollectionLabel = cms.InputTag(myCollection),
            MaxNumberOfCosmicClusters = cms.uint32(400000),
            MaxNumberOfPixelClusters = cms.uint32(40000),
            PixelClusterCollectionLabel = cms.InputTag("siPixelClustersPreSplitting"+str(layers)),
            cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
            doClusterCheck = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            silentClusterCheck = cms.untracked.bool(False)
        )
    )
    
    setattr(process,"duplicateTrackCandidates"+str(layers),process.duplicateTrackCandidates.clone(
            GBRForestFileName = cms.string(''),
            chi2EstimatorName = cms.string('duplicateTrackCandidatesChi2Est'),
            forestLabel = cms.string('MVADuplicate'),
            maxDCA = cms.double(30),
            maxDLambda = cms.double(0.3),
            maxDPhi = cms.double(0.3),
            maxDQoP = cms.double(0.25),
            maxDdsz = cms.double(10),
            maxDdxy = cms.double(10),
            mightGet = cms.optional.untracked.vstring,
            minBDTG = cms.double(-0.1),
            minDeltaR3d = cms.double(-4),
            minP = cms.double(0.4),
            minpT = cms.double(0.2),
            overlapCheckMaxHits = cms.uint32(4),
            overlapCheckMaxMissingLayers = cms.uint32(1),
            overlapCheckMinCosT = cms.double(0.99),
            propagatorName = cms.string('PropagatorWithMaterial'),
            source = cms.InputTag("preDuplicateMergingGeneralTracks"+str(layers)),
            ttrhBuilderName = cms.string('WithAngleAndTemplate'),
            useInnermostState = cms.bool(True)
        )
    )
    
    setattr(process,"duplicateTrackClassifier"+str(layers),process.duplicateTrackClassifier.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                dr_par = cms.PSet(
                    d0err = cms.vdouble(0.003, 0.003, 0.003),
                    d0err_par = cms.vdouble(0.001, 0.001, 0.001),
                    drWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
                    dr_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dr_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
                ),
                dz_par = cms.PSet(
                    dzWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
                    dz_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dz_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
                ),
                isHLT = cms.bool(False),
                maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
                maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
                maxDr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                maxDz = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                maxDzWrtBS = cms.vdouble(3.4028234663852886e+38, 24, 15),
                maxLostLayers = cms.vint32(99, 99, 99),
                maxRelPtErr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                min3DLayers = cms.vint32(0, 0, 0),
                minHits = cms.vint32(0, 0, 1),
                minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
                minLayers = cms.vint32(0, 0, 0),
                minNVtxTrk = cms.int32(2),
                minNdof = cms.vdouble(-1, -1, -1),
                minPixelHits = cms.vint32(0, 0, 0)
            ),
            qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
            src = cms.InputTag("mergedDuplicateTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"generalTracks"+str(layers),process.generalTracks.clone(
            candidateComponents = cms.InputTag("duplicateTrackCandidates"+str(layers),"candidateMap"),
            candidateSource = cms.InputTag("duplicateTrackCandidates"+str(layers),"candidates"),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            diffHitsCut = cms.int32(5),
            mergedMVAVals = cms.InputTag("duplicateTrackClassifier"+str(layers),"MVAValues"),
            mergedSource = cms.InputTag("mergedDuplicateTracks"+str(layers)),
            mightGet = cms.optional.untracked.vstring,
            originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks"+str(layers),"MVAValues"),
            originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"+str(layers)),
            trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder')
        )
    )
    
    setattr(process,"mergedDuplicateTracks"+str(layers),process.mergedDuplicateTracks.clone(
            AlgorithmName = cms.string('undefAlgorithm'),
            Fitter = cms.string('RKFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("duplicateTrackCandidates"+str(layers),"candidates"),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"earlyMuons"+str(layers),process.earlyMuons.clone(
            CaloExtractorPSet = cms.PSet(
                CenterConeOnCalIntersection = cms.bool(False),
                ComponentName = cms.string('CaloExtractorByAssociator'),
                DR_Max = cms.double(0.5),
                DR_Veto_E = cms.double(0.07),
                DR_Veto_H = cms.double(0.1),
                DR_Veto_HO = cms.double(0.1),
                DepositInstanceLabels = cms.vstring(
                    'ecal',
                    'hcal',
                    'ho'
                ),
                DepositLabel = cms.untracked.string('Cal'),
                NoiseTow_EB = cms.double(0.04),
                NoiseTow_EE = cms.double(0.15),
                Noise_EB = cms.double(0.025),
                Noise_EE = cms.double(0.1),
                Noise_HB = cms.double(0.2),
                Noise_HE = cms.double(0.2),
                Noise_HO = cms.double(0.2),
                PrintTimeReport = cms.untracked.bool(False),
                PropagatorName = cms.string('SteppingHelixPropagatorAny'),
                ServiceParameters = cms.PSet(
                    Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
                    RPCLayers = cms.bool(False),
                    UseMuonNavigation = cms.untracked.bool(False)
                ),
                Threshold_E = cms.double(0.2),
                Threshold_H = cms.double(0.5),
                Threshold_HO = cms.double(0.5),
                TrackAssociatorParameters = cms.PSet(
                    CSCSegmentCollectionLabel = cms.InputTag("cscSegments"+str(layers)),
                    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
                    DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"+str(layers)),
                    EBRecHitCollectionLabel = cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEB"),
                    EERecHitCollectionLabel = cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEE"),
                    GEMSegmentCollectionLabel = cms.InputTag("gemSegments"+str(layers)),
                    HBHERecHitCollectionLabel = cms.InputTag("hbhereco"+str(layers)),
                    HORecHitCollectionLabel = cms.InputTag("horeco"+str(layers)),
                    ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
                    accountForTrajectoryChangeCalo = cms.bool(False),
                    dREcal = cms.double(1.0),
                    dREcalPreselection = cms.double(1.0),
                    dRHcal = cms.double(1.0),
                    dRHcalPreselection = cms.double(1.0),
                    dRMuon = cms.double(9999.0),
                    dRMuonPreselection = cms.double(0.2),
                    dRPreshowerPreselection = cms.double(0.2),
                    muonMaxDistanceSigmaX = cms.double(0.0),
                    muonMaxDistanceSigmaY = cms.double(0.0),
                    muonMaxDistanceX = cms.double(5.0),
                    muonMaxDistanceY = cms.double(5.0),
                    propagateAllDirections = cms.bool(True),
                    trajectoryUncertaintyTolerance = cms.double(-1.0),
                    truthMatch = cms.bool(False),
                    useCalo = cms.bool(True),
                    useEcal = cms.bool(False),
                    useGEM = cms.bool(False),
                    useHO = cms.bool(False),
                    useHcal = cms.bool(False),
                    useME0 = cms.bool(False),
                    useMuon = cms.bool(False),
                    usePreshower = cms.bool(False)
                ),
                UseRecHitsFlag = cms.bool(False)
            ),
            JetExtractorPSet = cms.PSet(
                ComponentName = cms.string('JetExtractor'),
                DR_Max = cms.double(1.0),
                DR_Veto = cms.double(0.1),
                ExcludeMuonVeto = cms.bool(True),
                JetCollectionLabel = cms.InputTag("ak4CaloJets"),
                PrintTimeReport = cms.untracked.bool(False),
                PropagatorName = cms.string('SteppingHelixPropagatorAny'),
                ServiceParameters = cms.PSet(
                    Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
                    RPCLayers = cms.bool(False),
                    UseMuonNavigation = cms.untracked.bool(False)
                ),
                Threshold = cms.double(5.0),
                TrackAssociatorParameters = cms.PSet(
                    CSCSegmentCollectionLabel = cms.InputTag("cscSegments"+str(layers)),
                    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
                    DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"+str(layers)),
                    EBRecHitCollectionLabel = cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEB"),
                    EERecHitCollectionLabel = cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEE"),
                    GEMSegmentCollectionLabel = cms.InputTag("gemSegments"+str(layers)),
                    HBHERecHitCollectionLabel = cms.InputTag("hbhereco"+str(layers)),
                    HORecHitCollectionLabel = cms.InputTag("horeco"+str(layers)),
                    ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
                    accountForTrajectoryChangeCalo = cms.bool(False),
                    dREcal = cms.double(0.5),
                    dREcalPreselection = cms.double(0.5),
                    dRHcal = cms.double(0.5),
                    dRHcalPreselection = cms.double(0.5),
                    dRMuon = cms.double(9999.0),
                    dRMuonPreselection = cms.double(0.2),
                    dRPreshowerPreselection = cms.double(0.2),
                    muonMaxDistanceSigmaX = cms.double(0.0),
                    muonMaxDistanceSigmaY = cms.double(0.0),
                    muonMaxDistanceX = cms.double(5.0),
                    muonMaxDistanceY = cms.double(5.0),
                    propagateAllDirections = cms.bool(True),
                    trajectoryUncertaintyTolerance = cms.double(-1.0),
                    truthMatch = cms.bool(False),
                    useCalo = cms.bool(True),
                    useEcal = cms.bool(False),
                    useGEM = cms.bool(False),
                    useHO = cms.bool(False),
                    useHcal = cms.bool(False),
                    useME0 = cms.bool(False),
                    useMuon = cms.bool(False),
                    usePreshower = cms.bool(False)
                )
            ),
            MuonCaloCompatibility = cms.PSet(
                MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
                PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
                allSiPMHO = cms.bool(False),
                delta_eta = cms.double(0.02),
                delta_phi = cms.double(0.02)
            ),
            ShowerDigiFillerParameters = cms.PSet(
                cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
                digiMaxDistanceX = cms.double(25.0),
                dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
            ),
            TimingFillerParameters = cms.PSet(
                CSCTimingParameters = cms.PSet(
                    CSCStripError = cms.double(7.0),
                    CSCStripTimeOffset = cms.double(0.0),
                    CSCWireError = cms.double(8.6),
                    CSCWireTimeOffset = cms.double(0.0),
                    PruneCut = cms.double(9.0),
                    ServiceParameters = cms.PSet(
                        Propagators = cms.untracked.vstring(
                            'SteppingHelixPropagatorAny',
                            'PropagatorWithMaterial',
                            'PropagatorWithMaterialOpposite'
                        ),
                        RPCLayers = cms.bool(True)
                    ),
                    UseStripTime = cms.bool(True),
                    UseWireTime = cms.bool(True),
                    debug = cms.bool(False)
                ),
                DTTimingParameters = cms.PSet(
                    DTTimeOffset = cms.double(0.0),
                    DoWireCorr = cms.bool(True),
                    DropTheta = cms.bool(True),
                    HitError = cms.double(2.8),
                    HitsMin = cms.int32(3),
                    PruneCut = cms.double(5.0),
                    RequireBothProjections = cms.bool(False),
                    ServiceParameters = cms.PSet(
                        Propagators = cms.untracked.vstring(
                            'SteppingHelixPropagatorAny',
                            'PropagatorWithMaterial',
                            'PropagatorWithMaterialOpposite'
                        ),
                        RPCLayers = cms.bool(True)
                    ),
                    UseSegmentT0 = cms.bool(False),
                    debug = cms.bool(False)
                ),
                EcalEnergyCut = cms.double(0.4),
                ErrorEB = cms.double(2.085),
                ErrorEE = cms.double(6.95),
                MatchParameters = cms.PSet(
                    CSCsegments = cms.InputTag("cscSegments"+str(layers)),
                    DTradius = cms.double(0.01),
                    DTsegments = cms.InputTag("dt4DSegments"+str(layers)),
                    RPChits = cms.InputTag("rpcRecHits"+str(layers)),
                    TightMatchCSC = cms.bool(True),
                    TightMatchDT = cms.bool(False)
                ),
                UseCSC = cms.bool(True),
                UseDT = cms.bool(True),
                UseECAL = cms.bool(False)
            ),
            TrackAssociatorParameters = cms.PSet(
                CSCSegmentCollectionLabel = cms.InputTag("cscSegments"+str(layers)),
                CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
                DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"+str(layers)),
                EBRecHitCollectionLabel = cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEB"),
                EERecHitCollectionLabel = cms.InputTag("ecalRecHit"+str(layers),"EcalRecHitsEE"),
                GEMSegmentCollectionLabel = cms.InputTag("gemSegments"+str(layers)),
                HBHERecHitCollectionLabel = cms.InputTag("hbhereco"+str(layers)),
                HORecHitCollectionLabel = cms.InputTag("horeco"+str(layers)),
                ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
                accountForTrajectoryChangeCalo = cms.bool(False),
                dREcal = cms.double(9999.0),
                dREcalPreselection = cms.double(0.05),
                dRHcal = cms.double(9999.0),
                dRHcalPreselection = cms.double(0.2),
                dRMuon = cms.double(9999.0),
                dRMuonPreselection = cms.double(0.2),
                dRPreshowerPreselection = cms.double(0.2),
                muonMaxDistanceSigmaX = cms.double(0.0),
                muonMaxDistanceSigmaY = cms.double(0.0),
                muonMaxDistanceX = cms.double(5.0),
                muonMaxDistanceY = cms.double(5.0),
                propagateAllDirections = cms.bool(True),
                trajectoryUncertaintyTolerance = cms.double(-1.0),
                truthMatch = cms.bool(False),
                useCalo = cms.bool(False),
                useEcal = cms.bool(False),
                useGEM = cms.bool(True),
                useHO = cms.bool(False),
                useHcal = cms.bool(False),
                useME0 = cms.bool(False),
                useMuon = cms.bool(True),
                usePreshower = cms.bool(False)
            ),
            TrackExtractorPSet = cms.PSet(
                BeamSpotLabel = cms.InputTag("offlineBeamSpot"+str(layers)),
                BeamlineOption = cms.string('BeamSpotFromEvent'),
                Chi2Ndof_Max = cms.double(1e+64),
                Chi2Prob_Min = cms.double(-1.0),
                ComponentName = cms.string('TrackExtractor'),
                DR_Max = cms.double(0.5),
                DR_Veto = cms.double(0.01),
                DepositLabel = cms.untracked.string(''),
                Diff_r = cms.double(0.1),
                Diff_z = cms.double(0.2),
                NHits_Min = cms.uint32(0),
                Pt_Min = cms.double(-1.0),
                inputTrackCollection = cms.InputTag("generalTracks"+str(layers))
            ),
            TrackerKinkFinderParameters = cms.PSet(
                DoPredictionsOnly = cms.bool(False),
                Fitter = cms.string('KFFitterForRefitInsideOut'),
                MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
                MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
                Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
                RefitDirection = cms.string('alongMomentum'),
                RefitRPCHits = cms.bool(True),
                Smoother = cms.string('KFSmootherForRefitInsideOut'),
                TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
                diagonalOnly = cms.bool(False),
                usePosition = cms.bool(True)
            ),
            addExtraSoftMuons = cms.bool(False),
            arbitrateTrackerMuons = cms.bool(True),
            arbitrationCleanerOptions = cms.PSet(
                ClusterDPhi = cms.double(0.6),
                ClusterDTheta = cms.double(0.02),
                Clustering = cms.bool(True),
                ME1a = cms.bool(True),
                Overlap = cms.bool(True),
                OverlapDPhi = cms.double(0.0786),
                OverlapDTheta = cms.double(0.02)
            ),
            debugWithTruthMatching = cms.bool(False),
            ecalDepositName = cms.string('ecal'),
            fillCaloCompatibility = cms.bool(False),
            fillEnergy = cms.bool(False),
            fillGlobalTrackQuality = cms.bool(False),
            fillGlobalTrackRefits = cms.bool(False),
            fillIsolation = cms.bool(False),
            fillMatching = cms.bool(True),
            fillShowerDigis = cms.bool(True),
            fillTrackerKink = cms.bool(False),
            globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
            hcalDepositName = cms.string('hcal'),
            hoDepositName = cms.string('ho'),
            inputCollectionLabels = cms.VInputTag("earlyGeneralTracks"+str(layers), "standAloneMuons"+str(layers)+":UpdatedAtVtx"),
            inputCollectionTypes = cms.vstring(
                'inner tracks',
                'outer tracks'
            ),
            jetDepositName = cms.string('jets'),
            maxAbsDx = cms.double(3.0),
            maxAbsDy = cms.double(9999.0),
            maxAbsEta = cms.double(3.0),
            maxAbsPullX = cms.double(3.0),
            maxAbsPullY = cms.double(9999.0),
            minCaloCompatibility = cms.double(0.6),
            minNumberOfMatches = cms.int32(1),
            minP = cms.double(3.0),
            minPCaloMuon = cms.double(3.0),
            minPt = cms.double(2.0),
            ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
            pvInputTag = cms.InputTag("offlinePrimaryVertices"+str(layers)),
            runArbitrationCleaner = cms.bool(True),
            selectHighPurity = cms.bool(False),
            sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
            storeCrossedHcalRecHits = cms.bool(True),
            trackDepositName = cms.string('tracker'),
            writeIsoDeposits = cms.bool(True)
        )
    )
    
    setattr(process,"detachedQuadStep"+str(layers),process.detachedQuadStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.63, -0.14, 0.49),
            src = cms.InputTag("detachedQuadStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"detachedQuadStepClusters"+str(layers),process.detachedQuadStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("lowPtTripletStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("lowPtTripletStepTracks"+str(layers))
        )
    )
    
    setattr(process,"detachedQuadStepHitDoublets"+str(layers),process.detachedQuadStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0, 1, 2),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("detachedQuadStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"detachedQuadStepHitQuadruplets"+str(layers),process.detachedQuadStepHitQuadruplets.clone(
            CAHardPtCut = cms.double(0),
            CAOnlyOneLastHitPerLayerFilter = cms.optional.bool,
            CAPhiCut = cms.double(0),
            CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            CAThetaCut = cms.double(0.0011),
            CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            doublets = cms.InputTag("detachedQuadStepHitDoublets"+str(layers)),
            extraHitRPhitolerance = cms.double(0),
            fitFastCircle = cms.bool(True),
            fitFastCircleChi2Cut = cms.bool(True),
            maxChi2 = cms.PSet(
                enabled = cms.bool(True),
                pt1 = cms.double(0.8),
                pt2 = cms.double(2),
                value1 = cms.double(500),
                value2 = cms.double(100)
            ),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedQuadStepHitDoublets'+str(layers)+'__reRECO'),
            useBendingCorrection = cms.bool(True)
        )
    )
    
    setattr(process,"detachedQuadStepSeedLayers"+str(layers),process.detachedQuadStepSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("detachedQuadStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("detachedQuadStepClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2+BPix3+BPix4',
                'BPix1+BPix2+BPix3+FPix1_pos',
                'BPix1+BPix2+BPix3+FPix1_neg',
                'BPix1+BPix2+FPix1_pos+FPix2_pos',
                'BPix1+BPix2+FPix1_neg+FPix2_neg',
                'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
                'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"detachedQuadStepSeeds"+str(layers),process.detachedQuadStepSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(False),
                FilterPixelHits = cms.bool(True),
                FilterStripHits = cms.bool(False)
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedQuadStepHitQuadruplets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets"+str(layers))
        )
    )
    
    setattr(process,"detachedQuadStepTrackCandidates"+str(layers),process.detachedQuadStepTrackCandidates.clone(
            mightGet = cms.untracked.vstring(
                'MkFitOutputWrapper_detachedQuadStepTrackCandidatesMkFit'+str(layers)+'__reRECO',
                'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            mkFitSeeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+str(layers)),
            mkFitStripHits = cms.InputTag("mkFitSiStripHits"+str(layers)),
            propagatorAlong = cms.ESInputTag("","PropagatorWithMaterial"),
            propagatorOpposite = cms.ESInputTag("","PropagatorWithMaterialOpposite"),
            seeds = cms.InputTag("detachedQuadStepSeeds"+str(layers)),
            tracks = cms.InputTag("detachedQuadStepTrackCandidatesMkFit"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"detachedQuadStepTrackCandidatesMkFit"+str(layers),process.detachedQuadStepTrackCandidatesMkFit.clone(
            backwardFitInCMSSW = cms.bool(False),
            buildingRoutine = cms.string('cloneEngine'),
            clustersToSkip = cms.InputTag("detachedQuadStepClusters"+str(layers)),
            config = cms.ESInputTag("","detachedQuadStepTrackCandidatesMkFitConfig"+str(layers)),
            eventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            limitConcurrency = cms.untracked.bool(False),
            mightGet = cms.untracked.vstring(
                'MkFitSeedWrapper_detachedQuadStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            minGoodStripCharge = cms.PSet(
                refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
            ),
            mkFitSilent = cms.untracked.bool(True),
            pixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            removeDuplicates = cms.bool(True),
            seedCleaning = cms.bool(True),
            seeds = cms.InputTag("detachedQuadStepTrackCandidatesMkFitSeeds"+str(layers)),
            stripHits = cms.InputTag("mkFitSiStripHits"+str(layers))
        )
    )
    
    setattr(process,"detachedQuadStepTrackCandidatesMkFitConfig"+str(layers),process.detachedQuadStepTrackCandidatesMkFitConfig.clone(
            ComponentName = cms.string('detachedQuadStepTrackCandidatesMkFitConfig'+str(layers)),
            appendToDataLabel = cms.string(''),
            config = cms.FileInPath('RecoTracker/MkFit/data/mkfit-phase1-detachedQuadStep.json')
        )
    )
    
    setattr(process,"detachedQuadStepTrackCandidatesMkFitSeeds"+str(layers),process.detachedQuadStepTrackCandidatesMkFitSeeds.clone(
            mightGet = cms.optional.untracked.vstring,
            seeds = cms.InputTag("detachedQuadStepSeeds"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"detachedQuadStepTrackingRegions"+str(layers),process.detachedQuadStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(0),
                originHalfLength = cms.double(15.0),
                originRadius = cms.double(1.5),
                precise = cms.bool(True),
                ptMin = cms.double(0.3),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"detachedQuadStepTracks"+str(layers),process.detachedQuadStepTracks.clone(
            AlgorithmName = cms.string('detachedQuadStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("detachedQuadStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"detachedTripletStep"+str(layers),process.detachedTripletStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.32, 0.24, 0.81),
            src = cms.InputTag("detachedTripletStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"detachedTripletStepClassifier1"+str(layers),process.detachedTripletStepClassifier1.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter3_13TeV')
            ),
            qualityCuts = cms.vdouble(-0.5, 0.0, 0.5),
            src = cms.InputTag("detachedTripletStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"detachedTripletStepClassifier2"+str(layers),process.detachedTripletStepClassifier2.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
            ),
            qualityCuts = cms.vdouble(-0.2, 0.0, 0.4),
            src = cms.InputTag("detachedTripletStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"detachedTripletStepClusters"+str(layers),process.detachedTripletStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("detachedQuadStepClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("detachedQuadStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("detachedQuadStepTracks"+str(layers))
        )
    )
    
    setattr(process,"detachedTripletStepHitDoublets"+str(layers),process.detachedTripletStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0, 1),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"detachedTripletStepHitTriplets"+str(layers),process.detachedTripletStepHitTriplets.clone(
            CAHardPtCut = cms.double(0.2),
            CAPhiCut = cms.double(0),
            CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            CAThetaCut = cms.double(0.001),
            CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            doublets = cms.InputTag("detachedTripletStepHitDoublets"+str(layers)),
            extraHitRPhitolerance = cms.double(0),
            maxChi2 = cms.PSet(
                enabled = cms.bool(True),
                pt1 = cms.double(0.8),
                pt2 = cms.double(2),
                value1 = cms.double(300),
                value2 = cms.double(10)
            ),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_detachedTripletStepHitDoublets'+str(layers)+'__reRECO'),
            useBendingCorrection = cms.bool(True)
        )
    )
    
    setattr(process,"detachedTripletStepSeedLayers"+str(layers),process.detachedTripletStepSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("detachedTripletStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("detachedTripletStepClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2+BPix3',
                'BPix2+BPix3+BPix4',
                'BPix2+BPix3+FPix1_pos',
                'BPix2+BPix3+FPix1_neg',
                'BPix2+FPix1_pos+FPix2_pos',
                'BPix2+FPix1_neg+FPix2_neg',
                'FPix1_pos+FPix2_pos+FPix3_pos',
                'FPix1_neg+FPix2_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"detachedTripletStepSeeds"+str(layers),process.detachedTripletStepSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(False),
                FilterPixelHits = cms.bool(True),
                FilterStripHits = cms.bool(False)
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_detachedTripletStepHitTriplets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets"+str(layers))
        )
    )
    
    setattr(process,"detachedTripletStepTrackCandidates"+str(layers),process.detachedTripletStepTrackCandidates.clone(
            mightGet = cms.untracked.vstring(
                'MkFitOutputWrapper_detachedTripletStepTrackCandidatesMkFit'+str(layers)+'__reRECO',
                'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            mkFitSeeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+str(layers)),
            mkFitStripHits = cms.InputTag("mkFitSiStripHits"+str(layers)),
            propagatorAlong = cms.ESInputTag("","PropagatorWithMaterial"),
            propagatorOpposite = cms.ESInputTag("","PropagatorWithMaterialOpposite"),
            seeds = cms.InputTag("detachedTripletStepSeeds"+str(layers)),
            tracks = cms.InputTag("detachedTripletStepTrackCandidatesMkFit"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"detachedTripletStepTrackCandidatesMkFit"+str(layers),process.detachedTripletStepTrackCandidatesMkFit.clone(
            backwardFitInCMSSW = cms.bool(False),
            buildingRoutine = cms.string('cloneEngine'),
            clustersToSkip = cms.InputTag("detachedTripletStepClusters"+str(layers)),
            config = cms.ESInputTag("","detachedTripletStepTrackCandidatesMkFitConfig"+str(layers)),
            eventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            limitConcurrency = cms.untracked.bool(False),
            mightGet = cms.untracked.vstring(
                'MkFitSeedWrapper_detachedTripletStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            minGoodStripCharge = cms.PSet(
                refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
            ),
            mkFitSilent = cms.untracked.bool(True),
            pixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            removeDuplicates = cms.bool(True),
            seedCleaning = cms.bool(True),
            seeds = cms.InputTag("detachedTripletStepTrackCandidatesMkFitSeeds"+str(layers)),
            stripHits = cms.InputTag("mkFitSiStripHits"+str(layers))
        )
    )
    
    setattr(process,"detachedTripletStepTrackCandidatesMkFitConfig"+str(layers),process.detachedTripletStepTrackCandidatesMkFitConfig.clone(
            ComponentName = cms.string('detachedTripletStepTrackCandidatesMkFitConfig'+str(layers)),
            appendToDataLabel = cms.string(''),
            config = cms.FileInPath('RecoTracker/MkFit/data/mkfit-phase1-detachedTripletStep.json')
        )
    )
    
    setattr(process,"detachedTripletStepTrackCandidatesMkFitSeeds"+str(layers),process.detachedTripletStepTrackCandidatesMkFitSeeds.clone(
            mightGet = cms.optional.untracked.vstring,
            seeds = cms.InputTag("detachedTripletStepSeeds"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"detachedTripletStepTrackingRegions"+str(layers),process.detachedTripletStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(0),
                originHalfLength = cms.double(15.0),
                originRadius = cms.double(1.5),
                precise = cms.bool(True),
                ptMin = cms.double(0.25),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"detachedTripletStepTracks"+str(layers),process.detachedTripletStepTracks.clone(
            AlgorithmName = cms.string('detachedTripletStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("detachedTripletStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"highPtTripletStep"+str(layers),process.highPtTripletStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(0.41, 0.49, 0.57),
            src = cms.InputTag("highPtTripletStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"highPtTripletStepClusters"+str(layers),process.highPtTripletStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("lowPtQuadStepClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("lowPtQuadStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("lowPtQuadStepTracks"+str(layers))
        )
    )
    
    setattr(process,"highPtTripletStepHitDoublets"+str(layers),process.highPtTripletStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0, 1),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"highPtTripletStepHitTriplets"+str(layers),process.highPtTripletStepHitTriplets.clone(
            CAHardPtCut = cms.double(0.3),
            CAPhiCut = cms.double(0.07),
            CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            CAThetaCut = cms.double(0.004),
            CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
                clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
            ),
            doublets = cms.InputTag("highPtTripletStepHitDoublets"+str(layers)),
            extraHitRPhitolerance = cms.double(0.032),
            maxChi2 = cms.PSet(
                enabled = cms.bool(True),
                pt1 = cms.double(0.8),
                pt2 = cms.double(8),
                value1 = cms.double(100),
                value2 = cms.double(6)
            ),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets'+str(layers)+'__reRECO'),
            useBendingCorrection = cms.bool(True)
        )
    )
    
    setattr(process,"highPtTripletStepSeedLayers"+str(layers),process.highPtTripletStepSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("highPtTripletStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("highPtTripletStepClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2+BPix3',
                'BPix2+BPix3+BPix4',
                'BPix1+BPix3+BPix4',
                'BPix1+BPix2+BPix4',
                'BPix2+BPix3+FPix1_pos',
                'BPix2+BPix3+FPix1_neg',
                'BPix1+BPix2+FPix1_pos',
                'BPix1+BPix2+FPix1_neg',
                'BPix1+BPix3+FPix1_pos',
                'BPix1+BPix3+FPix1_neg',
                'BPix2+FPix1_pos+FPix2_pos',
                'BPix2+FPix1_neg+FPix2_neg',
                'BPix1+FPix1_pos+FPix2_pos',
                'BPix1+FPix1_neg+FPix2_neg',
                'BPix1+BPix2+FPix2_pos',
                'BPix1+BPix2+FPix2_neg',
                'FPix1_pos+FPix2_pos+FPix3_pos',
                'FPix1_neg+FPix2_neg+FPix3_neg',
                'BPix1+FPix2_pos+FPix3_pos',
                'BPix1+FPix2_neg+FPix3_neg',
                'BPix1+FPix1_pos+FPix3_pos',
                'BPix1+FPix1_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"highPtTripletStepSeeds"+str(layers),process.highPtTripletStepSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets"+str(layers))
        )
    )
    
    setattr(process,"highPtTripletStepTrackCandidates"+str(layers),process.highPtTripletStepTrackCandidates.clone(
            mightGet = cms.untracked.vstring(
                'MkFitOutputWrapper_highPtTripletStepTrackCandidatesMkFit'+str(layers)+'__reRECO',
                'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            mkFitSeeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+str(layers)),
            mkFitStripHits = cms.InputTag("mkFitSiStripHits"+str(layers)),
            propagatorAlong = cms.ESInputTag("","PropagatorWithMaterial"),
            propagatorOpposite = cms.ESInputTag("","PropagatorWithMaterialOpposite"),
            seeds = cms.InputTag("highPtTripletStepSeeds"+str(layers)),
            tracks = cms.InputTag("highPtTripletStepTrackCandidatesMkFit"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle"),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"highPtTripletStepTrackCandidatesMkFit"+str(layers),process.highPtTripletStepTrackCandidatesMkFit.clone(
            backwardFitInCMSSW = cms.bool(False),
            buildingRoutine = cms.string('cloneEngine'),
            clustersToSkip = cms.InputTag("highPtTripletStepClusters"+str(layers)),
            config = cms.ESInputTag("","highPtTripletStepTrackCandidatesMkFitConfig"+str(layers)),
            eventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            limitConcurrency = cms.untracked.bool(False),
            mightGet = cms.untracked.vstring(
                'MkFitSeedWrapper_highPtTripletStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            minGoodStripCharge = cms.PSet(
                refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
            ),
            mkFitSilent = cms.untracked.bool(True),
            pixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            removeDuplicates = cms.bool(True),
            seedCleaning = cms.bool(True),
            seeds = cms.InputTag("highPtTripletStepTrackCandidatesMkFitSeeds"+str(layers)),
            stripHits = cms.InputTag("mkFitSiStripHits"+str(layers))
        )
    )
    
    setattr(process,"highPtTripletStepTrackCandidatesMkFitConfig"+str(layers),process.highPtTripletStepTrackCandidatesMkFitConfig.clone(
            ComponentName = cms.string('highPtTripletStepTrackCandidatesMkFitConfig'+str(layers)),
            appendToDataLabel = cms.string(''),
            config = cms.FileInPath('RecoTracker/MkFit/data/mkfit-phase1-highPtTripletStep.json')
        )
    )
    
    setattr(process,"highPtTripletStepTrackCandidatesMkFitSeeds"+str(layers),process.highPtTripletStepTrackCandidatesMkFitSeeds.clone(
            mightGet = cms.optional.untracked.vstring,
            seeds = cms.InputTag("highPtTripletStepSeeds"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"highPtTripletStepTrackingRegions"+str(layers),process.highPtTripletStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(4),
                originHalfLength = cms.double(0),
                originRadius = cms.double(0.02),
                precise = cms.bool(True),
                ptMin = cms.double(0.55),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"highPtTripletStepTracks"+str(layers),process.highPtTripletStepTracks.clone(
            AlgorithmName = cms.string('highPtTripletStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("highPtTripletStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"firstStepPrimaryVertices"+str(layers),process.firstStepPrimaryVertices.clone(
            assignment = cms.PSet(
                DzCutForChargedFromPUVtxs = cms.double(0.2),
                EtaMinUseDz = cms.double(-1),
                NumOfPUVtxsForCharged = cms.uint32(0),
                OnlyUseFirstDz = cms.bool(False),
                PtMaxCharged = cms.double(-1),
                maxDistanceToJetAxis = cms.double(0.07),
                maxDtSigForPrimaryAssignment = cms.double(3),
                maxDxyForJetAxisAssigment = cms.double(0.1),
                maxDxyForNotReconstructedPrimary = cms.double(0.01),
                maxDxySigForNotReconstructedPrimary = cms.double(2),
                maxDzErrorForPrimaryAssignment = cms.double(0.05),
                maxDzForJetAxisAssigment = cms.double(0.1),
                maxDzForPrimaryAssignment = cms.double(0.1),
                maxDzSigForPrimaryAssignment = cms.double(5),
                maxJetDeltaR = cms.double(0.5),
                minJetPt = cms.double(25),
                preferHighRanked = cms.bool(False),
                useTiming = cms.bool(False),
                useVertexFit = cms.bool(True)
            ),
            jets = cms.InputTag("ak4CaloJetsForTrk"+str(layers)),
            mightGet = cms.optional.untracked.vstring,
            particles = cms.InputTag("initialStepTrackRefsForJets"+str(layers)),
            produceAssociationToOriginalVertices = cms.bool(False),
            produceNoPileUpCollection = cms.bool(False),
            producePileUpCollection = cms.bool(False),
            produceSortedVertices = cms.bool(True),
            qualityForPrimary = cms.int32(3),
            sorting = cms.PSet(
        
            ),
            trackTimeResoTag = cms.InputTag(""),
            trackTimeTag = cms.InputTag(""),
            usePVMET = cms.bool(True),
            vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted"+str(layers))
        )
    )
    
    setattr(process,"firstStepPrimaryVerticesUnsorted"+str(layers),process.firstStepPrimaryVerticesUnsorted.clone(
            TkClusParameters = cms.PSet(
                TkDAClusParameters = cms.PSet(
                    Tmin = cms.double(2.0),
                    Tpurge = cms.double(2.0),
                    Tstop = cms.double(0.5),
                    convergence_mode = cms.int32(0),
                    coolingFactor = cms.double(0.6),
                    d0CutOff = cms.double(3.0),
                    delta_highT = cms.double(0.01),
                    delta_lowT = cms.double(0.001),
                    dzCutOff = cms.double(3.0),
                    uniquetrkminp = cms.double(0.0),
                    uniquetrkweight = cms.double(0.8),
                    vertexSize = cms.double(0.006),
                    zmerge = cms.double(0.01),
                    zrange = cms.double(4.0)
                ),
                algorithm = cms.string('DA_vect')
            ),
            TkFilterParameters = cms.PSet(
                algorithm = cms.string('filter'),
                maxD0Error = cms.double(1.0),
                maxD0Significance = cms.double(4.0),
                maxDzError = cms.double(1.0),
                maxEta = cms.double(2.4),
                maxNormalizedChi2 = cms.double(10.0),
                minPixelLayersWithHits = cms.int32(2),
                minPt = cms.double(0.0),
                minSiliconLayersWithHits = cms.int32(5),
                trackQuality = cms.string('any')
            ),
            TrackLabel = cms.InputTag("initialStepTracks"+str(layers)),
            beamSpotLabel = cms.InputTag("offlineBeamSpot"+str(layers)),
            isRecoveryIteration = cms.bool(False),
            recoveryVtxCollection = cms.InputTag(""),
            verbose = cms.untracked.bool(False),
            vertexCollections = cms.VPSet(cms.PSet(
                algorithm = cms.string('AdaptiveVertexFitter'),
                chi2cutoff = cms.double(2.5),
                label = cms.string(''),
                maxDistanceToBeam = cms.double(1.0),
                minNdof = cms.double(0.0),
                useBeamConstraint = cms.bool(False)
            ))
        )
    )
    
    setattr(process,"initialStep"+str(layers),process.initialStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.56, -0.08, 0.17),
            src = cms.InputTag("initialStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"initialStepClassifier1"+str(layers),process.initialStepClassifier1.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
            ),
            qualityCuts = cms.vdouble(-0.9, -0.8, -0.7),
            src = cms.InputTag("initialStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"initialStepHitDoublets"+str(layers),process.initialStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0, 1, 2),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("initialStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("initialStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"initialStepHitQuadruplets"+str(layers),process.initialStepHitQuadruplets.clone(
            CAHardPtCut = cms.double(0),
            CAOnlyOneLastHitPerLayerFilter = cms.optional.bool,
            CAPhiCut = cms.double(0.2),
            CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            CAThetaCut = cms.double(0.0012),
            CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
                clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
            ),
            doublets = cms.InputTag("initialStepHitDoublets"+str(layers)),
            extraHitRPhitolerance = cms.double(0.032),
            fitFastCircle = cms.bool(True),
            fitFastCircleChi2Cut = cms.bool(True),
            maxChi2 = cms.PSet(
                enabled = cms.bool(True),
                pt1 = cms.double(0.7),
                pt2 = cms.double(2),
                value1 = cms.double(200),
                value2 = cms.double(50)
            ),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets'+str(layers)+'__reRECO'),
            useBendingCorrection = cms.bool(True)
        )
    )
    
    setattr(process,"initialStepSeedLayers"+str(layers),process.initialStepSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2+BPix3+BPix4',
                'BPix1+BPix2+BPix3+FPix1_pos',
                'BPix1+BPix2+BPix3+FPix1_neg',
                'BPix1+BPix2+FPix1_pos+FPix2_pos',
                'BPix1+BPix2+FPix1_neg+FPix2_neg',
                'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
                'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"initialStepSeeds"+str(layers),process.initialStepSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(False),
                FilterPixelHits = cms.bool(True),
                FilterStripHits = cms.bool(False)
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("initialStepHitQuadruplets"+str(layers))
        )
    )
    
    setattr(process,"initialStepTrackCandidates"+str(layers),process.initialStepTrackCandidates.clone(
            mightGet = cms.untracked.vstring(
                'MkFitOutputWrapper_initialStepTrackCandidatesMkFit'+str(layers)+'__reRECO',
                'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            mkFitSeeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+str(layers)),
            mkFitStripHits = cms.InputTag("mkFitSiStripHits"+str(layers)),
            propagatorAlong = cms.ESInputTag("","PropagatorWithMaterial"),
            propagatorOpposite = cms.ESInputTag("","PropagatorWithMaterialOpposite"),
            seeds = cms.InputTag("initialStepSeeds"+str(layers)),
            tracks = cms.InputTag("initialStepTrackCandidatesMkFit"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"initialStepTrackCandidatesMkFit"+str(layers),process.initialStepTrackCandidatesMkFit.clone(
            backwardFitInCMSSW = cms.bool(False),
            buildingRoutine = cms.string('cloneEngine'),
            clustersToSkip = cms.InputTag(""),
            config = cms.ESInputTag("","initialStepTrackCandidatesMkFitConfig"+str(layers)),
            eventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            limitConcurrency = cms.untracked.bool(False),
            mightGet = cms.untracked.vstring(
                'MkFitSeedWrapper_initialStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO',
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            minGoodStripCharge = cms.PSet(
                refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
            ),
            mkFitSilent = cms.untracked.bool(True),
            pixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            removeDuplicates = cms.bool(True),
            seedCleaning = cms.bool(True),
            seeds = cms.InputTag("initialStepTrackCandidatesMkFitSeeds"+str(layers)),
            stripHits = cms.InputTag("mkFitSiStripHits"+str(layers))
        )
    )
    
    setattr(process,"initialStepTrackCandidatesMkFitConfig"+str(layers),process.initialStepTrackCandidatesMkFitConfig.clone(
            ComponentName = cms.string('initialStepTrackCandidatesMkFitConfig'+str(layers)),
            appendToDataLabel = cms.string(''),
            config = cms.FileInPath('RecoTracker/MkFit/data/mkfit-phase1-initialStep.json')
        )
    )
    
    setattr(process,"initialStepTrackCandidatesMkFitSeeds"+str(layers),process.initialStepTrackCandidatesMkFitSeeds.clone(
            mightGet = cms.optional.untracked.vstring,
            seeds = cms.InputTag("initialStepSeeds"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"initialStepTrackRefsForJets"+str(layers),process.initialStepTrackRefsForJets.clone(
            particleType = cms.string('pi+'),
            src = cms.InputTag("initialStepTracks"+str(layers))
        )
    )
    
    setattr(process,"initialStepTrackingRegions"+str(layers),process.initialStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(4),
                originHalfLength = cms.double(0),
                originRadius = cms.double(0.02),
                precise = cms.bool(True),
                ptMin = cms.double(0.5),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"initialStepTracks"+str(layers),process.initialStepTracks.clone(
            AlgorithmName = cms.string('initialStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("initialStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"mkFitEventOfHits"+str(layers),process.mkFitEventOfHits.clone(
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            mightGet = cms.untracked.vstring(
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO'
            ),
            pixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            stripHits = cms.InputTag("mkFitSiStripHits"+str(layers)),
            usePixelQualityDB = cms.bool(True),
            useStripStripQualityDB = cms.bool(True)
        )
    )
    
    setattr(process,"mkFitSiPixelHits"+str(layers),process.mkFitSiPixelHits.clone(
            hits = cms.InputTag("siPixelRecHits"+str(layers)),
            mightGet = cms.optional.untracked.vstring,
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"firstStepGoodPrimaryVertices"+str(layers),process.firstStepGoodPrimaryVertices.clone(
            filterParams = cms.PSet(
                maxRho = cms.double(2.0),
                maxZ = cms.double(15.0),
                minNdof = cms.double(25.0)
            ),
            src = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"jetCoreRegionalStep"+str(layers),process.jetCoreRegionalStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.53, -0.33, 0.18),
            src = cms.InputTag("jetCoreRegionalStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"jetCoreRegionalStepHitDoublets"+str(layers),process.jetCoreRegionalStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(1000000),
            maxElementTotal = cms.uint32(12000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"jetCoreRegionalStepSeedLayers"+str(layers),process.jetCoreRegionalStepSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                hitErrorRPhi = cms.double(0.0027),
                hitErrorRZ = cms.double(0.006),
                useErrorsFromParam = cms.bool(True)
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                hitErrorRPhi = cms.double(0.0051),
                hitErrorRZ = cms.double(0.0036),
                useErrorsFromParam = cms.bool(True)
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutNone')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit")
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2',
                'BPix1+BPix3',
                'BPix1+BPix4',
                'BPix2+BPix3',
                'BPix2+BPix4',
                'BPix3+BPix4',
                'BPix1+FPix1_pos',
                'BPix1+FPix1_neg',
                'BPix2+FPix1_pos',
                'BPix2+FPix1_neg',
                'FPix1_pos+FPix2_pos',
                'FPix1_neg+FPix2_neg',
                'FPix1_pos+FPix3_pos',
                'FPix1_neg+FPix3_neg',
                'FPix2_pos+FPix3_pos',
                'FPix2_neg+FPix3_neg',
                'BPix4+TIB1',
                'BPix4+TIB2'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"jetCoreRegionalStepSeeds"+str(layers),process.jetCoreRegionalStepSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(True),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_jetCoreRegionalStepHitDoublets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets"+str(layers))
        )
    )
    
    setattr(process,"jetCoreRegionalStepTrackCandidates"+str(layers),process.jetCoreRegionalStepTrackCandidates.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('jetCoreRegionalStepTrajectoryBuilder')
            ),
            TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag(""),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(10000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(4),
            onlyPixelHitsForSeedCleaner = cms.bool(False),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("jetCoreRegionalStepSeeds"+str(layers)),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"jetCoreRegionalStepTrackingRegions"+str(layers),process.jetCoreRegionalStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                JetSrc = cms.InputTag("jetsForCoreTracking"+str(layers)),
                deltaEtaRegion = cms.double(0.2),
                deltaPhiRegion = cms.double(0.2),
                howToUseMeasurementTracker = cms.string('Never'),
                measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
                originHalfLength = cms.double(0.2),
                originRadius = cms.double(0.2),
                ptMin = cms.double(10),
                searchOpt = cms.bool(False),
                vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices"+str(layers))
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"jetCoreRegionalStepTracks"+str(layers),process.jetCoreRegionalStepTracks.clone(
            AlgorithmName = cms.string('jetCoreRegionalStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("jetCoreRegionalStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"jetsForCoreTracking"+str(layers),process.jetsForCoreTracking.clone(
            cut = cms.string('pt > 100 && abs(eta) < 2.5'),
            filter = cms.bool(False),
            src = cms.InputTag("ak4CaloJetsForTrk"+str(layers))
        )
    )
    
    setattr(process,"lowPtQuadStep"+str(layers),process.lowPtQuadStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.35, 0.13, 0.36),
            src = cms.InputTag("lowPtQuadStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"lowPtQuadStepClusters"+str(layers),process.lowPtQuadStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag(""),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("initialStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("initialStepTracks"+str(layers))
        )
    )
    
    setattr(process,"lowPtQuadStepHitDoublets"+str(layers),process.lowPtQuadStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0, 1, 2),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"lowPtQuadStepHitQuadruplets"+str(layers),process.lowPtQuadStepHitQuadruplets.clone(
            CAHardPtCut = cms.double(0),
            CAOnlyOneLastHitPerLayerFilter = cms.optional.bool,
            CAPhiCut = cms.double(0.3),
            CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            CAThetaCut = cms.double(0.0017),
            CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
                clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
            ),
            doublets = cms.InputTag("lowPtQuadStepHitDoublets"+str(layers)),
            extraHitRPhitolerance = cms.double(0.032),
            fitFastCircle = cms.bool(True),
            fitFastCircleChi2Cut = cms.bool(True),
            maxChi2 = cms.PSet(
                enabled = cms.bool(True),
                pt1 = cms.double(0.7),
                pt2 = cms.double(2),
                value1 = cms.double(1000),
                value2 = cms.double(150)
            ),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtQuadStepHitDoublets'+str(layers)+'__reRECO'),
            useBendingCorrection = cms.bool(True)
        )
    )
    
    setattr(process,"lowPtQuadStepSeedLayers"+str(layers),process.lowPtQuadStepSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("lowPtQuadStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("lowPtQuadStepClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2+BPix3+BPix4',
                'BPix1+BPix2+BPix3+FPix1_pos',
                'BPix1+BPix2+BPix3+FPix1_neg',
                'BPix1+BPix2+FPix1_pos+FPix2_pos',
                'BPix1+BPix2+FPix1_neg+FPix2_neg',
                'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
                'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"lowPtQuadStepSeeds"+str(layers),process.lowPtQuadStepSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtQuadStepHitQuadruplets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets"+str(layers))
        )
    )
    
    setattr(process,"lowPtQuadStepTrackCandidates"+str(layers),process.lowPtQuadStepTrackCandidates.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('lowPtQuadStepTrajectoryBuilder')
            ),
            TrajectoryCleaner = cms.string('lowPtQuadStepTrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag("lowPtQuadStepClusters"+str(layers)),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(5000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(50),
            onlyPixelHitsForSeedCleaner = cms.bool(True),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("lowPtQuadStepSeeds"+str(layers)),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"lowPtQuadStepTrackingRegions"+str(layers),process.lowPtQuadStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(4),
                originHalfLength = cms.double(0),
                originRadius = cms.double(0.02),
                precise = cms.bool(True),
                ptMin = cms.double(0.15),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"lowPtQuadStepTracks"+str(layers),process.lowPtQuadStepTracks.clone(
            AlgorithmName = cms.string('lowPtQuadStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("lowPtQuadStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"lowPtTripletStep"+str(layers),process.lowPtTripletStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.29, 0.09, 0.36),
            src = cms.InputTag("lowPtTripletStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"lowPtTripletStepClusters"+str(layers),process.lowPtTripletStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("highPtTripletStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("highPtTripletStepTracks"+str(layers))
        )
    )
    
    setattr(process,"lowPtTripletStepHitDoublets"+str(layers),process.lowPtTripletStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0, 1),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"lowPtTripletStepHitTriplets"+str(layers),process.lowPtTripletStepHitTriplets.clone(
            CAHardPtCut = cms.double(0),
            CAPhiCut = cms.double(0.05),
            CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            CAThetaCut = cms.double(0.002),
            CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
                cut = cms.double(-1),
                seedingLayers = cms.string('')
            )),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
                clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
            ),
            doublets = cms.InputTag("lowPtTripletStepHitDoublets"+str(layers)),
            extraHitRPhitolerance = cms.double(0.032),
            maxChi2 = cms.PSet(
                enabled = cms.bool(True),
                pt1 = cms.double(0.8),
                pt2 = cms.double(2),
                value1 = cms.double(70),
                value2 = cms.double(8)
            ),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_lowPtTripletStepHitDoublets'+str(layers)+'__reRECO'),
            useBendingCorrection = cms.bool(True)
        )
    )
    
    setattr(process,"lowPtTripletStepSeedLayers"+str(layers),process.lowPtTripletStepSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("lowPtTripletStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("lowPtTripletStepClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2+BPix3',
                'BPix2+BPix3+BPix4',
                'BPix1+BPix3+BPix4',
                'BPix1+BPix2+BPix4',
                'BPix2+BPix3+FPix1_pos',
                'BPix2+BPix3+FPix1_neg',
                'BPix1+BPix2+FPix1_pos',
                'BPix1+BPix2+FPix1_neg',
                'BPix1+BPix3+FPix1_pos',
                'BPix1+BPix3+FPix1_neg',
                'BPix2+FPix1_pos+FPix2_pos',
                'BPix2+FPix1_neg+FPix2_neg',
                'BPix1+FPix1_pos+FPix2_pos',
                'BPix1+FPix1_neg+FPix2_neg',
                'BPix1+BPix2+FPix2_pos',
                'BPix1+BPix2+FPix2_neg',
                'FPix1_pos+FPix2_pos+FPix3_pos',
                'FPix1_neg+FPix2_neg+FPix3_neg',
                'BPix1+FPix2_pos+FPix3_pos',
                'BPix1+FPix2_neg+FPix3_neg',
                'BPix1+FPix1_pos+FPix3_pos',
                'BPix1+FPix1_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"lowPtTripletStepSeeds"+str(layers),process.lowPtTripletStepSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_lowPtTripletStepHitTriplets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets"+str(layers))
        )
    )
    
    setattr(process,"lowPtTripletStepTrackCandidates"+str(layers),process.lowPtTripletStepTrackCandidates.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('lowPtTripletStepTrajectoryBuilder')
            ),
            TrajectoryCleaner = cms.string('lowPtTripletStepTrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag("lowPtTripletStepClusters"+str(layers)),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(5000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(50),
            onlyPixelHitsForSeedCleaner = cms.bool(True),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("lowPtTripletStepSeeds"+str(layers)),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"lowPtTripletStepTrackingRegions"+str(layers),process.lowPtTripletStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(4),
                originHalfLength = cms.double(0),
                originRadius = cms.double(0.02),
                precise = cms.bool(True),
                ptMin = cms.double(0.2),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"lowPtTripletStepTracks"+str(layers),process.lowPtTripletStepTracks.clone(
            AlgorithmName = cms.string('lowPtTripletStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("lowPtTripletStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"chargeCut2069Clusters"+str(layers),process.chargeCut2069Clusters.clone(
            clusterChargeCut = cms.PSet(
                refToPSet_ = cms.string('SiStripClusterChargeCutTight')
            ),
            oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection)
        )
    )
    
    setattr(process,"mixedTripletStep"+str(layers),process.mixedTripletStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.83, -0.63, -0.38),
            src = cms.InputTag("mixedTripletStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"mixedTripletStepClassifier1"+str(layers),process.mixedTripletStepClassifier1.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter4_13TeV')
            ),
            qualityCuts = cms.vdouble(-0.5, 0.0, 0.5),
            src = cms.InputTag("mixedTripletStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"mixedTripletStepClassifier2"+str(layers),process.mixedTripletStepClassifier2.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
            ),
            qualityCuts = cms.vdouble(-0.2, -0.2, -0.2),
            src = cms.InputTag("mixedTripletStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"mixedTripletStepClusters"+str(layers),process.mixedTripletStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("pixelPairStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("pixelPairStepTracks"+str(layers))
        )
    )
    
    setattr(process,"mixedTripletStepHitDoubletsA"+str(layers),process.mixedTripletStepHitDoubletsA.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"+str(layers)),
            trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"mixedTripletStepHitDoubletsB"+str(layers),process.mixedTripletStepHitDoubletsB.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"+str(layers)),
            trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"mixedTripletStepHitTripletsA"+str(layers),process.mixedTripletStepHitTripletsA.clone(
            doublets = cms.InputTag("mixedTripletStepHitDoubletsA"+str(layers)),
            extraHitRPhitolerance = cms.double(0),
            extraHitRZtolerance = cms.double(0),
            maxElement = cms.uint32(1000000),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+str(layers)+'__reRECO'),
            phiPreFiltering = cms.double(0.3),
            produceIntermediateHitTriplets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            useMultScattering = cms.bool(True)
        )
    )
    
    setattr(process,"mixedTripletStepHitTripletsB"+str(layers),process.mixedTripletStepHitTripletsB.clone(
            doublets = cms.InputTag("mixedTripletStepHitDoubletsB"+str(layers)),
            extraHitRPhitolerance = cms.double(0),
            extraHitRZtolerance = cms.double(0),
            maxElement = cms.uint32(1000000),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+str(layers)+'__reRECO'),
            phiPreFiltering = cms.double(0.3),
            produceIntermediateHitTriplets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            useMultScattering = cms.bool(True)
        )
    )
    
    setattr(process,"mixedTripletStepSeedLayersA"+str(layers),process.mixedTripletStepSeedLayersA.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("mixedTripletStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("mixedTripletStepClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                maxRing = cms.int32(1),
                minRing = cms.int32(1),
                skipClusters = cms.InputTag("mixedTripletStepClusters"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix2+FPix1_pos+FPix2_pos',
                'BPix2+FPix1_neg+FPix2_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"mixedTripletStepSeedLayersB"+str(layers),process.mixedTripletStepSeedLayersB.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("mixedTripletStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
        
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                skipClusters = cms.InputTag("mixedTripletStepClusters"+str(layers))
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring('BPix3+BPix4+TIB1'),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"mixedTripletStepSeeds"+str(layers),process.mixedTripletStepSeeds.clone(
            seedCollections = cms.VInputTag("mixedTripletStepSeedsA"+str(layers), "mixedTripletStepSeedsB"+str(layers))
        )
    )
    
    setattr(process,"mixedTripletStepSeedsA"+str(layers),process.mixedTripletStepSeedsA.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(False),
                FilterPixelHits = cms.bool(True),
                FilterStripHits = cms.bool(True)
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring(
                'RegionsSeedingHitSets_mixedTripletStepHitTripletsA'+str(layers)+'__reRECO',
                'IntermediateHitDoublets_mixedTripletStepHitDoubletsA'+str(layers)+'__reRECO'
            ),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA"+str(layers))
        )
    )
    
    setattr(process,"mixedTripletStepSeedsB"+str(layers),process.mixedTripletStepSeedsB.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(False),
                FilterPixelHits = cms.bool(True),
                FilterStripHits = cms.bool(True)
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring(
                'RegionsSeedingHitSets_mixedTripletStepHitTripletsB'+str(layers)+'__reRECO',
                'IntermediateHitDoublets_mixedTripletStepHitDoubletsB'+str(layers)+'__reRECO'
            ),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB"+str(layers))
        )
    )
    
    setattr(process,"mixedTripletStepTrackCandidates"+str(layers),process.mixedTripletStepTrackCandidates.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('mixedTripletStepTrajectoryBuilder')
            ),
            TrajectoryCleaner = cms.string('mixedTripletStepTrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag("mixedTripletStepClusters"+str(layers)),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(5000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(50),
            onlyPixelHitsForSeedCleaner = cms.bool(False),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("mixedTripletStepSeeds"+str(layers)),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"mixedTripletStepTrackingRegionsA"+str(layers),process.mixedTripletStepTrackingRegionsA.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(0),
                originHalfLength = cms.double(15.0),
                originRadius = cms.double(1.5),
                precise = cms.bool(True),
                ptMin = cms.double(0.4),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"mixedTripletStepTrackingRegionsB"+str(layers),process.mixedTripletStepTrackingRegionsB.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(0),
                originHalfLength = cms.double(10.0),
                originRadius = cms.double(1.5),
                precise = cms.bool(True),
                ptMin = cms.double(0.6),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"mixedTripletStepTracks"+str(layers),process.mixedTripletStepTracks.clone(
            AlgorithmName = cms.string('mixedTripletStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("mixedTripletStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"pixelLessStep"+str(layers),process.pixelLessStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.6, -0.4, 0.02),
            src = cms.InputTag("pixelLessStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"pixelLessStepClassifier1"+str(layers),process.pixelLessStepClassifier1.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter5_13TeV')
            ),
            qualityCuts = cms.vdouble(-0.4, 0.0, 0.4),
            src = cms.InputTag("pixelLessStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"pixelLessStepClassifier2"+str(layers),process.pixelLessStepClassifier2.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
            ),
            qualityCuts = cms.vdouble(-0.0, 0.0, 0.0),
            src = cms.InputTag("pixelLessStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"pixelLessStepClusters"+str(layers),process.pixelLessStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("mixedTripletStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("mixedTripletStepTracks"+str(layers))
        )
    )
    
    setattr(process,"pixelLessStepHitDoublets"+str(layers),process.pixelLessStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("pixelLessStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"pixelLessStepHitTriplets"+str(layers),process.pixelLessStepHitTriplets.clone(
            ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
            TTRHBuilder = cms.string('WithTrackAngle'),
            chi2VsPtCut = cms.bool(True),
            chi2_cuts = cms.vdouble(3, 4, 5, 5),
            detIdsToDebug = cms.vint32(0, 0, 0),
            doublets = cms.InputTag("pixelLessStepHitDoublets"+str(layers)),
            extraHitRPhitolerance = cms.double(0),
            extraHitRZtolerance = cms.double(0),
            extraPhiKDBox = cms.double(0.005),
            extraRKDBox = cms.double(0.2),
            extraZKDBox = cms.double(0.2),
            fnSigmaRZ = cms.double(2),
            maxChi2 = cms.double(5),
            maxElement = cms.uint32(1000000),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_pixelLessStepHitDoublets'+str(layers)+'__reRECO'),
            phiPreFiltering = cms.double(0.3),
            pt_interv = cms.vdouble(0.4, 0.7, 1, 2),
            refitHits = cms.bool(True),
            useFixedPreFiltering = cms.bool(False)
        )
    )
    
    setattr(process,"pixelLessStepSeedLayers"+str(layers),process.pixelLessStepSeedLayers.clone(
            BPix = cms.PSet(
        
            ),
            FPix = cms.PSet(
        
            ),
            MTEC = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                maxRing = cms.int32(3),
                minRing = cms.int32(3),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHit"),
                skipClusters = cms.InputTag("pixelLessStepClusters"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            MTIB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHit"),
                skipClusters = cms.InputTag("pixelLessStepClusters"+str(layers))
            ),
            MTID = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                maxRing = cms.int32(3),
                minRing = cms.int32(3),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHit"),
                skipClusters = cms.InputTag("pixelLessStepClusters"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                maxRing = cms.int32(2),
                minRing = cms.int32(1),
                skipClusters = cms.InputTag("pixelLessStepClusters"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            TIB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                skipClusters = cms.InputTag("pixelLessStepClusters"+str(layers))
            ),
            TID = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                maxRing = cms.int32(2),
                minRing = cms.int32(1),
                skipClusters = cms.InputTag("pixelLessStepClusters"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'TIB1+TIB2+MTIB3',
                'TIB1+TIB2+MTIB4',
                'TIB1+TIB2+MTID1_pos',
                'TIB1+TIB2+MTID1_neg',
                'TID1_pos+TID2_pos+TID3_pos',
                'TID1_neg+TID2_neg+TID3_neg',
                'TID1_pos+TID2_pos+MTID3_pos',
                'TID1_neg+TID2_neg+MTID3_neg',
                'TID1_pos+TID2_pos+MTEC1_pos',
                'TID1_neg+TID2_neg+MTEC1_neg',
                'TID2_pos+TID3_pos+TEC1_pos',
                'TID2_neg+TID3_neg+TEC1_neg',
                'TID2_pos+TID3_pos+MTEC1_pos',
                'TID2_neg+TID3_neg+MTEC1_neg',
                'TEC1_pos+TEC2_pos+TEC3_pos',
                'TEC1_neg+TEC2_neg+TEC3_neg',
                'TEC1_pos+TEC2_pos+MTEC3_pos',
                'TEC1_neg+TEC2_neg+MTEC3_neg',
                'TEC1_pos+TEC2_pos+TEC4_pos',
                'TEC1_neg+TEC2_neg+TEC4_neg',
                'TEC1_pos+TEC2_pos+MTEC4_pos',
                'TEC1_neg+TEC2_neg+MTEC4_neg',
                'TEC2_pos+TEC3_pos+TEC4_pos',
                'TEC2_neg+TEC3_neg+TEC4_neg',
                'TEC2_pos+TEC3_pos+MTEC4_pos',
                'TEC2_neg+TEC3_neg+MTEC4_neg',
                'TEC2_pos+TEC3_pos+TEC5_pos',
                'TEC2_neg+TEC3_neg+TEC5_neg',
                'TEC2_pos+TEC3_pos+TEC6_pos',
                'TEC2_neg+TEC3_neg+TEC6_neg',
                'TEC3_pos+TEC4_pos+TEC5_pos',
                'TEC3_neg+TEC4_neg+TEC5_neg',
                'TEC3_pos+TEC4_pos+MTEC5_pos',
                'TEC3_neg+TEC4_neg+MTEC5_neg',
                'TEC3_pos+TEC5_pos+TEC6_pos',
                'TEC3_neg+TEC5_neg+TEC6_neg',
                'TEC4_pos+TEC5_pos+TEC6_pos',
                'TEC4_neg+TEC5_neg+TEC6_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"pixelLessStepSeeds"+str(layers),process.pixelLessStepSeeds.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('CombinedSeedComparitor'),
                comparitors = cms.VPSet(
                    cms.PSet(
                        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                        ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                        FilterAtHelixStage = cms.bool(True),
                        FilterPixelHits = cms.bool(False),
                        FilterStripHits = cms.bool(True)
                    ),
                    cms.PSet(
                        ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                        FilterAtHelixStage = cms.bool(False),
                        label = cms.untracked.string('Seeds'),
                        layerMask = cms.PSet(
        
                        ),
                        maxNSat = cms.uint32(3),
                        maxTrimmedSizeDiffNeg = cms.double(1.0),
                        maxTrimmedSizeDiffPos = cms.double(0.7),
                        seedCutMIPs = cms.double(0.35),
                        seedCutSN = cms.double(7.0),
                        subclusterCutMIPs = cms.double(0.45),
                        subclusterCutSN = cms.double(12.0),
                        subclusterWindow = cms.double(0.7),
                        trimMaxADC = cms.double(30.0),
                        trimMaxFracNeigh = cms.double(0.25),
                        trimMaxFracTotal = cms.double(0.15)
                    )
                ),
                mode = cms.string('and')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring(
                'RegionsSeedingHitSets_pixelLessStepHitTriplets'+str(layers)+'__reRECO',
                'BaseTrackerRecHitsOwned_pixelLessStepHitTriplets'+str(layers)+'__reRECO'
            ),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("pixelLessStepHitTriplets"+str(layers))
        )
    )
    
    setattr(process,"pixelLessStepTrackCandidates"+str(layers),process.pixelLessStepTrackCandidates.clone(
            mightGet = cms.untracked.vstring(
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitOutputWrapper_pixelLessStepTrackCandidatesMkFit'+str(layers)+'__reRECO',
                'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO'
            ),
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            mkFitEventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            mkFitPixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            mkFitSeeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+str(layers)),
            mkFitStripHits = cms.InputTag("mkFitSiStripHits"+str(layers)),
            propagatorAlong = cms.ESInputTag("","PropagatorWithMaterial"),
            propagatorOpposite = cms.ESInputTag("","PropagatorWithMaterialOpposite"),
            seeds = cms.InputTag("pixelLessStepSeeds"+str(layers)),
            tracks = cms.InputTag("pixelLessStepTrackCandidatesMkFit"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle"),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"pixelLessStepTrackCandidatesMkFit"+str(layers),process.pixelLessStepTrackCandidatesMkFit.clone(
            backwardFitInCMSSW = cms.bool(False),
            buildingRoutine = cms.string('cloneEngine'),
            clustersToSkip = cms.InputTag("pixelLessStepClusters"+str(layers)),
            config = cms.ESInputTag("","pixelLessStepTrackCandidatesMkFitConfig"),
            eventOfHits = cms.InputTag("mkFitEventOfHits"+str(layers)),
            limitConcurrency = cms.untracked.bool(False),
            mightGet = cms.untracked.vstring(
                'MkFitEventOfHits_mkFitEventOfHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiPixelHits'+str(layers)+'__reRECO',
                'MkFitHitWrapper_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitClusterIndexToHit_mkFitSiStripHits'+str(layers)+'__reRECO',
                'floats_mkFitSiStripHits'+str(layers)+'__reRECO',
                'MkFitSeedWrapper_pixelLessStepTrackCandidatesMkFitSeeds'+str(layers)+'__reRECO'
            ),
            minGoodStripCharge = cms.PSet(
                refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
            ),
            mkFitSilent = cms.untracked.bool(True),
            pixelHits = cms.InputTag("mkFitSiPixelHits"+str(layers)),
            removeDuplicates = cms.bool(True),
            seedCleaning = cms.bool(True),
            seeds = cms.InputTag("pixelLessStepTrackCandidatesMkFitSeeds"+str(layers)),
            stripHits = cms.InputTag("mkFitSiStripHits"+str(layers))
        )
    )
    
    setattr(process,"pixelLessStepTrackCandidatesMkFitSeeds"+str(layers),process.pixelLessStepTrackCandidatesMkFitSeeds.clone(
            mightGet = cms.optional.untracked.vstring,
            seeds = cms.InputTag("pixelLessStepSeeds"+str(layers)),
            ttrhBuilder = cms.ESInputTag("","WithTrackAngle")
        )
    )
    
    setattr(process,"pixelLessStepTrackingRegions"+str(layers),process.pixelLessStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(0),
                originHalfLength = cms.double(12.0),
                originRadius = cms.double(1.0),
                precise = cms.bool(True),
                ptMin = cms.double(0.4),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"pixelLessStepTracks"+str(layers),process.pixelLessStepTracks.clone(
            AlgorithmName = cms.string('pixelLessStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("pixelLessStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"pixelPairStep"+str(layers),process.pixelPairStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.38, -0.23, 0.04),
            src = cms.InputTag("pixelPairStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"pixelPairStepClusters"+str(layers),process.pixelPairStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("detachedTripletStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("detachedTripletStepTracks"+str(layers))
        )
    )
    
    setattr(process,"pixelPairStepHitDoublets"+str(layers),process.pixelPairStepHitDoublets.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(1000000),
            maxElementTotal = cms.uint32(12000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            seedingLayers = cms.InputTag("pixelPairStepSeedLayers"+str(layers)),
            trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"pixelPairStepHitDoubletsB"+str(layers),process.pixelPairStepHitDoubletsB.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(1000000),
            maxElementTotal = cms.uint32(12000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            seedingLayers = cms.InputTag(""),
            trackingRegions = cms.InputTag(""),
            trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB"+str(layers))
        )
    )
    
    setattr(process,"pixelPairStepSeedLayers"+str(layers),process.pixelPairStepSeedLayers.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("pixelPairStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("pixelPairStepClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            layerList = cms.vstring(
                'BPix1+BPix2',
                'BPix1+BPix3',
                'BPix2+BPix3',
                'BPix1+FPix1_pos',
                'BPix1+FPix1_neg',
                'BPix2+FPix1_pos',
                'BPix2+FPix1_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"pixelPairStepSeeds"+str(layers),process.pixelPairStepSeeds.clone(
            seedCollections = cms.VInputTag("pixelPairStepSeedsA"+str(layers), "pixelPairStepSeedsB"+str(layers))
        )
    )
    
    setattr(process,"pixelPairStepSeedsA"+str(layers),process.pixelPairStepSeedsA.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(True),
                FilterStripHits = cms.bool(False)
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoublets'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("pixelPairStepHitDoublets"+str(layers))
        )
    )
    
    setattr(process,"pixelPairStepSeedsB"+str(layers),process.pixelPairStepSeedsB.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(True),
                FilterStripHits = cms.bool(False)
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_pixelPairStepHitDoubletsB'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB"+str(layers))
        )
    )
    
    setattr(process,"pixelPairStepTrackCandidates"+str(layers),process.pixelPairStepTrackCandidates.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('pixelPairStepTrajectoryBuilder')
            ),
            TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag("pixelPairStepClusters"+str(layers)),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(5000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(50),
            onlyPixelHitsForSeedCleaner = cms.bool(True),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("pixelPairStepSeeds"+str(layers)),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"pixelPairStepTrackingRegions"+str(layers),process.pixelPairStepTrackingRegions.clone(
            RegionPSet = cms.PSet(
                VertexCollection = cms.InputTag("firstStepPrimaryVertices"+str(layers)),
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                fixedError = cms.double(0.03),
                halfLengthScaling4BigEvts = cms.bool(False),
                maxNVertices = cms.int32(5),
                maxPtMin = cms.double(1000),
                minHalfLength = cms.double(0),
                minOriginR = cms.double(0),
                nSigmaZ = cms.double(4),
                originRScaling4BigEvts = cms.bool(False),
                originRadius = cms.double(0.015),
                pixelClustersForScaling = cms.InputTag(myCollection),
                precise = cms.bool(True),
                ptMin = cms.double(0.6),
                ptMinScaling4BigEvts = cms.bool(False),
                scalingEndNPix = cms.double(1),
                scalingStartNPix = cms.double(0),
                sigmaZVertex = cms.double(3),
                useFakeVertices = cms.bool(False),
                useFixedError = cms.bool(True),
                useFoundVertices = cms.bool(True),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"pixelPairStepTrackingRegionsSeedLayersB"+str(layers),process.pixelPairStepTrackingRegionsSeedLayersB.clone(
            BPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("pixelPairStepClusters"+str(layers))
            ),
            FPix = cms.PSet(
                HitProducer = cms.string('siPixelRecHits'+str(layers)),
                TTRHBuilder = cms.string('WithTrackAngle'),
                skipClusters = cms.InputTag("pixelPairStepClusters"+str(layers))
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                deltaEta_Cand = cms.double(-1),
                deltaPhi_Cand = cms.double(-1),
                extraEta = cms.double(0),
                extraPhi = cms.double(0),
                input = cms.InputTag(""),
                maxNVertices = cms.int32(5),
                measurementTrackerName = cms.InputTag(""),
                nSigmaZBeamSpot = cms.double(4),
                nSigmaZVertex = cms.double(3),
                operationMode = cms.string('VerticesFixed'),
                originRadius = cms.double(0.015),
                precise = cms.bool(True),
                ptMin = cms.double(0.6),
                searchOpt = cms.bool(False),
                seedingMode = cms.string('Global'),
                vertexCollection = cms.InputTag("firstStepPrimaryVertices"+str(layers)),
                whereToUseMeasurementTracker = cms.string('Never'),
                zErrorBeamSpot = cms.double(24.2),
                zErrorVertex = cms.double(0.03)
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
        
            ),
            badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
            createPlottingFiles = cms.untracked.bool(False),
            debug = cms.untracked.bool(False),
            ignoreSingleFPixPanelModules = cms.bool(True),
            inactivePixelDetectorLabels = cms.VInputTag("siPixelDigis"),
            layerList = cms.vstring(
                'BPix1+BPix4',
                'BPix2+BPix4',
                'BPix3+BPix4',
                'BPix1+FPix2_pos',
                'BPix1+FPix2_neg',
                'BPix1+FPix3_pos',
                'BPix1+FPix3_neg',
                'BPix2+FPix2_pos',
                'BPix2+FPix2_neg',
                'BPix3+FPix1_pos',
                'BPix3+FPix1_neg',
                'FPix1_pos+FPix2_pos',
                'FPix1_neg+FPix2_neg',
                'FPix1_pos+FPix3_pos',
                'FPix1_neg+FPix3_neg',
                'FPix2_pos+FPix3_pos',
                'FPix2_neg+FPix3_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"pixelPairStepTracks"+str(layers),process.pixelPairStepTracks.clone(
            AlgorithmName = cms.string('pixelPairStep'),
            Fitter = cms.string('FlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("pixelPairStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"tobTecStep"+str(layers),process.tobTecStep.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                tfDnnLabel = cms.string('trackSelectionTf')
            ),
            qualityCuts = cms.vdouble(-0.71, -0.58, -0.46),
            src = cms.InputTag("tobTecStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"tobTecStepClassifier1"+str(layers),process.tobTecStepClassifier1.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter6_13TeV')
            ),
            qualityCuts = cms.vdouble(-0.6, -0.45, -0.3),
            src = cms.InputTag("tobTecStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"tobTecStepClassifier2"+str(layers),process.tobTecStepClassifier2.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                GBRForestFileName = cms.string(''),
                GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
            ),
            qualityCuts = cms.vdouble(0.0, 0.0, 0.0),
            src = cms.InputTag("tobTecStepTracks"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"tobTecStepClusters"+str(layers),process.tobTecStepClusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(9.0),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("pixelLessStep"+str(layers),"QualityMasks"),
            trajectories = cms.InputTag("pixelLessStepTracks"+str(layers))
        )
    )
    
    setattr(process,"tobTecStepHitDoubletsPair"+str(layers),process.tobTecStepHitDoubletsPair.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(1000000),
            maxElementTotal = cms.uint32(12000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(False),
            produceSeedingHitSets = cms.bool(True),
            seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"+str(layers)),
            trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"tobTecStepHitDoubletsTripl"+str(layers),process.tobTecStepHitDoubletsTripl.clone(
            clusterCheck = cms.InputTag("trackerClusterCheck"+str(layers)),
            layerPairs = cms.vuint32(0),
            maxElement = cms.uint32(50000000),
            maxElementTotal = cms.uint32(50000000),
            mightGet = cms.optional.untracked.vstring,
            produceIntermediateHitDoublets = cms.bool(True),
            produceSeedingHitSets = cms.bool(False),
            seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"+str(layers)),
            trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"+str(layers)),
            trackingRegionsSeedingLayers = cms.InputTag("")
        )
    )
    
    setattr(process,"tobTecStepHitTripletsTripl"+str(layers),process.tobTecStepHitTripletsTripl.clone(
            ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
            TTRHBuilder = cms.string('WithTrackAngle'),
            chi2VsPtCut = cms.bool(True),
            chi2_cuts = cms.vdouble(3, 4, 5, 5),
            detIdsToDebug = cms.vint32(0, 0, 0),
            doublets = cms.InputTag("tobTecStepHitDoubletsTripl"+str(layers)),
            extraHitRPhitolerance = cms.double(0),
            extraHitRZtolerance = cms.double(0),
            extraPhiKDBox = cms.double(0.01),
            extraRKDBox = cms.double(0.2),
            extraZKDBox = cms.double(0.2),
            fnSigmaRZ = cms.double(2),
            maxChi2 = cms.double(5),
            maxElement = cms.uint32(1000000),
            mightGet = cms.untracked.vstring('IntermediateHitDoublets_tobTecStepHitDoubletsTripl'+str(layers)+'__reRECO'),
            phiPreFiltering = cms.double(0.3),
            pt_interv = cms.vdouble(0.4, 0.7, 1, 2),
            refitHits = cms.bool(True),
            useFixedPreFiltering = cms.bool(False)
        )
    )
    
    setattr(process,"tobTecStepSeedLayersPair"+str(layers),process.tobTecStepSeedLayersPair.clone(
            BPix = cms.PSet(
        
            ),
            FPix = cms.PSet(
        
            ),
            MTEC = cms.PSet(
        
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
        
            ),
            TEC = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                maxRing = cms.int32(5),
                minRing = cms.int32(5),
                skipClusters = cms.InputTag("tobTecStepClusters"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                skipClusters = cms.InputTag("tobTecStepClusters"+str(layers))
            ),
            layerList = cms.vstring(
                'TOB1+TEC1_pos',
                'TOB1+TEC1_neg',
                'TEC1_pos+TEC2_pos',
                'TEC1_neg+TEC2_neg',
                'TEC2_pos+TEC3_pos',
                'TEC2_neg+TEC3_neg',
                'TEC3_pos+TEC4_pos',
                'TEC3_neg+TEC4_neg',
                'TEC4_pos+TEC5_pos',
                'TEC4_neg+TEC5_neg',
                'TEC5_pos+TEC6_pos',
                'TEC5_neg+TEC6_neg',
                'TEC6_pos+TEC7_pos',
                'TEC6_neg+TEC7_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"tobTecStepSeedLayersTripl"+str(layers),process.tobTecStepSeedLayersTripl.clone(
            BPix = cms.PSet(
        
            ),
            FPix = cms.PSet(
        
            ),
            MTEC = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                maxRing = cms.int32(7),
                minRing = cms.int32(6),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHit"),
                skipClusters = cms.InputTag("tobTecStepClusters"+str(layers)),
                useRingSlector = cms.bool(True)
            ),
            MTIB = cms.PSet(
        
            ),
            MTID = cms.PSet(
        
            ),
            MTOB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"rphiRecHit"),
                skipClusters = cms.InputTag("tobTecStepClusters"+str(layers))
            ),
            TEC = cms.PSet(
        
            ),
            TIB = cms.PSet(
        
            ),
            TID = cms.PSet(
        
            ),
            TOB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutTight')
                ),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits"+str(layers),"matchedRecHit"),
                skipClusters = cms.InputTag("tobTecStepClusters"+str(layers))
            ),
            layerList = cms.vstring(
                'TOB1+TOB2+MTOB3',
                'TOB1+TOB2+MTOB4',
                'TOB1+TOB2+MTEC1_pos',
                'TOB1+TOB2+MTEC1_neg'
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"tobTecStepSeeds"+str(layers),process.tobTecStepSeeds.clone(
            seedCollections = cms.VInputTag("tobTecStepSeedsTripl"+str(layers), "tobTecStepSeedsPair"+str(layers))
        )
    )
    
    setattr(process,"tobTecStepSeedsPair"+str(layers),process.tobTecStepSeedsPair.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('CombinedSeedComparitor'),
                comparitors = cms.VPSet(
                    cms.PSet(
                        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                        ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                        FilterAtHelixStage = cms.bool(True),
                        FilterPixelHits = cms.bool(False),
                        FilterStripHits = cms.bool(True)
                    ),
                    cms.PSet(
                        ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                        FilterAtHelixStage = cms.bool(False),
                        label = cms.untracked.string('Seeds'),
                        layerMask = cms.PSet(
        
                        ),
                        maxNSat = cms.uint32(3),
                        maxTrimmedSizeDiffNeg = cms.double(1.0),
                        maxTrimmedSizeDiffPos = cms.double(0.7),
                        seedCutMIPs = cms.double(0.35),
                        seedCutSN = cms.double(7.0),
                        subclusterCutMIPs = cms.double(0.45),
                        subclusterCutSN = cms.double(12.0),
                        subclusterWindow = cms.double(0.7),
                        trimMaxADC = cms.double(30.0),
                        trimMaxFracNeigh = cms.double(0.25),
                        trimMaxFracTotal = cms.double(0.15)
                    )
                ),
                mode = cms.string('and')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring('RegionsSeedingHitSets_tobTecStepHitDoubletsPair'+str(layers)+'__reRECO'),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair"+str(layers))
        )
    )
    
    setattr(process,"tobTecStepSeedsTripl"+str(layers),process.tobTecStepSeedsTripl.clone(
            MinOneOverPtError = cms.double(1),
            OriginTransverseErrorMultiplier = cms.double(1),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('CombinedSeedComparitor'),
                comparitors = cms.VPSet(
                    cms.PSet(
                        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                        ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                        FilterAtHelixStage = cms.bool(True),
                        FilterPixelHits = cms.bool(False),
                        FilterStripHits = cms.bool(True)
                    ),
                    cms.PSet(
                        ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                        FilterAtHelixStage = cms.bool(False),
                        label = cms.untracked.string('Seeds'),
                        layerMask = cms.PSet(
        
                        ),
                        maxNSat = cms.uint32(3),
                        maxTrimmedSizeDiffNeg = cms.double(1.0),
                        maxTrimmedSizeDiffPos = cms.double(0.7),
                        seedCutMIPs = cms.double(0.35),
                        seedCutSN = cms.double(7.0),
                        subclusterCutMIPs = cms.double(0.45),
                        subclusterCutSN = cms.double(12.0),
                        subclusterWindow = cms.double(0.7),
                        trimMaxADC = cms.double(30.0),
                        trimMaxFracNeigh = cms.double(0.25),
                        trimMaxFracTotal = cms.double(0.15)
                    )
                ),
                mode = cms.string('and')
            ),
            SeedMomentumForBOFF = cms.double(5),
            TTRHBuilder = cms.string('WithTrackAngle'),
            forceKinematicWithRegionDirection = cms.bool(False),
            magneticField = cms.string('ParabolicMf'),
            mightGet = cms.untracked.vstring(
                'RegionsSeedingHitSets_tobTecStepHitTripletsTripl'+str(layers)+'__reRECO',
                'BaseTrackerRecHitsOwned_tobTecStepHitTripletsTripl'+str(layers)+'__reRECO'
            ),
            propagator = cms.string('PropagatorWithMaterialParabolicMf'),
            seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl"+str(layers))
        )
    )
    
    setattr(process,"tobTecStepTrackCandidates"+str(layers),process.tobTecStepTrackCandidates.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('tobTecStepTrajectoryBuilder')
            ),
            TrajectoryCleaner = cms.string('tobTecStepTrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag("tobTecStepClusters"+str(layers)),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(5000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(50),
            onlyPixelHitsForSeedCleaner = cms.bool(False),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("tobTecStepSeeds"+str(layers)),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"tobTecStepTrackingRegionsPair"+str(layers),process.tobTecStepTrackingRegionsPair.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(0),
                originHalfLength = cms.double(30.0),
                originRadius = cms.double(6.0),
                precise = cms.bool(True),
                ptMin = cms.double(0.6),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"tobTecStepTrackingRegionsTripl"+str(layers),process.tobTecStepTrackingRegionsTripl.clone(
            RegionPSet = cms.PSet(
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                nSigmaZ = cms.double(0),
                originHalfLength = cms.double(20.0),
                originRadius = cms.double(3.5),
                precise = cms.bool(True),
                ptMin = cms.double(0.55),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"tobTecStepTracks"+str(layers),process.tobTecStepTracks.clone(
            AlgorithmName = cms.string('tobTecStep'),
            Fitter = cms.string('tobTecFlexibleKFFittingSmoother'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("tobTecStepTrackCandidates"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
   
    setattr(process,"muonSeededTracksOutInClassifier"+str(layers),process.muonSeededTracksOutInClassifier.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                dr_par = cms.PSet(
                    d0err = cms.vdouble(0.003, 0.003, 0.003),
                    d0err_par = cms.vdouble(0.001, 0.001, 0.001),
                    drWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
                    dr_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dr_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
                ),
                dz_par = cms.PSet(
                    dzWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
                    dz_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dz_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
                ),
                isHLT = cms.bool(False),
                maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
                maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
                maxDr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                maxDz = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                maxDzWrtBS = cms.vdouble(3.4028234663852886e+38, 24, 15),
                maxLostLayers = cms.vint32(4, 3, 2),
                maxRelPtErr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                min3DLayers = cms.vint32(1, 2, 2),
                minHits = cms.vint32(0, 0, 1),
                minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
                minLayers = cms.vint32(3, 5, 5),
                minNVtxTrk = cms.int32(2),
                minNdof = cms.vdouble(-1, -1, -1),
                minPixelHits = cms.vint32(0, 0, 0)
            ),
            qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
            src = cms.InputTag("muonSeededTracksOutIn"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"muonSeededSeedsInOut"+str(layers),process.muonSeededSeedsInOut.clone(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('KFFitterForRefitInsideOut'),
            MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
            RefitDirection = cms.string('alongMomentum'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('KFSmootherForRefitInsideOut'),
            TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
            cut = cms.string('pt > 2'),
            debug = cms.untracked.bool(False),
            insideOut = cms.bool(True),
            layersToKeep = cms.int32(5),
            src = cms.InputTag("earlyMuons"+str(layers))
        )
    )
    
    setattr(process,"muonSeededTrackCandidatesInOut"+str(layers),process.muonSeededTrackCandidatesInOut.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('none'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('muonSeededTrajectoryBuilderForInOut')
            ),
            TrajectoryCleaner = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag(""),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(5000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(4),
            onlyPixelHitsForSeedCleaner = cms.bool(False),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("muonSeededSeedsInOut"+str(layers)),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"muonSeededTracksInOut"+str(layers),process.muonSeededTracksInOut.clone(
            AlgorithmName = cms.string('muonSeededStepInOut'),
            Fitter = cms.string('muonSeededFittingSmootherWithOutliersRejectionAndRK'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("muonSeededTrackCandidatesInOut"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"muonSeededSeedsOutIn"+str(layers),process.muonSeededSeedsOutIn.clone(
            cut = cms.string('pt > 10 && outerTrack.hitPattern.muonStationsWithValidHits >= 2'),
            debug = cms.untracked.bool(False),
            errorRescaleFactor = cms.double(2.0),
            fromVertex = cms.bool(True),
            hitCollector = cms.string('hitCollectorForOutInMuonSeeds'),
            hitsToTry = cms.int32(3),
            layersToTry = cms.int32(3),
            maxEtaForTOB = cms.double(1.8),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            minEtaForTEC = cms.double(0.7),
            muonPropagator = cms.string('SteppingHelixPropagatorAlong'),
            src = cms.InputTag("earlyMuons"+str(layers)),
            trackerPropagator = cms.string('PropagatorWithMaterial')
        )
    )
    
    setattr(process,"muonSeededTrackCandidatesOutIn"+str(layers),process.muonSeededTrackCandidatesOutIn.clone(
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
            TrajectoryBuilderPSet = cms.PSet(
                refToPSet_ = cms.string('muonSeededTrajectoryBuilderForOutIn')
            ),
            TrajectoryCleaner = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
            TransientInitialStateEstimatorParameters = cms.PSet(
                numberMeasurementsForFit = cms.int32(4),
                propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
                propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
            ),
            cleanTrajectoryAfterInOut = cms.bool(True),
            clustersToSkip = cms.InputTag(""),
            doSeedingRegionRebuilding = cms.bool(True),
            maxNSeeds = cms.uint32(500000),
            maxSeedsBeforeCleaning = cms.uint32(5000),
            mightGet = cms.optional.untracked.vstring,
            numHitsForSeedCleaner = cms.int32(50),
            onlyPixelHitsForSeedCleaner = cms.bool(False),
            phase2clustersToSkip = cms.InputTag(""),
            reverseTrajectories = cms.bool(False),
            src = cms.InputTag("muonSeededSeedsOutIn"+str(layers)),
            useHitsSplitting = cms.bool(True)
        )
    )
    
    setattr(process,"muonSeededTracksOutIn"+str(layers),process.muonSeededTracksOutIn.clone(
            AlgorithmName = cms.string('muonSeededStepOutIn'),
            Fitter = cms.string('muonSeededFittingSmootherWithOutliersRejectionAndRK'),
            GeometricInnerState = cms.bool(False),
            MeasurementTracker = cms.string(''),
            MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"+str(layers)),
            NavigationSchool = cms.string('SimpleNavigationSchool'),
            Propagator = cms.string('RungeKuttaTrackerPropagator'),
            SimpleMagneticField = cms.string(''),
            TTRHBuilder = cms.string('WithAngleAndTemplate'),
            TrajectoryInEvent = cms.bool(False),
            alias = cms.untracked.string('ctfWithMaterialTracks'),
            beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
            clusterRemovalInfo = cms.InputTag(""),
            src = cms.InputTag("muonSeededTrackCandidatesOutIn"+str(layers)),
            useHitsSplitting = cms.bool(False),
            useSimpleMF = cms.bool(False)
        )
    )
    
    setattr(process,"muonSeededTracksInOutClassifier"+str(layers),process.muonSeededTracksInOutClassifier.clone(
            beamspot = cms.InputTag("offlineBeamSpot"+str(layers)),
            ignoreVertices = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            mva = cms.PSet(
                dr_par = cms.PSet(
                    d0err = cms.vdouble(0.003, 0.003, 0.003),
                    d0err_par = cms.vdouble(0.001, 0.001, 0.001),
                    drWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
                    dr_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dr_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
                ),
                dz_par = cms.PSet(
                    dzWPVerr_par = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
                    dz_par1 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                    dz_par2 = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)
                ),
                isHLT = cms.bool(False),
                maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
                maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
                maxDr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                maxDz = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                maxDzWrtBS = cms.vdouble(3.4028234663852886e+38, 24, 15),
                maxLostLayers = cms.vint32(4, 3, 2),
                maxRelPtErr = cms.vdouble(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38),
                min3DLayers = cms.vint32(1, 2, 2),
                minHits = cms.vint32(0, 0, 1),
                minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
                minLayers = cms.vint32(3, 5, 5),
                minNVtxTrk = cms.int32(2),
                minNdof = cms.vdouble(-1, -1, -1),
                minPixelHits = cms.vint32(0, 0, 0)
            ),
            qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
            src = cms.InputTag("muonSeededTracksInOut"+str(layers)),
            vertices = cms.InputTag("firstStepPrimaryVertices"+str(layers))
        )
    )
    
#    setattr(process,"bunchSpacingProducer"+str(layers),process.bunchSpacingProducer.clone())
    
    setattr(process,"rpcRecHits"+str(layers),process.rpcRecHits.clone(
            deadSource = cms.string('File'),
            deadvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat'),
            maskSource = cms.string('File'),
            maskvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat'),
            recAlgo = cms.string('RPCRecHitStandardAlgo'),
            recAlgoConfig = cms.PSet(
        
            ),
            rpcDigiLabel = cms.InputTag("muonRPCDigis")
        )
    )
    
    setattr(process,"ctppsLocalTrackLiteProducer"+str(layers),process.ctppsLocalTrackLiteProducer.clone(
            includeDiamonds = cms.bool(True),
            includePixels = cms.bool(True),
            includeStrips = cms.bool(True),
            mightGet = cms.optional.untracked.vstring,
            pixelTrackTxMax = cms.double(10),
            pixelTrackTxMin = cms.double(-10),
            pixelTrackTyMax = cms.double(10),
            pixelTrackTyMin = cms.double(-10),
            tagDiamondTrack = cms.InputTag("ctppsDiamondLocalTracks"+str(layers)),
            tagPixelTrack = cms.InputTag("ctppsPixelLocalTracks"+str(layers)),
            tagSiStripTrack = cms.InputTag("totemRPLocalTrackFitter"+str(layers)),
            timingTrackTMax = cms.double(12.5),
            timingTrackTMin = cms.double(-12.5)
        )
    )
    
    setattr(process,"ctppsProtons"+str(layers),process.ctppsProtons.clone(
            default_time = cms.double(-999.0),
            doMultiRPReconstruction = cms.bool(True),
            doSingleRPReconstruction = cms.bool(True),
            fitVtxY = cms.bool(True),
            lhcInfoLabel = cms.string(''),
            localAngleXMax = cms.double(0.03),
            localAngleXMin = cms.double(-0.03),
            localAngleYMax = cms.double(0.04),
            localAngleYMin = cms.double(-0.04),
            max_n_timing_tracks = cms.uint32(5),
            mightGet = cms.optional.untracked.vstring,
            multiRPAlgorithm = cms.string('chi2'),
            multiRPReconstructionLabel = cms.string('multiRP'),
            opticsLabel = cms.string(''),
            pixelDiscardBXShiftedTracks = cms.bool(True),
            ppsAssociationCutsLabel = cms.string(''),
            singleRPReconstructionLabel = cms.string('singleRP'),
            tagLocalTrackLite = cms.InputTag("ctppsLocalTrackLiteProducer"+str(layers)),
            useImprovedInitialEstimate = cms.bool(True),
            verbosity = cms.untracked.uint32(0)
        )
    )
    
    setattr(process,"clusterSummaryProducer"+str(layers),process.clusterSummaryProducer.clone(
            doPixels = cms.bool(True),
            doStrips = cms.bool(True),
            pixelClusters = cms.InputTag("siPixelClustersPreSplitting"+str(layers)),
            stripClusters = cms.InputTag(myCollection),
            verbose = cms.bool(False),
            wantedSubDets = cms.vstring(
                'TOB',
                'TIB',
                'TID',
                'TEC',
                'STRIP',
                'BPIX',
                'FPIX',
                'PIXEL'
            ),
            wantedUserSubDets = cms.VPSet()
        )
    )
    
    setattr(process,"hfprereco"+str(layers),process.hfprereco.clone(
            digiLabel = cms.InputTag("hcalDigis"),
            dropZSmarkedPassed = cms.bool(False),
            forceSOI = cms.int32(-1),
            soiShift = cms.int32(0),
            sumAllTimeSlices = cms.bool(False),
            tsFromDB = cms.bool(False)
        )
    )
    
    setattr(process,"hfreco"+str(layers),process.hfreco.clone(
            HFStripFilter = cms.PSet(
                gap = cms.int32(2),
                lstrips = cms.int32(2),
                maxStripTime = cms.double(10.0),
                maxThreshold = cms.double(100.0),
                seedHitIetaMax = cms.int32(35),
                stripThreshold = cms.double(40.0),
                timeMax = cms.double(6.0),
                verboseLevel = cms.untracked.int32(10),
                wedgeCut = cms.double(0.05)
            ),
            PETstat = cms.PSet(
                HcalAcceptSeverityLevel = cms.int32(9),
                longETParams = cms.vdouble(
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0
                ),
                longEnergyParams = cms.vdouble(
                    43.5, 45.7, 48.32, 51.36, 54.82,
                    58.7, 63.0, 67.72, 72.86, 78.42,
                    84.4, 90.8, 97.62
                ),
                long_R = cms.vdouble(0.98),
                long_R_29 = cms.vdouble(0.8),
                shortETParams = cms.vdouble(
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0
                ),
                shortEnergyParams = cms.vdouble(
                    35.1773, 35.37, 35.7933, 36.4472, 37.3317,
                    38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
                    47.4813, 49.98, 52.7093
                ),
                short_R = cms.vdouble(0.8),
                short_R_29 = cms.vdouble(0.8)
            ),
            S8S1stat = cms.PSet(
                HcalAcceptSeverityLevel = cms.int32(9),
                isS8S1 = cms.bool(True),
                longETParams = cms.vdouble(
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0
                ),
                longEnergyParams = cms.vdouble(
                    40, 100, 100, 100, 100,
                    100, 100, 100, 100, 100,
                    100, 100, 100
                ),
                long_optimumSlope = cms.vdouble(
                    0.3, 0.1, 0.1, 0.1, 0.1,
                    0.1, 0.1, 0.1, 0.1, 0.1,
                    0.1, 0.1, 0.1
                ),
                shortETParams = cms.vdouble(
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0
                ),
                shortEnergyParams = cms.vdouble(
                    40, 100, 100, 100, 100,
                    100, 100, 100, 100, 100,
                    100, 100, 100
                ),
                short_optimumSlope = cms.vdouble(
                    0.3, 0.1, 0.1, 0.1, 0.1,
                    0.1, 0.1, 0.1, 0.1, 0.1,
                    0.1, 0.1, 0.1
                )
            ),
            S9S1stat = cms.PSet(
                HcalAcceptSeverityLevel = cms.int32(9),
                isS8S1 = cms.bool(False),
                longETParams = cms.vdouble(
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0
                ),
                longEnergyParams = cms.vdouble(
                    43.5, 45.7, 48.32, 51.36, 54.82,
                    58.7, 63.0, 67.72, 72.86, 78.42,
                    84.4, 90.8, 97.62
                ),
                long_optimumSlope = cms.vdouble(
                    -99999.0, 0.041226250000000006, 0.05251356000000001, 0.0642766, 0.0743328,
                    0.08214848000000001, 0.0622789, 0.0741041, 0.0868186, 0.100422,
                    0.135313, 0.136289, 0.0589927
                ),
                shortETParams = cms.vdouble(
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0
                ),
                shortEnergyParams = cms.vdouble(
                    35.1773, 35.37, 35.7933, 36.4472, 37.3317,
                    38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
                    47.4813, 49.98, 52.7093
                ),
                short_optimumSlope = cms.vdouble(
                    -99999.0, 0.041226250000000006, 0.05251356000000001, 0.0642766, 0.0743328,
                    0.08214848000000001, 0.0622789, 0.0741041, 0.0868186, 0.100422,
                    0.135313, 0.136289, 0.0589927
                )
            ),
            algoConfigClass = cms.string('HFPhase1PMTParams'),
            algorithm = cms.PSet(
                Class = cms.string('HFFlexibleTimeCheck'),
                alwaysCalculateQAsymmetry = cms.bool(False),
                energyWeights = cms.vdouble(
                    1.0, 1.0, 1.0, 0.0, 1.0,
                    0.0, 2.0, 0.0, 2.0, 0.0,
                    2.0, 0.0, 1.0, 0.0, 0.0,
                    1.0, 0.0, 1.0, 0.0, 2.0,
                    0.0, 2.0, 0.0, 2.0, 0.0,
                    1.0
                ),
                minChargeForOvershoot = cms.double(10000000000.0),
                minChargeForUndershoot = cms.double(10000000000.0),
                rejectAllFailures = cms.bool(True),
                soiPhase = cms.uint32(1),
                tfallIfNoTDC = cms.double(-101.0),
                timeShift = cms.double(0.0),
                tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
                triseIfNoTDC = cms.double(-100.0)
            ),
            checkChannelQualityForDepth3and4 = cms.bool(True),
            inputLabel = cms.InputTag("hfprereco"+str(layers)),
            runHFStripFilter = cms.bool(True),
            setNoiseFlags = cms.bool(True),
            useChannelQualityFromDB = cms.bool(True)
        )
    )
    
    setattr(process,"horeco"+str(layers),process.horeco.clone(
            Subdetector = cms.string('HO'),
            correctForPhaseContainment = cms.bool(True),
            correctForTimeslew = cms.bool(True),
            correctTiming = cms.bool(True),
            correctionPhaseNS = cms.double(13.0),
            dataOOTCorrectionCategory = cms.string('Data'),
            dataOOTCorrectionName = cms.string(''),
            digiLabel = cms.InputTag("hcalDigis"),
            dropZSmarkedPassed = cms.bool(True),
            firstAuxTS = cms.int32(4),
            firstSample = cms.int32(4),
            mcOOTCorrectionCategory = cms.string('MC'),
            mcOOTCorrectionName = cms.string(''),
            recoParamsFromDB = cms.bool(True),
            samplesToAdd = cms.int32(4),
            saturationParameters = cms.PSet(
                maxADCvalue = cms.int32(127)
            ),
            setHSCPFlags = cms.bool(True),
            setNegativeFlags = cms.bool(False),
            setNoiseFlags = cms.bool(True),
            setPulseShapeFlags = cms.bool(False),
            setSaturationFlags = cms.bool(True),
            setTimingTrustFlags = cms.bool(False),
            tsFromDB = cms.bool(True),
            useLeakCorrection = cms.bool(False)
        )
    )
    
    setattr(process,"zdcreco"+str(layers),process.zdcreco.clone(
            AuxTSvec = cms.vint32(4, 5, 6, 7),
            Subdetector = cms.string('ZDC'),
            correctForPhaseContainment = cms.bool(False),
            correctForTimeslew = cms.bool(False),
            correctTiming = cms.bool(True),
            correctionPhaseNS = cms.double(0.0),
            digiLabelQIE10ZDC = cms.InputTag("hcalDigis","ZDC"),
            digiLabelcastor = cms.InputTag("castorDigis"),
            digiLabelhcal = cms.InputTag("hcalDigis"),
            dropZSmarkedPassed = cms.bool(True),
            lowGainFrac = cms.double(8.15),
            lowGainOffset = cms.int32(1),
            recoMethod = cms.int32(2),
            saturationParameters = cms.PSet(
                maxADCvalue = cms.int32(127)
            ),
            setHSCPFlags = cms.bool(True),
            setNoiseFlags = cms.bool(True),
            setSaturationFlags = cms.bool(True),
            setTimingTrustFlags = cms.bool(False)
        )
    )
    
    setattr(process,"csc2DRecHits"+str(layers),process.csc2DRecHits.clone(
            CSCDebug = cms.untracked.bool(False),
            CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
            CSCStripClusterChargeCut = cms.double(25),
            CSCStripPeakThreshold = cms.double(10),
            CSCStripxtalksOffset = cms.double(0.03),
            CSCUseCalibrations = cms.bool(True),
            CSCUseGasGainCorrections = cms.bool(False),
            CSCUseReducedWireTimeWindow = cms.bool(True),
            CSCUseStaticPedestals = cms.bool(False),
            CSCUseTimingCorrections = cms.bool(True),
            CSCWireClusterDeltaT = cms.int32(1),
            CSCWireTimeWindowHigh = cms.int32(11),
            CSCWireTimeWindowLow = cms.int32(5),
            CSCstripWireDeltaTime = cms.int32(8),
            ConstSyst_ME12 = cms.double(0.02),
            ConstSyst_ME13 = cms.double(0.03),
            ConstSyst_ME1a = cms.double(0.01),
            ConstSyst_ME1b = cms.double(0.02),
            ConstSyst_ME21 = cms.double(0.03),
            ConstSyst_ME22 = cms.double(0.03),
            ConstSyst_ME31 = cms.double(0.03),
            ConstSyst_ME32 = cms.double(0.03),
            ConstSyst_ME41 = cms.double(0.03),
            NoiseLevel_ME12 = cms.double(7),
            NoiseLevel_ME13 = cms.double(4),
            NoiseLevel_ME1a = cms.double(9),
            NoiseLevel_ME1b = cms.double(6),
            NoiseLevel_ME21 = cms.double(5),
            NoiseLevel_ME22 = cms.double(7),
            NoiseLevel_ME31 = cms.double(5),
            NoiseLevel_ME32 = cms.double(7),
            NoiseLevel_ME41 = cms.double(5),
            UseAverageTime = cms.bool(False),
            UseFivePoleFit = cms.bool(True),
            UseParabolaFit = cms.bool(False),
            XTasymmetry_ME12 = cms.double(0.015),
            XTasymmetry_ME13 = cms.double(0.02),
            XTasymmetry_ME1a = cms.double(0.023),
            XTasymmetry_ME1b = cms.double(0.01),
            XTasymmetry_ME21 = cms.double(0.023),
            XTasymmetry_ME22 = cms.double(0.023),
            XTasymmetry_ME31 = cms.double(0.023),
            XTasymmetry_ME32 = cms.double(0.023),
            XTasymmetry_ME41 = cms.double(0.023),
            mightGet = cms.optional.untracked.vstring,
            readBadChambers = cms.bool(True),
            readBadChannels = cms.bool(False),
            stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
            wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi")
        )
    )
    
    setattr(process,"cscSegments"+str(layers),process.cscSegments.clone(
            algo_psets = cms.VPSet(
                cms.PSet(
                    algo_name = cms.string('CSCSegAlgoSK'),
                    algo_psets = cms.VPSet(
                        cms.PSet(
                            chi2Max = cms.double(99999.0),
                            dPhiFineMax = cms.double(0.025),
                            dPhiMax = cms.double(0.003),
                            dRPhiFineMax = cms.double(8.0),
                            dRPhiMax = cms.double(8.0),
                            minLayersApart = cms.int32(2),
                            verboseInfo = cms.untracked.bool(True),
                            wideSeg = cms.double(3.0)
                        ),
                        cms.PSet(
                            chi2Max = cms.double(99999.0),
                            dPhiFineMax = cms.double(0.025),
                            dPhiMax = cms.double(0.025),
                            dRPhiFineMax = cms.double(3.0),
                            dRPhiMax = cms.double(8.0),
                            minLayersApart = cms.int32(2),
                            verboseInfo = cms.untracked.bool(True),
                            wideSeg = cms.double(3.0)
                        )
                    ),
                    chamber_types = cms.vstring(
                        'ME1/a',
                        'ME1/b',
                        'ME1/2',
                        'ME1/3',
                        'ME2/1',
                        'ME2/2',
                        'ME3/1',
                        'ME3/2',
                        'ME4/1',
                        'ME4/2'
                    ),
                    parameters_per_chamber_type = cms.vint32(
                        2, 1, 1, 1, 1,
                        1, 1, 1, 1, 1
                    )
                ),
                cms.PSet(
                    algo_name = cms.string('CSCSegAlgoTC'),
                    algo_psets = cms.VPSet(
                        cms.PSet(
                            SegmentSorting = cms.int32(1),
                            chi2Max = cms.double(6000.0),
                            chi2ndfProbMin = cms.double(0.0001),
                            dPhiFineMax = cms.double(0.02),
                            dPhiMax = cms.double(0.003),
                            dRPhiFineMax = cms.double(6.0),
                            dRPhiMax = cms.double(1.2),
                            minLayersApart = cms.int32(2),
                            verboseInfo = cms.untracked.bool(True)
                        ),
                        cms.PSet(
                            SegmentSorting = cms.int32(1),
                            chi2Max = cms.double(6000.0),
                            chi2ndfProbMin = cms.double(0.0001),
                            dPhiFineMax = cms.double(0.013),
                            dPhiMax = cms.double(0.00198),
                            dRPhiFineMax = cms.double(3.0),
                            dRPhiMax = cms.double(0.6),
                            minLayersApart = cms.int32(2),
                            verboseInfo = cms.untracked.bool(True)
                        )
                    ),
                    chamber_types = cms.vstring(
                        'ME1/a',
                        'ME1/b',
                        'ME1/2',
                        'ME1/3',
                        'ME2/1',
                        'ME2/2',
                        'ME3/1',
                        'ME3/2',
                        'ME4/1',
                        'ME4/2'
                    ),
                    parameters_per_chamber_type = cms.vint32(
                        2, 1, 1, 1, 1,
                        1, 1, 1, 1, 1
                    )
                ),
                cms.PSet(
                    algo_name = cms.string('CSCSegAlgoDF'),
                    algo_psets = cms.VPSet(
                        cms.PSet(
                            CSCSegmentDebug = cms.untracked.bool(False),
                            Pruning = cms.untracked.bool(False),
                            chi2Max = cms.double(5000.0),
                            dPhiFineMax = cms.double(0.025),
                            dRPhiFineMax = cms.double(8.0),
                            dXclusBoxMax = cms.double(8.0),
                            dYclusBoxMax = cms.double(8.0),
                            maxDPhi = cms.double(999.0),
                            maxDTheta = cms.double(999.0),
                            maxRatioResidualPrune = cms.double(3.0),
                            minHitsForPreClustering = cms.int32(10),
                            minHitsPerSegment = cms.int32(3),
                            minLayersApart = cms.int32(2),
                            nHitsPerClusterIsShower = cms.int32(20),
                            preClustering = cms.untracked.bool(False),
                            tanPhiMax = cms.double(0.5),
                            tanThetaMax = cms.double(1.2)
                        ),
                        cms.PSet(
                            CSCSegmentDebug = cms.untracked.bool(False),
                            Pruning = cms.untracked.bool(False),
                            chi2Max = cms.double(5000.0),
                            dPhiFineMax = cms.double(0.025),
                            dRPhiFineMax = cms.double(12.0),
                            dXclusBoxMax = cms.double(8.0),
                            dYclusBoxMax = cms.double(12.0),
                            maxDPhi = cms.double(999.0),
                            maxDTheta = cms.double(999.0),
                            maxRatioResidualPrune = cms.double(3.0),
                            minHitsForPreClustering = cms.int32(10),
                            minHitsPerSegment = cms.int32(3),
                            minLayersApart = cms.int32(2),
                            nHitsPerClusterIsShower = cms.int32(20),
                            preClustering = cms.untracked.bool(False),
                            tanPhiMax = cms.double(0.8),
                            tanThetaMax = cms.double(2.0)
                        ),
                        cms.PSet(
                            CSCSegmentDebug = cms.untracked.bool(False),
                            Pruning = cms.untracked.bool(False),
                            chi2Max = cms.double(5000.0),
                            dPhiFineMax = cms.double(0.025),
                            dRPhiFineMax = cms.double(8.0),
                            dXclusBoxMax = cms.double(8.0),
                            dYclusBoxMax = cms.double(8.0),
                            maxDPhi = cms.double(999.0),
                            maxDTheta = cms.double(999.0),
                            maxRatioResidualPrune = cms.double(3.0),
                            minHitsForPreClustering = cms.int32(30),
                            minHitsPerSegment = cms.int32(3),
                            minLayersApart = cms.int32(2),
                            nHitsPerClusterIsShower = cms.int32(20),
                            preClustering = cms.untracked.bool(False),
                            tanPhiMax = cms.double(0.5),
                            tanThetaMax = cms.double(1.2)
                        )
                    ),
                    chamber_types = cms.vstring(
                        'ME1/a',
                        'ME1/b',
                        'ME1/2',
                        'ME1/3',
                        'ME2/1',
                        'ME2/2',
                        'ME3/1',
                        'ME3/2',
                        'ME4/1',
                        'ME4/2'
                    ),
                    parameters_per_chamber_type = cms.vint32(
                        3, 1, 2, 2, 1,
                        2, 1, 2, 1, 2
                    )
                ),
                cms.PSet(
                    algo_name = cms.string('CSCSegAlgoST'),
                    algo_psets = cms.VPSet(
                        cms.PSet(
                            BPMinImprovement = cms.double(10000.0),
                            BrutePruning = cms.bool(True),
                            CSCDebug = cms.untracked.bool(False),
                            CorrectTheErrors = cms.bool(True),
                            Covariance = cms.double(0.0),
                            ForceCovariance = cms.bool(False),
                            ForceCovarianceAll = cms.bool(False),
                            NormChi2Cut2D = cms.double(20.0),
                            NormChi2Cut3D = cms.double(10.0),
                            Pruning = cms.bool(True),
                            SeedBig = cms.double(0.0015),
                            SeedSmall = cms.double(0.0002),
                            curvePenalty = cms.double(2.0),
                            curvePenaltyThreshold = cms.double(0.85),
                            dPhiFineMax = cms.double(0.025),
                            dRPhiFineMax = cms.double(8.0),
                            dXclusBoxMax = cms.double(4.0),
                            dYclusBoxMax = cms.double(8.0),
                            hitDropLimit4Hits = cms.double(0.6),
                            hitDropLimit5Hits = cms.double(0.8),
                            hitDropLimit6Hits = cms.double(0.3333),
                            maxDPhi = cms.double(999.0),
                            maxDTheta = cms.double(999.0),
                            maxRatioResidualPrune = cms.double(3),
                            maxRecHitsInCluster = cms.int32(20),
                            minHitsPerSegment = cms.int32(3),
                            onlyBestSegment = cms.bool(False),
                            preClustering = cms.bool(True),
                            preClusteringUseChaining = cms.bool(True),
                            prePrun = cms.bool(True),
                            prePrunLimit = cms.double(3.17),
                            tanPhiMax = cms.double(0.5),
                            tanThetaMax = cms.double(1.2),
                            useShowering = cms.bool(False),
                            yweightPenalty = cms.double(1.5),
                            yweightPenaltyThreshold = cms.double(1.0)
                        ),
                        cms.PSet(
                            BPMinImprovement = cms.double(10000.0),
                            BrutePruning = cms.bool(True),
                            CSCDebug = cms.untracked.bool(False),
                            CorrectTheErrors = cms.bool(True),
                            Covariance = cms.double(0.0),
                            ForceCovariance = cms.bool(False),
                            ForceCovarianceAll = cms.bool(False),
                            NormChi2Cut2D = cms.double(20.0),
                            NormChi2Cut3D = cms.double(10.0),
                            Pruning = cms.bool(True),
                            SeedBig = cms.double(0.0015),
                            SeedSmall = cms.double(0.0002),
                            curvePenalty = cms.double(2.0),
                            curvePenaltyThreshold = cms.double(0.85),
                            dPhiFineMax = cms.double(0.025),
                            dRPhiFineMax = cms.double(8.0),
                            dXclusBoxMax = cms.double(4.0),
                            dYclusBoxMax = cms.double(8.0),
                            hitDropLimit4Hits = cms.double(0.6),
                            hitDropLimit5Hits = cms.double(0.8),
                            hitDropLimit6Hits = cms.double(0.3333),
                            maxDPhi = cms.double(999.0),
                            maxDTheta = cms.double(999.0),
                            maxRatioResidualPrune = cms.double(3),
                            maxRecHitsInCluster = cms.int32(24),
                            minHitsPerSegment = cms.int32(3),
                            onlyBestSegment = cms.bool(False),
                            preClustering = cms.bool(True),
                            preClusteringUseChaining = cms.bool(True),
                            prePrun = cms.bool(True),
                            prePrunLimit = cms.double(3.17),
                            tanPhiMax = cms.double(0.5),
                            tanThetaMax = cms.double(1.2),
                            useShowering = cms.bool(False),
                            yweightPenalty = cms.double(1.5),
                            yweightPenaltyThreshold = cms.double(1.0)
                        )
                    ),
                    chamber_types = cms.vstring(
                        'ME1/a',
                        'ME1/b',
                        'ME1/2',
                        'ME1/3',
                        'ME2/1',
                        'ME2/2',
                        'ME3/1',
                        'ME3/2',
                        'ME4/1',
                        'ME4/2'
                    ),
                    parameters_per_chamber_type = cms.vint32(
                        2, 1, 1, 1, 1,
                        1, 1, 1, 1, 1
                    )
                ),
                cms.PSet(
                    algo_name = cms.string('CSCSegAlgoRU'),
                    algo_psets = cms.VPSet(
                        cms.PSet(
                            chi2Max = cms.double(100.0),
                            chi2Norm_2D_ = cms.double(35),
                            chi2_str = cms.double(50.0),
                            dPhiIntMax = cms.double(0.005),
                            dPhiMax = cms.double(0.006),
                            dRIntMax = cms.double(2.0),
                            dRMax = cms.double(1.5),
                            doCollisions = cms.bool(True),
                            minLayersApart = cms.int32(1),
                            wideSeg = cms.double(3.0)
                        ),
                        cms.PSet(
                            chi2Max = cms.double(100.0),
                            chi2Norm_2D_ = cms.double(35),
                            chi2_str = cms.double(50.0),
                            dPhiIntMax = cms.double(0.004),
                            dPhiMax = cms.double(0.005),
                            dRIntMax = cms.double(2.0),
                            dRMax = cms.double(1.5),
                            doCollisions = cms.bool(True),
                            minLayersApart = cms.int32(1),
                            wideSeg = cms.double(3.0)
                        ),
                        cms.PSet(
                            chi2Max = cms.double(100.0),
                            chi2Norm_2D_ = cms.double(35),
                            chi2_str = cms.double(50.0),
                            dPhiIntMax = cms.double(0.003),
                            dPhiMax = cms.double(0.004),
                            dRIntMax = cms.double(2.0),
                            dRMax = cms.double(1.5),
                            doCollisions = cms.bool(True),
                            minLayersApart = cms.int32(1),
                            wideSeg = cms.double(3.0)
                        ),
                        cms.PSet(
                            chi2Max = cms.double(60.0),
                            chi2Norm_2D_ = cms.double(20),
                            chi2_str = cms.double(30.0),
                            dPhiIntMax = cms.double(0.002),
                            dPhiMax = cms.double(0.003),
                            dRIntMax = cms.double(2.0),
                            dRMax = cms.double(1.5),
                            doCollisions = cms.bool(True),
                            minLayersApart = cms.int32(1),
                            wideSeg = cms.double(3.0)
                        ),
                        cms.PSet(
                            chi2Max = cms.double(180.0),
                            chi2Norm_2D_ = cms.double(60),
                            chi2_str = cms.double(80.0),
                            dPhiIntMax = cms.double(0.005),
                            dPhiMax = cms.double(0.007),
                            dRIntMax = cms.double(2.0),
                            dRMax = cms.double(1.5),
                            doCollisions = cms.bool(True),
                            minLayersApart = cms.int32(1),
                            wideSeg = cms.double(3.0)
                        ),
                        cms.PSet(
                            chi2Max = cms.double(100.0),
                            chi2Norm_2D_ = cms.double(35),
                            chi2_str = cms.double(50.0),
                            dPhiIntMax = cms.double(0.004),
                            dPhiMax = cms.double(0.006),
                            dRIntMax = cms.double(2.0),
                            dRMax = cms.double(1.5),
                            doCollisions = cms.bool(True),
                            minLayersApart = cms.int32(1),
                            wideSeg = cms.double(3.0)
                        )
                    ),
                    chamber_types = cms.vstring(
                        'ME1/a',
                        'ME1/b',
                        'ME1/2',
                        'ME1/3',
                        'ME2/1',
                        'ME2/2',
                        'ME3/1',
                        'ME3/2',
                        'ME4/1',
                        'ME4/2'
                    ),
                    parameters_per_chamber_type = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 5, 6, 5, 6
                    )
                )
            ),
            algo_type = cms.int32(5),
            inputObjects = cms.InputTag("csc2DRecHits"+str(layers))
        )
    )
    
    setattr(process,"dt1DCosmicRecHits"+str(layers),process.dt1DCosmicRecHits.clone(
            debug = cms.untracked.bool(False),
            dtDigiLabel = cms.InputTag("muonDTDigis"),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doVdriftCorr = cms.bool(False),
                maxTime = cms.double(420.0),
                minTime = cms.double(-3.0),
                readLegacyTTrigDB = cms.bool(True),
                readLegacyVDriftDB = cms.bool(True),
                stepTwoFromDigi = cms.bool(False),
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                tTrigModeConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doT0Correction = cms.bool(True),
                    doTOFCorrection = cms.bool(False),
                    doWirePropCorrection = cms.bool(False),
                    t0Label = cms.string(''),
                    tTrigLabel = cms.string('cosmics'),
                    tofCorrType = cms.int32(0),
                    vPropWire = cms.double(24.4),
                    wirePropCorrType = cms.int32(0)
                ),
                useUncertDB = cms.bool(False)
            )
        )
    )
    
    setattr(process,"dt1DRecHits"+str(layers),process.dt1DRecHits.clone(
            debug = cms.untracked.bool(False),
            dtDigiLabel = cms.InputTag("muonDTDigis"),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doVdriftCorr = cms.bool(True),
                maxTime = cms.double(420.0),
                minTime = cms.double(-3.0),
                readLegacyTTrigDB = cms.bool(True),
                readLegacyVDriftDB = cms.bool(True),
                stepTwoFromDigi = cms.bool(False),
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                tTrigModeConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doT0Correction = cms.bool(True),
                    doTOFCorrection = cms.bool(True),
                    doWirePropCorrection = cms.bool(True),
                    t0Label = cms.string(''),
                    tTrigLabel = cms.string(''),
                    tofCorrType = cms.int32(0),
                    vPropWire = cms.double(24.4),
                    wirePropCorrType = cms.int32(0)
                ),
                useUncertDB = cms.bool(True)
            )
        )
    )
    
    setattr(process,"dt4DCosmicSegments"+str(layers),process.dt4DCosmicSegments.clone(
            Reco4DAlgoConfig = cms.PSet(
                AllDTRecHits = cms.bool(True),
                Reco2DAlgoConfig = cms.PSet(
                    AlphaMaxPhi = cms.double(100.0),
                    AlphaMaxTheta = cms.double(100.0),
                    MaxAllowedHits = cms.uint32(50),
                    MaxChi2 = cms.double(4.0),
                    debug = cms.untracked.bool(False),
                    hit_afterT0_resolution = cms.double(0.03),
                    intime_cut = cms.double(-1.0),
                    nSharedHitsMax = cms.int32(2),
                    nUnSharedHitsMin = cms.int32(2),
                    performT0SegCorrection = cms.bool(False),
                    performT0_vdriftSegCorrection = cms.bool(False),
                    perform_delta_rejecting = cms.bool(False),
                    recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
                    recAlgoConfig = cms.PSet(
                        debug = cms.untracked.bool(False),
                        doVdriftCorr = cms.bool(False),
                        maxTime = cms.double(420.0),
                        minTime = cms.double(-3.0),
                        readLegacyTTrigDB = cms.bool(True),
                        readLegacyVDriftDB = cms.bool(True),
                        stepTwoFromDigi = cms.bool(False),
                        tTrigMode = cms.string('DTTTrigSyncFromDB'),
                        tTrigModeConfig = cms.PSet(
                            debug = cms.untracked.bool(False),
                            doT0Correction = cms.bool(True),
                            doTOFCorrection = cms.bool(False),
                            doWirePropCorrection = cms.bool(False),
                            t0Label = cms.string(''),
                            tTrigLabel = cms.string('cosmics'),
                            tofCorrType = cms.int32(0),
                            vPropWire = cms.double(24.4),
                            wirePropCorrType = cms.int32(0)
                        ),
                        useUncertDB = cms.bool(False)
                    ),
                    segmCleanerMode = cms.int32(2)
                ),
                Reco2DAlgoName = cms.string('DTMeantimerPatternReco'),
                debug = cms.untracked.bool(False),
                hit_afterT0_resolution = cms.double(0.03),
                intime_cut = cms.double(-1.0),
                nUnSharedHitsMin = cms.int32(2),
                performT0SegCorrection = cms.bool(False),
                performT0_vdriftSegCorrection = cms.bool(False),
                perform_delta_rejecting = cms.bool(False),
                recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
                recAlgoConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doVdriftCorr = cms.bool(False),
                    maxTime = cms.double(420.0),
                    minTime = cms.double(-3.0),
                    readLegacyTTrigDB = cms.bool(True),
                    readLegacyVDriftDB = cms.bool(True),
                    stepTwoFromDigi = cms.bool(False),
                    tTrigMode = cms.string('DTTTrigSyncFromDB'),
                    tTrigModeConfig = cms.PSet(
                        debug = cms.untracked.bool(False),
                        doT0Correction = cms.bool(True),
                        doTOFCorrection = cms.bool(False),
                        doWirePropCorrection = cms.bool(False),
                        t0Label = cms.string(''),
                        tTrigLabel = cms.string('cosmics'),
                        tofCorrType = cms.int32(0),
                        vPropWire = cms.double(24.4),
                        wirePropCorrType = cms.int32(0)
                    ),
                    useUncertDB = cms.bool(False)
                )
            ),
            Reco4DAlgoName = cms.string('DTMeantimerPatternReco4D'),
            debug = cms.untracked.bool(False),
            recHits1DLabel = cms.InputTag("dt1DCosmicRecHits"+str(layers)),
            recHits2DLabel = cms.InputTag("dt2DCosmicSegments")
        )
    )
    
    setattr(process,"dt4DSegments"+str(layers),process.dt4DSegments.clone(
            Reco4DAlgoConfig = cms.PSet(
                AllDTRecHits = cms.bool(True),
                Reco2DAlgoConfig = cms.PSet(
                    AlphaMaxPhi = cms.double(1.0),
                    AlphaMaxTheta = cms.double(0.9),
                    MaxAllowedHits = cms.uint32(50),
                    MaxChi2 = cms.double(4.0),
                    debug = cms.untracked.bool(False),
                    hit_afterT0_resolution = cms.double(0.03),
                    nSharedHitsMax = cms.int32(2),
                    nUnSharedHitsMin = cms.int32(2),
                    performT0SegCorrection = cms.bool(False),
                    performT0_vdriftSegCorrection = cms.bool(False),
                    perform_delta_rejecting = cms.bool(False),
                    recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
                    recAlgoConfig = cms.PSet(
                        debug = cms.untracked.bool(False),
                        doVdriftCorr = cms.bool(True),
                        maxTime = cms.double(420.0),
                        minTime = cms.double(-3.0),
                        readLegacyTTrigDB = cms.bool(True),
                        readLegacyVDriftDB = cms.bool(True),
                        stepTwoFromDigi = cms.bool(False),
                        tTrigMode = cms.string('DTTTrigSyncFromDB'),
                        tTrigModeConfig = cms.PSet(
                            debug = cms.untracked.bool(False),
                            doT0Correction = cms.bool(True),
                            doTOFCorrection = cms.bool(True),
                            doWirePropCorrection = cms.bool(True),
                            t0Label = cms.string(''),
                            tTrigLabel = cms.string(''),
                            tofCorrType = cms.int32(0),
                            vPropWire = cms.double(24.4),
                            wirePropCorrType = cms.int32(0)
                        ),
                        useUncertDB = cms.bool(True)
                    ),
                    segmCleanerMode = cms.int32(2)
                ),
                Reco2DAlgoName = cms.string('DTMeantimerPatternReco'),
                debug = cms.untracked.bool(False),
                hit_afterT0_resolution = cms.double(0.03),
                nUnSharedHitsMin = cms.int32(2),
                performT0SegCorrection = cms.bool(False),
                performT0_vdriftSegCorrection = cms.bool(False),
                perform_delta_rejecting = cms.bool(False),
                recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
                recAlgoConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doVdriftCorr = cms.bool(True),
                    maxTime = cms.double(420.0),
                    minTime = cms.double(-3.0),
                    readLegacyTTrigDB = cms.bool(True),
                    readLegacyVDriftDB = cms.bool(True),
                    stepTwoFromDigi = cms.bool(False),
                    tTrigMode = cms.string('DTTTrigSyncFromDB'),
                    tTrigModeConfig = cms.PSet(
                        debug = cms.untracked.bool(False),
                        doT0Correction = cms.bool(True),
                        doTOFCorrection = cms.bool(True),
                        doWirePropCorrection = cms.bool(True),
                        t0Label = cms.string(''),
                        tTrigLabel = cms.string(''),
                        tofCorrType = cms.int32(0),
                        vPropWire = cms.double(24.4),
                        wirePropCorrType = cms.int32(0)
                    ),
                    useUncertDB = cms.bool(True)
                )
            ),
            Reco4DAlgoName = cms.string('DTMeantimerPatternReco4D'),
            debug = cms.untracked.bool(False),
            recHits1DLabel = cms.InputTag("dt1DRecHits"+str(layers)),
            recHits2DLabel = cms.InputTag("dt2DSegments")
        )
    )
    
    setattr(process,"gemRecHits"+str(layers),process.gemRecHits.clone(
            applyMasking = cms.bool(False),
            deadFile = cms.optional.FileInPath,
            gemDigiLabel = cms.InputTag("muonGEMDigis"),
            maskFile = cms.optional.FileInPath,
            mightGet = cms.optional.untracked.vstring,
            recAlgo = cms.string('GEMRecHitStandardAlgo'),
            recAlgoConfig = cms.PSet(
        
            )
        )
    )
    
    setattr(process,"gemSegments"+str(layers),process.gemSegments.clone(
            algo_name = cms.string('GEMSegmentAlgorithm'),
            algo_pset = cms.PSet(
                clusterOnlySameBXRecHits = cms.bool(True),
                dEtaChainBoxMax = cms.double(0.05),
                dPhiChainBoxMax = cms.double(0.02),
                dXclusBoxMax = cms.double(1.0),
                dYclusBoxMax = cms.double(5.0),
                maxRecHitsInCluster = cms.int32(4),
                minHitsPerSegment = cms.uint32(2),
                preClustering = cms.bool(True),
                preClusteringUseChaining = cms.bool(True)
            ),
            ge0_name = cms.string('GE0SegAlgoRU'),
            ge0_pset = cms.PSet(
                allowWideSegments = cms.bool(True),
                doCollisions = cms.bool(True),
                maxChi2Additional = cms.double(100.0),
                maxChi2GoodSeg = cms.double(50),
                maxChi2Prune = cms.double(50),
                maxETASeeds = cms.double(0.1),
                maxNumberOfHits = cms.uint32(300),
                maxNumberOfHitsPerLayer = cms.uint32(100),
                maxPhiAdditional = cms.double(0.001096605744),
                maxPhiSeeds = cms.double(0.001096605744),
                maxTOFDiff = cms.double(25),
                minNumberOfHits = cms.uint32(4),
                requireCentralBX = cms.bool(True)
            ),
            gemRecHitLabel = cms.InputTag("gemRecHits"+str(layers))
        )
    )
    
    setattr(process,"ctppsDiamondLocalTracks"+str(layers),process.ctppsDiamondLocalTracks.clone(
            mightGet = cms.optional.untracked.vstring,
            recHitsTag = cms.InputTag("ctppsDiamondRecHits"+str(layers)),
            trackingAlgorithmParams = cms.PSet(
                excludeSingleEdgeHits = cms.bool(True),
                pixelEfficiencyFunction = cms.string('(x>[0]-0.5*[1])*(x<[0]+0.5*[1])+0*[2]'),
                resolution = cms.double(0.01),
                sigma = cms.double(0.1),
                startFromX = cms.double(-0.5),
                stopAtX = cms.double(19.5),
                threshold = cms.double(1.5),
                thresholdFromMaximum = cms.double(0.5),
                tolerance = cms.double(0.1),
                yPosition = cms.double(0),
                yWidth = cms.double(0)
            )
        )
    )
    
    setattr(process,"ctppsDiamondRecHits"+str(layers),process.ctppsDiamondRecHits.clone(
            applyCalibration = cms.bool(True),
            digiTag = cms.InputTag("ctppsDiamondRawToDigi","TimingDiamond"),
            mightGet = cms.optional.untracked.vstring,
            timeSliceNs = cms.double(0.0244140625),
            timingCalibrationTag = cms.string('GlobalTag:PPSDiamondTimingCalibration')
        )
    )
    
    setattr(process,"ctppsPixelClusters"+str(layers),process.ctppsPixelClusters.clone(
            ADCThreshold = cms.int32(2),
            ElectronADCGain = cms.double(135),
            RPixVerbosity = cms.untracked.int32(0),
            SeedADCThreshold = cms.int32(2),
            VCaltoElectronGain = cms.int32(50),
            VCaltoElectronOffset = cms.int32(-411),
            doSingleCalibration = cms.bool(False),
            mightGet = cms.optional.untracked.vstring,
            tag = cms.InputTag("ctppsPixelDigis")
        )
    )
    
    setattr(process,"ctppsPixelLocalTracks"+str(layers),process.ctppsPixelLocalTracks.clone(
            maxHitPerPlane = cms.int32(20),
            maxHitPerRomanPot = cms.int32(60),
            maxRoadSize = cms.int32(20),
            maxTrackPerPattern = cms.int32(5),
            maxTrackPerRomanPot = cms.int32(10),
            maximumChi2OverNDF = cms.double(5),
            maximumXLocalDistanceFromTrack = cms.double(0.2),
            maximumYLocalDistanceFromTrack = cms.double(0.3),
            mightGet = cms.optional.untracked.vstring,
            minRoadSize = cms.int32(3),
            numberOfPlanesPerPot = cms.int32(6),
            patternFinderAlgorithm = cms.string('RPixRoadFinder'),
            roadRadius = cms.double(1),
            tag = cms.InputTag("ctppsPixelRecHits"+str(layers)),
            trackFinderAlgorithm = cms.string('RPixPlaneCombinatoryTracking'),
            trackMinNumberOfPoints = cms.uint32(3),
            verbosity = cms.untracked.int32(0)
        )
    )
    
    setattr(process,"ctppsPixelRecHits"+str(layers),process.ctppsPixelRecHits.clone(
            RPixClusterTag = cms.InputTag("ctppsPixelClusters"+str(layers)),
            RPixVerbosity = cms.untracked.int32(0),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"diamondSampicLocalTracks"+str(layers),process.diamondSampicLocalTracks.clone(
            maxPlaneActiveChannels = cms.int32(2),
            mightGet = cms.optional.untracked.vstring,
            recHitsTag = cms.InputTag("totemTimingRecHits"+str(layers)),
            trackingAlgorithmParams = cms.PSet(
                pixelEfficiencyFunction = cms.string('(x>[0]-0.5*[1]-0.05)*(x<[0]+0.5*[1]-0.05)+0*[2]'),
                resolution = cms.double(0.01),
                sigma = cms.double(0),
                threshold = cms.double(1.5),
                thresholdFromMaximum = cms.double(0.5),
                tolerance = cms.double(0.1),
                yPosition = cms.double(0),
                yWidth = cms.double(0)
            )
        )
    )
    
    setattr(process,"totemTimingRecHits"+str(layers),process.totemTimingRecHits.clone(
            baselinePoints = cms.int32(8),
            cfdFraction = cms.double(0.3),
            digiTag = cms.InputTag("totemTimingRawToDigi","TotemTiming"),
            hysteresis = cms.double(0.005),
            lowPassFrequency = cms.double(0.7),
            mergeTimePeaks = cms.bool(True),
            mightGet = cms.optional.untracked.vstring,
            sampicOffset = cms.double(1),
            sampicSamplingPeriodNs = cms.double(0.1299545159194282),
            saturationLimit = cms.double(0.1),
            smoothingPoints = cms.int32(20),
            timingCalibrationTag = cms.string('GlobalTag:TotemTimingCalibration')
        )
    )
    
    setattr(process,"totemRPClusterProducer"+str(layers),process.totemRPClusterProducer.clone(
            mightGet = cms.optional.untracked.vstring,
            tagDigi = cms.InputTag("totemRPRawToDigi","TrackingStrip"),
            verbosity = cms.int32(0)
        )
    )
    
    setattr(process,"totemRPLocalTrackFitter"+str(layers),process.totemRPLocalTrackFitter.clone(
            mightGet = cms.optional.untracked.vstring,
            tagUVPattern = cms.InputTag("totemRPUVPatternFinder"+str(layers)),
            verbosity = cms.int32(0)
        )
    )
    
    setattr(process,"totemRPRecHitProducer"+str(layers),process.totemRPRecHitProducer.clone(
            mightGet = cms.optional.untracked.vstring,
            tagCluster = cms.InputTag("totemRPClusterProducer"+str(layers)),
            verbosity = cms.int32(0)
        )
    )
    
    setattr(process,"totemRPUVPatternFinder"+str(layers),process.totemRPUVPatternFinder.clone(
            allowAmbiguousCombination = cms.bool(False),
            clusterSize_a = cms.double(0.02),
            clusterSize_b = cms.double(0.3),
            exceptionalSettings = cms.VPSet(),
            maxHitsPerPlaneToSearch = cms.uint32(5),
            max_a_toFit = cms.double(10),
            mightGet = cms.optional.untracked.vstring,
            minPlanesPerProjectionToFit = cms.uint32(3),
            minPlanesPerProjectionToSearch = cms.uint32(3),
            tagRecHit = cms.InputTag("totemRPRecHitProducer"+str(layers)),
            threshold = cms.double(2.99),
            verbosity = cms.untracked.uint32(0)
        )
    )
    
    setattr(process,"siStripClusters"+str(layers),process.siStripClusters.clone(
            Clusterizer = cms.PSet(
                Algorithm = cms.string('ThreeThresholdAlgorithm'),
                ChannelThreshold = cms.double(2.0),
                ClusterThreshold = cms.double(5.0),
                ConditionsLabel = cms.string(''),
                MaxAdjacentBad = cms.uint32(0),
                MaxSequentialBad = cms.uint32(1),
                MaxSequentialHoles = cms.uint32(0),
                RemoveApvShots = cms.bool(True),
                SeedThreshold = cms.double(3.0),
                clusterChargeCut = cms.PSet(
                    refToPSet_ = cms.string('SiStripClusterChargeCutNone')
                )
            ),
            DigiProducersList = cms.VInputTag(cms.InputTag("siStripDigis","ZeroSuppressed"), cms.InputTag("siStripZeroSuppression"+str(layers),"VirginRaw"), cms.InputTag("siStripZeroSuppression"+str(layers),"ProcessedRaw"), cms.InputTag("siStripZeroSuppression"+str(layers),"ScopeMode"))
        )
    )
    
    setattr(process,"siStripMatchedRecHits"+str(layers),process.siStripMatchedRecHits.clone(
            ClusterProducer = cms.InputTag(myCollection),
            MaskBadAPVFibers = cms.bool(False),
            Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
            StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
            VerbosityLevel = cms.optional.untracked.int32,
            doMatching = cms.bool(True),
            matchedRecHits = cms.string('matchedRecHit'),
            mightGet = cms.optional.untracked.vstring,
            rphiRecHits = cms.string('rphiRecHit'),
            siStripQualityLabel = cms.ESInputTag("",""),
            stereoRecHits = cms.string('stereoRecHit'),
            useSiStripQuality = cms.bool(False)
        )
    )
    
    setattr(process,"siStripZeroSuppression"+str(layers),process.siStripZeroSuppression.clone(
            Algorithms = cms.PSet(
                APVInspectMode = cms.string('BaselineFollower'),
                APVRestoreMode = cms.string('BaselineFollower'),
                ApplyBaselineCleaner = cms.bool(True),
                ApplyBaselineRejection = cms.bool(True),
                CleaningSequence = cms.uint32(1),
                CommonModeNoiseSubtractionMode = cms.string('IteratedMedian'),
                CutToAvoidSignal = cms.double(2.0),
                DeltaCMThreshold = cms.uint32(20),
                Deviation = cms.uint32(25),
                ForceNoRestore = cms.bool(False),
                Fraction = cms.double(0.2),
                Iterations = cms.int32(3),
                MeanCM = cms.int32(0),
                PedestalSubtractionFedMode = cms.bool(False),
                SiStripFedZeroSuppressionMode = cms.uint32(4),
                TruncateInSuppressor = cms.bool(True),
                Use10bitsTruncation = cms.bool(False),
                consecThreshold = cms.uint32(5),
                discontinuityThreshold = cms.int32(12),
                distortionThreshold = cms.uint32(20),
                doAPVRestore = cms.bool(True),
                filteredBaselineDerivativeSumSquare = cms.double(30),
                filteredBaselineMax = cms.double(6),
                hitStripThreshold = cms.uint32(40),
                lastGradient = cms.int32(10),
                minStripsToFit = cms.uint32(4),
                nSaturatedStrip = cms.uint32(2),
                nSigmaNoiseDerTh = cms.uint32(4),
                nSmooth = cms.uint32(9),
                restoreThreshold = cms.double(0.5),
                sizeWindow = cms.int32(1),
                slopeX = cms.int32(3),
                slopeY = cms.int32(4),
                useCMMeanMap = cms.bool(False),
                useRealMeanCM = cms.bool(False),
                widthCluster = cms.int32(64)
            ),
            RawDigiProducersList = cms.VInputTag(cms.InputTag("siStripDigis","VirginRaw"), cms.InputTag("siStripDigis","ProcessedRaw"), cms.InputTag("siStripDigis","ScopeMode")),
            fixCM = cms.bool(False),
            produceBaselinePoints = cms.bool(False),
            produceCalculatedBaseline = cms.bool(False),
            produceHybridFormat = cms.bool(False),
            produceRawDigis = cms.bool(True),
            storeCM = cms.bool(True),
            storeInZScollBadAPV = cms.bool(True)
        )
    )
    
    setattr(process,"ecalCompactTrigPrim"+str(layers),process.ecalCompactTrigPrim.clone(
            inColl = cms.InputTag("ecalDigis","EcalTriggerPrimitives"),
            outColl = cms.string('')
        )
    )
    
    setattr(process,"ecalTPSkim"+str(layers),process.ecalTPSkim.clone(
            chStatusToSelectTP = cms.vuint32(13),
            doBarrel = cms.bool(True),
            doEndcap = cms.bool(True),
            skipModule = cms.bool(False),
            tpInputCollection = cms.InputTag("ecalDigis","EcalTriggerPrimitives"),
            tpOutputCollection = cms.string('')
        )
    )
    
    setattr(process,"ecalDetIdToBeRecovered"+str(layers),process.ecalDetIdToBeRecovered.clone(
            ebDetIdToBeRecovered = cms.string('ebDetId'),
            ebFEToBeRecovered = cms.string('ebFE'),
            ebIntegrityChIdErrors = cms.InputTag("ecalDigis","EcalIntegrityChIdErrors"),
            ebIntegrityGainErrors = cms.InputTag("ecalDigis","EcalIntegrityGainErrors"),
            ebIntegrityGainSwitchErrors = cms.InputTag("ecalDigis","EcalIntegrityGainSwitchErrors"),
            ebSrFlagCollection = cms.InputTag("ecalDigis"),
            eeDetIdToBeRecovered = cms.string('eeDetId'),
            eeFEToBeRecovered = cms.string('eeFE'),
            eeIntegrityChIdErrors = cms.InputTag("ecalDigis","EcalIntegrityChIdErrors"),
            eeIntegrityGainErrors = cms.InputTag("ecalDigis","EcalIntegrityGainErrors"),
            eeIntegrityGainSwitchErrors = cms.InputTag("ecalDigis","EcalIntegrityGainSwitchErrors"),
            eeSrFlagCollection = cms.InputTag("ecalDigis"),
            integrityBlockSizeErrors = cms.InputTag("ecalDigis","EcalIntegrityBlockSizeErrors"),
            integrityTTIdErrors = cms.InputTag("ecalDigis","EcalIntegrityTTIdErrors")
        )
    )
    
    setattr(process,"siPixelClustersPreSplitting"+str(layers),process.siPixelClustersPreSplitting.clone(
            cpu = cms.EDProducer("SiPixelClusterProducer",
                ChannelThreshold = cms.int32(10),
                ClusterMode = cms.string('PixelThresholdClusterizer'),
                ClusterThreshold = cms.int32(4000),
                ClusterThreshold_L1 = cms.int32(4000),
                ElectronPerADCGain = cms.double(135),
                MissCalibrate = cms.bool(True),
                Phase2Calibration = cms.bool(False),
                Phase2DigiBaseline = cms.double(1200),
                Phase2KinkADC = cms.int32(8),
                Phase2ReadoutMode = cms.int32(-1),
                SeedThreshold = cms.int32(1000),
                SplitClusters = cms.bool(False),
                VCaltoElectronGain = cms.int32(1),
                VCaltoElectronGain_L1 = cms.int32(1),
                VCaltoElectronOffset = cms.int32(0),
                VCaltoElectronOffset_L1 = cms.int32(0),
                maxNumberOfClusters = cms.int32(-1),
                mightGet = cms.optional.untracked.vstring,
                payloadType = cms.string('Offline'),
                src = cms.InputTag("siPixelDigis")
            )
        )
    )
    
    setattr(process,"siPixelRecHitsPreSplitting"+str(layers),process.siPixelRecHitsPreSplitting.clone(
            cpu = cms.EDProducer("SiPixelRecHitConverter",
                CPE = cms.string('PixelCPEGeneric'),
                VerboseLevel = cms.untracked.int32(0),
                src = cms.InputTag("siPixelClustersPreSplitting"+str(layers))
            )
        )
    )
    
    setattr(process,"ecalPreshowerRecHit"+str(layers),process.ecalPreshowerRecHit.clone(
            ESRecoAlgo = cms.int32(0),
            ESdigiCollection = cms.InputTag("ecalPreshowerDigis"),
            ESrechitCollection = cms.string('EcalRecHitsES'),
            algo = cms.string('ESRecHitWorker')
        )
    )
    
    setattr(process,"ecalMultiFitUncalibRecHit"+str(layers),process.ecalMultiFitUncalibRecHit.clone(
            cpu = cms.EDProducer("EcalUncalibRecHitProducer",
                EBdigiCollection = cms.InputTag("ecalDigis","ebDigis"),
                EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
                EEdigiCollection = cms.InputTag("ecalDigis","eeDigis"),
                EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
                algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
                algoPSet = cms.PSet(
                    EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
                    EBtimeConstantTerm = cms.double(0.6),
                    EBtimeFitLimits_Lower = cms.double(0.2),
                    EBtimeFitLimits_Upper = cms.double(1.4),
                    EBtimeFitParameters = cms.vdouble(
                        -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
                        91.01147, -50.35761, 11.05621
                    ),
                    EBtimeNconst = cms.double(28.5),
                    EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
                    EEtimeConstantTerm = cms.double(1.0),
                    EEtimeFitLimits_Lower = cms.double(0.2),
                    EEtimeFitLimits_Upper = cms.double(1.4),
                    EEtimeFitParameters = cms.vdouble(
                        -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
                        140.7432, -75.41106, 16.20277
                    ),
                    EEtimeNconst = cms.double(31.8),
                    activeBXs = cms.vint32(
                        -5, -4, -3, -2, -1,
                        0, 1, 2, 3, 4
                    ),
                    addPedestalUncertaintyEB = cms.double(0.0),
                    addPedestalUncertaintyEE = cms.double(0.0),
                    ampErrorCalculation = cms.bool(True),
                    amplitudeThresholdEB = cms.double(10),
                    amplitudeThresholdEE = cms.double(10),
                    crossCorrelationStartTime = cms.double(-25),
                    crossCorrelationStopTime = cms.double(25),
                    crossCorrelationTargetTimePrecision = cms.double(0.01),
                    doPrefitEB = cms.bool(False),
                    doPrefitEE = cms.bool(False),
                    dynamicPedestalsEB = cms.bool(False),
                    dynamicPedestalsEE = cms.bool(False),
                    gainSwitchUseMaxSampleEB = cms.bool(True),
                    gainSwitchUseMaxSampleEE = cms.bool(False),
                    mitigateBadSamplesEB = cms.bool(False),
                    mitigateBadSamplesEE = cms.bool(False),
                    outOfTimeThresholdGain12mEB = cms.double(5),
                    outOfTimeThresholdGain12mEE = cms.double(1000),
                    outOfTimeThresholdGain12pEB = cms.double(5),
                    outOfTimeThresholdGain12pEE = cms.double(1000),
                    outOfTimeThresholdGain61mEB = cms.double(5),
                    outOfTimeThresholdGain61mEE = cms.double(1000),
                    outOfTimeThresholdGain61pEB = cms.double(5),
                    outOfTimeThresholdGain61pEE = cms.double(1000),
                    prefitMaxChiSqEB = cms.double(25.0),
                    prefitMaxChiSqEE = cms.double(10.0),
                    selectiveBadSampleCriteriaEB = cms.bool(False),
                    selectiveBadSampleCriteriaEE = cms.bool(False),
                    simplifiedNoiseModelForGainSwitch = cms.bool(True),
                    timealgo = cms.string('RatioMethod'),
                    useLumiInfoRunHeader = cms.bool(True)
                )
            )
        )
    )
    
    setattr(process,"ecalRecHit"+str(layers),process.ecalRecHit.clone(
            cpu = cms.EDProducer("EcalRecHitProducer",
                ChannelStatusToBeExcluded = cms.vstring(
                    'kDAC',
                    'kNoisy',
                    'kNNoisy',
                    'kFixedG6',
                    'kFixedG1',
                    'kFixedG0',
                    'kNonRespondingIsolated',
                    'kDeadVFE',
                    'kDeadFE',
                    'kNoDataNoTP'
                ),
                EBLaserMAX = cms.double(3.0),
                EBLaserMIN = cms.double(0.5),
                EBrechitCollection = cms.string('EcalRecHitsEB'),
                EBuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHit"+str(layers),"EcalUncalibRecHitsEB"),
                EELaserMAX = cms.double(8.0),
                EELaserMIN = cms.double(0.5),
                EErechitCollection = cms.string('EcalRecHitsEE'),
                EEuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHit"+str(layers),"EcalUncalibRecHitsEE"),
                algo = cms.string('EcalRecHitWorkerSimple'),
                algoRecover = cms.string('EcalRecHitWorkerRecover'),
                bdtWeightFileCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_onlyCracks_ZskimData2017_v1.xml'),
                bdtWeightFileNoCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_noCracks_ZskimData2017_v1.xml'),
                cleaningConfig = cms.PSet(
                    cThreshold_barrel = cms.double(4),
                    cThreshold_double = cms.double(10),
                    cThreshold_endcap = cms.double(15),
                    e4e1Threshold_barrel = cms.double(0.08),
                    e4e1Threshold_endcap = cms.double(0.3),
                    e4e1_a_barrel = cms.double(0.02),
                    e4e1_a_endcap = cms.double(0.02),
                    e4e1_b_barrel = cms.double(0.02),
                    e4e1_b_endcap = cms.double(-0.0125),
                    e6e2thresh = cms.double(0.04),
                    ignoreOutOfTimeThresh = cms.double(1000000000.0),
                    tightenCrack_e1_double = cms.double(2),
                    tightenCrack_e1_single = cms.double(1),
                    tightenCrack_e4e1_single = cms.double(2.5),
                    tightenCrack_e6e2_double = cms.double(3)
                ),
                dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
                dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
                ebDetIdToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered"+str(layers),"ebDetId"),
                ebFEToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered"+str(layers),"ebFE"),
                eeDetIdToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered"+str(layers),"eeDetId"),
                eeFEToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered"+str(layers),"eeFE"),
                flagsMapDBReco = cms.PSet(
                    kDead = cms.vstring('kNoDataNoTP'),
                    kGood = cms.vstring(
                        'kOk',
                        'kDAC',
                        'kNoLaser',
                        'kNoisy'
                    ),
                    kNeighboursRecovered = cms.vstring(
                        'kFixedG0',
                        'kNonRespondingIsolated',
                        'kDeadVFE'
                    ),
                    kNoisy = cms.vstring(
                        'kNNoisy',
                        'kFixedG6',
                        'kFixedG1'
                    ),
                    kTowerRecovered = cms.vstring('kDeadFE')
                ),
                killDeadChannels = cms.bool(True),
                laserCorrection = cms.bool(True),
                logWarningEtThreshold_EB_FE = cms.double(50),
                logWarningEtThreshold_EE_FE = cms.double(50),
                recoverEBFE = cms.bool(True),
                recoverEBIsolatedChannels = cms.bool(False),
                recoverEBVFE = cms.bool(False),
                recoverEEFE = cms.bool(True),
                recoverEEIsolatedChannels = cms.bool(False),
                recoverEEVFE = cms.bool(False),
                singleChannelRecoveryMethod = cms.string('BDTG'),
                singleChannelRecoveryThreshold = cms.double(0.7),
                skipTimeCalib = cms.bool(False),
                sum8ChannelRecoveryThreshold = cms.double(0.0),
                triggerPrimitiveDigiCollection = cms.InputTag("ecalDigis","EcalTriggerPrimitives")
            )
        )
    )

#######################################################################################

    setattr(process,"pixelPairStepSeedClusterMask"+str(layers),process.pixelPairStepSeedClusterMask.clone(
            Common = cms.PSet(
                maxChi2 = cms.double(9.0)
            ),
            oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("pixelPairStepSeeds"+str(layers))
        )
    )
    
    setattr(process,"CommonClusterCheckPSet"+str(layers),process.CommonClusterCheckPSet.clone(
            ClusterCollectionLabel = cms.InputTag(myCollection),
            MaxNumberOfCosmicClusters = cms.uint32(400000),
            MaxNumberOfPixelClusters = cms.uint32(40000),
            PixelClusterCollectionLabel = cms.InputTag(myCollection),
            cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
            doClusterCheck = cms.bool(False)
        )
    )
    
    setattr(process,"beamhaloTrackerSeeds"+str(layers),process.beamhaloTrackerSeeds.clone(
            Charges = cms.vint32(-1, 1),
            CheckHitsAreOnDifferentLayers = cms.bool(False),
            ClusterCollectionLabel = cms.InputTag(myCollection),
            ErrorRescaling = cms.double(50.0),
            MaxNumberOfCosmicClusters = cms.uint32(10000),
            MaxNumberOfPixelClusters = cms.uint32(10000),
            OrderedHitsFactoryPSets = cms.VPSet(
                cms.PSet(
                    ComponentName = cms.string('BeamHaloPairGenerator'),
                    LayerSrc = cms.InputTag("beamhaloTrackerSeedingLayers"),
                    NavigationDirection = cms.string('outsideIn'),
                    PropagationDirection = cms.string('alongMomentum'),
                    maxTheta = cms.double(0.1)
                ),
                cms.PSet(
                    ComponentName = cms.string('BeamHaloPairGenerator'),
                    LayerSrc = cms.InputTag("beamhaloTrackerSeedingLayers"),
                    NavigationDirection = cms.string('outsideIn'),
                    PropagationDirection = cms.string('oppositeToMomentum'),
                    maxTheta = cms.double(0.1)
                )
            ),
            PixelClusterCollectionLabel = cms.InputTag(myCollection),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalRegionProducer'),
                RegionPSet = cms.PSet(
                    originHalfLength = cms.double(21.2),
                    originRadius = cms.double(0.2),
                    originXPos = cms.double(0.0),
                    originYPos = cms.double(0.0),
                    originZPos = cms.double(0.0),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.9),
                    useMultipleScattering = cms.bool(False)
                )
            ),
            SeedMomentum = cms.double(15.0),
            SeedsFromNegativeY = cms.bool(False),
            SeedsFromPositiveY = cms.bool(False),
            SetMomentum = cms.bool(True),
            TTRHBuilder = cms.string('WithTrackAngle'),
            UseScintillatorsConstraint = cms.bool(False),
            doClusterCheck = cms.bool(True),
            maxSeeds = cms.int32(10000),
            requireBOFF = cms.bool(False)
        )
    )
    
    setattr(process,"clusterSummaryProducerNoSplitting"+str(layers),process.clusterSummaryProducerNoSplitting.clone(
            doPixels = cms.bool(True),
            doStrips = cms.bool(True),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            verbose = cms.bool(False),
            wantedSubDets = cms.vstring(
                'TOB',
                'TIB',
                'TID',
                'TEC',
                'STRIP',
                'BPIX',
                'FPIX',
                'PIXEL'
            ),
            wantedUserSubDets = cms.VPSet()
        )
    )
    
    setattr(process,"conv2Clusters"+str(layers),process.conv2Clusters.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(30),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag("convClusters"+str(layers)),
            overrideTrkQuals = cms.InputTag("convStepSelector"+str(layers),"convStep"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("","QualityMasks"),
            trajectories = cms.InputTag("convStepTracks"+str(layers))
        )
    )
    
    setattr(process,"globalMixedSeeds"+str(layers),process.globalMixedSeeds.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(400000),
                MaxNumberOfPixelClusters = cms.uint32(40000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
                doClusterCheck = cms.bool(False)
            ),
            OrderedHitsFactoryPSet = cms.PSet(
                ComponentName = cms.string('StandardHitPairGenerator'),
                SeedingLayers = cms.InputTag("MixedLayerPairs"),
                maxElement = cms.uint32(1000000)
            ),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
                RegionPSet = cms.PSet(
                    beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                    originHalfLength = cms.double(21.2),
                    originRadius = cms.double(0.2),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.9),
                    useMultipleScattering = cms.bool(False)
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
                MinOneOverPtError = cms.double(1.0),
                OriginTransverseErrorMultiplier = cms.double(1.0),
                SeedMomentumForBOFF = cms.double(5.0),
                TTRHBuilder = cms.string('WithTrackAngle'),
                forceKinematicWithRegionDirection = cms.bool(False),
                magneticField = cms.string('ParabolicMf'),
                propagator = cms.string('PropagatorWithMaterialParabolicMf')
            )
        )
    )
    
    setattr(process,"globalPixelLessSeeds"+str(layers),process.globalPixelLessSeeds.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(5000),
                MaxNumberOfPixelClusters = cms.uint32(40000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
                doClusterCheck = cms.bool(False)
            ),
            OrderedHitsFactoryPSet = cms.PSet(
                ComponentName = cms.string('StandardHitPairGenerator'),
                SeedingLayers = cms.InputTag("pixelLessLayerPairs4PixelLessTracking"),
                maxElement = cms.uint32(100000)
            ),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
                RegionPSet = cms.PSet(
                    beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                    originHalfLength = cms.double(40),
                    originRadius = cms.double(0.2),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.9),
                    useMultipleScattering = cms.bool(False)
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
                MinOneOverPtError = cms.double(1.0),
                OriginTransverseErrorMultiplier = cms.double(1.0),
                SeedMomentumForBOFF = cms.double(5.0),
                TTRHBuilder = cms.string('WithTrackAngle'),
                forceKinematicWithRegionDirection = cms.bool(False),
                magneticField = cms.string('ParabolicMf'),
                propagator = cms.string('PropagatorWithMaterialParabolicMf')
            )
        )
    )
    
    setattr(process,"globalPixelSeeds"+str(layers),process.globalPixelSeeds.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(400000),
                MaxNumberOfPixelClusters = cms.uint32(40000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
                doClusterCheck = cms.bool(False)
            ),
            OrderedHitsFactoryPSet = cms.PSet(
                ComponentName = cms.string('StandardHitPairGenerator'),
                SeedingLayers = cms.InputTag("PixelLayerPairs")
            ),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
                RegionPSet = cms.PSet(
                    beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                    originHalfLength = cms.double(21.2),
                    originRadius = cms.double(0.2),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.9),
                    useMultipleScattering = cms.bool(False)
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
                MinOneOverPtError = cms.double(1.0),
                OriginTransverseErrorMultiplier = cms.double(1.0),
                SeedMomentumForBOFF = cms.double(5.0),
                TTRHBuilder = cms.string('WithTrackAngle'),
                forceKinematicWithRegionDirection = cms.bool(False),
                magneticField = cms.string('ParabolicMf'),
                propagator = cms.string('PropagatorWithMaterialParabolicMf')
            )
        )
    )
    
    setattr(process,"globalSeedsFromPairsWithVertices"+str(layers),process.globalSeedsFromPairsWithVertices.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(400000),
                MaxNumberOfPixelClusters = cms.uint32(40000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
                doClusterCheck = cms.bool(False)
            ),
            OrderedHitsFactoryPSet = cms.PSet(
                ComponentName = cms.string('StandardHitPairGenerator'),
                SeedingLayers = cms.InputTag("MixedLayerPairs"),
                maxElement = cms.uint32(1000000)
            ),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalTrackingRegionWithVerticesProducer'),
                RegionPSet = cms.PSet(
                    VertexCollection = cms.InputTag("firstStepPrimaryVertices"+str(layers)),
                    beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                    fixedError = cms.double(0.2),
                    halfLengthScaling4BigEvts = cms.bool(False),
                    maxNVertices = cms.int32(-1),
                    maxPtMin = cms.double(1000),
                    minHalfLength = cms.double(0),
                    minOriginR = cms.double(0),
                    nSigmaZ = cms.double(4),
                    originRScaling4BigEvts = cms.bool(False),
                    originRadius = cms.double(0.2),
                    pixelClustersForScaling = cms.InputTag(myCollection),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.9),
                    ptMinScaling4BigEvts = cms.bool(False),
                    scalingEndNPix = cms.double(1),
                    scalingStartNPix = cms.double(0),
                    sigmaZVertex = cms.double(3),
                    useFakeVertices = cms.bool(False),
                    useFixedError = cms.bool(True),
                    useFoundVertices = cms.bool(True),
                    useMultipleScattering = cms.bool(False)
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
                MinOneOverPtError = cms.double(1.0),
                OriginTransverseErrorMultiplier = cms.double(1.0),
                SeedMomentumForBOFF = cms.double(5.0),
                TTRHBuilder = cms.string('WithTrackAngle'),
                forceKinematicWithRegionDirection = cms.bool(False),
                magneticField = cms.string('ParabolicMf'),
                propagator = cms.string('PropagatorWithMaterialParabolicMf')
            )
        )
    )
    
    setattr(process,"globalSeedsFromTriplets"+str(layers),process.globalSeedsFromTriplets.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(400000),
                MaxNumberOfPixelClusters = cms.uint32(40000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
                doClusterCheck = cms.bool(False)
            ),
            OrderedHitsFactoryPSet = cms.PSet(
                ComponentName = cms.string('StandardHitTripletGenerator'),
                GeneratorPSet = cms.PSet(
                    ComponentName = cms.string('PixelTripletHLTGenerator'),
                    SeedComparitorPSet = cms.PSet(
                        ComponentName = cms.string('none')
                    ),
                    extraHitRPhitolerance = cms.double(0.032),
                    extraHitRZtolerance = cms.double(0.037),
                    maxElement = cms.uint32(1000000),
                    phiPreFiltering = cms.double(0.3),
                    useBending = cms.bool(True),
                    useFixedPreFiltering = cms.bool(False),
                    useMultScattering = cms.bool(True)
                ),
                SeedingLayers = cms.InputTag("PixelLayerTriplets"),
                maxElement = cms.uint32(1000000)
            ),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
                RegionPSet = cms.PSet(
                    beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                    originHalfLength = cms.double(21.2),
                    originRadius = cms.double(0.2),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.9),
                    useMultipleScattering = cms.bool(False)
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
                MinOneOverPtError = cms.double(1.0),
                OriginTransverseErrorMultiplier = cms.double(1.0),
                SeedMomentumForBOFF = cms.double(5.0),
                TTRHBuilder = cms.string('WithTrackAngle'),
                forceKinematicWithRegionDirection = cms.bool(False),
                magneticField = cms.string('ParabolicMf'),
                propagator = cms.string('PropagatorWithMaterialParabolicMf')
            )
        )
    )
    
    setattr(process,"globalTrackingRegionWithVertices"+str(layers),process.globalTrackingRegionWithVertices.clone(
            RegionPSet = cms.PSet(
                VertexCollection = cms.InputTag("firstStepPrimaryVertices"+str(layers)),
                beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                fixedError = cms.double(0.2),
                halfLengthScaling4BigEvts = cms.bool(False),
                maxNVertices = cms.int32(-1),
                maxPtMin = cms.double(1000),
                minHalfLength = cms.double(0),
                minOriginR = cms.double(0),
                nSigmaZ = cms.double(4),
                originRScaling4BigEvts = cms.bool(False),
                originRadius = cms.double(0.2),
                pixelClustersForScaling = cms.InputTag(myCollection),
                precise = cms.bool(True),
                ptMin = cms.double(0.9),
                ptMinScaling4BigEvts = cms.bool(False),
                scalingEndNPix = cms.double(1),
                scalingStartNPix = cms.double(0),
                sigmaZVertex = cms.double(3),
                useFakeVertices = cms.bool(False),
                useFixedError = cms.bool(True),
                useFoundVertices = cms.bool(True),
                useMultipleScattering = cms.bool(False)
            ),
            mightGet = cms.optional.untracked.vstring
        )
    )
    
    setattr(process,"highPtTripletStepSeedClusterMask"+str(layers),process.highPtTripletStepSeedClusterMask.clone(
            Common = cms.PSet(
                maxChi2 = cms.double(9.0)
            ),
            oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"+str(layers)),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("highPtTripletStepSeeds"+str(layers))
        )
    )
    
    setattr(process,"photonConvTrajSeedFromQuadruplets"+str(layers),process.photonConvTrajSeedFromQuadruplets.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(50000),
                MaxNumberOfPixelClusters = cms.uint32(10000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                doClusterCheck = cms.bool(True)
            ),
            DoxcheckSeedCandidates = cms.bool(False),
            OrderedHitsFactoryPSet = cms.PSet(
                SeedingLayers = cms.InputTag("conv2LayerPairs"),
                maxElement = cms.uint32(900000)
            ),
            QuadCutPSet = cms.PSet(
                Cut_BeamPipeRadius = cms.double(3.0),
                Cut_DeltaRho = cms.double(12.0),
                Cut_maxLegPt = cms.double(10.0),
                Cut_minLegPt = cms.double(0.6),
                Cut_zCA = cms.double(100),
                apply_Arbitration = cms.bool(True),
                apply_ClusterShapeFilter = cms.bool(True),
                apply_DeltaPhiCuts = cms.bool(True),
                apply_zCACut = cms.bool(False),
                rejectAllQuads = cms.bool(False)
            ),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
                RegionPSet = cms.PSet(
                    beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                    originHalfLength = cms.double(12.0),
                    originRadius = cms.double(3.0),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.2)
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"+str(layers)),
                ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('SeedForPhotonConversionFromQuadruplets'),
                SeedMomentumForBOFF = cms.double(5.0),
                propagator = cms.string('PropagatorWithMaterial')
            ),
            TrackRefitter = cms.InputTag("generalTracks"+str(layers)),
            beamSpotInputTag = cms.InputTag("offlineBeamSpot"+str(layers)),
            newSeedCandidates = cms.string('conv2SeedCandidates'),
            primaryVerticesTag = cms.InputTag("pixelVertices"),
            xcheckSeedCandidates = cms.string('xcheckSeedCandidates')
        )
    )
    
    setattr(process,"pixelClusterTagInfos"+str(layers),process.pixelClusterTagInfos.clone(
            addForward = cms.bool(True),
            hadronMass = cms.double(12.0),
            isPhase1 = cms.bool(True),
            jets = cms.InputTag("ak4PFJetsCHS"),
            maxJetEtaCut = cms.double(2.5),
            minAdcCount = cms.int32(-1),
            minJetPtCut = cms.double(100.0),
            pixelhit = cms.InputTag(myCollection),
            vertices = cms.InputTag("offlinePrimaryVertices"+str(layers))
        )
    )
    
    setattr(process,"regionalCosmicTrackerSeeds"+str(layers),process.regionalCosmicTrackerSeeds.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(10000),
                MaxNumberOfPixelClusters = cms.uint32(10000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                doClusterCheck = cms.bool(False)
            ),
            OrderedHitsFactoryPSet = cms.PSet(
                ComponentName = cms.string('GenericPairGenerator'),
                LayerSrc = cms.InputTag("regionalCosmicTrackerSeedingLayers")
            ),
            RegionFactoryPSet = cms.PSet(
                CollectionsPSet = cms.PSet(
                    recoL2MuonsCollection = cms.InputTag(""),
                    recoMuonsCollection = cms.InputTag(""),
                    recoTrackMuonsCollection = cms.InputTag("cosmicMuons")
                ),
                ComponentName = cms.string('CosmicRegionalSeedGenerator'),
                RegionInJetsCheckPSet = cms.PSet(
                    deltaRExclusionSize = cms.double(0.3),
                    doJetsExclusionCheck = cms.bool(True),
                    jetsPtMin = cms.double(5),
                    recoCaloJetsCollection = cms.InputTag("ak4CaloJets")
                ),
                RegionPSet = cms.PSet(
                    deltaEtaRegion = cms.double(0.1),
                    deltaPhiRegion = cms.double(0.1),
                    measurementTrackerName = cms.string(''),
                    precise = cms.bool(True),
                    ptMin = cms.double(1.0),
                    rVertex = cms.double(5),
                    zVertex = cms.double(5)
                ),
                ToolsPSet = cms.PSet(
                    regionBase = cms.string('seedOnCosmicMuon'),
                    thePropagatorName = cms.string('AnalyticalPropagator')
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('CosmicSeedCreator'),
                MinOneOverPtError = cms.double(1.0),
                OriginTransverseErrorMultiplier = cms.double(1.0),
                SeedMomentumForBOFF = cms.double(5.0),
                TTRHBuilder = cms.string('WithTrackAngle'),
                forceKinematicWithRegionDirection = cms.bool(False),
                magneticField = cms.string('ParabolicMf'),
                maxseeds = cms.int32(10000),
                propagator = cms.string('PropagatorWithMaterialParabolicMf')
            )
        )
    )
    
    setattr(process,"seedClusterRemover"+str(layers),process.seedClusterRemover.clone(
            Common = cms.PSet(
                maxChi2 = cms.double(9.0)
            ),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("initialStepSeeds"+str(layers))
        )
    )
    
    
    setattr(process,"seedClusterRemoverPhase2"+str(layers),process.seedClusterRemoverPhase2.clone(
            phase2OTClusters = cms.InputTag("siPhase2Clusters"),
            pixelClusters = cms.InputTag(myCollection),
            trajectories = cms.InputTag("initialStepSeeds"+str(layers))
        )
    )
    
    setattr(process,"seedGeneratorFromRegionHitsEDProducer"+str(layers),process.seedGeneratorFromRegionHitsEDProducer.clone(
            ClusterCheckPSet = cms.PSet(
                ClusterCollectionLabel = cms.InputTag(myCollection),
                MaxNumberOfCosmicClusters = cms.uint32(400000),
                MaxNumberOfPixelClusters = cms.uint32(40000),
                PixelClusterCollectionLabel = cms.InputTag(myCollection),
                cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
                doClusterCheck = cms.bool(False)
            ),
            OrderedHitsFactoryPSet = cms.PSet(
                ComponentName = cms.string(''),
                SeedingLayers = cms.InputTag(""),
                maxElement = cms.uint32(1000000)
            ),
            RegionFactoryPSet = cms.PSet(
                ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
                RegionPSet = cms.PSet(
                    beamSpot = cms.InputTag("offlineBeamSpot"+str(layers)),
                    originHalfLength = cms.double(21.2),
                    originRadius = cms.double(0.2),
                    precise = cms.bool(True),
                    ptMin = cms.double(0.9),
                    useMultipleScattering = cms.bool(False)
                )
            ),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            SeedCreatorPSet = cms.PSet(
                ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
                MinOneOverPtError = cms.double(1.0),
                OriginTransverseErrorMultiplier = cms.double(1.0),
                SeedMomentumForBOFF = cms.double(5.0),
                TTRHBuilder = cms.string('WithTrackAngle'),
                forceKinematicWithRegionDirection = cms.bool(False),
                magneticField = cms.string('ParabolicMf'),
                propagator = cms.string('PropagatorWithMaterialParabolicMf')
            )
        )
    )
    
    setattr(process,"tpClusterProducer"+str(layers),process.tpClusterProducer.clone(
            mightGet = cms.optional.untracked.vstring,
            phase2OTClusterSrc = cms.InputTag("siPhase2Clusters"),
            phase2OTSimLinkSrc = cms.InputTag("simSiPixelDigis","Tracker"),
            pixelClusterSrc = cms.InputTag(myCollection),
            pixelSimLinkSrc = cms.InputTag("simSiPixelDigis"),
            simTrackSrc = cms.InputTag("g4SimHits"),
            stripClusterSrc = cms.InputTag(myCollection),
            stripSimLinkSrc = cms.InputTag("simSiStripDigis"),
            throwOnMissingCollections = cms.bool(True),
            trackingParticleSrc = cms.InputTag("mix","MergedTrackTruth")
        )
    )
    
    setattr(process,"trackClusterRemover"+str(layers),process.trackClusterRemover.clone(
            TrackQuality = cms.string('highPurity'),
            maxChi2 = cms.double(30),
            mightGet = cms.optional.untracked.vstring,
            minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
            oldClusterRemovalInfo = cms.InputTag(""),
            overrideTrkQuals = cms.InputTag(""),
            pixelClusters = cms.InputTag(myCollection),
            stripClusters = cms.InputTag(myCollection),
            trackClassifier = cms.InputTag("","QualityMasks"),
            trajectories = cms.InputTag("")
        )
    )

def shortTrackTask(process):

    process.reconstruction_trackingOnly_3layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.siPixelClusterShapeCachePreSplitting,process.siPixelClusterShapeCachePreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.hbhereco,process.hbhereco3)
    process.reconstruction_trackingOnly_3layers.replace(process.offlineBeamSpot,process.offlineBeamSpot3)
    process.reconstruction_trackingOnly_3layers.replace(process.displacedMuonSeeds,process.displacedMuonSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.displacedStandAloneMuons,process.displacedStandAloneMuons3)
    process.reconstruction_trackingOnly_3layers.replace(process.refittedStandAloneMuons,process.refittedStandAloneMuons3)
    process.reconstruction_trackingOnly_3layers.replace(process.standAloneMuons,process.standAloneMuons3)
    process.reconstruction_trackingOnly_3layers.replace(process.trackExtrapolator,process.trackExtrapolator3)
    process.reconstruction_trackingOnly_3layers.replace(process.generalV0Candidates,process.generalV0Candidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices3)
    process.reconstruction_trackingOnly_3layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS3)
    process.reconstruction_trackingOnly_3layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting3)
    process.reconstruction_trackingOnly_3layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting3)
    process.reconstruction_trackingOnly_3layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices3)
    process.reconstruction_trackingOnly_3layers.replace(process.ancientMuonSeed,process.ancientMuonSeed3)
    process.reconstruction_trackingOnly_3layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk3)
    process.reconstruction_trackingOnly_3layers.replace(process.caloTowerForTrk,process.caloTowerForTrk3)
    process.reconstruction_trackingOnly_3layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices3)
    process.reconstruction_trackingOnly_3layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder3)
    process.reconstruction_trackingOnly_3layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator3)
    process.reconstruction_trackingOnly_3layers.replace(process.vertexMerger,process.vertexMerger3)
    process.reconstruction_trackingOnly_3layers.replace(process.dedxHarmonic2,process.dedxHarmonic23)
    process.reconstruction_trackingOnly_3layers.replace(process.dedxHitInfo,process.dedxHitInfo3)
    process.reconstruction_trackingOnly_3layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0853)
    process.reconstruction_trackingOnly_3layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic23)
    process.reconstruction_trackingOnly_3layers.replace(process.dedxTruncated40,process.dedxTruncated403)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask3)
    process.reconstruction_trackingOnly_3layers.replace(process.newCombinedSeeds,process.newCombinedSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.stripPairElectronTrackingRegions,process.stripPairElectronTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask3)
    process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets3)
    process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.tripletElectronTrackingRegions,process.tripletElectronTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.conversionStepTracks,process.conversionStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.trackdnn_source,process.trackdnn_source3)
    process.reconstruction_trackingOnly_3layers.replace(process.trackerClusterCheck,process.trackerClusterCheck3)
    process.reconstruction_trackingOnly_3layers.replace(process.convClusters,process.convClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.convLayerPairs,process.convLayerPairs3)
    process.reconstruction_trackingOnly_3layers.replace(process.convStepSelector,process.convStepSelector3)
    process.reconstruction_trackingOnly_3layers.replace(process.convStepTracks,process.convStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.convTrackCandidates,process.convTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg3)
    process.reconstruction_trackingOnly_3layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent3)
    process.reconstruction_trackingOnly_3layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.caloTowerForTrkPreSplitting,process.caloTowerForTrkPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeedLayersPreSplitting,process.initialStepSeedLayersPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackingRegionsPreSplitting,process.initialStepTrackingRegionsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.mkFitSiPixelHitsPreSplitting,process.mkFitSiPixelHitsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache3)
    process.reconstruction_trackingOnly_3layers.replace(process.siPixelClusters,process.siPixelClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.siPixelRecHits,process.siPixelRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier3)
    process.reconstruction_trackingOnly_3layers.replace(process.generalTracks,process.generalTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.earlyMuons,process.earlyMuons3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStep,process.detachedQuadStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTrackingRegions,process.detachedQuadStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStep,process.detachedTripletStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier13)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier23)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTrackingRegions,process.detachedTripletStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStep,process.highPtTripletStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTrackingRegions,process.highPtTripletStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices3)
    process.reconstruction_trackingOnly_3layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStep,process.initialStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepClassifier1,process.initialStepClassifier13)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepSeeds,process.initialStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTrackingRegions,process.initialStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.initialStepTracks,process.initialStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStep,process.lowPtQuadStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepTrackingRegions,process.lowPtQuadStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStep,process.lowPtTripletStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepTrackingRegions,process.lowPtTripletStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStep,process.mixedTripletStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier13)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier23)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepTrackingRegionsA,process.mixedTripletStepTrackingRegionsA3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepTrackingRegionsB,process.mixedTripletStepTrackingRegionsB3)
    process.reconstruction_trackingOnly_3layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStep,process.pixelLessStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier13)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier23)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTrackingRegions,process.pixelLessStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStep,process.pixelPairStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB3)
    process.reconstruction_trackingOnly_3layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStep,process.tobTecStep3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier13)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier23)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepClusters,process.tobTecStepClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepTrackingRegionsPair,process.tobTecStepTrackingRegionsPair3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepTrackingRegionsTripl,process.tobTecStepTrackingRegionsTripl3)
    process.reconstruction_trackingOnly_3layers.replace(process.tobTecStepTracks,process.tobTecStepTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier3)
    process.reconstruction_trackingOnly_3layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut3)
    process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut3)
    process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut3)
    process.reconstruction_trackingOnly_3layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn3)
    process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn3)
    process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn3)
    process.reconstruction_trackingOnly_3layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier3)
#    process.reconstruction_trackingOnly_3layers.replace(process.bunchSpacingProducer,process.bunchSpacingProducer3)
    process.reconstruction_trackingOnly_3layers.replace(process.rpcRecHits,process.rpcRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.ctppsLocalTrackLiteProducer,process.ctppsLocalTrackLiteProducer3)
    process.reconstruction_trackingOnly_3layers.replace(process.ctppsProtons,process.ctppsProtons3)
    process.reconstruction_trackingOnly_3layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer3)
    process.reconstruction_trackingOnly_3layers.replace(process.hfprereco,process.hfprereco3)
    process.reconstruction_trackingOnly_3layers.replace(process.hfreco,process.hfreco3)
    process.reconstruction_trackingOnly_3layers.replace(process.horeco,process.horeco3)
    process.reconstruction_trackingOnly_3layers.replace(process.zdcreco,process.zdcreco3)
    process.reconstruction_trackingOnly_3layers.replace(process.csc2DRecHits,process.csc2DRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.cscSegments,process.cscSegments3)
    process.reconstruction_trackingOnly_3layers.replace(process.dt1DCosmicRecHits,process.dt1DCosmicRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.dt1DRecHits,process.dt1DRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.dt4DCosmicSegments,process.dt4DCosmicSegments3)
    process.reconstruction_trackingOnly_3layers.replace(process.dt4DSegments,process.dt4DSegments3)
    process.reconstruction_trackingOnly_3layers.replace(process.gemRecHits,process.gemRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.gemSegments,process.gemSegments3)
    process.reconstruction_trackingOnly_3layers.replace(process.ctppsDiamondLocalTracks,process.ctppsDiamondLocalTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.ctppsDiamondRecHits,process.ctppsDiamondRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.ctppsPixelClusters,process.ctppsPixelClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.ctppsPixelLocalTracks,process.ctppsPixelLocalTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.ctppsPixelRecHits,process.ctppsPixelRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.diamondSampicLocalTracks,process.diamondSampicLocalTracks3)
    process.reconstruction_trackingOnly_3layers.replace(process.totemTimingRecHits,process.totemTimingRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.totemRPClusterProducer,process.totemRPClusterProducer3)
    process.reconstruction_trackingOnly_3layers.replace(process.totemRPLocalTrackFitter,process.totemRPLocalTrackFitter3)
    process.reconstruction_trackingOnly_3layers.replace(process.totemRPRecHitProducer,process.totemRPRecHitProducer3)
    process.reconstruction_trackingOnly_3layers.replace(process.totemRPUVPatternFinder,process.totemRPUVPatternFinder3)
    process.reconstruction_trackingOnly_3layers.replace(process.siStripClusters,process.siStripClusters3)
    process.reconstruction_trackingOnly_3layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits3)
    process.reconstruction_trackingOnly_3layers.replace(process.siStripZeroSuppression,process.siStripZeroSuppression3)
    process.reconstruction_trackingOnly_3layers.replace(process.ecalCompactTrigPrim,process.ecalCompactTrigPrim3)
    process.reconstruction_trackingOnly_3layers.replace(process.ecalTPSkim,process.ecalTPSkim3)
    process.reconstruction_trackingOnly_3layers.replace(process.ecalDetIdToBeRecovered,process.ecalDetIdToBeRecovered3)
    process.reconstruction_trackingOnly_3layers.replace(process.siPixelClustersPreSplitting,process.siPixelClustersPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.siPixelRecHitsPreSplitting,process.siPixelRecHitsPreSplitting3)
    process.reconstruction_trackingOnly_3layers.replace(process.ecalPreshowerRecHit,process.ecalPreshowerRecHit3)
    process.reconstruction_trackingOnly_3layers.replace(process.ecalMultiFitUncalibRecHit,process.ecalMultiFitUncalibRecHit3)
    process.reconstruction_trackingOnly_3layers.replace(process.ecalRecHit,process.ecalRecHit3)
    
    ############################################################################################################################################################################################
    
    process.reconstruction_trackingOnly_4layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.siPixelClusterShapeCachePreSplitting,process.siPixelClusterShapeCachePreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.hbhereco,process.hbhereco4)
    process.reconstruction_trackingOnly_4layers.replace(process.offlineBeamSpot,process.offlineBeamSpot4)
    process.reconstruction_trackingOnly_4layers.replace(process.displacedMuonSeeds,process.displacedMuonSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.displacedStandAloneMuons,process.displacedStandAloneMuons4)
    process.reconstruction_trackingOnly_4layers.replace(process.refittedStandAloneMuons,process.refittedStandAloneMuons4)
    process.reconstruction_trackingOnly_4layers.replace(process.standAloneMuons,process.standAloneMuons4)
    process.reconstruction_trackingOnly_4layers.replace(process.trackExtrapolator,process.trackExtrapolator4)
    process.reconstruction_trackingOnly_4layers.replace(process.generalV0Candidates,process.generalV0Candidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices4)
    process.reconstruction_trackingOnly_4layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS4)
    process.reconstruction_trackingOnly_4layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting4)
    process.reconstruction_trackingOnly_4layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting4)
    process.reconstruction_trackingOnly_4layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices4)
    process.reconstruction_trackingOnly_4layers.replace(process.ancientMuonSeed,process.ancientMuonSeed4)
    process.reconstruction_trackingOnly_4layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk4)
    process.reconstruction_trackingOnly_4layers.replace(process.caloTowerForTrk,process.caloTowerForTrk4)
    process.reconstruction_trackingOnly_4layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices4)
    process.reconstruction_trackingOnly_4layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder4)
    process.reconstruction_trackingOnly_4layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator4)
    process.reconstruction_trackingOnly_4layers.replace(process.vertexMerger,process.vertexMerger4)
    process.reconstruction_trackingOnly_4layers.replace(process.dedxHarmonic2,process.dedxHarmonic24)
    process.reconstruction_trackingOnly_4layers.replace(process.dedxHitInfo,process.dedxHitInfo4)
    process.reconstruction_trackingOnly_4layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0854)
    process.reconstruction_trackingOnly_4layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic24)
    process.reconstruction_trackingOnly_4layers.replace(process.dedxTruncated40,process.dedxTruncated404)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask4)
    process.reconstruction_trackingOnly_4layers.replace(process.newCombinedSeeds,process.newCombinedSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.stripPairElectronTrackingRegions,process.stripPairElectronTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask4)
    process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets4)
    process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.tripletElectronTrackingRegions,process.tripletElectronTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.conversionStepTracks,process.conversionStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.trackdnn_source,process.trackdnn_source4)
    process.reconstruction_trackingOnly_4layers.replace(process.trackerClusterCheck,process.trackerClusterCheck4)
    process.reconstruction_trackingOnly_4layers.replace(process.convClusters,process.convClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.convLayerPairs,process.convLayerPairs4)
    process.reconstruction_trackingOnly_4layers.replace(process.convStepSelector,process.convStepSelector4)
    process.reconstruction_trackingOnly_4layers.replace(process.convStepTracks,process.convStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.convTrackCandidates,process.convTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg4)
    process.reconstruction_trackingOnly_4layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent4)
    process.reconstruction_trackingOnly_4layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.caloTowerForTrkPreSplitting,process.caloTowerForTrkPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeedLayersPreSplitting,process.initialStepSeedLayersPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackingRegionsPreSplitting,process.initialStepTrackingRegionsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.mkFitSiPixelHitsPreSplitting,process.mkFitSiPixelHitsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache4)
    process.reconstruction_trackingOnly_4layers.replace(process.siPixelClusters,process.siPixelClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.siPixelRecHits,process.siPixelRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier4)
    process.reconstruction_trackingOnly_4layers.replace(process.generalTracks,process.generalTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.earlyMuons,process.earlyMuons4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStep,process.detachedQuadStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTrackingRegions,process.detachedQuadStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStep,process.detachedTripletStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier14)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier24)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTrackingRegions,process.detachedTripletStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStep,process.highPtTripletStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTrackingRegions,process.highPtTripletStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices4)
    process.reconstruction_trackingOnly_4layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStep,process.initialStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepClassifier1,process.initialStepClassifier14)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepSeeds,process.initialStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTrackingRegions,process.initialStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.initialStepTracks,process.initialStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStep,process.lowPtQuadStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepTrackingRegions,process.lowPtQuadStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStep,process.lowPtTripletStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepTrackingRegions,process.lowPtTripletStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStep,process.mixedTripletStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier14)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier24)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepTrackingRegionsA,process.mixedTripletStepTrackingRegionsA4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepTrackingRegionsB,process.mixedTripletStepTrackingRegionsB4)
    process.reconstruction_trackingOnly_4layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStep,process.pixelLessStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier14)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier24)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTrackingRegions,process.pixelLessStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStep,process.pixelPairStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB4)
    process.reconstruction_trackingOnly_4layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStep,process.tobTecStep4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier14)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier24)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepClusters,process.tobTecStepClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepTrackingRegionsPair,process.tobTecStepTrackingRegionsPair4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepTrackingRegionsTripl,process.tobTecStepTrackingRegionsTripl4)
    process.reconstruction_trackingOnly_4layers.replace(process.tobTecStepTracks,process.tobTecStepTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier4)
    process.reconstruction_trackingOnly_4layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut4)
    process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut4)
    process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut4)
    process.reconstruction_trackingOnly_4layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn4)
    process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn4)
    process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn4)
    process.reconstruction_trackingOnly_4layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier4)
#    process.reconstruction_trackingOnly_4layers.replace(process.bunchSpacingProducer,process.bunchSpacingProducer4)
    process.reconstruction_trackingOnly_4layers.replace(process.rpcRecHits,process.rpcRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.ctppsLocalTrackLiteProducer,process.ctppsLocalTrackLiteProducer4)
    process.reconstruction_trackingOnly_4layers.replace(process.ctppsProtons,process.ctppsProtons4)
    process.reconstruction_trackingOnly_4layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer4)
    process.reconstruction_trackingOnly_4layers.replace(process.hfprereco,process.hfprereco4)
    process.reconstruction_trackingOnly_4layers.replace(process.hfreco,process.hfreco4)
    process.reconstruction_trackingOnly_4layers.replace(process.horeco,process.horeco4)
    process.reconstruction_trackingOnly_4layers.replace(process.zdcreco,process.zdcreco4)
    process.reconstruction_trackingOnly_4layers.replace(process.csc2DRecHits,process.csc2DRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.cscSegments,process.cscSegments4)
    process.reconstruction_trackingOnly_4layers.replace(process.dt1DCosmicRecHits,process.dt1DCosmicRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.dt1DRecHits,process.dt1DRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.dt4DCosmicSegments,process.dt4DCosmicSegments4)
    process.reconstruction_trackingOnly_4layers.replace(process.dt4DSegments,process.dt4DSegments4)
    process.reconstruction_trackingOnly_4layers.replace(process.gemRecHits,process.gemRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.gemSegments,process.gemSegments4)
    process.reconstruction_trackingOnly_4layers.replace(process.ctppsDiamondLocalTracks,process.ctppsDiamondLocalTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.ctppsDiamondRecHits,process.ctppsDiamondRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.ctppsPixelClusters,process.ctppsPixelClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.ctppsPixelLocalTracks,process.ctppsPixelLocalTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.ctppsPixelRecHits,process.ctppsPixelRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.diamondSampicLocalTracks,process.diamondSampicLocalTracks4)
    process.reconstruction_trackingOnly_4layers.replace(process.totemTimingRecHits,process.totemTimingRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.totemRPClusterProducer,process.totemRPClusterProducer4)
    process.reconstruction_trackingOnly_4layers.replace(process.totemRPLocalTrackFitter,process.totemRPLocalTrackFitter4)
    process.reconstruction_trackingOnly_4layers.replace(process.totemRPRecHitProducer,process.totemRPRecHitProducer4)
    process.reconstruction_trackingOnly_4layers.replace(process.totemRPUVPatternFinder,process.totemRPUVPatternFinder4)
    process.reconstruction_trackingOnly_4layers.replace(process.siStripClusters,process.siStripClusters4)
    process.reconstruction_trackingOnly_4layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits4)
    process.reconstruction_trackingOnly_4layers.replace(process.siStripZeroSuppression,process.siStripZeroSuppression4)
    process.reconstruction_trackingOnly_4layers.replace(process.ecalCompactTrigPrim,process.ecalCompactTrigPrim4)
    process.reconstruction_trackingOnly_4layers.replace(process.ecalTPSkim,process.ecalTPSkim4)
    process.reconstruction_trackingOnly_4layers.replace(process.ecalDetIdToBeRecovered,process.ecalDetIdToBeRecovered4)
    process.reconstruction_trackingOnly_4layers.replace(process.siPixelClustersPreSplitting,process.siPixelClustersPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.siPixelRecHitsPreSplitting,process.siPixelRecHitsPreSplitting4)
    process.reconstruction_trackingOnly_4layers.replace(process.ecalPreshowerRecHit,process.ecalPreshowerRecHit4)
    process.reconstruction_trackingOnly_4layers.replace(process.ecalMultiFitUncalibRecHit,process.ecalMultiFitUncalibRecHit4)
    process.reconstruction_trackingOnly_4layers.replace(process.ecalRecHit,process.ecalRecHit4)
    
    ############################################################################################################################################################################################
    
    process.reconstruction_trackingOnly_5layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.siPixelClusterShapeCachePreSplitting,process.siPixelClusterShapeCachePreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.hbhereco,process.hbhereco5)
    process.reconstruction_trackingOnly_5layers.replace(process.offlineBeamSpot,process.offlineBeamSpot5)
    process.reconstruction_trackingOnly_5layers.replace(process.displacedMuonSeeds,process.displacedMuonSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.displacedStandAloneMuons,process.displacedStandAloneMuons5)
    process.reconstruction_trackingOnly_5layers.replace(process.refittedStandAloneMuons,process.refittedStandAloneMuons5)
    process.reconstruction_trackingOnly_5layers.replace(process.standAloneMuons,process.standAloneMuons5)
    process.reconstruction_trackingOnly_5layers.replace(process.trackExtrapolator,process.trackExtrapolator5)
    process.reconstruction_trackingOnly_5layers.replace(process.generalV0Candidates,process.generalV0Candidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices5)
    process.reconstruction_trackingOnly_5layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS5)
    process.reconstruction_trackingOnly_5layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting5)
    process.reconstruction_trackingOnly_5layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting5)
    process.reconstruction_trackingOnly_5layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices5)
    process.reconstruction_trackingOnly_5layers.replace(process.ancientMuonSeed,process.ancientMuonSeed5)
    process.reconstruction_trackingOnly_5layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk5)
    process.reconstruction_trackingOnly_5layers.replace(process.caloTowerForTrk,process.caloTowerForTrk5)
    process.reconstruction_trackingOnly_5layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices5)
    process.reconstruction_trackingOnly_5layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder5)
    process.reconstruction_trackingOnly_5layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator5)
    process.reconstruction_trackingOnly_5layers.replace(process.vertexMerger,process.vertexMerger5)
    process.reconstruction_trackingOnly_5layers.replace(process.dedxHarmonic2,process.dedxHarmonic25)
    process.reconstruction_trackingOnly_5layers.replace(process.dedxHitInfo,process.dedxHitInfo5)
    process.reconstruction_trackingOnly_5layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0855)
    process.reconstruction_trackingOnly_5layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic25)
    process.reconstruction_trackingOnly_5layers.replace(process.dedxTruncated40,process.dedxTruncated405)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask5)
    process.reconstruction_trackingOnly_5layers.replace(process.newCombinedSeeds,process.newCombinedSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.stripPairElectronTrackingRegions,process.stripPairElectronTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask5)
    process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets5)
    process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.tripletElectronTrackingRegions,process.tripletElectronTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.conversionStepTracks,process.conversionStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.trackdnn_source,process.trackdnn_source5)
    process.reconstruction_trackingOnly_5layers.replace(process.trackerClusterCheck,process.trackerClusterCheck5)
    process.reconstruction_trackingOnly_5layers.replace(process.convClusters,process.convClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.convLayerPairs,process.convLayerPairs5)
    process.reconstruction_trackingOnly_5layers.replace(process.convStepSelector,process.convStepSelector5)
    process.reconstruction_trackingOnly_5layers.replace(process.convStepTracks,process.convStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.convTrackCandidates,process.convTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg5)
    process.reconstruction_trackingOnly_5layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent5)
    process.reconstruction_trackingOnly_5layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.caloTowerForTrkPreSplitting,process.caloTowerForTrkPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeedLayersPreSplitting,process.initialStepSeedLayersPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackingRegionsPreSplitting,process.initialStepTrackingRegionsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.mkFitSiPixelHitsPreSplitting,process.mkFitSiPixelHitsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache5)
    process.reconstruction_trackingOnly_5layers.replace(process.siPixelClusters,process.siPixelClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.siPixelRecHits,process.siPixelRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier5)
    process.reconstruction_trackingOnly_5layers.replace(process.generalTracks,process.generalTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.earlyMuons,process.earlyMuons5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStep,process.detachedQuadStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTrackingRegions,process.detachedQuadStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStep,process.detachedTripletStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier15)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier25)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTrackingRegions,process.detachedTripletStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStep,process.highPtTripletStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTrackingRegions,process.highPtTripletStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices5)
    process.reconstruction_trackingOnly_5layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStep,process.initialStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepClassifier1,process.initialStepClassifier15)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepSeeds,process.initialStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTrackingRegions,process.initialStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.initialStepTracks,process.initialStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStep,process.lowPtQuadStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepTrackingRegions,process.lowPtQuadStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStep,process.lowPtTripletStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepTrackingRegions,process.lowPtTripletStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStep,process.mixedTripletStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier15)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier25)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepTrackingRegionsA,process.mixedTripletStepTrackingRegionsA5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepTrackingRegionsB,process.mixedTripletStepTrackingRegionsB5)
    process.reconstruction_trackingOnly_5layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStep,process.pixelLessStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier15)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier25)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTrackingRegions,process.pixelLessStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStep,process.pixelPairStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB5)
    process.reconstruction_trackingOnly_5layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStep,process.tobTecStep5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier15)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier25)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepClusters,process.tobTecStepClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepTrackingRegionsPair,process.tobTecStepTrackingRegionsPair5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepTrackingRegionsTripl,process.tobTecStepTrackingRegionsTripl5)
    process.reconstruction_trackingOnly_5layers.replace(process.tobTecStepTracks,process.tobTecStepTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier5)
    process.reconstruction_trackingOnly_5layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut5)
    process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut5)
    process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut5)
    process.reconstruction_trackingOnly_5layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn5)
    process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn5)
    process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn5)
    process.reconstruction_trackingOnly_5layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier5)
#    process.reconstruction_trackingOnly_5layers.replace(process.bunchSpacingProducer,process.bunchSpacingProducer5)
    process.reconstruction_trackingOnly_5layers.replace(process.rpcRecHits,process.rpcRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.ctppsLocalTrackLiteProducer,process.ctppsLocalTrackLiteProducer5)
    process.reconstruction_trackingOnly_5layers.replace(process.ctppsProtons,process.ctppsProtons5)
    process.reconstruction_trackingOnly_5layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer5)
    process.reconstruction_trackingOnly_5layers.replace(process.hfprereco,process.hfprereco5)
    process.reconstruction_trackingOnly_5layers.replace(process.hfreco,process.hfreco5)
    process.reconstruction_trackingOnly_5layers.replace(process.horeco,process.horeco5)
    process.reconstruction_trackingOnly_5layers.replace(process.zdcreco,process.zdcreco5)
    process.reconstruction_trackingOnly_5layers.replace(process.csc2DRecHits,process.csc2DRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.cscSegments,process.cscSegments5)
    process.reconstruction_trackingOnly_5layers.replace(process.dt1DCosmicRecHits,process.dt1DCosmicRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.dt1DRecHits,process.dt1DRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.dt4DCosmicSegments,process.dt4DCosmicSegments5)
    process.reconstruction_trackingOnly_5layers.replace(process.dt4DSegments,process.dt4DSegments5)
    process.reconstruction_trackingOnly_5layers.replace(process.gemRecHits,process.gemRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.gemSegments,process.gemSegments5)
    process.reconstruction_trackingOnly_5layers.replace(process.ctppsDiamondLocalTracks,process.ctppsDiamondLocalTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.ctppsDiamondRecHits,process.ctppsDiamondRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.ctppsPixelClusters,process.ctppsPixelClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.ctppsPixelLocalTracks,process.ctppsPixelLocalTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.ctppsPixelRecHits,process.ctppsPixelRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.diamondSampicLocalTracks,process.diamondSampicLocalTracks5)
    process.reconstruction_trackingOnly_5layers.replace(process.totemTimingRecHits,process.totemTimingRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.totemRPClusterProducer,process.totemRPClusterProducer5)
    process.reconstruction_trackingOnly_5layers.replace(process.totemRPLocalTrackFitter,process.totemRPLocalTrackFitter5)
    process.reconstruction_trackingOnly_5layers.replace(process.totemRPRecHitProducer,process.totemRPRecHitProducer5)
    process.reconstruction_trackingOnly_5layers.replace(process.totemRPUVPatternFinder,process.totemRPUVPatternFinder5)
    process.reconstruction_trackingOnly_5layers.replace(process.siStripClusters,process.siStripClusters5)
    process.reconstruction_trackingOnly_5layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits5)
    process.reconstruction_trackingOnly_5layers.replace(process.siStripZeroSuppression,process.siStripZeroSuppression5)
    process.reconstruction_trackingOnly_5layers.replace(process.ecalCompactTrigPrim,process.ecalCompactTrigPrim5)
    process.reconstruction_trackingOnly_5layers.replace(process.ecalTPSkim,process.ecalTPSkim5)
    process.reconstruction_trackingOnly_5layers.replace(process.ecalDetIdToBeRecovered,process.ecalDetIdToBeRecovered5)
    process.reconstruction_trackingOnly_5layers.replace(process.siPixelClustersPreSplitting,process.siPixelClustersPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.siPixelRecHitsPreSplitting,process.siPixelRecHitsPreSplitting5)
    process.reconstruction_trackingOnly_5layers.replace(process.ecalPreshowerRecHit,process.ecalPreshowerRecHit5)
    process.reconstruction_trackingOnly_5layers.replace(process.ecalMultiFitUncalibRecHit,process.ecalMultiFitUncalibRecHit5)
    process.reconstruction_trackingOnly_5layers.replace(process.ecalRecHit,process.ecalRecHit5)
    
    ############################################################################################################################################################################################
    
    process.reconstruction_trackingOnly_6layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.siPixelClusterShapeCachePreSplitting,process.siPixelClusterShapeCachePreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.hbhereco,process.hbhereco6)
    process.reconstruction_trackingOnly_6layers.replace(process.offlineBeamSpot,process.offlineBeamSpot6)
    process.reconstruction_trackingOnly_6layers.replace(process.displacedMuonSeeds,process.displacedMuonSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.displacedStandAloneMuons,process.displacedStandAloneMuons6)
    process.reconstruction_trackingOnly_6layers.replace(process.refittedStandAloneMuons,process.refittedStandAloneMuons6)
    process.reconstruction_trackingOnly_6layers.replace(process.standAloneMuons,process.standAloneMuons6)
    process.reconstruction_trackingOnly_6layers.replace(process.trackExtrapolator,process.trackExtrapolator6)
    process.reconstruction_trackingOnly_6layers.replace(process.generalV0Candidates,process.generalV0Candidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices6)
    process.reconstruction_trackingOnly_6layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS6)
    process.reconstruction_trackingOnly_6layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting6)
    process.reconstruction_trackingOnly_6layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting6)
    process.reconstruction_trackingOnly_6layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices6)
    process.reconstruction_trackingOnly_6layers.replace(process.ancientMuonSeed,process.ancientMuonSeed6)
    process.reconstruction_trackingOnly_6layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk6)
    process.reconstruction_trackingOnly_6layers.replace(process.caloTowerForTrk,process.caloTowerForTrk6)
    process.reconstruction_trackingOnly_6layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices6)
    process.reconstruction_trackingOnly_6layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder6)
    process.reconstruction_trackingOnly_6layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator6)
    process.reconstruction_trackingOnly_6layers.replace(process.vertexMerger,process.vertexMerger6)
    process.reconstruction_trackingOnly_6layers.replace(process.dedxHarmonic2,process.dedxHarmonic26)
    process.reconstruction_trackingOnly_6layers.replace(process.dedxHitInfo,process.dedxHitInfo6)
    process.reconstruction_trackingOnly_6layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0856)
    process.reconstruction_trackingOnly_6layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic26)
    process.reconstruction_trackingOnly_6layers.replace(process.dedxTruncated40,process.dedxTruncated406)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask6)
    process.reconstruction_trackingOnly_6layers.replace(process.newCombinedSeeds,process.newCombinedSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.stripPairElectronTrackingRegions,process.stripPairElectronTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask6)
    process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets6)
    process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.tripletElectronTrackingRegions,process.tripletElectronTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.conversionStepTracks,process.conversionStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.trackdnn_source,process.trackdnn_source6)
    process.reconstruction_trackingOnly_6layers.replace(process.trackerClusterCheck,process.trackerClusterCheck6)
    process.reconstruction_trackingOnly_6layers.replace(process.convClusters,process.convClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.convLayerPairs,process.convLayerPairs6)
    process.reconstruction_trackingOnly_6layers.replace(process.convStepSelector,process.convStepSelector6)
    process.reconstruction_trackingOnly_6layers.replace(process.convStepTracks,process.convStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.convTrackCandidates,process.convTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg6)
    process.reconstruction_trackingOnly_6layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent6)
    process.reconstruction_trackingOnly_6layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.caloTowerForTrkPreSplitting,process.caloTowerForTrkPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeedLayersPreSplitting,process.initialStepSeedLayersPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackingRegionsPreSplitting,process.initialStepTrackingRegionsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.mkFitSiPixelHitsPreSplitting,process.mkFitSiPixelHitsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache6)
    process.reconstruction_trackingOnly_6layers.replace(process.siPixelClusters,process.siPixelClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.siPixelRecHits,process.siPixelRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier6)
    process.reconstruction_trackingOnly_6layers.replace(process.generalTracks,process.generalTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.earlyMuons,process.earlyMuons6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStep,process.detachedQuadStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTrackingRegions,process.detachedQuadStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStep,process.detachedTripletStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier16)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier26)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTrackingRegions,process.detachedTripletStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStep,process.highPtTripletStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTrackingRegions,process.highPtTripletStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices6)
    process.reconstruction_trackingOnly_6layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStep,process.initialStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepClassifier1,process.initialStepClassifier16)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepSeeds,process.initialStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTrackingRegions,process.initialStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.initialStepTracks,process.initialStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStep,process.lowPtQuadStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepTrackingRegions,process.lowPtQuadStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStep,process.lowPtTripletStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepTrackingRegions,process.lowPtTripletStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStep,process.mixedTripletStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier16)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier26)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepTrackingRegionsA,process.mixedTripletStepTrackingRegionsA6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepTrackingRegionsB,process.mixedTripletStepTrackingRegionsB6)
    process.reconstruction_trackingOnly_6layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStep,process.pixelLessStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier16)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier26)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTrackingRegions,process.pixelLessStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStep,process.pixelPairStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB6)
    process.reconstruction_trackingOnly_6layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStep,process.tobTecStep6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier16)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier26)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepClusters,process.tobTecStepClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepTrackingRegionsPair,process.tobTecStepTrackingRegionsPair6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepTrackingRegionsTripl,process.tobTecStepTrackingRegionsTripl6)
    process.reconstruction_trackingOnly_6layers.replace(process.tobTecStepTracks,process.tobTecStepTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier6)
    process.reconstruction_trackingOnly_6layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut6)
    process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut6)
    process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut6)
    process.reconstruction_trackingOnly_6layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn6)
    process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn6)
    process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn6)
    process.reconstruction_trackingOnly_6layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier6)
#    process.reconstruction_trackingOnly_6layers.replace(process.bunchSpacingProducer,process.bunchSpacingProducer6)
    process.reconstruction_trackingOnly_6layers.replace(process.rpcRecHits,process.rpcRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.ctppsLocalTrackLiteProducer,process.ctppsLocalTrackLiteProducer6)
    process.reconstruction_trackingOnly_6layers.replace(process.ctppsProtons,process.ctppsProtons6)
    process.reconstruction_trackingOnly_6layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer6)
    process.reconstruction_trackingOnly_6layers.replace(process.hfprereco,process.hfprereco6)
    process.reconstruction_trackingOnly_6layers.replace(process.hfreco,process.hfreco6)
    process.reconstruction_trackingOnly_6layers.replace(process.horeco,process.horeco6)
    process.reconstruction_trackingOnly_6layers.replace(process.zdcreco,process.zdcreco6)
    process.reconstruction_trackingOnly_6layers.replace(process.csc2DRecHits,process.csc2DRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.cscSegments,process.cscSegments6)
    process.reconstruction_trackingOnly_6layers.replace(process.dt1DCosmicRecHits,process.dt1DCosmicRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.dt1DRecHits,process.dt1DRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.dt4DCosmicSegments,process.dt4DCosmicSegments6)
    process.reconstruction_trackingOnly_6layers.replace(process.dt4DSegments,process.dt4DSegments6)
    process.reconstruction_trackingOnly_6layers.replace(process.gemRecHits,process.gemRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.gemSegments,process.gemSegments6)
    process.reconstruction_trackingOnly_6layers.replace(process.ctppsDiamondLocalTracks,process.ctppsDiamondLocalTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.ctppsDiamondRecHits,process.ctppsDiamondRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.ctppsPixelClusters,process.ctppsPixelClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.ctppsPixelLocalTracks,process.ctppsPixelLocalTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.ctppsPixelRecHits,process.ctppsPixelRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.diamondSampicLocalTracks,process.diamondSampicLocalTracks6)
    process.reconstruction_trackingOnly_6layers.replace(process.totemTimingRecHits,process.totemTimingRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.totemRPClusterProducer,process.totemRPClusterProducer6)
    process.reconstruction_trackingOnly_6layers.replace(process.totemRPLocalTrackFitter,process.totemRPLocalTrackFitter6)
    process.reconstruction_trackingOnly_6layers.replace(process.totemRPRecHitProducer,process.totemRPRecHitProducer6)
    process.reconstruction_trackingOnly_6layers.replace(process.totemRPUVPatternFinder,process.totemRPUVPatternFinder6)
    process.reconstruction_trackingOnly_6layers.replace(process.siStripClusters,process.siStripClusters6)
    process.reconstruction_trackingOnly_6layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits6)
    process.reconstruction_trackingOnly_6layers.replace(process.siStripZeroSuppression,process.siStripZeroSuppression6)
    process.reconstruction_trackingOnly_6layers.replace(process.ecalCompactTrigPrim,process.ecalCompactTrigPrim6)
    process.reconstruction_trackingOnly_6layers.replace(process.ecalTPSkim,process.ecalTPSkim6)
    process.reconstruction_trackingOnly_6layers.replace(process.ecalDetIdToBeRecovered,process.ecalDetIdToBeRecovered6)
    process.reconstruction_trackingOnly_6layers.replace(process.siPixelClustersPreSplitting,process.siPixelClustersPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.siPixelRecHitsPreSplitting,process.siPixelRecHitsPreSplitting6)
    process.reconstruction_trackingOnly_6layers.replace(process.ecalPreshowerRecHit,process.ecalPreshowerRecHit6)
    process.reconstruction_trackingOnly_6layers.replace(process.ecalMultiFitUncalibRecHit,process.ecalMultiFitUncalibRecHit6)
    process.reconstruction_trackingOnly_6layers.replace(process.ecalRecHit,process.ecalRecHit6)
    
    ############################################################################################################################################################################################
    
    process.reconstruction_trackingOnly_7layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.siPixelClusterShapeCachePreSplitting,process.siPixelClusterShapeCachePreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.hbhereco,process.hbhereco7)
    process.reconstruction_trackingOnly_7layers.replace(process.offlineBeamSpot,process.offlineBeamSpot7)
    process.reconstruction_trackingOnly_7layers.replace(process.displacedMuonSeeds,process.displacedMuonSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.displacedStandAloneMuons,process.displacedStandAloneMuons7)
    process.reconstruction_trackingOnly_7layers.replace(process.refittedStandAloneMuons,process.refittedStandAloneMuons7)
    process.reconstruction_trackingOnly_7layers.replace(process.standAloneMuons,process.standAloneMuons7)
    process.reconstruction_trackingOnly_7layers.replace(process.trackExtrapolator,process.trackExtrapolator7)
    process.reconstruction_trackingOnly_7layers.replace(process.generalV0Candidates,process.generalV0Candidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices7)
    process.reconstruction_trackingOnly_7layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS7)
    process.reconstruction_trackingOnly_7layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting7)
    process.reconstruction_trackingOnly_7layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting7)
    process.reconstruction_trackingOnly_7layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices7)
    process.reconstruction_trackingOnly_7layers.replace(process.ancientMuonSeed,process.ancientMuonSeed7)
    process.reconstruction_trackingOnly_7layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk7)
    process.reconstruction_trackingOnly_7layers.replace(process.caloTowerForTrk,process.caloTowerForTrk7)
    process.reconstruction_trackingOnly_7layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices7)
    process.reconstruction_trackingOnly_7layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder7)
    process.reconstruction_trackingOnly_7layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator7)
    process.reconstruction_trackingOnly_7layers.replace(process.vertexMerger,process.vertexMerger7)
    process.reconstruction_trackingOnly_7layers.replace(process.dedxHarmonic2,process.dedxHarmonic27)
    process.reconstruction_trackingOnly_7layers.replace(process.dedxHitInfo,process.dedxHitInfo7)
    process.reconstruction_trackingOnly_7layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0857)
    process.reconstruction_trackingOnly_7layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic27)
    process.reconstruction_trackingOnly_7layers.replace(process.dedxTruncated40,process.dedxTruncated407)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask7)
    process.reconstruction_trackingOnly_7layers.replace(process.newCombinedSeeds,process.newCombinedSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.stripPairElectronTrackingRegions,process.stripPairElectronTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask7)
    process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets7)
    process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.tripletElectronTrackingRegions,process.tripletElectronTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.conversionStepTracks,process.conversionStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.trackdnn_source,process.trackdnn_source7)
    process.reconstruction_trackingOnly_7layers.replace(process.trackerClusterCheck,process.trackerClusterCheck7)
    process.reconstruction_trackingOnly_7layers.replace(process.convClusters,process.convClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.convLayerPairs,process.convLayerPairs7)
    process.reconstruction_trackingOnly_7layers.replace(process.convStepSelector,process.convStepSelector7)
    process.reconstruction_trackingOnly_7layers.replace(process.convStepTracks,process.convStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.convTrackCandidates,process.convTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg7)
    process.reconstruction_trackingOnly_7layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent7)
    process.reconstruction_trackingOnly_7layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.caloTowerForTrkPreSplitting,process.caloTowerForTrkPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeedLayersPreSplitting,process.initialStepSeedLayersPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackingRegionsPreSplitting,process.initialStepTrackingRegionsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.mkFitSiPixelHitsPreSplitting,process.mkFitSiPixelHitsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache7)
    process.reconstruction_trackingOnly_7layers.replace(process.siPixelClusters,process.siPixelClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.siPixelRecHits,process.siPixelRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier7)
    process.reconstruction_trackingOnly_7layers.replace(process.generalTracks,process.generalTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.earlyMuons,process.earlyMuons7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStep,process.detachedQuadStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTrackingRegions,process.detachedQuadStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStep,process.detachedTripletStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier17)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier27)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTrackingRegions,process.detachedTripletStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStep,process.highPtTripletStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTrackingRegions,process.highPtTripletStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices7)
    process.reconstruction_trackingOnly_7layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStep,process.initialStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepClassifier1,process.initialStepClassifier17)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepSeeds,process.initialStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTrackingRegions,process.initialStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.initialStepTracks,process.initialStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStep,process.lowPtQuadStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepTrackingRegions,process.lowPtQuadStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStep,process.lowPtTripletStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepTrackingRegions,process.lowPtTripletStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStep,process.mixedTripletStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier17)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier27)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepTrackingRegionsA,process.mixedTripletStepTrackingRegionsA7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepTrackingRegionsB,process.mixedTripletStepTrackingRegionsB7)
    process.reconstruction_trackingOnly_7layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStep,process.pixelLessStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier17)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier27)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTrackingRegions,process.pixelLessStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStep,process.pixelPairStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB7)
    process.reconstruction_trackingOnly_7layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStep,process.tobTecStep7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier17)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier27)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepClusters,process.tobTecStepClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepTrackingRegionsPair,process.tobTecStepTrackingRegionsPair7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepTrackingRegionsTripl,process.tobTecStepTrackingRegionsTripl7)
    process.reconstruction_trackingOnly_7layers.replace(process.tobTecStepTracks,process.tobTecStepTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier7)
    process.reconstruction_trackingOnly_7layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut7)
    process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut7)
    process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut7)
    process.reconstruction_trackingOnly_7layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn7)
    process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn7)
    process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn7)
    process.reconstruction_trackingOnly_7layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier7)
#    process.reconstruction_trackingOnly_7layers.replace(process.bunchSpacingProducer,process.bunchSpacingProducer7)
    process.reconstruction_trackingOnly_7layers.replace(process.rpcRecHits,process.rpcRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.ctppsLocalTrackLiteProducer,process.ctppsLocalTrackLiteProducer7)
    process.reconstruction_trackingOnly_7layers.replace(process.ctppsProtons,process.ctppsProtons7)
    process.reconstruction_trackingOnly_7layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer7)
    process.reconstruction_trackingOnly_7layers.replace(process.hfprereco,process.hfprereco7)
    process.reconstruction_trackingOnly_7layers.replace(process.hfreco,process.hfreco7)
    process.reconstruction_trackingOnly_7layers.replace(process.horeco,process.horeco7)
    process.reconstruction_trackingOnly_7layers.replace(process.zdcreco,process.zdcreco7)
    process.reconstruction_trackingOnly_7layers.replace(process.csc2DRecHits,process.csc2DRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.cscSegments,process.cscSegments7)
    process.reconstruction_trackingOnly_7layers.replace(process.dt1DCosmicRecHits,process.dt1DCosmicRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.dt1DRecHits,process.dt1DRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.dt4DCosmicSegments,process.dt4DCosmicSegments7)
    process.reconstruction_trackingOnly_7layers.replace(process.dt4DSegments,process.dt4DSegments7)
    process.reconstruction_trackingOnly_7layers.replace(process.gemRecHits,process.gemRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.gemSegments,process.gemSegments7)
    process.reconstruction_trackingOnly_7layers.replace(process.ctppsDiamondLocalTracks,process.ctppsDiamondLocalTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.ctppsDiamondRecHits,process.ctppsDiamondRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.ctppsPixelClusters,process.ctppsPixelClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.ctppsPixelLocalTracks,process.ctppsPixelLocalTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.ctppsPixelRecHits,process.ctppsPixelRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.diamondSampicLocalTracks,process.diamondSampicLocalTracks7)
    process.reconstruction_trackingOnly_7layers.replace(process.totemTimingRecHits,process.totemTimingRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.totemRPClusterProducer,process.totemRPClusterProducer7)
    process.reconstruction_trackingOnly_7layers.replace(process.totemRPLocalTrackFitter,process.totemRPLocalTrackFitter7)
    process.reconstruction_trackingOnly_7layers.replace(process.totemRPRecHitProducer,process.totemRPRecHitProducer7)
    process.reconstruction_trackingOnly_7layers.replace(process.totemRPUVPatternFinder,process.totemRPUVPatternFinder7)
    process.reconstruction_trackingOnly_7layers.replace(process.siStripClusters,process.siStripClusters7)
    process.reconstruction_trackingOnly_7layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits7)
    process.reconstruction_trackingOnly_7layers.replace(process.siStripZeroSuppression,process.siStripZeroSuppression7)
    process.reconstruction_trackingOnly_7layers.replace(process.ecalCompactTrigPrim,process.ecalCompactTrigPrim7)
    process.reconstruction_trackingOnly_7layers.replace(process.ecalTPSkim,process.ecalTPSkim7)
    process.reconstruction_trackingOnly_7layers.replace(process.ecalDetIdToBeRecovered,process.ecalDetIdToBeRecovered7)
    process.reconstruction_trackingOnly_7layers.replace(process.siPixelClustersPreSplitting,process.siPixelClustersPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.siPixelRecHitsPreSplitting,process.siPixelRecHitsPreSplitting7)
    process.reconstruction_trackingOnly_7layers.replace(process.ecalPreshowerRecHit,process.ecalPreshowerRecHit7)
    process.reconstruction_trackingOnly_7layers.replace(process.ecalMultiFitUncalibRecHit,process.ecalMultiFitUncalibRecHit7)
    process.reconstruction_trackingOnly_7layers.replace(process.ecalRecHit,process.ecalRecHit7)
    
    ############################################################################################################################################################################################
    
    process.reconstruction_trackingOnly_8layers.replace(process.MeasurementTrackerEventPreSplitting,process.MeasurementTrackerEventPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.siPixelClusterShapeCachePreSplitting,process.siPixelClusterShapeCachePreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.hbhereco,process.hbhereco8)
    process.reconstruction_trackingOnly_8layers.replace(process.offlineBeamSpot,process.offlineBeamSpot8)
    process.reconstruction_trackingOnly_8layers.replace(process.displacedMuonSeeds,process.displacedMuonSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.displacedStandAloneMuons,process.displacedStandAloneMuons8)
    process.reconstruction_trackingOnly_8layers.replace(process.refittedStandAloneMuons,process.refittedStandAloneMuons8)
    process.reconstruction_trackingOnly_8layers.replace(process.standAloneMuons,process.standAloneMuons8)
    process.reconstruction_trackingOnly_8layers.replace(process.trackExtrapolator,process.trackExtrapolator8)
    process.reconstruction_trackingOnly_8layers.replace(process.generalV0Candidates,process.generalV0Candidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.offlinePrimaryVertices,process.offlinePrimaryVertices8)
    process.reconstruction_trackingOnly_8layers.replace(process.offlinePrimaryVerticesWithBS,process.offlinePrimaryVerticesWithBS8)
    process.reconstruction_trackingOnly_8layers.replace(process.trackRefsForJetsBeforeSorting,process.trackRefsForJetsBeforeSorting8)
    process.reconstruction_trackingOnly_8layers.replace(process.trackWithVertexRefSelectorBeforeSorting,process.trackWithVertexRefSelectorBeforeSorting8)
    process.reconstruction_trackingOnly_8layers.replace(process.unsortedOfflinePrimaryVertices,process.unsortedOfflinePrimaryVertices8)
    process.reconstruction_trackingOnly_8layers.replace(process.ancientMuonSeed,process.ancientMuonSeed8)
    process.reconstruction_trackingOnly_8layers.replace(process.ak4CaloJetsForTrk,process.ak4CaloJetsForTrk8)
    process.reconstruction_trackingOnly_8layers.replace(process.caloTowerForTrk,process.caloTowerForTrk8)
    process.reconstruction_trackingOnly_8layers.replace(process.inclusiveSecondaryVertices,process.inclusiveSecondaryVertices8)
    process.reconstruction_trackingOnly_8layers.replace(process.inclusiveVertexFinder,process.inclusiveVertexFinder8)
    process.reconstruction_trackingOnly_8layers.replace(process.trackVertexArbitrator,process.trackVertexArbitrator8)
    process.reconstruction_trackingOnly_8layers.replace(process.vertexMerger,process.vertexMerger8)
    process.reconstruction_trackingOnly_8layers.replace(process.dedxHarmonic2,process.dedxHarmonic28)
    process.reconstruction_trackingOnly_8layers.replace(process.dedxHitInfo,process.dedxHitInfo8)
    process.reconstruction_trackingOnly_8layers.replace(process.dedxPixelAndStripHarmonic2T085,process.dedxPixelAndStripHarmonic2T0858)
    process.reconstruction_trackingOnly_8layers.replace(process.dedxPixelHarmonic2,process.dedxPixelHarmonic28)
    process.reconstruction_trackingOnly_8layers.replace(process.dedxTruncated40,process.dedxTruncated408)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepSeedClusterMask,process.detachedTripletStepSeedClusterMask8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeedClusterMask,process.initialStepSeedClusterMask8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedClusterMask,process.mixedTripletStepSeedClusterMask8)
    process.reconstruction_trackingOnly_8layers.replace(process.newCombinedSeeds,process.newCombinedSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepSeedClusterMask,process.pixelLessStepSeedClusterMask8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairElectronHitDoublets,process.pixelPairElectronHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairElectronSeedLayers,process.pixelPairElectronSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairElectronSeeds,process.pixelPairElectronSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairElectronTrackingRegions,process.pixelPairElectronTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.stripPairElectronHitDoublets,process.stripPairElectronHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.stripPairElectronSeedLayers,process.stripPairElectronSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.stripPairElectronSeeds,process.stripPairElectronSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.stripPairElectronTrackingRegions,process.stripPairElectronTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronClusterMask,process.tripletElectronClusterMask8)
    process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronHitDoublets,process.tripletElectronHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronHitTriplets,process.tripletElectronHitTriplets8)
    process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronSeedLayers,process.tripletElectronSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronSeeds,process.tripletElectronSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.tripletElectronTrackingRegions,process.tripletElectronTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.conversionStepTracks,process.conversionStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.earlyGeneralTracks,process.earlyGeneralTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.preDuplicateMergingGeneralTracks,process.preDuplicateMergingGeneralTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.trackdnn_source,process.trackdnn_source8)
    process.reconstruction_trackingOnly_8layers.replace(process.trackerClusterCheck,process.trackerClusterCheck8)
    process.reconstruction_trackingOnly_8layers.replace(process.convClusters,process.convClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.convLayerPairs,process.convLayerPairs8)
    process.reconstruction_trackingOnly_8layers.replace(process.convStepSelector,process.convStepSelector8)
    process.reconstruction_trackingOnly_8layers.replace(process.convStepTracks,process.convStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.convTrackCandidates,process.convTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.photonConvTrajSeedFromSingleLeg,process.photonConvTrajSeedFromSingleLeg8)
    process.reconstruction_trackingOnly_8layers.replace(process.MeasurementTrackerEvent,process.MeasurementTrackerEvent8)
    process.reconstruction_trackingOnly_8layers.replace(process.ak4CaloJetsForTrkPreSplitting,process.ak4CaloJetsForTrkPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.caloTowerForTrkPreSplitting,process.caloTowerForTrkPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.firstStepPrimaryVerticesPreSplitting,process.firstStepPrimaryVerticesPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitDoubletsPreSplitting,process.initialStepHitDoubletsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitQuadrupletsPreSplitting,process.initialStepHitQuadrupletsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeedLayersPreSplitting,process.initialStepSeedLayersPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeedsPreSplitting,process.initialStepSeedsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitConfigPreSplitting,process.initialStepTrackCandidatesMkFitConfigPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitPreSplitting,process.initialStepTrackCandidatesMkFitPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitSeedsPreSplitting,process.initialStepTrackCandidatesMkFitSeedsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesPreSplitting,process.initialStepTrackCandidatesPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackRefsForJetsPreSplitting,process.initialStepTrackRefsForJetsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackingRegionsPreSplitting,process.initialStepTrackingRegionsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTracksPreSplitting,process.initialStepTracksPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetsForCoreTrackingPreSplitting,process.jetsForCoreTrackingPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.mkFitEventOfHitsPreSplitting,process.mkFitEventOfHitsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.mkFitSiPixelHitsPreSplitting,process.mkFitSiPixelHitsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.mkFitSiStripHits,process.mkFitSiStripHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.siPixelClusterShapeCache,process.siPixelClusterShapeCache8)
    process.reconstruction_trackingOnly_8layers.replace(process.siPixelClusters,process.siPixelClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.siPixelRecHits,process.siPixelRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.trackerClusterCheckPreSplitting,process.trackerClusterCheckPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.duplicateTrackCandidates,process.duplicateTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.duplicateTrackClassifier,process.duplicateTrackClassifier8)
    process.reconstruction_trackingOnly_8layers.replace(process.generalTracks,process.generalTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.mergedDuplicateTracks,process.mergedDuplicateTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.earlyMuons,process.earlyMuons8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStep,process.detachedQuadStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepClusters,process.detachedQuadStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepHitDoublets,process.detachedQuadStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepHitQuadruplets,process.detachedQuadStepHitQuadruplets8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepSeedLayers,process.detachedQuadStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepSeeds,process.detachedQuadStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackCandidates,process.detachedQuadStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackCandidatesMkFit,process.detachedQuadStepTrackCandidatesMkFit8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackCandidatesMkFitConfig,process.detachedQuadStepTrackCandidatesMkFitConfig8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackCandidatesMkFitSeeds,process.detachedQuadStepTrackCandidatesMkFitSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTrackingRegions,process.detachedQuadStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedQuadStepTracks,process.detachedQuadStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStep,process.detachedTripletStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepClassifier1,process.detachedTripletStepClassifier18)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepClassifier2,process.detachedTripletStepClassifier28)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepClusters,process.detachedTripletStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepHitDoublets,process.detachedTripletStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepHitTriplets,process.detachedTripletStepHitTriplets8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepSeedLayers,process.detachedTripletStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepSeeds,process.detachedTripletStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackCandidates,process.detachedTripletStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackCandidatesMkFit,process.detachedTripletStepTrackCandidatesMkFit8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackCandidatesMkFitConfig,process.detachedTripletStepTrackCandidatesMkFitConfig8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackCandidatesMkFitSeeds,process.detachedTripletStepTrackCandidatesMkFitSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTrackingRegions,process.detachedTripletStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.detachedTripletStepTracks,process.detachedTripletStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStep,process.highPtTripletStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepClusters,process.highPtTripletStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepHitDoublets,process.highPtTripletStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepHitTriplets,process.highPtTripletStepHitTriplets8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepSeedLayers,process.highPtTripletStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepSeeds,process.highPtTripletStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackCandidates,process.highPtTripletStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackCandidatesMkFit,process.highPtTripletStepTrackCandidatesMkFit8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackCandidatesMkFitConfig,process.highPtTripletStepTrackCandidatesMkFitConfig8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackCandidatesMkFitSeeds,process.highPtTripletStepTrackCandidatesMkFitSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTrackingRegions,process.highPtTripletStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.highPtTripletStepTracks,process.highPtTripletStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.firstStepPrimaryVertices,process.firstStepPrimaryVertices8)
    process.reconstruction_trackingOnly_8layers.replace(process.firstStepPrimaryVerticesUnsorted,process.firstStepPrimaryVerticesUnsorted8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStep,process.initialStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepClassifier1,process.initialStepClassifier18)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitDoublets,process.initialStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepHitQuadruplets,process.initialStepHitQuadruplets8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeedLayers,process.initialStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepSeeds,process.initialStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidates,process.initialStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFit,process.initialStepTrackCandidatesMkFit8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitConfig,process.initialStepTrackCandidatesMkFitConfig8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackCandidatesMkFitSeeds,process.initialStepTrackCandidatesMkFitSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackRefsForJets,process.initialStepTrackRefsForJets8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTrackingRegions,process.initialStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.initialStepTracks,process.initialStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.mkFitEventOfHits,process.mkFitEventOfHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.mkFitSiPixelHits,process.mkFitSiPixelHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.firstStepGoodPrimaryVertices,process.firstStepGoodPrimaryVertices8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStep,process.jetCoreRegionalStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepHitDoublets,process.jetCoreRegionalStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepSeedLayers,process.jetCoreRegionalStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepSeeds,process.jetCoreRegionalStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepTrackCandidates,process.jetCoreRegionalStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepTrackingRegions,process.jetCoreRegionalStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetCoreRegionalStepTracks,process.jetCoreRegionalStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.jetsForCoreTracking,process.jetsForCoreTracking8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStep,process.lowPtQuadStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepClusters,process.lowPtQuadStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepHitDoublets,process.lowPtQuadStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepHitQuadruplets,process.lowPtQuadStepHitQuadruplets8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepSeedLayers,process.lowPtQuadStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepSeeds,process.lowPtQuadStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepTrackCandidates,process.lowPtQuadStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepTrackingRegions,process.lowPtQuadStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtQuadStepTracks,process.lowPtQuadStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStep,process.lowPtTripletStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepClusters,process.lowPtTripletStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepHitDoublets,process.lowPtTripletStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepHitTriplets,process.lowPtTripletStepHitTriplets8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepSeedLayers,process.lowPtTripletStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepSeeds,process.lowPtTripletStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepTrackCandidates,process.lowPtTripletStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepTrackingRegions,process.lowPtTripletStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.lowPtTripletStepTracks,process.lowPtTripletStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.chargeCut2069Clusters,process.chargeCut2069Clusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStep,process.mixedTripletStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepClassifier1,process.mixedTripletStepClassifier18)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepClassifier2,process.mixedTripletStepClassifier28)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepClusters,process.mixedTripletStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepHitDoubletsA,process.mixedTripletStepHitDoubletsA8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepHitDoubletsB,process.mixedTripletStepHitDoubletsB8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepHitTripletsA,process.mixedTripletStepHitTripletsA8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepHitTripletsB,process.mixedTripletStepHitTripletsB8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedLayersA,process.mixedTripletStepSeedLayersA8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedLayersB,process.mixedTripletStepSeedLayersB8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeeds,process.mixedTripletStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedsA,process.mixedTripletStepSeedsA8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepSeedsB,process.mixedTripletStepSeedsB8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepTrackCandidates,process.mixedTripletStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepTrackingRegionsA,process.mixedTripletStepTrackingRegionsA8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepTrackingRegionsB,process.mixedTripletStepTrackingRegionsB8)
    process.reconstruction_trackingOnly_8layers.replace(process.mixedTripletStepTracks,process.mixedTripletStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStep,process.pixelLessStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepClassifier1,process.pixelLessStepClassifier18)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepClassifier2,process.pixelLessStepClassifier28)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepClusters,process.pixelLessStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepHitDoublets,process.pixelLessStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepHitTriplets,process.pixelLessStepHitTriplets8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepSeedLayers,process.pixelLessStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepSeeds,process.pixelLessStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTrackCandidates,process.pixelLessStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTrackCandidatesMkFit,process.pixelLessStepTrackCandidatesMkFit8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTrackCandidatesMkFitSeeds,process.pixelLessStepTrackCandidatesMkFitSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTrackingRegions,process.pixelLessStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelLessStepTracks,process.pixelLessStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStep,process.pixelPairStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepClusters,process.pixelPairStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepHitDoublets,process.pixelPairStepHitDoublets8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepHitDoubletsB,process.pixelPairStepHitDoubletsB8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepSeedLayers,process.pixelPairStepSeedLayers8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepSeeds,process.pixelPairStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepSeedsA,process.pixelPairStepSeedsA8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepSeedsB,process.pixelPairStepSeedsB8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepTrackCandidates,process.pixelPairStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepTrackingRegions,process.pixelPairStepTrackingRegions8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepTrackingRegionsSeedLayersB,process.pixelPairStepTrackingRegionsSeedLayersB8)
    process.reconstruction_trackingOnly_8layers.replace(process.pixelPairStepTracks,process.pixelPairStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStep,process.tobTecStep8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepClassifier1,process.tobTecStepClassifier18)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepClassifier2,process.tobTecStepClassifier28)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepClusters,process.tobTecStepClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepHitDoubletsPair,process.tobTecStepHitDoubletsPair8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepHitDoubletsTripl,process.tobTecStepHitDoubletsTripl8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepHitTripletsTripl,process.tobTecStepHitTripletsTripl8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeedLayersPair,process.tobTecStepSeedLayersPair8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeedLayersTripl,process.tobTecStepSeedLayersTripl8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeeds,process.tobTecStepSeeds8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeedsPair,process.tobTecStepSeedsPair8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepSeedsTripl,process.tobTecStepSeedsTripl8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepTrackCandidates,process.tobTecStepTrackCandidates8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepTrackingRegionsPair,process.tobTecStepTrackingRegionsPair8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepTrackingRegionsTripl,process.tobTecStepTrackingRegionsTripl8)
    process.reconstruction_trackingOnly_8layers.replace(process.tobTecStepTracks,process.tobTecStepTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTracksOutInClassifier,process.muonSeededTracksOutInClassifier8)
    process.reconstruction_trackingOnly_8layers.replace(process.muonSeededSeedsInOut,process.muonSeededSeedsInOut8)
    process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTrackCandidatesInOut,process.muonSeededTrackCandidatesInOut8)
    process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTracksInOut,process.muonSeededTracksInOut8)
    process.reconstruction_trackingOnly_8layers.replace(process.muonSeededSeedsOutIn,process.muonSeededSeedsOutIn8)
    process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTrackCandidatesOutIn,process.muonSeededTrackCandidatesOutIn8)
    process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTracksOutIn,process.muonSeededTracksOutIn8)
    process.reconstruction_trackingOnly_8layers.replace(process.muonSeededTracksInOutClassifier,process.muonSeededTracksInOutClassifier8)
#    process.reconstruction_trackingOnly_8layers.replace(process.bunchSpacingProducer,process.bunchSpacingProducer8)
    process.reconstruction_trackingOnly_8layers.replace(process.rpcRecHits,process.rpcRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.ctppsLocalTrackLiteProducer,process.ctppsLocalTrackLiteProducer8)
    process.reconstruction_trackingOnly_8layers.replace(process.ctppsProtons,process.ctppsProtons8)
    process.reconstruction_trackingOnly_8layers.replace(process.clusterSummaryProducer,process.clusterSummaryProducer8)
    process.reconstruction_trackingOnly_8layers.replace(process.hfprereco,process.hfprereco8)
    process.reconstruction_trackingOnly_8layers.replace(process.hfreco,process.hfreco8)
    process.reconstruction_trackingOnly_8layers.replace(process.horeco,process.horeco8)
    process.reconstruction_trackingOnly_8layers.replace(process.zdcreco,process.zdcreco8)
    process.reconstruction_trackingOnly_8layers.replace(process.csc2DRecHits,process.csc2DRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.cscSegments,process.cscSegments8)
    process.reconstruction_trackingOnly_8layers.replace(process.dt1DCosmicRecHits,process.dt1DCosmicRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.dt1DRecHits,process.dt1DRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.dt4DCosmicSegments,process.dt4DCosmicSegments8)
    process.reconstruction_trackingOnly_8layers.replace(process.dt4DSegments,process.dt4DSegments8)
    process.reconstruction_trackingOnly_8layers.replace(process.gemRecHits,process.gemRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.gemSegments,process.gemSegments8)
    process.reconstruction_trackingOnly_8layers.replace(process.ctppsDiamondLocalTracks,process.ctppsDiamondLocalTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.ctppsDiamondRecHits,process.ctppsDiamondRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.ctppsPixelClusters,process.ctppsPixelClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.ctppsPixelLocalTracks,process.ctppsPixelLocalTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.ctppsPixelRecHits,process.ctppsPixelRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.diamondSampicLocalTracks,process.diamondSampicLocalTracks8)
    process.reconstruction_trackingOnly_8layers.replace(process.totemTimingRecHits,process.totemTimingRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.totemRPClusterProducer,process.totemRPClusterProducer8)
    process.reconstruction_trackingOnly_8layers.replace(process.totemRPLocalTrackFitter,process.totemRPLocalTrackFitter8)
    process.reconstruction_trackingOnly_8layers.replace(process.totemRPRecHitProducer,process.totemRPRecHitProducer8)
    process.reconstruction_trackingOnly_8layers.replace(process.totemRPUVPatternFinder,process.totemRPUVPatternFinder8)
    process.reconstruction_trackingOnly_8layers.replace(process.siStripClusters,process.siStripClusters8)
    process.reconstruction_trackingOnly_8layers.replace(process.siStripMatchedRecHits,process.siStripMatchedRecHits8)
    process.reconstruction_trackingOnly_8layers.replace(process.siStripZeroSuppression,process.siStripZeroSuppression8)
    process.reconstruction_trackingOnly_8layers.replace(process.ecalCompactTrigPrim,process.ecalCompactTrigPrim8)
    process.reconstruction_trackingOnly_8layers.replace(process.ecalTPSkim,process.ecalTPSkim8)
    process.reconstruction_trackingOnly_8layers.replace(process.ecalDetIdToBeRecovered,process.ecalDetIdToBeRecovered8)
    process.reconstruction_trackingOnly_8layers.replace(process.siPixelClustersPreSplitting,process.siPixelClustersPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.siPixelRecHitsPreSplitting,process.siPixelRecHitsPreSplitting8)
    process.reconstruction_trackingOnly_8layers.replace(process.ecalPreshowerRecHit,process.ecalPreshowerRecHit8)
    process.reconstruction_trackingOnly_8layers.replace(process.ecalMultiFitUncalibRecHit,process.ecalMultiFitUncalibRecHit8)
    process.reconstruction_trackingOnly_8layers.replace(process.ecalRecHit,process.ecalRecHit8)
