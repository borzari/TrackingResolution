# Tracking Resolution

This is a repository compiling all the tracking pT resolution work. Please, use **CMSSW 13_1_0_pre2** for the tests. Every step is performed for each value of layer threshold (from 3 to 8 for now).

To produce the histograms, there is only a few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should:
  - Compile the modules `scram b -j 8`;
  - Execute the DQM and the Harvest step in one command with:
     - `python test/runAllAlignment.py --step=DQM,Harvest --layersThreshold=0`;

The output file with the histograms will be named something that is defined in lines 88-90 of `test/runAllAlignment.py`. The default is `Harvest_Alignment_+layersThreshold+layers.root` if layersThreshold is in between 3 and 8, and `Harvest_Alignment_allLayers.root` in any other case. Running with layersThreshold in between 3 and 8 is good for debugging purposes, since it produces the histograms for only one of the layer requirements.

**Necessary checks**
  - Number of layers in shortened tracks (after selection) is a bit different from the number of layers asked for;
     - Answer: the module **TrackerTrackHitFilter** doesn't have a very fine control about the number of layers with measurement to remain in the refitted track. Need to check what is the better option here;
  - In config file, modules **MeasurementTrackerEvent** and **TrackRefitter** were needed. Couldn't pass **generalTracks** directly to **TrackerTrackHitFilter** and don't understand why this happens very well (**MeasurementTrackerEvent** is just used by **TrackRefitter**)
     - Answer: Indeed the refitting is needed to construct track collections (instead of reco::Tracks only as is the generalTracks case), and, in that case, **MeasurementTrackerEvent** is necessary.

**Improvements**
  - Only performing track recHits selection and refitting after, event throughput is much higher, around 75 ev/s;
     - The throughput actually depends a lot: sometimes it can be as high as 200 ev/s, but also as low as 30 ev/s;
  - Can start from GEN-SIM-RECO and don't need to perform any reconstruction (or re-reconstruction).
