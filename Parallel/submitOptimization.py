#!/usr/bin/env python

#Running command
#python submitOptimization.py --bdtfilename bdtboundaries.txt --bdtstep 0.01 --numofcats 2 --workpath /afs/cern.ch/work/a/apsallid/CMS/Hgg/FinalFits_STXS_stage1/CMSSW_8_1_0/src/flashggFinalFit/Parallel --runbkg True --runsignal False --rundatacard False --runcombine False --baseFilePath '/eos/cms/store/user/apsallid/HggAnalysis/input/STXS_stage1/RunIISummer16-2_4_1-25ns_Moriond17/workspaces/pergenprocess/' --ext 'OptimizationStage1_DCB'

import numpy as np
import os, sys

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--bdtfilename",default="bdtboundaries.txt",help="Name of boundaries file to print (default: %default)")
parser.add_option("--bdtstep",type="float",default=0.01,help="Name of boundaries file to print (default: %default)")
parser.add_option("--numofcats",type="int",default=3,help="Name of boundaries file to print (default: %default)")
parser.add_option("--workpath",help="The workpath where we will create jobs and logfiles")
parser.add_option("--runbkg",default=False)
parser.add_option("--runsignal",default=False)
parser.add_option("--rundatacard",default=False)
parser.add_option("--runcombine",default=False)
parser.add_option("--baseFilePath", help="Path to input files from flashgg")
parser.add_option("--ext",help="Extension")
(options,args)=parser.parse_args()

#make the grid giving as input the number of categories
#and the step size of the scan
def makegrid2cat(step):
    outFile = open(options.bdtfilename,'w')
    for inda, a in enumerate(np.arange(0.2,1.0,step)):
        if (a-0.2)<0.1 or (1-a)<0.1: continue
        print inda, a
        outFile.write("0.2,%0.2f,1.0\n"%(a) )
        
def makegrid3cat(step):
    outFile = open(options.bdtfilename,'w')
    for inda, a in enumerate(np.arange(0.2,1.0,step)):
        for indb, b in enumerate(np.arange(0.2,1.0,step)):
            if a>=b : continue
            if (b-a)<0.1 or (a-0.2)<0.1 or (1-b)<0.1: continue
            print a, b
            outFile.write("0.2,%0.2f,%0.2f,1.0\n"%(a,b) )

def makegrid4cat(step):
    outFile = open(options.bdtfilename,'w')
    for inda, a in enumerate(np.arange(0.2,1.0,step)):
        for indb, b in enumerate(np.arange(0.2,1.0,step)):
            for indc, c in enumerate(np.arange(0.2,1.0,step)):
                if a>=b or a>=c or b>=c: continue
                if (b-a)<0.1 or (a-0.2)<0.1 or (c-b)<0.1 or (1-c)<0.1: continue
                print a, b, c
                outFile.write("0.2,%0.2f,%0.2f,%0.2f,1.0\n"%(a,b,c) )

def writePreamble(sub_file):
    #print "[INFO] writing preamble"
    sub_file.write('#!/bin/bash\n')
    sub_file.write('sleep $[ ( $RANDOM % 10 )  + 1 ]s\n')
    sub_file.write('cd %s\n'%options.workpath)
    sub_file.write('eval `scramv1 runtime -sh`\n')
    sub_file.write('cd -\n')
    #Copy latest files in workpath"
    sub_file.write('cp %s/../edStyleRunFinalFitsScripts.py . \n'%options.workpath)
    sub_file.write('cp %s/../runFinalFitsScripts.sh . \n'%options.workpath)
    sub_file.write('mkdir -p Background/bin \n')
    sub_file.write('cp %s/../Background/runBackgroundScripts.sh $PWD/Background/. \n'%options.workpath)
    sub_file.write('cp %s/../Background/bin/fTest $PWD/Background/bin/. \n'%options.workpath)
    sub_file.write('cp %s/../Background/bin/makeBkgPlots $PWD/Background/bin/. \n'%options.workpath)
    sub_file.write('mkdir -p Signal/bin \n')
    sub_file.write('cp %s/../Signal/runSignalScripts.sh $PWD/Signal/. \n'%options.workpath)


def writePostamble(sub_file, exec_line, line):
    
    #print "[INFO] writing to postamble"
    sub_file.write('%s \n'%exec_line)
    sub_file.write('cp CMS-HGG_multipdf_mva.root %s/results/Bkg/Workspaces/CMS-HGG_mva_13TeV_multipdf_%s.root \n'%(options.workpath,line.replace(",", "_")))
    sub_file.write('cp $PWD/Background/outdir_%s/bkgPlots-Data/bkgplot_*.png %s/results/Bkg/. \n'%(options.ext,options.workpath))
    sub_file.close()

print "------------------------------------------------"
print "------------>> Creating BDT Grid"
print "------------------------------------------------"

if options.numofcats == 2: 
    makegrid2cat(options.bdtstep)
elif options.numofcats == 3: 
    makegrid3cat(options.bdtstep)
elif options.numofcats == 4: 
    makegrid4cat(options.bdtstep)
else: 
    print '[ERROR] Categories supported are 2,3 and 4 -- Exiting'
    sys.exit(1)

print "------------------------------------------------"
print "------------>> Creating jobs"
print "------------------------------------------------"

print "------------>> Preparing structure"

os.system('mkdir -p %s/jobs'%options.workpath)
os.system('mkdir -p %s/logfiles'%options.workpath)
os.system('mkdir -p %s/results/Signal/Plots'%options.workpath)
os.system('mkdir -p %s/results/Signal/dat'%options.workpath)
os.system('mkdir -p %s/results/Signal/combine'%options.workpath)
os.system('mkdir -p %s/results/Bkg/Workspaces'%options.workpath)
os.system('mkdir -p %s/files'%options.workpath)

os.system('chmod 755 %s/jobs'%options.workpath)
os.system('chmod 755 %s/logfiles'%options.workpath)
os.system('chmod 755 %s/results/Signal/Plots'%options.workpath)
os.system('chmod 755 %s/results/Signal/dat'%options.workpath)
os.system('chmod 755 %s/results/Signal/combine'%options.workpath)
os.system('chmod 755 %s/results/Bkg/Workspaces'%options.workpath)

print "------------>> Copy latest files in workpath"

os.system('cp %s/../ %s/files/. '%(options.workpath,options.workpath))
os.system('cp %s/../ %s/files/. '%(options.workpath,options.workpath))

os.system('cp %s/../ %s/files/. '%(options.workpath,options.workpath))


counter=0
with open(options.bdtfilename) as f:
    lines = f.read().splitlines()
    for line in lines:
        #line = line.split(',')
        print "job ", counter, line, line[0], line[1], line[2], len(line)
        thejobfile = open('%s/jobs/sub%d.sh'%(options.workpath,counter),'w')
        writePreamble(thejobfile)

        exec_line = 'python edStyleRunFinalFitsScripts.py --cutforBDT %s --runbkg %s --runsignal %s --rundatacard %s --runcombine %s --baseFilePath %s --workpath %s --ext %s'%(line,options.runbkg,options.runsignal,options.rundatacard,options.runcombine,options.baseFilePath,options.workpath,options.ext)

        os.system('chmod 755 %s/jobs/sub%d.sh'%(options.workpath,counter))
        print exec_line
        writePostamble(thejobfile,exec_line,line)

        counter =  counter+1
