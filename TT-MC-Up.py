import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '91X_upgrade2023_realistic_v2'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(400)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-022EEFB6-B058-E711-9A19-0025907B50E4.root'
        'file:/hdfs/store/user/ymaravin/CRAB/DYJetsToLL_M-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/crab_job_phase2_DYJetsToLL_test/170724_102227/0000/step4_1.root'
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-0215E0C6-3758-E711-9095-F02FA768CF8A.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02174737-675E-E711-BDA3-782BCB539695.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-022EEFB6-B058-E711-9A19-0025907B50E4.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-023ACFA2-025C-E711-9421-D4AE527EEA1D.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-024753C1-FB58-E711-869C-48FD8E069BA7.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-0248CC58-2E5B-E711-8123-5065F3810301.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-025C6ABB-325B-E711-82FE-782BCB20EDFD.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02793B01-4E5C-E711-BBE0-002590D9D8D4.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-027B34F0-5C59-E711-9D10-48FD8E28249D.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02BC4910-5A59-E711-A533-0090FAA57F34.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02C1CE34-2E59-E711-96E6-002590D0B080.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02C32D21-5459-E711-8C03-0CC47A4DED58.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02CAE3E0-6359-E711-AE38-00259073E4BC.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02DB74F5-8C5B-E711-A7D6-0025901ABB72.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02E7BAB1-805E-E711-93A4-1866DAEEB358.root',
        #'file:/hdfs/store/user/ymaravin/2017_Aug04_DYJetsToLL_M-50_PU200-SUB/SUB-02F556ED-4A5E-E711-8A8B-0CC47AA992AE.root'
        #'file:/cms/ojalvo/Timing-Htt/VBF-Htt-PU200-MINI.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisToolsUpgrade import *
defaultReconstructionMC(process,'HLT2',
        [
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v2'
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTauUpgrade_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)

#Specifies which gen particles we wish to keep, this collection is used in the
#RecoTools/interface/CompositePtrCandidateT1T2MEtAlgorithm.h
#Most of the algorithm tools are done in the composite ptr candidate algorithm 
#module. 
createGeneratedParticles(process,
        'genDaughters',
        [
            "keep++ pdgId = {Z0}",
            "keep pdgId = {tau+}",
            "keep pdgId = {tau-}",
            "keep pdgId = {mu+}",
            "keep pdgId = {mu-}",
            "keep pdgId = 6",
            "keep pdgId = -6",
            "keep pdgId = 11",
            "keep pdgId = -11",
            "keep pdgId = 25",
            "keep pdgId = 35",
            "keep pdgId = 37",
            "keep pdgId = 36"
            ]
        )

#TBH, I am not sure if this is currently used.
createGeneratedParticles(process,
        'genTauCands',
        [
            "keep pdgId = {tau+} & mother.pdgId()= {Z0}",
            "keep pdgId = {tau-} & mother.pdgId() = {Z0}"
            ]
        )

#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleToolsUpgrade import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTree','diTausSync')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')

#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

