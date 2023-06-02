# Tracking Resolution

This is a repository compiling all the tracking pT resolution work. Please, use **CMSSW 13_1_0_pre2** for the tests. Every step is performed for each value of layer threshold (from 3 to 8 for now).

To produce the histograms, there is only a few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should:
  - Compile the modules `scram b -j 8`;
  - Execute the DQM and the Harvest step in one command with:
     - `python3 test/runAllAlignment.py --step=DQM --layersThreshold=0 --numEvents=15292 --isMC=True --isPU=False --isAOD=False`;
        - This command will run over RelValZMM events without PU. To run over MC with PU do: `--isMC=True --isPU=True --isAOD=False`. To run over RAW data (`/Muon/Run2022G-v1/RAW`) do: `--isMC=False --isPU=False --isAOD=False`. To run over AOD data (`/Muon/Run2022G-PromptReco-v1/AOD`) do: `--isMC=False --isPU=False --isAOD=True`.

The output file with the histograms will be named something that is defined in lines 92-98 of `test/runAllAlignment.py`. The default is `{MC|MCPU|Data|DataAOD}_Harvest_Alignment_+layersThreshold+layers.root` if layersThreshold is in between 3 and 8, and `{MC|MCPU|Data|DataAOD}_Harvest_Alignment_allLayers.root` in any other case. Running with layersThreshold in between 3 and 8 is good for debugging purposes, since it produces the histograms for only one of the layer requirements.

**Necessary checks**
  - A few events still have shortened tracks with one less layer with measurement than what is requested. This might be a bug in the refitter, but need to be investigated further (under discussion [here](https://github.com/CMSTrackingPOG/cmssw/issues/2))
  - Still need to implement in DQM

**Improvements**
  - Only performing track recHits selection and refitting after, event throughput is much higher, around 75 ev/s;
     - The throughput actually depends a lot: sometimes it can be as high as 200 ev/s, but also as low as 30 ev/s;
  - Can start from GEN-SIM-RECO and don't need to perform any reconstruction for MC files.
     - For Data, due to runing reconstruction, the throughput is around 1.5 ev/s
     - Added the AOD option as well to speed up running over data
  - Modified the shortening procedure and now the number of layers with measurement in the shortened tracks is much more precise.
     - By default the procedure is turned off, but can be turned on in a given module
