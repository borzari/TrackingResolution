# Tracking Resolution

This a repository compiling all the tracking resolution work. Please, use **CMSSW 10_2_7** for the tests, which is the version that works so far.

To produce the histograms, there are a few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should
  - Amputate the tracks
     - this is performed by the command `cmsRun python/ClusterSurgeon.py outputFile=OUTPUT_FILE_NAME.root` (the input files for this step are ZMM RelVal samples, so far)
  - Run the reRECO file: `cmsRun python/reRECO_Autumn18.py inputFiles=file:OUTPUT_FILE_NAME.root outputFileName=reRECO_OUTPUT_FILE_NAME.root`
  - Run the DQM file: `cmsRun test/Tracker_DataMCValidation_cfg.py inputFiles=reRECO_OUTPUT_FILE_NAME.root outputFile=DQM_reRECO_OUTPUT_FILE_NAME.root`
  - Run the Harvest file: `cmsRun test/Tracker_DataMCValidation_Harvest_cfg.py inputFiles=DQM_reRECO_OUTPUT_FILE_NAME.root`
  - The output file with the histograms will be named something similar to `DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root`

It is also possible to use the file `python/reRECO_new.py` instead of `python/reRECO_Autumn18.py`. Both are equivalent, but `python/reRECO_new.py` only uses the relevant modules and might be easily portable to other CMSSW versions. Tests are being made with **CMSSW 11_3_0_pre2**, using the `python/reRECO_new.py` (notice that the track amputation step works without any issue in this version), but no success so far. The error is the following:

```
Exception Message:
Principal::getByToken: Found zero products matching all criteria
Looking for type: edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >
Looking for module label: hbheprereco
Looking for productInstanceName:
```
Regardless of the module `hbheprereco` being defined in line 360 of `python/reRECO_new.py`.
