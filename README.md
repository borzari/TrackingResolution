# Tracking Resolution

This a repository compiling all the tracking pT resolution work. Please, use **CMSSW 12_3_0_pre5** for the tests. For now the reRECO, DQM and Harvesting steps have to be made for each value of the layer threshold (from 3 to 8; this will change)

To produce the histograms, there are a few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should
  - Compile the modules `scram b -j 8`
  - Get/change the input files (RelVal ZMM examples for now)
     - `cmsRun python/RECO.py outputFile=OUTPUT_FILE_NAME`
  - Shorten the tracks
     - `cmsRun python/ClusterSurgeon.py inputFiles=OUTPUT_FILE_NAME outputFile=OUTPUT_FILE_NAME` (the input files for this step are ZMM RelVal samples, so far)
  - Run the re-reconstruction
     - `cmsRun python/reRECO.py inputFiles=OUTPUT_FILE_NAME outputFile=OUTPUT_FILE_NAME layersThreshold=3`
  - Run the DQM
     - `cmsRun test/Tracker_DataMCValidation_cfg.py inputFiles=OUTPUT_FILE_NAME outputFile=OUTPUT_FILE_NAME layersThreshold=3`
  - Run the Harvest
     - `cmsRun test/Tracker_DataMCValidation_Harvest_cfg.py inputFiles=OUTPUT_FILE_NAME layersThreshold=3`
The output file with the histograms will be named something similar to `DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root`

**Necessary checks**
  - Why the number of reconstructed tracks (before selection) is extremely higher than the number of good tracks to reconstruct? See where and how this tracks appear in the detector
  - Number of hits in reconstructed tracks (after selection) is a bit different from the number of hits provided in the dataset to be reconstructed. Compare reco hits with hits from dataset

**Improvements**
  - Instead of clonning the relevant paths to reconstruct tracks, pass only the hits to the InitialStep and use the same other modules for reconstruction, Faster and more reliable (?)
