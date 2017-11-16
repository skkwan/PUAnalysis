{
   gROOT->ProcessLine(".L ../../ROOT/plotMacros/makePlotHThTh.C");

//makeLTauStack(TString name,TString file,TString dir,int s,TString labelX,TString units = "GeV",bool left=false,TString channel = "",TString json = "Golden",bool log = false,bool dndm=false,bool doRatio = false)

   //makeLTauStack("~/www/Research/muTau_m_vis","muTauPlots/muTau_m_vis.root","mt_inclusive",0,"visible mass","GeV",false,"#tau_{#mu}#tau_{h}","Golden",true,false,true);

   //diTauPlots_VBF/tauTau_decayMode_1.root
   TString outFile = "~/www/htt_upgrade_VBF_Oct23_col2/";
   TString inFile = "diTauPlots_VBF/";
   makeDiTauStack(outFile+"diTau_mvis_vbf",inFile+"tauTau_m_vis.root","tt_vbf",3,"m_{vis}","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_decayMode_2",inFile+"tauTau_decayMode_2.root","tt_vbf",3,"decayMode_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_decayMode_1",inFile+"tauTau_decayMode_1.root","tt_vbf",3,"decayMode_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_charge",inFile+"tauTau_charge.root","tt_vbf",3,"charge","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_eta_2",inFile+"tauTau_eta_2.root","tt_vbf",3,"eta_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_eta_1",inFile+"tauTau_eta_1.root","tt_vbf",3,"eta_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_gen_match_2",inFile+"tauTau_gen_match_2.root","tt_vbf",3,"gen_match_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_gen_match_1",inFile+"tauTau_gen_match_1.root","tt_vbf",3,"gen_match_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_m_2",inFile+"tauTau_m_2.root","tt_vbf",3,"m_2","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_m_1",inFile+"tauTau_m_1.root","tt_vbf",3,"m_1","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jeta_2",inFile+"tauTau_jeta_2.root","tt_vbf",3,"jeta_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jeta_1",inFile+"tauTau_jeta_1.root","tt_vbf",3,"jeta_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jphi_2",inFile+"tauTau_jphi_2.root","tt_vbf",3,"jphi_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jphi_1",inFile+"tauTau_jphi_1.root","tt_vbf",3,"jphi_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jpt_2",inFile+"tauTau_jpt_2.root","tt_vbf",3,"jpt_2","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jpt_1",inFile+"tauTau_jpt_1.root","tt_vbf",3,"jpt_1","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_pt_2",inFile+"tauTau_pt_2.root","tt_vbf",3,"#tau_{2} p_{T}","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_pt_1",inFile+"tauTau_pt_1.root","tt_vbf",3,"#tau_{1} p_{T}","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jdeta",inFile+"tauTau_jdeta.root","tt_vbf",3,"jdeta","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jdeta_2",inFile+"tauTau_jdeta_2.root","tt_vbf",3,"jdeta_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jdeta_1",inFile+"tauTau_jdeta_1.root","tt_vbf",3,"jdeta_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jdphi_2",inFile+"tauTau_jdphi_2.root","tt_vbf",3,"jdphi_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jdphi_1",inFile+"tauTau_jdphi_1.root","tt_vbf",3,"jdphi_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jpt_res_2",inFile+"tauTau_jpt_res_2.root","tt_vbf",3,"jpt_2 resolution","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jpt_res_1",inFile+"tauTau_jpt_res_1.root","tt_vbf",3,"jpt_1 resolution","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_ptH",inFile+"tauTau_pth.root","tt_vbf",3,"p_{T} h","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_ptJJ",inFile+"tauTau_ptJJ.root","tt_vbf",3,"p_{T}(JJ)","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_met",inFile+"tauTau_met.root","tt_vbf",3,"MET","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_mJJ",inFile+"tauTau_mjj.root","tt_vbf",3,"m(JJ)","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_njets",inFile+"tauTau_njets.root","tt_vbf",3,"NJETS","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);


   outFile = "~/www/htt_upgrade_VBF_MTD_Oct23_col2/";
   inFile = "diTauPlots_VBF_MTD/";
   makeDiTauStack(outFile+"diTau_mvis_vbf",inFile+"tauTau_m_vis.root","tt_vbf",3,"m_{vis}","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_decayMode_2",inFile+"tauTau_decayMode_2.root","tt_vbf",3,"decayMode_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_decayMode_1",inFile+"tauTau_decayMode_1.root","tt_vbf",3,"decayMode_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_charge",inFile+"tauTau_charge.root","tt_vbf",3,"charge","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_eta_2",inFile+"tauTau_eta_2.root","tt_vbf",3,"eta_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_eta_1",inFile+"tauTau_eta_1.root","tt_vbf",3,"eta_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_gen_match_2",inFile+"tauTau_gen_match_2.root","tt_vbf",3,"gen_match_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_gen_match_1",inFile+"tauTau_gen_match_1.root","tt_vbf",3,"gen_match_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_m_2",inFile+"tauTau_m_2.root","tt_vbf",3,"m_2","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_m_1",inFile+"tauTau_m_1.root","tt_vbf",3,"m_1","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jeta_2",inFile+"tauTau_jeta_2.root","tt_vbf",3,"jeta_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jeta_1",inFile+"tauTau_jeta_1.root","tt_vbf",3,"jeta_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jphi_2",inFile+"tauTau_jphi_2.root","tt_vbf",3,"jphi_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jphi_1",inFile+"tauTau_jphi_1.root","tt_vbf",3,"jphi_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jpt_2",inFile+"tauTau_jpt_2.root","tt_vbf",3,"jpt_2","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jpt_1",inFile+"tauTau_jpt_1.root","tt_vbf",3,"jpt_1","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_pt_2",inFile+"tauTau_pt_2.root","tt_vbf",3,"#tau_{2} p_{T}","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_pt_1",inFile+"tauTau_pt_1.root","tt_vbf",3,"#tau_{1} p_{T}","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jdeta",inFile+"tauTau_jdeta.root","tt_vbf",3,"jdeta","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jdeta_2",inFile+"tauTau_jdeta_2.root","tt_vbf",3,"jdeta_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jdeta_1",inFile+"tauTau_jdeta_1.root","tt_vbf",3,"jdeta_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jdphi_2",inFile+"tauTau_jdphi_2.root","tt_vbf",3,"jdphi_2","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jdphi_1",inFile+"tauTau_jdphi_1.root","tt_vbf",3,"jdphi_1","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_jpt_res_2",inFile+"tauTau_jpt_res_2.root","tt_vbf",3,"jpt_2 resolution","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_jpt_res_1",inFile+"tauTau_jpt_res_1.root","tt_vbf",3,"jpt_1 resolution","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_ptH",inFile+"tauTau_pth.root","tt_vbf",3,"p_{T} h","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_ptJJ",inFile+"tauTau_ptJJ.root","tt_vbf",3,"p_{T}(JJ)","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_met",inFile+"tauTau_met.root","tt_vbf",3,"MET","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);

   makeDiTauStack(outFile+"diTau_mJJ",inFile+"tauTau_mjj.root","tt_vbf",3,"m(JJ)","GeV",false,"#tau_{h}#tau_{h}","Golden",false,false,true);
   makeDiTauStack(outFile+"diTau_njets",inFile+"tauTau_njets.root","tt_vbf",3,"NJETS","",false,"#tau_{h}#tau_{h}","Golden",false,false,true);


}
