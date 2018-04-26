#!/usr/bin/env python
# code to make first-pass stxs transfer matrix plots

from os import walk
import ROOT as r
from collections import OrderedDict as od

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option('-k', '--key', default='GluGluHToGG', help='choose the sample to run on')
#parser.add_option('-d', '--doLoose', default=False, action='store_true', help='use loose photons (default false, ie use only tight photons)')
#(opts,args) = parser.parse_args()

r.gROOT.SetBatch(True)

#setup files 
ext          = 'fullStage1Test'
#ext          = 'reCategorised'
print 'ext = %s'%ext
#baseFilePath  = '/vols/cms/es811/FinalFits/ws_%s/'%ext
baseFilePath  = '/afs/cern.ch/work/a/apsallid/CMS/Hgg/flashgg_STXS_stage1/CMSSW_8_0_28/src/flashgg/Systematics/scripts/output/'
fileNames     = []

fileNames      = ['output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ttHJetToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root','output_ttHJetToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root','output_ttHJetToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root','output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root','output_ttHJetToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root','output_ttHJetToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root','output_ttHJetToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root'] 

'''
for root,dirs,files in walk(baseFilePath):
  for fileName in files: 
    if not fileName.startswith('output_'): continue
    if not fileName.endswith('.root'):     continue
    if ('pythia8.root' or 'BBH' or 'GG2HLL') in fileName: continue
    fileNames.append(fileName)
'''
fullFileNames = '' 
for fileName in fileNames: fullFileNames += baseFilePath+fileName+','
fullFileNames = fullFileNames[:-1]
fullFileNames = fullFileNames.split(',')

#define processes and categories
procs         = od()
for fileName in fileNames: 
  if 'M125' not in fileName: continue
  print fileName
  print fileName.split('pythia8_')[1].split('.root')[0]
  procs[ fileName.split('pythia8_')[1].split('.root')[0] ] = 0.
cats          = 'NOTAG,RECO_0J,RECO_1J_PTH_0_60,RECO_1J_PTH_60_120,RECO_1J_PTH_120_200,RECO_1J_PTH_GT200,RECO_GE2J_PTH_0_60,RECO_GE2J_PTH_60_120,RECO_GE2J_PTH_120_200,RECO_GE2J_PTH_GT200,RECO_VBFTOPO_JET3VETO,RECO_VBFTOPO_JET3,RECO_VH2JET,RECO_0LEP_PTV_0_150,RECO_0LEP_PTV_150_250_0J,RECO_0LEP_PTV_150_250_GE1J,RECO_0LEP_PTV_GT250,RECO_1LEP_PTV_0_150,RECO_1LEP_PTV_150_250_0J,RECO_1LEP_PTV_150_250_GE1J,RECO_1LEP_PTV_GT250,RECO_2LEP_PTV_0_150,RECO_2LEP_PTV_150_250_0J,RECO_2LEP_PTV_150_250_GE1J,RECO_2LEP_PTV_GT250,RECO_TTH_LEP,RECO_TTH_HAD'
#cats  = 'RECO_0J_Tag0,RECO_0J_Tag1,RECO_1J_PTH_0_60_Tag0,RECO_1J_PTH_0_60_Tag1,RECO_1J_PTH_60_120_Tag0,RECO_1J_PTH_60_120_Tag1,RECO_1J_PTH_120_200_Tag0,RECO_1J_PTH_120_200_Tag1,RECO_1J_PTH_GT200,'
#cats += 'RECO_GE2J_PTH_0_60_Tag0,RECO_GE2J_PTH_0_60_Tag1,RECO_GE2J_PTH_60_120_Tag0,RECO_GE2J_PTH_60_120_Tag1,RECO_GE2J_PTH_120_200_Tag0,RECO_GE2J_PTH_120_200_Tag1,RECO_GE2J_PTH_GT200_Tag0,RECO_GE2J_PTH_GT200_Tag1,RECO_VBFTOPO_JET3VETO_Tag0,RECO_VBFTOPO_JET3VETO_Tag1,RECO_VBFTOPO_JET3_Tag0,RECO_VBFTOPO_JET3_Tag1,'
#cats += 'RECO_WHLEP,RECO_ZHLEP,RECO_VHLEPLOOSE,RECO_VHMET,RECO_VHHAD,'
#cats += 'RECO_TTH_LEP,RECO_TTH_HAD'
#cats          = 'RECO_VBFTOPO_JET3VETO,RECO_VBFTOPO_JET3'

cats = cats.split(',')
stage0procs = {}
stage0procs['GG2H']    = 0.
stage0procs['VBF']     = 0.
stage0procs['WH2HQQ']  = 0.
stage0procs['ZH2HQQ']  = 0.
stage0procs['QQ2HLL']  = 0.
stage0procs['QQ2HLNU'] = 0.
stage0procs['QQ2HLNU'] = 0.
stage0procs['TTH'] = 0.
print procs 
print cats

nameMap  = {}
nameMap['GG2H']    = 'ggh'
nameMap['VBF']     = 'vbf'
nameMap['WH2HQQ']  = 'wh'
nameMap['ZH2HQQ']  = 'zh'
nameMap['QQ2HLL']  = 'zh'
nameMap['QQ2HLNU'] = 'wh'
nameMap['TTH'] = 'tth'

def main():
  checkZeros()
  #exit(0)
  for fileName in fullFileNames:
    if 'M125' not in fileName: continue
    theProc = fileName.split('pythia8_')[1].split('.root')[0]
    theProc0 = theProc.split('_')[0]
    print 'processing %s'%theProc
    theFile = r.TFile(fileName, 'READ')
    theWS = theFile.Get('tagsDumper/cms_hgg_13TeV')
    for cat in cats:
      dataName = '%s_125_13TeV_%s'%(nameMap[theProc0], cat)
      sumEntries = theWS.data(dataName).sumEntries()
      stage0procs[theProc0] += sumEntries
      procs[theProc] += sumEntries

  print '\n\n\nStage 1 fractions:'
  for proc,val in procs.iteritems():
    procTot = stage0procs[ proc.split('_')[0] ]
    theFrac = val / procTot
    print 'fraction for process %s is %1.4f'%(proc,theFrac)
  print '\n'

def checkZeros():
  print 'About to check for low sumEntries'
  #masses = [120,123,124,125,126,127,130]
  masses = [120,125,130]
  for mass in masses:
    mass = str(mass)
    print 'processing mass %s'%mass
    for fileName in fullFileNames:
      if 'M%s'%mass not in fileName: continue
      theProc = fileName.split('pythia8_')[1].split('.root')[0]
      theProc0 = theProc.split('_')[0]
      print 'processing %s'%theProc
      theFile = r.TFile(fileName, 'READ')
      theWS = theFile.Get('tagsDumper/cms_hgg_13TeV')
      for cat in cats:
        dataName = '%s_%s_13TeV_%s'%(nameMap[theProc0], mass, cat)
        sumEntries = theWS.data(dataName).sumEntries()
        #if cat == 'RECO_VBFTOPO_JET3VETO':
          #print 'sumEntries is %1.3f for %s, %s at %s GeV'%(sumEntries, theProc, cat, mass)
        if sumEntries < 0.1 and cat == 'RECO_VBFTOPO_JET3VETO':
          print 'WARNING: sumEntries is %1.3f for %s, %s at %s GeV'%(sumEntries, theProc, cat, mass)

if __name__ == '__main__':
  main()
