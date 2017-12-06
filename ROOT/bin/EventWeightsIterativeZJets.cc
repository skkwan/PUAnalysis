#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include "TFileMerger.h"
#include <iostream>

std::vector<float> data;
std::vector<float> mc;

void readdir(TDirectory *dir,optutl::CommandLineParser parser,std::vector<float> ev); 



int main (int argc, char* argv[]) 
{
   optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
   parser.addOption("histoName",optutl::CommandLineParser::kString,"Counter Histogram Name","EventSummary");
   parser.addOption("weight",optutl::CommandLineParser::kDouble,"Weight to apply",1.0);
   parser.addOption("branch",optutl::CommandLineParser::kString,"Branch","__WEIGHT__");
   parser.addOption("AllJets",   optutl::CommandLineParser::kString,"AllJets",  "DYJets.root");
   parser.addOption("ZeroJets",  optutl::CommandLineParser::kString,"ZeroJets", "DY0Jets.root");
   parser.addOption("OneJets",   optutl::CommandLineParser::kString,"OneJets",  "DY1Jets.root");
   parser.addOption("TwoJets",   optutl::CommandLineParser::kString,"TwoJets",  "DY2Jets.root");
   parser.addOption("ThreeJets", optutl::CommandLineParser::kString,"ThreeJets","DY3Jets.root");
   parser.addOption("FourJets",  optutl::CommandLineParser::kString,"FourJets", "DY4Jets.root");

   
   parser.parseArguments (argc, argv);
   

   TFile *w = new TFile(parser.stringValue("AllJets").c_str(),
			"READ");
   TH1F* evC;
   float evW = 0;
   if(w->IsOpen() && w != 0 ){
     std::cout<<"Opening all jets "<<std::endl;
     evC  = (TH1F*)w->Get(parser.stringValue("histoName").c_str());
     evW = evC->GetBinContent(1);
   }
   w->Close();
  
   TFile *w1 = new TFile(parser.stringValue("ZeroJets").c_str(),
			 "READ");
   TH1F* evC1;
   float evW1 = 0;
   if(w1->IsOpen()){
     evC1  = (TH1F*)w1->Get(parser.stringValue("histoName").c_str());
     evW1 = evC1->GetBinContent(1);
   }
   w1->Close();   

   TFile *w2 = new TFile(parser.stringValue("OneJets").c_str(),
			 "READ");
   TH1F* evC2;
   float evW2 = 0;
   if(w2->IsOpen()){
     evC2  = (TH1F*)w2->Get(parser.stringValue("histoName").c_str());
     evW2 = evC2->GetBinContent(1);
   }
   w2->Close();

   TFile *w3 = new TFile(parser.stringValue("TwoJets").c_str(),
			 "READ");
   TH1F* evC3;
   float evW3 = 0;
   if(w3->IsOpen()){
     evC3  = (TH1F*)w3->Get(parser.stringValue("histoName").c_str());
     evW3 = evC3->GetBinContent(1);
   }
   w3->Close();

   TFile *w4 = new TFile(parser.stringValue("ThreeJets").c_str(),
			 "READ");
   TH1F* evC4; 
   float evW4 = 0;
   if(w4->IsOpen()){
     evC4 = (TH1F*)w4->Get(parser.stringValue("histoName").c_str());
     evW4 = evC4->GetBinContent(1);
   }
   w4->Close();

   TFile *w5 = new TFile(parser.stringValue("FourJets").c_str(),
			 "READ");
   TH1F* evC5;
   float evW5 = 0;

   if(w5->IsOpen()){
     evC5  = (TH1F*)w5->Get(parser.stringValue("histoName").c_str());
     evW5 = evC5->GetBinContent(1);
   }
   w5->Close();
 
   printf("Found  %f Z+NJet Events\n",evW);
   printf("Found  %f Z+0Jet Events\n",evW1);
   printf("Found  %f Z+1Jet Events\n",evW2);
   printf("Found  %f Z+2Jet Events\n",evW3);
   printf("Found  %f Z+3Jet Events\n",evW4);
   printf("Found  %f Z+4Jet Events\n",evW4);
  
   //Note we are using the NNLo to LO from 13TeV here the 
   //difference from 13 to 14 TeV is about 3%
   double LOtoNNLO=5765.4/4954.0;
   double DYLo =evW/(LOtoNNLO*4954.0);
   double DYLo1=evW1/(LOtoNNLO*3452.9);
   double DYLo2=evW2/(LOtoNNLO*1012.5);
   double DYLo3=evW3/(LOtoNNLO*332.8);
   double DYLo4=evW4/(LOtoNNLO*101.8);
   double DYLo5=evW5/(LOtoNNLO*54.8);

   //double DYLo5=evW5/(LOtoNNLO*6.7);

 
   std::vector<float> ev;
   ev.push_back(DYLo);
   ev.push_back(DYLo1);
   ev.push_back(DYLo2);
   ev.push_back(DYLo3);
   ev.push_back(DYLo4);
   ev.push_back(DYLo5);
   

   if(evW>0){
     TFile *f0 = new TFile(parser.stringValue("AllJets").c_str(),
			   "UPDATE");
     readdir(f0,parser,ev);
     f0->Close();
   }
   
   if(evW1>0){
     TFile *f1 = new TFile(parser.stringValue("ZeroJets").c_str(),
			   "UPDATE");
     readdir(f1,parser,ev);
     f1->Close();
   }
   
   if(evW2>0){
     TFile *f2 = new TFile(parser.stringValue("OneJets").c_str(),
			   "UPDATE");  
     readdir(f2,parser,ev);
     f2->Close();
   }
   
   if(evW3>0){
     TFile *f3 = new TFile(parser.stringValue("TwoJets").c_str(),
			   "UPDATE");
     readdir(f3,parser,ev);
     f3->Close();
   }
   

   if( evW4>0 ){
   TFile *f4 = new TFile(parser.stringValue("ThreeJets").c_str(),
			 "UPDATE");
     readdir(f4,parser,ev);
     f4->Close();
   }
 

   if(evW5>0){
     TFile *f5 = new TFile(parser.stringValue("FourJets").c_str(),
			   "UPDATE");
     readdir(f5,parser,ev);
     f5->Close();
   }
   
} 


