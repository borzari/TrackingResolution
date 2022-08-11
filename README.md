# Tracking Resolution

This a repository compiling all the tracking pT resolution work. Please, use **CMSSW 12_5_0_pre2** for the tests. Every step is performed for each value of layer threshold (from 3 to 8)

To produce the histograms, there are a few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should
  - Compile the modules `scram b -j 8`
  - Get/change the input files (RelVal ZMM examples for now)
     - `cmsRun python/RECO.py outputFile=OUTPUT_FILE_NAME`
  - Shorten the tracks
     - `cmsRun python/ClusterSurgeon.py inputFiles=OUTPUT_FILE_NAME outputFile=OUTPUT_FILE_NAME`
  - Run the re-reconstruction (there is no layersThreshold value equal to 9, but setting it to 9 makes every number of layers from 3 to 8; setting layersThreshold between 3 and 8 generates each given value -> good for debbuging)
     - `cmsRun python/reRECO.py inputFiles=OUTPUT_FILE_NAME outputFile=OUTPUT_FILE_NAME layersThreshold=9`
  - Run the DQM
     - `cmsRun test/Tracker_DataMCValidation_cfg.py inputFiles=OUTPUT_FILE_NAME outputFile=OUTPUT_FILE_NAME layersThreshold=9`
  - Run the Harvest
     - `cmsRun test/Tracker_DataMCValidation_Harvest_cfg.py inputFiles=OUTPUT_FILE_NAME layersThreshold=9`
The output file with the histograms will be named something similar to `DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root`

**Necessary checks**
  - Why the number of reconstructed tracks (before selection) is extremely higher than the number of good tracks to reconstruct? See where and how this tracks appear in the detector
     - Answer: the `ClusterSurgeon.py` script was only removing the extra clusters of the shortened track, and saving everything else, providing a lot of tracks with more hits than the number of layers of threshold
  - Number of hits in reconstructed tracks (after selection) is a bit different from the number of hits provided in the dataset to be reconstructed. Compare reco hits with hits from dataset
     - Answer: for more hits than layers threshold, the answer is above; for less hits than layers threshold I still don't have an answer.

**Improvements**
  - Instead of clonning the relevant paths to reconstruct tracks, pass only the hits to the InitialStep and use the same other modules for reconstruction, faster and more reliable (?)
