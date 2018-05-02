#!/usr/bin/env python

#Running command
#python submitOptimization.py --bdtfilename bdtboundaries.txt --bdtstep 0.01 --numofcats 2 --workpath /afs/cern.ch/work/a/apsallid/CMS/Hgg/FinalFits_STXS_stage1/CMSSW_8_1_0/src/flashggFinalFit/Parallel --runbkg False --runsignal True --rundatacard True --runcombine True --baseFilePath '/eos/cms/store/user/apsallid/HggAnalysis/input/STXS_stage1/RunIISummer16-2_4_1-25ns_Moriond17/workspaces/pergenprocess/' --ext 'OptimizationStage1_DCB' --cats 'RECO_VBFTOPO_JET3VETO_0,RECO_VBFTOPO_JET3VETO_1' --flashggCatsIn 'RECO_VBFTOPO_JET3VETO' --queue '2nd' --dryRun True --quick True --resubmit True

import numpy as np
import os, sys

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--bdtfilename",default="bdtboundaries.txt",help="Name of boundaries file to print (default: %default)")
parser.add_option("--bdtstep",type="float",default=0.01,help="The step of the dijet_mva cut (default: %default)")
parser.add_option("--numofcats",type="int",default=3,help="The number of subcategories we examine (default: %default)")
parser.add_option("--workpath",help="The workpath where we will create jobs and logfiles")
parser.add_option("--runbkg",default=False)
parser.add_option("--runsignal",default=False)
parser.add_option("--rundatacard",default=False)
parser.add_option("--runcombine",default=False)
parser.add_option("--baseFilePath", help="Path to input files from flashgg")
parser.add_option("--ext",help="Extension")
parser.add_option("--cats",help="We focus on the categories we want to optimize.This is the categories we define splitting the main flashgg category.")
parser.add_option("--flashggCatsIn",help="This is the category we are interested to optimize. We can only check and optimize one category at a time.")
parser.add_option("--queue",help="Which batch queue to use.")
parser.add_option('--dryRun',default=True,help="Whether you want to sent the jobs or just print.")
parser.add_option('--quick',default=True, help="In case we have already run the bkg, no need to run it again.Also, set runbkg to False if this is True.")
parser.add_option('--resubmit',default=False, help="In case of failed jobs, resubmit only those")
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
    #Copy latest files in workpath
    sub_file.write('cp %s/../edStyleRunFinalFitsScripts.py . \n'%options.workpath)
    sub_file.write('cp %s/../runFinalFitsScripts.sh . \n'%options.workpath)
    sub_file.write('mkdir -p Background/bin \n')
    sub_file.write('cp %s/../Background/runBackgroundScripts.sh $PWD/Background/. \n'%options.workpath)
    sub_file.write('cp %s/../Background/bin/fTest $PWD/Background/bin/. \n'%options.workpath)
    sub_file.write('cp %s/../Background/bin/makeBkgPlots $PWD/Background/bin/. \n'%options.workpath)
    sub_file.write('cp %s/../Background/RootDict* $PWD/Background/. \n'%options.workpath)
    sub_file.write('mkdir -p Signal/bin \n')
    sub_file.write('mkdir -p Signal/dat \n')
    sub_file.write('cp %s/../Signal/runSignalScripts.sh $PWD/Signal/. \n'%options.workpath)
    sub_file.write('cp %s/../Signal/bin/* $PWD/Signal/bin/. \n'%options.workpath)
    sub_file.write('cp %s/../Signal/RootDict* $PWD/Signal/. \n'%options.workpath)
    sub_file.write('mkdir -p Datacard \n')
    sub_file.write('cp %s/../Datacard/makeStage1Datacard.py $PWD/Datacard/. \n'%options.workpath)
    sub_file.write('mkdir -p Plots/FinalResults \n')
    sub_file.write('cp %s/../Plots/FinalResults/combineHarvesterOptions13TeV_Template.dat $PWD/Plots/FinalResults/. \n'%options.workpath)
    sub_file.write('cp %s/../Plots/FinalResults/allPlots_Template.sh $PWD/Plots/FinalResults/. \n'%options.workpath)
    sub_file.write('cp %s/../Plots/FinalResults/combinePlotsOptions_Template.dat $PWD/Plots/FinalResults/. \n'%options.workpath)
    sub_file.write('cp %s/../Plots/FinalResults/makeCombinePlots.py $PWD/Plots/FinalResults/. \n'%options.workpath)
    sub_file.write('cp %s/../Plots/FinalResults/combineHarvester.py $PWD/Plots/FinalResults/. \n'%options.workpath)
    if options.quick == "True":
        sub_file.write('cp %s/results/Bkg/Workspaces/CMS-HGG_mva_13TeV_multipdf_%s.root $PWD/Background/CMS-HGG_multipdf_%s.root \n'%(options.workpath,line.replace(",", "_"),options.ext))

