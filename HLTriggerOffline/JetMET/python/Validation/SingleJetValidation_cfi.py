import FWCore.ParameterSet.Config as cms

rootfile="relval220_ideal/ttbar_fastsim_output.root"

# calojetcoll="iterativeCone5CaloJets"
calojetcoll="hltIterativeCone5CaloJets"

hltlow15  ="HLT_L1Jet6U"
hltname15="HLT_Jet15U"
folderjet15="HLT/HLTJETMET/SingleJet15U"

hltlow30  ="HLT_Jet15U"
hltname30="HLT_Jet30U"
folderjet30="HLT/HLTJETMET/SingleJet30U"

hltlow50  ="HLT_Jet30U"
hltname50="HLT_Jet50U"
folderjet50="HLT/HLTJETMET/SingleJet50U"

hltlow70="HLT_Jet50U"
hltname70="HLT_Jet70U"
folderjet70="HLT/HLTJETMET/SingleJet70U"

hltlow100="HLT_Jet70U"
hltname100="HLT_Jet100U"
folderjet100="HLT/HLTJETMET/SingleJet100U"

hltlowM35="HLT_L1MET20"
hltnameM35="HLT_MET35"
folderMET35="HLT/HLTJETMET/SingleMET35"

hltlowM45="HLT_L1MET20"
hltnameM45="HLT_MET45"
folderMET45="HLT/HLTJETMET/SingleMET45"

hltlowM60="HLT_MET35"
hltnameM60="HLT_MET60"
folderMET60="HLT/HLTJETMET/SingleMET60"

hltlowM100="HLT_MET60"
hltnameM100="HLT_MET100"
folderMET100="HLT/HLTJETMET/SingleMET100"

hltlowMHT="HLT_HT200"
hltnameMHT="HLT_HT300_MHT100"
folderMHT100="HLT/HLTJETMET/HT300MHT100"

hltlowQJ30="HLT_L1Jet15"
hltnameQJ30="HLT_QuadJet30"
folderQJ30="HLT/HLTJETMET/QuadJet30"

hltlowQJ60="HLT_L1Jet15"
hltnameQJ60="HLT_QuadJet60"
folderQJ60="HLT/HLTJETMET/QuadJet60"


SingleJetPathVal15 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderjet15),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlow15),
    HLTPath               = cms.untracked.InputTag(hltname15),
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),
)

SingleJetPathVal30 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderjet30),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlow30),
    HLTPath               = cms.untracked.InputTag(hltname30),
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),
)

SingleJetPathVal50 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderjet50),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlow50),
    HLTPath               = cms.untracked.InputTag(hltname50),
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),
)

SingleJetPathVal70 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderjet70),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlow70),
    HLTPath               = cms.untracked.InputTag(hltname70),                                  
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),                                  
)

SingleJetPathVal100 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderjet100),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlow100),
    HLTPath               = cms.untracked.InputTag(hltname100),                                   
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),
)

SingleMETPathVal35 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderMET35),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlowM35),
    HLTPath               = cms.untracked.InputTag(hltnameM35),                                  
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),                                  
)

SingleMETPathVal45 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderMET45),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlowM45),
    HLTPath               = cms.untracked.InputTag(hltnameM45),                                  
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),                                  
)

SingleMETPathVal60 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderMET60),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlowM60),
    HLTPath               = cms.untracked.InputTag(hltnameM60),                                  
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),                                  
)

SingleMETPathVal100 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderMET100),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlowM100),
    HLTPath               = cms.untracked.InputTag(hltnameM100),                                  
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),                                  
)

HTMHTPath = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderMHT100),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlowMHT),
    HLTPath               = cms.untracked.InputTag(hltnameMHT),                                  
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),                                  
)

QuadJetPathVal30 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderQJ30),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlowQJ30),
    HLTPath               = cms.untracked.InputTag(hltnameQJ30),
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),
)


QuadJetPathVal60 = cms.EDAnalyzer("HLTJetMETValidation",
    triggerEventObject    = cms.untracked.InputTag("hltTriggerSummaryRAW","","HLT"),
    DQMFolder             = cms.untracked.string(folderQJ60),
    OutputFileName        = cms.untracked.string(rootfile),
    LogFileName           = cms.untracked.string('JetMETSingleJetValidation.log'),
    HLTLow                = cms.untracked.InputTag(hltlowQJ60),
    HLTPath               = cms.untracked.InputTag(hltnameQJ60),
    CaloJetAlgorithm      = cms.untracked.InputTag(calojetcoll),
    GenJetAlgorithm       = cms.untracked.InputTag("iterativeCone5GenJets"),
    CaloMETCollection     = cms.untracked.InputTag("hltMet"),
    GenMETCollection      = cms.untracked.InputTag("genMetCalo"),
    HLTriggerResults = cms.InputTag("TriggerResults::HLT"),
)

#SingleJetValidation = cms.Sequence(SingleJetPathVal + SingleJetL2Val + SingleJetL25Val+SingleJetL3Val)
SingleJetValidation = cms.Sequence(SingleJetPathVal15 + SingleJetPathVal30 + SingleJetPathVal50 + SingleJetPathVal70 + SingleJetPathVal100 +
                                   SingleMETPathVal35 +
                                   SingleMETPathVal45 +
                                   SingleMETPathVal60 +
                                   SingleMETPathVal100 +
                                   HTMHTPath +
                                   QuadJetPathVal30 + QuadJetPathVal60
                                   )


