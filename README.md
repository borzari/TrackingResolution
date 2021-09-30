# Tracking Resolution

This a repository compiling all the tracking pT resolution work. Please, use **CMSSW 10_2_7** for the tests, which is the version that works so far.

To produce the histograms, there are a few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should
  - Amputate the tracks
     - this is performed by the command `cmsRun python/ClusterSurgeon.py outputFile=OUTPUT_FILE_NAME.root` (the input files for this step are ZMM RelVal samples, so far)
  - Run the reRECO file: `cmsRun python/reRECO_new.py inputFiles=file:OUTPUT_FILE_NAME.root outputFileName=reRECO_OUTPUT_FILE_NAME.root`
  - Run the DQM file: `cmsRun test/Tracker_DataMCValidation_cfg.py inputFiles=reRECO_OUTPUT_FILE_NAME.root outputFile=DQM_reRECO_OUTPUT_FILE_NAME.root`
  - Run the Harvest file: `cmsRun test/Tracker_DataMCValidation_Harvest_cfg.py inputFiles=DQM_reRECO_OUTPUT_FILE_NAME.root`
  - The output file with the histograms will be named something similar to `DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root`

Tests are being made to run the procedure in **CMSSW_12_0_0_pre3**. Even though it is possible to execute the tracks shortening, re-reconstruction and validation using the RelValZMM file from **CMSSW_10_2_5**, when trying to use files from **CMSSW_12_0_0_pre3**, it accuses that some modules are missing when they are defined into the task to be executed.

A way to more easily add modules into the re-recontruction step is work in progress so far.

**Necessary checks**
  - Why the number of reconstructed tracks (before selection) is extremely higher than the number of good tracks to reconstruct? See where and how this tracks appear in the detector
  - Number of hits in reconstructed tracks (after selection) is a bit different from the number of hits provided in the dataset to be reconstructed. Compare reco hits with hits from dataset

**Improvements**
  - Instead of clonning the relevant paths to reconstruct tracks, pass only the hits to the InitialStep and use the same other modules for reconstruction, Faster and more reliable (?)
