{
   gROOT->ProcessLine(".L ../../ROOT/plotMacros/makePlotHThTh.C");


   TString outFile = "~/www/htt_upgrade_VBF_lVeto_jec_QCD/";
   TString inFile = "diTauPlots_VBF_QCD/";
   makeDiTauStack(outFile+"diTau_mvis_vbf",inFile+"tauTau_m_vis.root","tt_vbf",3,"m_{vis}","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_gen_match_2",inFile+"tauTau_gen_match_2.root","tt_vbf",3,"gen_match_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_gen_match_1",inFile+"tauTau_gen_match_1.root","tt_vbf",3,"gen_match_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);



}
