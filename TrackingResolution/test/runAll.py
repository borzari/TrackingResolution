import os
import argparse
import sys

def find(test_list, val):
    for x in test_list:
        if x == val:
            return True
        else:
            x = None
    return False

parser = argparse.ArgumentParser(description='Passing mass and ctau to submit condor jobs for step4.')
parser.add_argument('--step', dest='step', default='RECO,reRECO,DQM,Harvest', help='Steps of tracking resolution (default [RECO,reRECO,DQM,Harvest])')
parser.add_argument('--layersThreshold', dest='layersThreshold', default=3, help='Number of threshold layers (from 3 to 8 so far)')

args = parser.parse_args()

stepList = args.step
stepList = stepList.split(',')
if find(stepList,'RECO'):
    if stepList[0] != 'RECO':
        stepList[stepList.index('RECO')] = stepList[0]
        stepList[0] = 'RECO'
    if find(stepList,'reRECO'):
        if stepList[1] != 'reRECO':
            stepList[stepList.index('reRECO')] = stepList[1]
            stepList[1] = 'reRECO'
        if find(stepList,'DQM'):
            if stepList[2] != 'DQM':
                stepList[stepList.index('DQM')] = stepList[2]
                stepList[2] = 'DQM'
            if find(stepList,'Harvest'):
                if stepList[3] != 'Harvest':
                    stepList[stepList.index('Harvest')] = stepList[3]
                    stepList[3] = 'Harvest'
elif find(stepList,'reRECO'):
    if stepList[0] != 'reRECO':
        stepList[stepList.index('reRECO')] = stepList[0]
        stepList[0] = 'reRECO'
    if find(stepList,'DQM'):
        if stepList[1] != 'DQM':
            stepList[stepList.index('DQM')] = stepList[1]
            stepList[1] = 'DQM'
        if find(stepList,'Harvest'):
            if stepList[2] != 'Harvest':
                stepList[stepList.index('Harvest')] = stepList[2]
                stepList[2] = 'Harvest'
elif find(stepList,'DQM'):
    if stepList[0] != 'DQM':
        stepList[stepList.index('DQM')] = stepList[0]
        stepList[0] = 'DQM'
    if find(stepList,'Harvest'):
        if stepList[1] != 'Harvest':
            stepList[stepList.index('Harvest')] = stepList[1]
            stepList[1] = 'Harvest'
elif find(stepList,'RECO')==False and find(stepList,'reRECO')==False and find(stepList,'DQM')==False and find(stepList,'Harvest')==False:
    print("Not valid step! Aborting.")
    sys.exit()
elif find(stepList,'reRECO')==False and find(stepList,'DQM')==False and find(stepList,'Harvest')==False:
    print("Not valid step! Aborting.")
    sys.exit()
elif find(stepList,'DQM')==False and find(stepList,'Harvest')==False:
    print("Not valid step! Aborting.")
    sys.exit()
elif find(stepList,'Harvest')==False:
    print("Not valid step! Aborting.")
    sys.exit()

print(stepList)

layersThreshold = str(args.layersThreshold)

for step in stepList:
    if step == 'RECO':
        print("Running RECO and track shortening")
        os.system("cmsRun python/RECO.py outputFile=OUTPUT_FILE_NAME")
    if step == 'reRECO':
        print("Running reRECO")
        os.system("cmsRun python/reRECO.py inputFiles=OUTPUT_FILE_NAME outputFile=OUTPUT_FILE_NAME layersThreshold="+layersThreshold)
    if step == 'DQM':
        print("Running DQM")
        os.system("cmsRun test/Tracker_DataMCValidation_cfg.py inputFiles=OUTPUT_FILE_NAME outputFile=OUTPUT_FILE_NAME layersThreshold="+layersThreshold)
    if step == 'Harvest':
        harvestFile = 'Harvest_test_run2LikeReRECO_definitive_allRECO_'+layersThreshold+'layers'
        print("Harvesting histograms and saving as "+harvestFile+".root")
        os.system("cmsRun test/Tracker_DataMCValidation_Harvest_cfg.py inputFiles=OUTPUT_FILE_NAME layersThreshold="+layersThreshold+"; mv DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root "+harvestFile+".root")
