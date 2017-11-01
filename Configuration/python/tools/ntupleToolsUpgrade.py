import FWCore.ParameterSet.Config as cms

#from PUAnalysis.Configuration.tools.analysisTools import TriggerPaths,TriggerRes,TriggerProcess,TriggerFilter

#from RecoMET.METFilters.BadChargedCandidateFilter_cfi import *


def makeCollSize(srcName,tagName):
  PSet = cms.PSet(
        pluginType = cms.string("CollectionSizeFiller"),
        src        = cms.InputTag(srcName),
        tag        = cms.string(tagName)
  )
  return PSet

def makeCollSizeVeto(srcName,size, tagName):
  PSet = cms.PSet(
        pluginType = cms.string("CollectionSizeVetoFiller"),
        src        = cms.InputTag(srcName),
        size       = cms.untracked.double(size),
        tag        = cms.string(tagName)
  )
  return PSet

def makeCollSizeOS(srcName,size, tagName):
  PSet = cms.PSet(
        pluginType = cms.string("OSCollectionSizeFiller"),
        src        = cms.InputTag(srcName),
        size       = cms.untracked.double(size),
        tag        = cms.string(tagName)
  )
  return PSet



def makeLTauGeneric(plugin,sourceDiTaus,tagName,methodName):
   PSet = cms.PSet(
         pluginType  = cms.string(plugin),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
   )
   return PSet


##start diTaus

#def makeDiTauVBFPair(sourceDiTaus):
#   PSet = cms.PSet(
#         pluginType  = cms.string("PATDiTauPairVBFVariableFiller"),
#         src         = cms.InputTag(sourceDiTaus)
#   )
#   return PSet

def makeDiTauPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet

def makeDiTauCSVPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairCSVJetVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeDiTauPtNoPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairPtJetVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeDiTauPtPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairPtJetPairVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeDiTauEventWeight(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairWeightFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string("Mu"),
         isMuon      = cms.bool(True)
   )
   return PSet

