# Tracking Resolution

This a repository compiling all the tracking resolution work.

To produce the histograms, there are a few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should
  - Amputate the tracks
     - this is performed by the command `cmsRun python/ClusterSurgeon.py outputFile=OUTPUT_FILE_NAME.root`
  - Run the reRECO file: `cmsRun python/reRECO_Autumn18 inputFiles=file:OUTPUT_FILE_NAME.root outputFileName=reRECO_OUTPUT_FILE_NAME step=3 MuonSeeds=1` (the arguments step and MuonSeeds are dummy arguments and will be removed)
  - Put the correct input file name (output file name of the step above) and define an output file name in the file `test/Tracker_DataMCValidation_cfg.py` and run it with `cmsRun test/Tracker_DataMCValidation_cfg.py`
  - Put the correct input file name (output file name of the step above) in the file `test/Tracker_DataMCValidation_Harvest_cfg.py` and run it with `cmsRun test/Tracker_DataMCValidation_Harvest_cfg.py`
  - The output file with the histograms will be named something similar to `DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root`