void readdir(TDirectory *dir,optutl::CommandLineParser parser,std::vector<float> ev) 
{
  TDirectory *dirsav = gDirectory;
  TIter next(dir->GetListOfKeys());
  TKey *key;
  while ((key = (TKey*)next())) {
    printf("Found key=%s \n",key->GetName());
    TObject *obj = key->ReadObj();

    if (obj->IsA()->InheritsFrom(TDirectory::Class())) {
      dir->cd(key->GetName());
      TDirectory *subdir = gDirectory;
      readdir(subdir,parser,ev);
      dirsav->cd();
    }
    else if(obj->IsA()->InheritsFrom(TTree::Class())) {
      TTree *t = (TTree*)obj;
      float weight;


      TBranch *newBranch = t->Branch(parser.stringValue("branch").c_str(),&weight,(parser.stringValue("branch")+"/F").c_str());
      int LHEProduct=0;
      int mLL=0;
      t->SetBranchAddress("LHEProduct_njet",&LHEProduct); //NJets
      t->SetBranchAddress("LHEProduct_mll",&mLL); //InvMass

      printf("Found tree -> weighting\n");
      for(Int_t i=0;i<t->GetEntries();++i){
	      t->GetEntry(i);
	      if(LHEProduct==0)
		weight = parser.doubleValue("weight")/(ev[0]+ev[1]); //0Jet
	      else if(LHEProduct==1)
		weight = parser.doubleValue("weight")/(ev[0]+ev[2]); //1Jet
	      else if(LHEProduct==2)
		weight = parser.doubleValue("weight")/(ev[0]+ev[3]); //2Jet
	      else if(LHEProduct==3)
		weight = parser.doubleValue("weight")/(ev[0]+ev[4]);
	      else if(LHEProduct==4)
		weight = parser.doubleValue("weight")/(ev[0]+ev[5]);
	      else 
		weight = parser.doubleValue("weight")/(ev[0]);

	      newBranch->Fill();
      }
      t->Write("",TObject::kOverwrite);
    }



  }

}