def makeDiTauGenMatch(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairGenMCMatching"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet

def makeDiTauNBTag(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairNBTagFiller"),
         src         = cms.InputTag(sourceDiTaus),
         doEffMap      = cms.bool(True)
   )
   return PSet

def makeDiTauEffCSV(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairEffCSVFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet

def makeDiTauCSVShape(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairCSVReweightFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet


def makeDiTauJetCountPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairJetCountFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet

###finish ditaus
def makeMuTauPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet

def makeMuTauCSVPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairCSVJetVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeMuTauPtNoPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairPtJetVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeMuTauPtPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairPtJetPairVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeMuTauMET(sourceDiTaus, sourceMET, prefix):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairMETFiller"),
         src         = cms.InputTag(sourceDiTaus),
         met         = cms.InputTag(sourceMET),
         tag         = cms.string(prefix)
   )
   return PSet

def makeMuTauEventWeight(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairWeightFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string("Mu"),
         isMuon      = cms.bool(True)
   )
   return PSet

def makeMuTauEventWeightTmp(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairWeightFillerTmp"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string("MyMu"),
         isMuon      = cms.bool(True)
   )
   return PSet
def makeMuTauGenMatch(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairGenMCMatching"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet
def makeMuTauNBTag(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairNBTagFiller"),
         src         = cms.InputTag(sourceDiTaus),
         doEffMap      = cms.bool(True)
   )
   return PSet

def makeMuTauEffCSV(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairEffCSVFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet

def makeMuTauCSVShape(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairCSVReweightFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet







def makeMuTauJetCountPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairJetCountFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet


def makeEleTauPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet

def makeEleTauCSVPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairCSVJetVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeEleTauPtNoPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairPtJetVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeEleTauPtPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairPtJetPairVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet

def makeEleTauJetCountPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairJetCountFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet

def makeEleTauMET(sourceDiTaus, sourceMET, prefix):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairMETFiller"),
         src         = cms.InputTag(sourceDiTaus),
         met         = cms.InputTag(sourceMET),
         tag         = cms.string(prefix)
   )
   return PSet


def makeEleTauEventWeight(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairWeightFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string("Ele"),
         isMuon      = cms.bool(False)
   )
   return PSet

def makeEleTauEventWeightTmp(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairWeightFillerTmp"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string("MyEle"),
         isMuon      = cms.bool(False)
   )
   return PSet
def makeEleTauGenMatch(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairGenMCMatching"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet
def makeEleTauNBTag(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairNBTagFiller"),
         src         = cms.InputTag(sourceDiTaus),
         doEffMap      = cms.bool(True)
   )
   return PSet

def makeEleTauEffCSV(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairEffCSVFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet

def makeEleTauCSVShape(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATEleTauPairCSVReweightFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet


def addDiTauEventTree(process,name,src = 'diTausOS', srcLL = 'diMuonsOSSorted', srcU='TightMuons', srcE='TightElectrons',triggerCollection='HLT',srcEE = 'diEleOSSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              genEvent = cms.InputTag('generator'),
                              coreCollections = cms.InputTag(src),
#                               trigger = cms.PSet(
#                                   pluginType = cms.string("TriggerFiller"),
#			           src        = cms.InputTag("TriggerResults","",triggerCollection),
#			           prescales = cms.InputTag("patTrigger"),
#                                   paths      = cms.vstring(TriggerPaths)
#                               ),
                               pu = cms.PSet(
                                   pluginType = cms.string("PUFiller"),
                                   src        = cms.InputTag("slimmedAddPileupInfo"),
                                   tag        = cms.string("pu")
                               ),
                               cov = cms.PSet(
                                   pluginType = cms.string("METSignificanceFiller"),
                                   src        = cms.InputTag("METSignificance"),
                                   tag        = cms.string("metcov")
                               ),
                               PVsSync = cms.PSet(
                                   pluginType = cms.string("VertexSizeFiller"),
                                   src        = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                   tag        = cms.string("npv")
                               ),
                               PVs = cms.PSet(
                                   pluginType = cms.string("VertexSizeFiller"),
                                   src        = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                   tag        = cms.string("vertices")
                              ),
                              diTauGenMCMatch = makeDiTauGenMatch(src),
#                              metfilter = cms.PSet(
#                                  pluginType = cms.string("TriggerFilterFiller"),
#                                  src = cms.InputTag(TriggerRes,"",TriggerFilter),
#                                  BadChargedCandidateFilter = cms.InputTag("BadChargedCandidateFilter"),
#                                  BadPFMuonFilter           = cms.InputTag("BadPFMuonFilter"),
#                                  paths      = cms.vstring(
#                                      "Flag_noBadMuons",
#                                      "Flag_HBHENoiseFilter",
#                                      "Flag_HBHENoiseIsoFilter",
#                                      "Flag_globalTightHalo2016Filter",
#                                      "Flag_goodVertices",
#                                      "Flag_eeBadScFilter",
#                                      "Flag_EcalDeadCellTriggerPrimitiveFilter"
#                                      )
#                              ),
                              diTauPt1 =  makeDiTauPair(src,"pt_1","leg1.pt"),
                              diTauPt2 =  makeDiTauPair(src,"pt_2","leg2.pt"), 
                              diTauEta1 = makeDiTauPair(src,"eta_1","leg1.eta"),
                              diTauEta2 = makeDiTauPair(src,"eta_2","leg2.eta"),
                              diTauPhi1 = makeDiTauPair(src,"phi_1","leg1.phi"),
                              diTauPhi2 = makeDiTauPair(src,"phi_2","leg2.phi"),
                              diTauHadMass1 = makeDiTauPair(src,"m_1",'leg1.mass()'),
                              diTauHadMass2 = makeDiTauPair(src,"m_2",'leg2.mass()'),
                              diTauCharge = makeDiTauPair(src,"charge","charge"),
                              q_1 = makeDiTauPair(src,"q_1","leg1.charge"),
                              q_2 = makeDiTauPair(src,"q_2","leg2.charge"),
                              diTauPt = makeDiTauPair(src,"pth","pt"),#FILLED
                              diTauHT = makeDiTauPair(src,"ht","ht"),#FILLED
                              diTauMass = makeDiTauPair(src,"m_vis","mass"),#FILLED
                              #diTauSVPt = makeDiTauPair(src,"pt_sv","svPt"),#FILLEDATLATERSTAGE
                              #diTauSVMass = makeDiTauPair(src,"m_sv","svMass"),#FILLEDATLATERSTAGE
			      diTaulVeto = makeDiTauPair(src,"lVeto","lVeto"),
		              diTauTopGenPt = makeDiTauPair(src,"topGenPt","topGenPt"),#FIXME
		              diTauAntiTopGenPt = makeDiTauPair(src,"antiTopGenPt","antiTopGenPt"),#FIXM

                              diTauFullPt = makeDiTauPair(src,"fullPt","fullPt"),#FILLED
                              diTauEta = makeDiTauPair(src,"fullEta","fullEta"),#FILLED
                              diTauPhi = makeDiTauPair(src,"fullPhi","fullPhi"),#FILLED
                              diTauE = makeDiTauPair(src,"fullEnergy","fullEnergy"),#FILLED
                              diTauMET = makeDiTauPair(src,"met","met.pt()"),#FILLED
                              diTauMETPhi = makeDiTauPair(src,"metphi","met.phi()"),#FILLED

                              diTauMT = makeDiTauPair(src,"mt12","mt12MET"),#FILLED
                              diTauMT1 = makeDiTauPair(src,"mt_1","mt1MET"),#FILLED
                              diTaupfMT1 = makeDiTauPair(src,"pfmt_1","mt1MET"),#FILLED
                              diTauMT2 = makeDiTauPair(src,"mt_2","mt2MET"),#FILLED
                              diTaupfMT2 = makeDiTauPair(src,"pfmt_2","mt2MET"),#FILLED
                              

			      #diTauMassLL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLmass","mass"),
                              #diTauPt1LL =  makeLTauGeneric("PATMuPairFiller",srcLL,"LLpt_1","leg1.pt"), #FILLED
                              #diTauPt2LL =  makeLTauGeneric("PATMuPairFiller",srcLL,"LLpt_2","leg2.pt"), #FILLED
                              #diTauEta1LL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLeta_1","leg1.eta"),#FILLED
                              #diTauEta2LL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLeta_2","leg2.eta"),#FILLED
                              #diTauPhi1LL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLphi_1","leg1.phi"),#FILLED
                              #diTauPhi2LL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLphi_2","leg2.phi"),#FILLED

			      diTauMassEE = makeLTauGeneric("PATElePairFiller",srcEE,"EEmass","mass"),
                              diTauPt1EE =  makeLTauGeneric("PATElePairFiller",srcEE,"EEpt_1","leg1.pt"), #FIEEED
                              diTauPt2EE =  makeLTauGeneric("PATElePairFiller",srcEE,"EEpt_2","leg2.pt"), #FIEEED
                              diTauEta1EE = makeLTauGeneric("PATElePairFiller",srcEE,"EEeta_1","leg1.eta"),#FIEEED
                              diTauEta2EE = makeLTauGeneric("PATElePairFiller",srcEE,"EEeta_2","leg2.eta"),#FIEEED
                              diTauPhi1EE = makeLTauGeneric("PATElePairFiller",srcEE,"EEphi_1","leg1.phi"),#FIEEED
                              diTauPhi2EE = makeLTauGeneric("PATElePairFiller",srcEE,"EEphi_2","leg2.phi"),#FIEEED

                              #diTauEffCSV = makeDiTauEffCSV(src),  ##need to put csv eff back in
                              #diTauCSVShape = makeDiTauCSVShape(src), ## need to put csv shape back in
                              #diTauJES = makeDiTauVBFPair(src),#FILLED

                              diTauSize = makeCollSize(src,"nCands"),
                              diTauOS = makeCollSizeOS(src,0,"os"),
                              genTaus = makeCollSize("genTauCands","genTaus"), 
                              muMuSize = makeCollSize(srcLL,"diLeptons"),#CHECKME
                              muMuSizeVeto = makeCollSizeVeto(srcLL,0,"dilepton_veto"),#CHECKME

                              eESize = makeCollSize(srcEE,"diLeptonsEE"),#CHECKME
                              eESizeVeto = makeCollSizeVeto(srcEE,0,"dileptonEE_veto"),#CHECKME

                              muonsSizeMT = makeCollSize(srcU,"tightMuons"),#FILLED
                              muonsSizeMTVeto = makeCollSizeVeto(srcU,0,"extramuon_veto"),#FILLED
                              muonsLooseSizeMT = makeCollSize("LooseMuons","looseMuons"),#FILLED
                              electronsSizeMT = makeCollSize(srcE,"tightElectrons"),#FILLED
                              electronsLooseSizeMT = makeCollSize("LooseElectrons","looseElectrons"),#FILLED
                              electronsSizeMTVeto = makeCollSizeVeto(srcE,0,"extraelec_veto"),#FILLED
                              #tauNIsoTracks =  makeDiTauPair(src,"tauNIsoTracks","leg2.userFloat('nIsoTracks')"), #FILLED
                              #tauNMatchedSeg =  makeDiTauPair(src,"tauMuonNMatchedSeg","leg2.userFloat('muonNMatchedSeg')"),#FILLED
                              #tauTauHadMatched = makeDiTauPair(src,"tauMuonMatched","leg2.userFloat('muonTauHadMatched')"),#FILLED
                              #tauLeadChargedHadrTrackPt = makeDiTauPair(src,"tauLeadChargedHadrTrackPt","leg2.userFloat('leadChargedHadrTrackPt')"),
                              diTauDecayModeLeg1 = makeDiTauPair(src,"decayMode_1",'leg1.decayMode()'),
                              diTauDecayModeLeg2 = makeDiTauPair(src,"decayMode_2",'leg2.decayMode()'),

                              diTauAgainstMuonTight3Leg1 = makeDiTauPair(src,"againstMuonTight3_1",'leg1.tauID("againstMuonTight3")'),
                              diTauAgainstMuonTight3Leg2 = makeDiTauPair(src,"againstMuonTight3_2",'leg2.tauID("againstMuonTight3")'),
                              diTauAgainstMuonLoose3Leg1 = makeDiTauPair(src,"againstMuonLoose3_1",'leg1.tauID("againstMuonLoose3")'),
                              diTauAgainstMuonLoose3Leg2 = makeDiTauPair(src,"againstMuonLoose3_2",'leg2.tauID("againstMuonLoose3")'),
                              diTauAgainstEleVLooseMVA6Leg1 = makeDiTauPair(src,"againstElectronVLooseMVA6_1",'leg1.tauID("againstElectronVLooseMVA6")'),
                              diTauAgainstEleVLooseMVA6Leg2 = makeDiTauPair(src,"againstElectronVLooseMVA6_2",'leg2.tauID("againstElectronVLooseMVA6")'),
                              diTauAgainstEleMVA6rawLeg1 = makeDiTauPair(src,"againstElectronMVA6Raw_1",'leg1.tauID("againstElectronMVA6Raw")'),
                              diTauAgainstEleMVA6rawLeg2 = makeDiTauPair(src,"againstElectronMVA6Raw_2",'leg2.tauID("againstElectronMVA6Raw")'),

                              diTauIsoLeg1 = makeDiTauPair(src,"iso_1",'leg1.tauID("byIsolationMVArun2v1DBoldDMwLTraw")'),
                              diTauIsoLeg2 = makeDiTauPair(src,"iso_2",'leg2.tauID("byIsolationMVArun2v1DBoldDMwLTraw")'),

                              diTauVTightIsoLeg1 = makeDiTauPair(src,"isoVTight_1",'leg1.tauID("byVTightIsolationMVArun2v1DBoldDMwLT")'),
                              diTauVTightIsoLeg2 = makeDiTauPair(src,"isoVTight_2",'leg2.tauID("byVTightIsolationMVArun2v1DBoldDMwLT")'),
                              diTauTightIsoLeg1 = makeDiTauPair(src,"isoTight_1",'leg1.tauID("byTightIsolationMVArun2v1DBoldDMwLT")'),
                              diTauTightIsoLeg2 = makeDiTauPair(src,"isoTight_2",'leg2.tauID("byTightIsolationMVArun2v1DBoldDMwLT")'),
                              diTauMediumIsoLeg1 = makeDiTauPair(src,"isoMed_1",'leg1.tauID("byMediumIsolationMVArun2v1DBoldDMwLT")'),
                              diTauMediumIsoLeg2 = makeDiTauPair(src,"isoMed_2",'leg2.tauID("byMediumIsolationMVArun2v1DBoldDMwLT")'),
                              diTauLooseIsoLeg1 = makeDiTauPair(src,"isoLoose_1",'leg1.tauID("byLooseIsolationMVArun2v1DBoldDMwLT")'),
                              diTauLooseIsoLeg2 = makeDiTauPair(src,"isoLoose_2",'leg2.tauID("byLooseIsolationMVArun2v1DBoldDMwLT")'),
                              diTauVLooseIsoLeg1 = makeDiTauPair(src,"isoVLoose_1",'leg1.tauID("byVLooseIsolationMVArun2v1DBoldDMwLT")'),
                              diTauVLooseIsoLeg2 = makeDiTauPair(src,"isoVLoose_2",'leg2.tauID("byVLooseIsolationMVArun2v1DBoldDMwLT")'),

			      diTauRawMVAIso1 = makeDiTauPair(src,"isoMVARaw_1",'leg1.tauID("byIsolationMVArun2v1DBoldDMwLTraw")'),
			      diTauRawMVAIso2 = makeDiTauPair(src,"isoMVARaw_2",'leg2.tauID("byIsolationMVArun2v1DBoldDMwLTraw")'),
			      diTauRawDBIso1 = makeDiTauPair(src,"isoDBRaw_1",'leg1.tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits")'),
			      diTauRawDBIso2 = makeDiTauPair(src,"isoDBRaw_2",'leg2.tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits")'),

                              diTauIsoLeg1NewCHIso3 =  makeDiTauPair(src,"newCHIso3_1",'leg1.userFloat("newChIso3")'),
                              diTauIsoLeg2NewCHIso3 =  makeDiTauPair(src,"newCHIso3_2",'leg2.userFloat("newChIso3")'),

                              diTauIsoLeg1NewCHIso4 =  makeDiTauPair(src,"newCHIso4_1",'leg1.userFloat("newChIso4")'),
                              diTauIsoLeg2NewCHIso4 =  makeDiTauPair(src,"newCHIso4_2",'leg2.userFloat("newChIso4")'),

                              diTauIsoLeg1NewCHIso6 =  makeDiTauPair(src,"newCHIso6_1",'leg1.userFloat("newChIso6")'),
                              diTauIsoLeg2NewCHIso6 =  makeDiTauPair(src,"newCHIso6_2",'leg2.userFloat("newChIso6")'),

                              diTauIsoLeg1NewCHIso12 =  makeDiTauPair(src,"newCHIso12_1",'leg1.userFloat("newChIso12")'),
                              diTauIsoLeg2NewCHIso12 =  makeDiTauPair(src,"newCHIso12_2",'leg2.userFloat("newChIso12")'),

                              diTauIsoLeg1NewCHIso18 =  makeDiTauPair(src,"newCHIso18_1",'leg1.userFloat("newChIso18")'),
                              diTauIsoLeg2NewCHIso18 =  makeDiTauPair(src,"newCHIso18_2",'leg2.userFloat("newChIso18")'),

                              diTauIsoLeg1NewCHiso3_ntracks =  makeDiTauPair(src,"newCHiso3_ntracks_1",'leg1.userFloat("newChIso3_ntracks")'),
                              diTauIsoLeg2NewCHIso3_ntracks =  makeDiTauPair(src,"newCHIso3_ntracks_2",'leg2.userFloat("newChIso3_ntracks")'),

                              diTauIsoLeg1NewCHIso4_ntracks =  makeDiTauPair(src,"newCHIso4_ntracks_1",'leg1.userFloat("newChIso4_ntracks")'),
                              diTauIsoLeg2NewCHIso4_ntracks =  makeDiTauPair(src,"newCHIso4_ntracks_2",'leg2.userFloat("newChIso4_ntracks")'),

                              diTauIsoLeg1NewCHIso6_ntracks =  makeDiTauPair(src,"newCHIso6_ntracks_1",'leg1.userFloat("newChIso6_ntracks")'),
                              diTauIsoLeg2NewCHIso6_ntracks =  makeDiTauPair(src,"newCHIso6_ntracks_2",'leg2.userFloat("newChIso6_ntracks")'),

                              diTauIsoLeg1NewCHIso12_ntracks =  makeDiTauPair(src,"newCHIso12_ntracks_1",'leg1.userFloat("newChIso12_ntracks")'),
                              diTauIsoLeg2NewCHIso12_ntracks =  makeDiTauPair(src,"newCHIso12_ntracks_2",'leg2.userFloat("newChIso12_ntracks")'),

                              diTauIsoLeg1NewCHIso18_ntracks =  makeDiTauPair(src,"newCHIso18_ntracks_1",'leg1.userFloat("newChIso18_ntracks")'),
                              diTauIsoLeg2NewCHIso18_ntracks =  makeDiTauPair(src,"newCHIso18_ntracks_2",'leg2.userFloat("newChIso18_ntracks")'),

####Rerun

                              #diTauIsoLeg1ReRun =  makeDiTauPair(src,"isoRerun_1",'leg1.userFloat("byVTightIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauIsoLeg2ReRun =  makeDiTauPair(src,"isoRerun_2",'leg2.userFloat("byVTightIsolationMVArun2v1DBoldDMwLTRerun")'),

                              #diTauVTightIsoLeg1ReRun =  makeDiTauPair(src,"isoVTightRerun_1",'leg1.userFloat("byVTightIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauVTightIsoLeg2ReRun =  makeDiTauPair(src,"isoVTightRerun_2",'leg2.userFloat("byVTightIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauTightIsoLeg1ReRun =  makeDiTauPair(src,"isoTightRerun_1",'leg1.userFloat("byTightIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauTightIsoLeg2ReRun =  makeDiTauPair(src,"isoTightRerun_2",'leg2.userFloat("byTightIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauMediumIsoLeg1ReRun =  makeDiTauPair(src,"isoMedRerun_1",'leg1.userFloat("byMediumIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauMediumIsoLeg2ReRun =  makeDiTauPair(src,"isoMedRerun_2",'leg2.userFloat("byMediumIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauLooseIsoLeg1ReRun =  makeDiTauPair(src,"isoLooseRerun_1",'leg1.userFloat("byLooseIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauLooseIsoLeg2ReRun =  makeDiTauPair(src,"isoLooseRerun_2",'leg2.userFloat("byLooseIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauVLooseIsoLeg1ReRun =  makeDiTauPair(src,"isoVLooseRerun_1",'leg1.userFloat("byVLooseIsolationMVArun2v1DBoldDMwLTRerun")'),
                              #diTauVLooseIsoLeg2ReRun =  makeDiTauPair(src,"isoVLooseRerun_2",'leg2.userFloat("byVLooseIsolationMVArun2v1DBoldDMwLTRerun")'),

			      #diTauRawMVAIso1ReRun =  makeDiTauPair(src,"isoMVARawRerun_1",'leg1.userFloat("byIsolationMVArun2v1DBoldDMwLTrawRerun")'),
			      #diTauRawMVAIso2ReRun =  makeDiTauPair(src,"isoMVARawRerun_2",'leg2.userFloat("byIsolationMVArun2v1DBoldDMwLTrawRerun")'),

####Rerun
                              diTauGenPt1 = makeDiTauPair(src,"genPt1",'p4Leg1gen().pt()'),
                              diTauGenPt2 = makeDiTauPair(src,"genPt2",'p4Leg2gen().pt()'),
                              diTauPdg1 = makeDiTauPair(src,"pdg1",'genPdg1()'),
                              diTauPdg2 = makeDiTauPair(src,"pdg2",'genPdg2()'),
                              diTauVisGenPt1 = makeDiTauPair(src,"genVisPt1",'p4VisLeg1gen().pt()'),
                              diTauVisGenPt2 = makeDiTauPair(src,"genVisPt2",'p4VisLeg2gen().pt()'),
                              diTauGenVisMass = makeDiTauPair(src,"genVisMass",'p4VisGen().M()'),
                              diTauGenMassMatched = makeDiTauPair(src,"genFullMassMatched",'p4gen().M()'),
                              diTauGenMass = makeDiTauPair(src,"fullGenMass",'genBosonMass()'),
                              diTauGenBosonPt = makeDiTauPair(src,"genpT",'p4GenBoson().pt()'),
                              diTauGenBosonMass = makeDiTauPair(src,"genMass",'p4GenBoson().M()'),
                              diTauGenBosonPx = makeDiTauPair(src,"genpX",'p4GenBoson().px()'),
                              diTauGenBosonPy = makeDiTauPair(src,"genpY",'p4GenBoson().py()'),
                              diTauGenBosonVisPx = makeDiTauPair(src,"vispX",'p4GenBosonVis().px()'),
                              diTauGenBosonVisPy = makeDiTauPair(src,"vispY",'p4GenBosonVis().py()'),
                              #Jets
                              diTauMJJReg = makeDiTauPair(src,"mJJReg","mJJReg"),#FIXME
                              diTauMJJ    = makeDiTauPair(src,"mJJ","mJJ"),#FILLED
                              diTauJJPt   = makeDiTauPair(src,"ptJJ","ptJJ"),
                              diTauJJEta  = makeDiTauPair(src,"etaJJ","etaJJ"),

                              diTauJJEnergy = makeDiTauPair(src,"energyJJ","energyJJ"),
                              diTauVBFDEta = makeDiTauPair(src,"jdeta","vbfDEta"),
                              diTauVBFMass = makeDiTauPair(src,"mjj","vbfMass"),#vbfMass
                              diTauVBFJets20 = makeDiTauPair(src,"njetingap20","vbfNJetsGap20"),
                              diTauVBFJets30 = makeDiTauPair(src,"njetingap","vbfNJetsGap30"),
                              ##FIX ME apply loose ID
                              #diTauJetsPt20nbtag = makeDiTauJetCountPair(src,"nbtag",'userFloat("isbtagged")&&pt()>20&&abs(eta)<2.4&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
                              diTauJetsPt20nbtagLoose = makeDiTauJetCountPair(src,"nbtagLooseNoSF",'pt()>20&&abs(eta)<2.4&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.46'),
                              diTauJetsPt20nbtagNoSF = makeDiTauJetCountPair(src,"nbtagNoSF",'pt()>20&&abs(eta)<2.4&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
                              #diTauJetsPt30nbtagNoSf = makeDiTauJetCountPair(src,"nbtag30",'userFloat("isbtagged")&&pt()>30&&abs(eta)<2.4&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
                              diTauJetsPt30nbtag = makeDiTauJetCountPair(src,"nbtag30",'pt()>30&&abs(eta)<2.4&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),

                              diTauJetsPt30njets = makeDiTauJetCountPair(src,"njets",'pt()>30&&abs(eta)<4.7'),
                              diTauJetsPt20njets = makeDiTauJetCountPair(src,"njetspt20",'pt()>20&&abs(eta)<4.7'),

                              diTauJet1PtPtSort = makeDiTauPtPair(src,"jpt_1",'abs(eta())<4.7&&pt()>20','pt()',0),
                              diTauJet2PtPtSort = makeDiTauPtPair(src,"jpt_2",'abs(eta())<4.7&&pt()>20','pt()',1),

                              diTauJet1EtaPtSort = makeDiTauPtPair(src,"jeta_1",'abs(eta())<4.7&&pt()>20','eta()',0),
                              diTauJet2EtaPtSort = makeDiTauPtPair(src,"jeta_2",'abs(eta())<4.7&&pt()>20','eta()',1),
                              diTauJet1PhiPtSort = makeDiTauPtPair(src,"jphi_1",'abs(eta())<4.7&&pt()>20','phi()',0),
                              diTauJet2PhiPtSort = makeDiTauPtPair(src,"jphi_2",'abs(eta())<4.7&&pt()>20','phi()',1),

                              diTauJet1GenPtPtSortDR = makeDiTauPtPair(src,"gen_jDR_1",'abs(eta())<4.7&&pt()>20','userFloat("genJetDR")',0),
                              diTauJet2GenPtPtSortDR = makeDiTauPtPair(src,"gen_jDR_2",'abs(eta())<4.7&&pt()>20','userFloat("genJetDR")',1),

                              diTauJet1GenPtPtSort = makeDiTauPtPair(src,"gen_jpt_1",'abs(eta())<4.7&&pt()>20','userFloat("genJetPt")',0),
                              diTauJet2GenPtPtSort = makeDiTauPtPair(src,"gen_jpt_2",'abs(eta())<4.7&&pt()>20','userFloat("genJetPt")',1),

                              diTauJet1GenEtaPtSort = makeDiTauPtPair(src,"gen_jeta_1",'abs(eta())<4.7&&pt()>20','userFloat("genJetEta")',0),
                              diTauJet2GenEtaPtSort = makeDiTauPtPair(src,"gen_jeta_2",'abs(eta())<4.7&&pt()>20','userFloat("genJetEta")',1),
                              diTauJet1GenPhiPtSort = makeDiTauPtPair(src,"gen_jphi_1",'abs(eta())<4.7&&pt()>20','userFloat("genJetPhi")',0),
                              diTauJet2GenPhiPtSort = makeDiTauPtPair(src,"gen_jphi_2",'abs(eta())<4.7&&pt()>20','userFloat("genJetPhi")',1),
####jet id
                              diTauJetsPt30njets_passid = makeDiTauJetCountPair(src,"njets_passid",'pt()>30&&abs(eta)<4.7&&userFloat("idTight_upgrade")>0'),
                              diTauJetsPt20njets_passid = makeDiTauJetCountPair(src,"njetspt20_passid",'pt()>20&&abs(eta)<4.7&&userFloat("idTight_upgrade")>0'),

                              diTauJet1PtPtSort_passid = makeDiTauPtPair(src,"jpassid_1",'abs(eta())<4.7&&pt()>20','userFloat("idTight_upgrade")',0),
                              diTauJet2PtPtSort_passid = makeDiTauPtPair(src,"jpassid_2",'abs(eta())<4.7&&pt()>20','userFloat("idTight_upgrade")',1),

###jet Id and Lepton ID applied
                              diTauJetsPt30njets_passid_veto = makeDiTauJetCountPair(src,"njets_passid_veto",'pt()>30&&abs(eta)<4.7&&userFloat("idTight_upgrade")>0&&userFloat("lepveto_upgrade")>0'),
                              diTauJetsPt20njets_passid_veto = makeDiTauJetCountPair(src,"njetspt20_passid_veto",'pt()>20&&abs(eta)<4.7&&userFloat("idTight_upgrade")>0&&userFloat("lepveto_upgrade")>0'),

                              diTauJet1PtPtSort_passid_veto = makeDiTauPtPair(src,"jpassid_veto_1",'abs(eta())<4.7&&pt()>20','userFloat("lepveto_upgrade")',0),
                              diTauJet2PtPtSort_passid_veto = makeDiTauPtPair(src,"jpassid_veto_2",'abs(eta())<4.7&&pt()>20','userFloat("lepveto_upgrade")',1),

                              higgsPt = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src        = cms.InputTag("genDaughters"),
                                  tag        = cms.string("higgsPt"),
                                  method     = cms.string('pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              diTauLHEProduct2 = cms.PSet(
                                  pluginType = cms.string("LHEProductFiller"),
                                  src        = cms.InputTag("externalLHEProducer"),
                                  tag        = cms.string("LHEProduct"),
                              )
                              )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)

