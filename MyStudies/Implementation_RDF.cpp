/******************************************************/
/* Implementation_RDF.cpp                             */
/* Usage: root -l Implementation_RDF.cpp              */
/******************************************************/


/******************************************************/

int Implementation_RDF()
{

  // Prepare input tree to run on
  auto fileName = "/hdfs/store/user/ojalvo/ztt_weighted_Apr7_svFit/ggH125.root";
  auto treeName = "diTauEventTree/eventTree";

  // Create a RDataFrame, a class that allows us to interact with the data
  // contained in the tree.
  ROOT::RDataFrame d(treeName, fileName, {"m_sv"});
  
  // Example of a simple cut
  auto cut = d.Filter("m_sv > 0");
  auto nEntries = cut.Count();
  std::cout << *nEntries << " passed all filters" << std::endl;

  // Draw the results
  auto hCut = cut.Histo1D("m_sv");
  auto c = new TCanvas();
  hCut->DrawCopy();

  return 0;
}


/******************************************************/
