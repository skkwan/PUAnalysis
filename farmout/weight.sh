
#2017_Sep13-2_Upgrade_DYJets_0PU-SUB/ 2017_Sep13-2_Upgrade_QCD_200PU-SUB/  2017_Sep13-2_Upgrade_VBF_200PU-SUB/
#2017_Sep13-2_Upgrade_GGH_0PU-SUB/    2017_Sep13-2_Upgrade_TTbar_0PU-SUB/
#2017_Sep13-2_Upgrade_GGH_200PU-SUB/  2017_Sep13-2_Upgrade_VBF_0PU-SUB/

submitDir="2017_Sep13-2_Upgrade"
mergeDir="Htt_Oct6"

cd /scratch/ojalvo/${mergeDir}_200PU

EventWeightsIterative outputFile='ggH125.root'     weight=3.045965       histoName='TT/results'  &
EventWeightsIterative outputFile='vbfH125.root'    weight=0.2371314      histoName='TT/results'  &
EventWeightsIterative outputFile='ttBar.root'      weight=831.76         histoName='TT/results'  &
EventWeightsIterative outputFile='DYJets.root'     weight=4854.0         histoName='TT/results'  &
EventWeightsIterative outputFile='QCD.root'        weight=1              histoName='TT/results'  &

cd /scratch/ojalvo/${mergeDir}_0PU

EventWeightsIterative outputFile='ggH125.root'     weight=3.045965       histoName='TT/results'  &
EventWeightsIterative outputFile='vbfH125.root'    weight=0.2371314      histoName='TT/results'  &
EventWeightsIterative outputFile='ttBar.root'      weight=831.76         histoName='TT/results'  &
EventWeightsIterative outputFile='DYJets.root'     weight=4854.0         histoName='TT/results'  &
EventWeightsIterative outputFile='QCD.root'        weight=1              histoName='TT/results'  &