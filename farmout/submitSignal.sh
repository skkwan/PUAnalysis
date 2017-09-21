#!/bin/sh
voms-proxy-init --voms cms --valid 100:00
jobID=2017_Sep7_Upgrade_pfjets

cat $CMSSW_BASE/src/PUAnalysis/TT-MC-Up.py > SUB.py
cat submit.py >>SUB.py

jobOptions="--vsize-limit=8000  --input-files-per-job=1 --assume-input-files-exist"
tailOptions="  $CMSSW_BASE $CMSSW_BASE/src/PUAnalysis/farmout/SUB.py"

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=DYJetsToLL_200PU.txt             ${jobID}_DYJets_200PU  $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=DYJetsToLL_0PU.txt               ${jobID}_DYJets_0PU  $tailOptions

rm SUB.py