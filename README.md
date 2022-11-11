# Tracking Resolution

This a repository compiling all the tracking pT resolution work. Please, use **CMSSW 12_6_0_pre3** for the tests. Every step is performed for each value of layer threshold (from 3 to 8)

To produce the histograms, there is only few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should
  - Compile the modules `scram b -j 8`
  - Execute the DQM and the Harvest step in one command with
     - `python test/runAllAlignment.py --step=DQM,Harvest --layersThreshold=0`
The output file with the histograms will be named something that is defined in `test/runAllAlignment.py`. The default is `Harvest_Alignment_+layersThreshold+layers.root` if layersThreshold is in between 3 and 8, and `Harvest_Alignment_allLayers.root`. Running with layersThreshold in between 3 and 8 is good for debugging purposes.

**Necessary checks**
  - Number of layers in shortened tracks (after selection) is a bit different from the number of layers asked for.
     - Answer: the module **TrackerTrackHitFilter** doesn't have a very fine control about the number of layers with measurement to remain in the refitted track. Need to check what is the better option here.

**Improvements**
  - Only performing track recHits selection and refitting after, event throughput is much higher, around 75 ev/s
