int copyAll(){

  gROOT->ProcessLine(".L copyNtuples.C");
  TString selections = "pt_1>45&&abs(eta_1)<2.1&&abs(eta_2)<2.1&&diLeptons==0&&extraelec_veto==0&&extramuon_veto==0&&againstMuonTight3_1>0&&againstMuonTight3_2>0&&againstElectronVLooseMVA6_1>0&&againstElectronVLooseMVA6_2>0&&(((isoMed_1>0.5&&isoTight_2<0.5&&isoLoose_2>0.5)||(isoMed_2>0.5&&isoTight_1<0.5&&isoLoose_1>0.5))||(isoTight_1>0.5&&isoTight_2>0.5))";

  TString directory = "/scratch/ojalvo/CP2016";
  copyNtuples(directory,"tauDATA-B.root",selections);  
  copyNtuples(directory,"tauDATA-C.root",selections);  
  copyNtuples(directory,"tauDATA-D.root",selections);  
  copyNtuples(directory,"tauDATA-E.root",selections);  
  copyNtuples(directory,"tauDATA-F.root",selections);  
  copyNtuples(directory,"tauDATA-G.root",selections);  
  copyNtuples(directory,"tauDATA-H.root",selections);  
  //copyNtuples(directory,"tauDATA.root",selections);  
  /*
  copyNtuples(directory,"DiBoson.root",selections);
  copyNtuples(directory,"ggH120.root",selections);
  copyNtuples(directory,"ggH125.root",selections);
  copyNtuples(directory,"ggH130.root",selections);
  copyNtuples(directory,"ttH120.root",selections);
  copyNtuples(directory,"ttH125.root",selections);
  copyNtuples(directory,"ttH130.root",selections);
  copyNtuples(directory,"TT.root",selections);
  copyNtuples(directory,"vbfH120.root",selections);
  copyNtuples(directory,"vbfH125.root",selections);
  copyNtuples(directory,"vbfH130.root",selections);
  copyNtuples(directory,"WH120.root",selections);
  copyNtuples(directory,"WH125.root",selections);
  copyNtuples(directory,"WH130.root",selections);
  copyNtuples(directory,"WJETS.root",selections);
  copyNtuples(directory,"WmH120.root",selections);
  copyNtuples(directory,"WmH125.root",selections);
  copyNtuples(directory,"WmH130.root",selections);
  copyNtuples(directory,"WpH120.root",selections);
  copyNtuples(directory,"WpH125.root",selections);
  copyNtuples(directory,"WpH130.root",selections);
  copyNtuples(directory,"ZH120.root",selections);
  copyNtuples(directory,"ZH125.root",selections);
  copyNtuples(directory,"ZH130.root",selections);
  copyNtuples(directory,"ZJETS.root",selections);
  copyNtuples(directory,"tauDATA.root",selections);  
  */
}

