void copyNtuples(TString dir, TString file, TString cuts) {
  gSystem->Load("$ROOTSYS/test/libEvent");
  //Get old file, old tree and set top branch address
  TFile *oldfile;
  oldfile = new TFile(dir+"/"+file);

  TTree *oldtree = (TTree*)oldfile->Get("diTauEventTree/eventTree");
  //oldtree->Print();
  //gROOT->cd();
  std::cout<<"here1"<<std::endl;

  //Create a new file + a clone of old tree in new file

  TFile *newfile = new TFile(dir+"/reduce/"+file,"recreate");
  
  TDirectory * diTauEventTree = newfile->mkdir("diTauEventTree");
  diTauEventTree->cd();
  TTree *newTree = oldtree->CopyTree(cuts);
  //TTree *newtree = oldtree->CloneTree();
  std::cout<<"here2"<<std::endl;
  //newTree->Print();
  newfile->Write();
  delete oldfile;
  delete newfile;
}