def writePostamble(sub_file, exec_line, line):
    
    #print "[INFO] writing to postamble"
    sub_file.write('%s \n'%exec_line)
    if options.quick == "False":
        sub_file.write('cp $PWD/Background/CMS-HGG_multipdf_%s.root %s/results/Bkg/Workspaces/CMS-HGG_mva_13TeV_multipdf_%s.root \n'%(options.ext,options.workpath,line.replace(",", "_")))

    for ct in options.cats.split(','):
        sub_file.write('cp $PWD/Background/outdir_%s/bkgPlots-Data/bkgplot_%s.png %s/results/Bkg/bkgplot_%s_%s.png \n'%(options.ext,ct,options.workpath,ct,line.replace(",", "_")))
        sub_file.write('cp $PWD/Background/outdir_%s/bkgPlots-Data/allPdfs_%s.png %s/results/Bkg/allPdfs_%s_%s.png \n'%(options.ext,ct,options.workpath,ct,line.replace(",", "_")))
        sub_file.write('cp $PWD/Background/tmp_STXS_stage1_%s.root %s/results/Bkg/Workspaces/tmp_%s_%s_%s.root \n'%(ct,options.workpath,options.ext,ct,line.replace(",", "_")))

    sub_file.write('cp $PWD/Signal/outdir_%s/sigplots/all.png %s/results/Signal/Plots/all_%s.png \n'%(options.ext,options.workpath,line.replace(",", "_")))
    sub_file.write('cp $PWD/Signal/dat/photonCatSyst_%s.dat %s/results/Signal/dat/photonCatSyst_%s_%s.png \n'%(options.ext,options.workpath,options.ext,line.replace(",", "_")))
    sub_file.write('cp $PWD/Signal/dat/newConfig_%s.dat %s/results/Signal/dat/newConfig_%s_%s.png \n'%(options.ext,options.workpath,options.ext,line.replace(",", "_")))

    sub_file.write('cp $PWD/Plots/FinalResults/combine_significance_%s.txt %s/results/combine/. \n'%(line.replace(",", "_"),options.workpath))

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

print "------------>> Preparing structure locally in lxplus"

os.system('mkdir -p %s/jobs'%options.workpath)
os.system('mkdir -p %s/logfiles'%options.workpath)
os.system('mkdir -p %s/results/Signal/Plots'%options.workpath)
os.system('mkdir -p %s/results/Signal/dat'%options.workpath)
os.system('mkdir -p %s/results/Signal/combine'%options.workpath)
os.system('mkdir -p %s/results/Bkg/Workspaces'%options.workpath)
os.system('mkdir -p %s/files'%options.workpath)
os.system('mkdir -p %s/results/combine'%options.workpath)

os.system('chmod 755 %s/jobs'%options.workpath)
os.system('chmod 755 %s/logfiles'%options.workpath)
os.system('chmod 755 %s/results/Signal/Plots'%options.workpath)
os.system('chmod 755 %s/results/Signal/dat'%options.workpath)
os.system('chmod 755 %s/results/Signal/combine'%options.workpath)
os.system('chmod 755 %s/results/Bkg/Workspaces'%options.workpath)

print "------------>> Copy latest files in workpath"

#os.system('cp %s/../ %s/files/. '%(options.workpath,options.workpath))
#os.system('cp %s/../ %s/files/. '%(options.workpath,options.workpath))

#os.system('cp %s/../ %s/files/. '%(options.workpath,options.workpath))


counter=0
with open(options.bdtfilename) as f:
    lines = f.read().splitlines()
    for line in lines:
        #line = line.split(',')
        print "job ", counter, line, line[0], line[1], line[2], len(line)
        thejobfile = open('%s/jobs/sub%d.sh'%(options.workpath,counter),'w')
        writePreamble(thejobfile)

        exec_line = 'python edStyleRunFinalFitsScripts.py --cutforBDT %s --runbkg %s --runsignal %s --rundatacard %s --runcombine %s --baseFilePath %s --workpath %s --ext %s --cats %s --flashggCatsIn %s'%(line,options.runbkg,options.runsignal,options.rundatacard,options.runcombine,options.baseFilePath,options.workpath,options.ext,options.cats,options.flashggCatsIn)

        os.system('chmod 755 %s/jobs/sub%d.sh'%(options.workpath,counter))
        print exec_line
        writePostamble(thejobfile,exec_line,line)

        if options.dryRun == "False" and options.resubmit == "False": 
            #Save logfiles if you have space
            os.system('bsub -q %s -o %s/logfiles/sub%d.log %s/jobs/sub%d.sh'%(options.queue,options.workpath,counter,options.workpath,counter))
            #os.system('bsub -q %s -o /tmp/junk %s/jobs/sub%d.sh'%(options.queue,options.workpath,counter))
        if options.dryRun == "False" and options.resubmit == "True": 
            #Check if the current job has any error assosiated in the relevant combine file
            if "Function evaluation error" in open( '%s/results/combine/combine_significance_%s.txt'%(options.workpath,line.replace(",", "_")) ).read(): 
                print "Function evaluation error for job ", '%s/jobs/sub%d.sh'%(options.workpath,counter) , ". Resubmitting ..."
            #Check if a significance value was printed
            if "Significance:" not in open( '%s/results/combine/combine_significance_%s.txt'%(options.workpath,line.replace(",", "_")) ).read(): 
                print "No significance was calculated for job ", '%s/jobs/sub%d.sh'%(options.workpath,counter) , ". Resubmitting ..."
                #print '%s/results/combine/combine_significance_%s.txt'%(options.workpath,line.replace(",", "_")) 
                #Save logfiles if you have space
                os.system('bsub -q %s -o %s/logfiles/sub%d.log %s/jobs/sub%d.sh'%(options.queue,options.workpath,counter,options.workpath,counter))
                #os.system('bsub -q %s -o /tmp/junk %s/jobs/sub%d.sh'%(options.queue,options.workpath,counter))
                #print 'bsub -q %s -o /tmp/junk %s/jobs/sub%d.sh'%(options.queue,options.workpath,counter)
        if options.dryRun == "True":     
            print 'bsub -q %s -o /tmp/junk %s/jobs/sub%d.sh'%(options.queue,options.workpath,counter)

        counter =  counter+1
