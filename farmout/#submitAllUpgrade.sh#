#!/bin/sh
#voms-proxy-init --voms cms --valid 100:00
jobID=2017_Oct6_Upgrade

cat $CMSSW_BASE/src/PUAnalysis/TT-MC-Up.py > SUB.py
cat submit.py >>SUB.py

jobOptions="--vsize-limit=8000  --input-files-per-job=1 --assume-input-files-exist"
tailOptions="  $CMSSW_BASE $CMSSW_BASE/src/PUAnalysis/farmout/SUB.py"

#farmoutAnalysisJobs  $1 $jobOptions --input-file-list=GGH_200PU.txt         --input-basenames-not-unique    ${jobID}_GGH_200PU     $tailOptions


farmoutAnalysisJobs  $1 $jobOptions --input-file-list=DYJetsToLL_200PU.txt  --input-basenames-not-unique    ${jobID}_DYJets_200PU  $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=DYJetsToLL_0PU.txt    --input-basenames-not-unique    ${jobID}_DYJets_0PU    $tailOptions

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=TTbar_200PU.txt       --input-basenames-not-unique    ${jobID}_TTbar_200PU   $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=TTbar_0PU.txt         --input-basenames-not-unique    ${jobID}_TTbar_0PU     $tailOptions

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=VBF_200PU.txt         --input-basenames-not-unique    ${jobID}_VBF_200PU     $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=VBF_0PU.txt           --input-basenames-not-unique    ${jobID}_VBF_0PU       $tailOptions

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=GGH_200PU.txt         --input-basenames-not-unique    ${jobID}_GGH_200PU     $tailOptions
farmoutAnalysisJobs  $1 $jobOptions --input-file-list=GGH_0PU.txt           --input-basenames-not-unique    ${jobID}_GGH_0PU       $tailOptions

farmoutAnalysisJobs  $1 $jobOptions --input-file-list=QCD_200PU.txt         --input-basenames-not-unique    ${jobID}_QCD_200PU     $tailOptions

#farmoutAnalysisJobs  $1 $jobOptions --input-dbs-path=/DYJetsToLL_M-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIITDRSpring17MiniAOD-PU200_91X_upgrade2023_realistic_v3-v1/MINIAODSIM     ${jobID}_DYJets_200PU  $tailOptions
#farmoutAnalysisJobs  $1 $jobOptions --input-dbs-path=/DYJetsToLL_M-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIITDRSpring17MiniAOD-noPU_91X_upgrade2023_realistic_v3-v1/MINIAODSIM      ${jobID}_DYJets_noPU  $tailOptions
#farmoutAnalysisJobs  $1 $jobOptions --input-dbs-path=/QCD_Flat_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIITDRSpring17MiniAOD-PU200_91X_upgrade2023_realistic_v3-v1/MINIAODSIM	    ${jobID}_QCD_200PU  $tailOptions
#farmoutAnalysisJobs  $1 $jobOptions --input-dbs-path=/QCD_Flat_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIITDRSpring17MiniAOD-noPU_91X_upgrade2023_realistic_v3-v1/MINIAODSIM             ${jobID}_QCD_noPU  $tailOptions
#farmoutAnalysisJobs  $1 $jobOptions --input-dbs-path=/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIITDRSpring17MiniAOD-PU200_91X_upgrade2023_realistic_v3-v1/MINIAODSIM		            ${jobID}_TT_200PU  $tailOptions
#farmoutAnalysisJobs  $1 $jobOptions --input-dbs-path=/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIITDRSpring17MiniAOD-noPU_91X_upgrade2023_realistic_v3-v1/MINIAODSIM                        ${jobID}_TT_noPU  $tailOptions

rm SUB.py

#DYJetsToLL_0PU.txt  DYJetsToLL_200PU.txt  GGH_0PU.txt  GGH_200PU.txt  QCD_200PU.txt  TTbar_0PU.txt  TTbar_200PU.txt  VBF_0PU.txt  VBF_200PU.txt