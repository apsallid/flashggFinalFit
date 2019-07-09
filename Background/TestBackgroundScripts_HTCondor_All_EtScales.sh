#!/bin/bash


###############################################################################
FILE="/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ttHJetToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ttHJetToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ttHJetToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ttHJetToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ttHJetToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_ttHJetToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root"

DATA="/eos/cms/store/user/youying/flashggNtuples/merged_2016_workspace/VHToGG_preopt_stage0_2016/output_DoubleEG.root"

FILE125="output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H.root,output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF.root,output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root"
###############################################################################

EXT="VHToGG"

echo "Ext is $EXT"
PROCS="GG2H,VBF,TTH,QQ2HLL,QQ2HLNU,WH2HQQ,ZH2HQQ"
echo "Procs are $PROCS"
CATS="ZHLeptonicTag,WHLeptonicTag,VHLeptonicLooseTag"

echo "Cats are $CATS"
INTLUMI=35.92
echo "Intlumi is $INTLUMI"
BATCH="HTCONDOR"
echo "Batch is $BATCH"
QUEUE="tomorrow"
echo "Batch is $QUEUE"
BSWIDTH=3.400000
echo "Bswidth is $BSWIDTH"
NBINS=320
echo "Nbins is $NBINS"

SCALES="HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB"
#CALES="HighR9EB,HighR9EE,LowR9EB,LowR9EE"
#SCALES="HighR9EBLow,HighR9EBHigh,HighR9EELow,HighR9EEHigh,LowR9EBLow,LowR9EBHigh,LowR9EELow,LowR9EEHigh"
#SCALES="HighR9LowEB,HighR9HighEB,HighR9LowEE,HighR9HighEE,LowR9LowEB,LowR9HighEB,LowR9LowEE,LowR9HighEE"

SCALESCORR="MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB"
SCALESGLOBAL="NonLinearity,Geant4"
SMEARS="HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"

MASSLIST="120,123,124,125,126,127,130"
#MASSLIST="120,125,130"
MLOW=120
MHIGH=130
echo "Masslist is $MASSLIST"

SIGFILE="/afs/cern.ch/work/a/apsallid/CMS/Hgg/VHToGG/FinalFits/CMSSW_8_1_0/src/flashggFinalFit/Signal/outdir_${EXT}/CMS-HGG_sigfit_${EXT}.root"

##################### Create background model ##############################
#./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData --unblind

./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData
#./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData --bkgPlotsOnly
############################################################################

##################### Create datacard ######################################
#./runFinalFitsScripts.sh -i $FILE125 -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --dataFile $DATA --isData --datacardOnly --smears $SMEARS --scales $SCALES --scalesCorr $SCALESCORR --scalesGlobal $SCALESGLOBAL --doSTXS
############################################################################
#./runFinalFitsScripts.sh -i $FILE -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --dataFile $DATA --isData --combineOnly
#./runFinalFitsScripts.sh -i $FILE -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --dataFile $DATA --isData --combinePlotsOnly
