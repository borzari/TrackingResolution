# Tracking Resolution

This is a repository compiling all the tracking pT resolution work. Please, use **CMSSW 13_1_0_pre2** for the tests. Every step is performed for each value of layer threshold (from 3 to 8 for now).

Running the code will filter events with "good muons" (in **GoodRecoMuonsFilter.cc**), creates a collection of good muon tracks (in **RClusterProducerAlignment.cc**), shorten those tracks (in **TrackingResolutionAlignment.cc**) and print some information/produce some histograms (in **TrackingResolutionAlignment.cc**). The histograms will not be useful to check the bug.

To reproduce the bug, there is only a few steps needed. Inside the `TrackingResolution/TrackingResolution/` folder you should:
  - Compile the modules `scram b -j 8`;
  - Execute the DQM step in one command with:
     - `python3 test/runAllAlignment.py --step=DQM --layersThreshold=0 --numEvents=15292 --isMC=True --isPU=False`;

Only one event will be executed (this bug is "rare"; I only observed it in 2 events out of 15292) and it will print on the screen a few information:
  - A few lines related to the validity and substructure/layer of the hits, checked in module **TrackerTrackHitFilterMod.cc**
     - The size of **ownHits** is the amount of hits used to create the track candidate that will be refitted
  - Then, in the following order: run/lumi/event information; number of tracker layers with measurement of the shortened track; number of layers of measurement requested for the short track to have; pT resolution; pT/eta/phi of short track; chi2/ndof of short track
  - Number of layers in each substructure that have a valid measurement in the order:
     - pxb  pxf  tib  tid  tob  tec -- total

It is possible to notice that, for the layer threshold of 8 (full output below), the short track only has 7 layers with measurement, and the missing hit is compatible with the 4th layer of pxb that is missing, although it is added to the **ownHits** vector as a hit of the track candidate. This doesn't happen for any of the layer thresholds below 8 (it can be checked by reproducing the bug), which might point to some bug.

```
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 1 -- thisLayer = 1 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 1
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 1 -- thisLayer = 2 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 2
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 1 -- thisLayer = 3 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 3
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 1 -- thisLayer = 4 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 4
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 3 -- thisLayer = 1 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 5
isFirstValidHitInLayerAux = 0 -- thisSubStruct = 3 -- thisLayer = 1 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 6
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 3 -- thisLayer = 2 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 7
isFirstValidHitInLayerAux = 0 -- thisSubStruct = 3 -- thisLayer = 2 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 8
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 3 -- thisLayer = 3 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 9
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 4 -- thisLayer = 1 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
ownHits.size(): 10
isFirstValidHitInLayerAux = 1 -- thisSubStruct = 5 -- thisLayer = 1 -- isNotValidVec[int(isNotValidVec.size()) - 2] = 0 -- isNotValidVec[int(isNotValidVec.size()) - 1] = 0
run: 1 lumi: 174 event: 17393
Tracker layers of short track: 7
Number of layers remaining: 8
pT resolution: 1.00315
pT of short track: 25.5926
eta of short track: 1.21391
phi of short track: 3.12039
chi2/ndof: 0.770975
Short track: 1 0 0 0 0 0 -- 1
Short track: 2 0 0 0 0 0 -- 2
Short track: 3 0 0 0 0 0 -- 3
Short track: 3 0 1 0 0 0 -- 4
Short track: 3 0 1 0 0 0 -- 4
Short track: 3 0 2 0 0 0 -- 5
Short track: 3 0 2 0 0 0 -- 5
Short track: 3 0 3 0 0 0 -- 6
Short track: 3 0 3 1 0 0 -- 7
Track: 1 0 0 0 0 0 -- 1
Track: 2 0 0 0 0 0 -- 2
Track: 3 0 0 0 0 0 -- 3
Track: 4 0 0 0 0 0 -- 4
Track: 4 0 1 0 0 0 -- 5
Track: 4 0 1 0 0 0 -- 5
Track: 4 0 2 0 0 0 -- 6
Track: 4 0 2 0 0 0 -- 6
Track: 4 0 3 0 0 0 -- 7
Track: 4 0 3 1 0 0 -- 8
Track: 4 0 3 1 1 0 -- 9
Track: 4 0 3 1 1 0 -- 9
Track: 4 0 3 1 2 0 -- 10
Track: 4 0 3 1 2 0 -- 10
Track: 4 0 3 1 2 1 -- 11
Track: 4 0 3 1 2 2 -- 12
Track: 4 0 3 1 2 3 -- 13
===================================
```