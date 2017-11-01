submitDir="2017_Oct6_Upgrade"
mergeDir="Htt_Oct16_Upgrade-qcdonly"

mkdir /scratch/ojalvo/${mergeDir}_200PU
cd /scratch/ojalvo/${mergeDir}_200PU
hadd -f QCD.root   /hdfs/store/user/ojalvo/${submitDir}_QCD_200PU-SUB/*
EventWeightsIterative outputFile='QCD.root'     weight=335469     histoName='TT/results' 

