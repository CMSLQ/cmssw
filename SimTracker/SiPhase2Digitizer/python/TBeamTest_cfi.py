import FWCore.ParameterSet.Config as cms

tbeamTest = cms.EDAnalyzer("TBeamTest",
    Verbosity = cms.bool(False),
    TopFolderName = cms.string("TBeamSimulation"),
    OuterTrackerDigiSource    = cms.InputTag("mix", "Tracker"),                          
    NumbeOfDigisH = cms.PSet(
           Nbins = cms.int32(10),
           xmin = cms.double(-0.5),
           xmax = cms.double(9.5)
    ),
    PositionOfDigisH = cms.PSet(
           Nxbins = cms.int32(255),
           xmin   = cms.double(-0.5),
           xmax   = cms.double(254.5)
    ),
    NumberOfClustersH = cms.PSet(
           Nbins = cms.int32(20),
           xmin = cms.double(-0.5),
           xmax = cms.double(19.5)
    ),
    ClusterWidthH = cms.PSet(
           Nbins = cms.int32(10),
           xmin   = cms.double(-0.5),
           xmax   = cms.double(9.5)
    ),
    ClusterPositionH = cms.PSet(
      Nbins = cms.int32(508),
      xmin   = cms.double(-0.5),
      xmax   = cms.double(254.5)
    )  
)
