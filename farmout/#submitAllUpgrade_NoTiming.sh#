#!/bin/sh
#voms-proxy-init --voms cms --valid 100:00
jobID=2017_Oct13_Upgrade_NoTiming

cat $CMSSW_BASE/src/PUAnalysis/TT-MC-Up.py > SUB.py
cat submit.py >>SUB.py

jobOptions="--vsize-limit=8000  --input-files-per-job=1 --assume-input-files-exist"
tailOptions="  $CMSSW_BASE $CMSSW_BASE/src/PUAnalysis/farmout/SUB.py"

#farmoutAnalysisJobs  $1 $jobOptions --input-file-list=GGH_200PU.txt         --input-basenames-not-unique    ${jobID}_GGH_200PU     $tailOptions


farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/DYJetsToLL_200PU.txt  --input-basenames-not-unique    ${jobID}_DYJets_200PU  $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/DYJetsToLL_0PU.txt    --input-basenames-not-unique    ${jobID}_DYJets_0PU    $tailOptions

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/TTbar_200PU.txt       --input-basenames-not-unique    ${jobID}_TTbar_200PU   $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/TTbar_0PU.txt         --input-basenames-not-unique    ${jobID}_TTbar_0PU     $tailOptions

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/VBF_200PU.txt         --input-basenames-not-unique    ${jobID}_VBF_200PU     $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/VBF_0PU.txt           --input-basenames-not-unique    ${jobID}_VBF_0PU       $tailOptions

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/GGH_200PU.txt         --input-basenames-not-unique    ${jobID}_GGH_200PU     $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/GGH_0PU.txt           --input-basenames-not-unique    ${jobID}_GGH_0PU       $tailOptions

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=samples_Upgrade_NoTiming/QCD_200PU.txt         --input-basenames-not-unique    ${jobID}_QCD_200PU     $tailOptions


rm SUB.py

#DYJetsToLL_0PU.txt  DYJetsToLL_200PU.txt  GGH_0PU.txt  GGH_200PU.txt  QCD_200PU.txt  TTbar_0PU.txt  TTbar_200PU.txt  VBF_0PU.txt  VBF_200PU.txt

#/DYJetsToLL_M-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIITDRSpring17MiniAOD-PU200_91X_upgrade2023_realistic_v3-v2/MINIAODSIM
#/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIITDRSpring17MiniAOD-PU200_91X_upgrade2023_realistic_v3-v3/MINIAODSIM
#/VBFHToTauTau_M125_14TeV_powheg_pythia8/PhaseIITDRSpring17MiniAOD-PU200_91X_upgrade2023_realistic_v3-v3/MINIAODSIM
#/GluGluHToTauTau_M125_14TeV_powheg_pythia8/PhaseIITDRSpring17MiniAOD-PU200_91X_upgrade2023_realistic_v3-v3/MINIAODSIM
#/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_14TeV_pythia8/PhaseIITDRSpring17MiniAOD-PU200_91X_upgrade2023_realistic_v3-v6/MINIAODSIM