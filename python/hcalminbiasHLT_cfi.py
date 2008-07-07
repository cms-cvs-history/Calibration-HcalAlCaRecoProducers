import FWCore.ParameterSet.Config as cms

hcalminbiasHLT = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('AlCa_HcalPhiSym'),
    byName = cms.bool(True),
    andOr = cms.bool(True),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
)


