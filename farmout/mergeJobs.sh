
#2017_Sep13-2_Upgrade_DYJets_0PU-SUB/ 2017_Sep13-2_Upgrade_QCD_200PU-SUB/  2017_Sep13-2_Upgrade_VBF_200PU-SUB/
#2017_Sep13-2_Upgrade_GGH_0PU-SUB/    2017_Sep13-2_Upgrade_TTbar_0PU-SUB/
#2017_Sep13-2_Upgrade_GGH_200PU-SUB/  2017_Sep13-2_Upgrade_VBF_0PU-SUB/

submitDir="2017_Sep22_Upgrade"
mergeDir="Htt_Sep22"

mkdir /scratch/ojalvo/${mergeDir}_200PU
cd /scratch/ojalvo/${mergeDir}_200PU
hadd -f DYJets.root /hdfs/store/user/ojalvo/${submitDir}_DYJets_200PU-SUB/*
hadd -f ttBar.root  /hdfs/store/user/ojalvo/${submitDir}_TTbar_200PU-SUB/*
hadd -f ggH125.root    /hdfs/store/user/ojalvo/${submitDir}_GGH_200PU-SUB/*
hadd -f vbfH125.root   /hdfs/store/user/ojalvo/${submitDir}_VBF_200PU-SUB/*
hadd -f QCD.root   /hdfs/store/user/ojalvo/${submitDir}_QCD_200PU-SUB/*
EventWeightsIterative outputFile='ggH125.root'     weight=3.045965       histoName='TT/results' 
EventWeightsIterative outputFile='vbfH125.root'    weight=0.2371314      histoName='TT/results' 
EventWeightsIterative outputFile='ttBar.root'      weight=831.76     histoName='TT/results' 
EventWeightsIterative outputFile='DYJets.root'     weight=4854.0     histoName='TT/results' 
EventWeightsIterative outputFile='QCD.root'     weight=1     histoName='TT/results' 

mkdir /scratch/ojalvo/${mergeDir}_0PU
cd /scratch/ojalvo/${mergeDir}_0PU
hadd -f DYJets.root /hdfs/store/user/ojalvo/${submitDir}_DYJets_0PU-SUB/*
hadd -f ttBar.root  /hdfs/store/user/ojalvo/${submitDir}_TTbar_0PU-SUB/*
hadd -f ggH125.root    /hdfs/store/user/ojalvo/${submitDir}_GGH_0PU-SUB/*
hadd -f vbfH125.root   /hdfs/store/user/ojalvo/${submitDir}_VBF_0PU-SUB/*
hadd -f QCD.root    /hdfs/store/user/ojalvo/${submitDir}_QCD_0PU-SUB/*


EventWeightsIterative outputFile='ggH125.root'     weight=3.045965       histoName='TT/results'
EventWeightsIterative outputFile='vbfH125.root'    weight=0.2371314      histoName='TT/results' 
EventWeightsIterative outputFile='ttBar.root'      weight=831.76     histoName='TT/results' 
EventWeightsIterative outputFile='DYJets.root'     weight=4854.0     histoName='TT/results' 
EventWeightsIterative outputFile='QCD.root'     weight=1     histoName='TT/results' 