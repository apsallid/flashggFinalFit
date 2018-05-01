import glob
import os
import re 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import operator
import math
from decimal import Decimal
from itertools import product

import ROOT as r
from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile

c1 = TCanvas( 'c1', 'Expected Significance (Asimov)', 200, 10, 800, 800 )
#Check for underflow/overflow and adjust binning and range. 
h1f = TH1F( 'h1f', 'Expected Significance (Asimov)', 50, 2, 3 )
#c1.SetLogy();

r.gStyle.SetOptStat(0)

files = glob.iglob('/afs/cern.ch/work/a/apsallid/CMS/Hgg/FinalFits_STXS_stage1/CMSSW_8_1_0/src/flashggFinalFit/Parallel/results/combine/*.txt')

exsig = {}
expval = {}

exsignozeropval = {}
exsigbelowthreshold = {}

for fname in files:
    m = re.search('significance_(.+?).txt', fname) 
    if m:
       #the bdt string 
       found = m.group(1)
       print found
    '''   
    #Check if we have an error in the relevant logfile 
    founderror = False   
    itemList =  os.listdir("/afs/cern.ch/work/a/apsallid/CMS/Hgg/FinalFits_STXS_stage1/CMSSW_8_1_0/src/flashggFinalFit/Parallel/logfiles")
    for item in itemList: 
        if found.replace("_",",") in open('/afs/cern.ch/work/a/apsallid/CMS/Hgg/FinalFits_STXS_stage1/CMSSW_8_1_0/src/flashggFinalFit/Parallel/logfiles/'+item).read(): 
            print item 
    '''        
    #Check for errors in the significance output file    
    if "Function evaluation error" in open(fname).read(): 
        print "Function evaluation error in file ", fname, ". Disregard it. "
        continue
            
    with open(fname) as f:
        for line in f:
            #if "Function evaluation error" in line:
            if "Significance:" in line:
                exsig[found] = float(line.split()[1])
                #print float(line.split()[1])
                print exsig[found]
                h1f.Fill(float(line.split()[1]))
                break
            if "p-value" in line:  
                #foundp = re.search("value = (\d+)\)", line).group(1)
                foundp = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                expval[found] = float( foundp[0] ) 
                #if float(line.split()[1]) == 0: 
                #    continue




#np.array(exsig)

#for key in expval: 
#   if expval[key] > 1e-20:
#       exsignozeropval[key] = exsig[key]


#for key in exsig: 
#   if exsig[key] <= 11.:
#       exsigbelowthreshold[key] = exsig[key]


#print exsig, expval

print max(exsig.iteritems(), key=operator.itemgetter(1))[0]


print "maximum expected significance ", max(exsig.values()) , " for " , max(exsig, key=exsig.get)

#print "maximum expected significance for none zero pval ", max(exsignozeropval.values()) , " for " , max(exsignozeropval, key=exsignozeropval.get)

#print "maximum expected significance for below ",  cutthres , " sig  ", max(exsigbelowthreshold.values()) , " for " , max(exsigbelowthreshold, key=exsigbelowthreshold.get)

h1f.Draw()
c1.Update()

c1.SaveAs('expsignificance_nosys.png', 'png')

myfile = TFile( 'expsignificancenosys.root', 'RECREATE' )
h1f.Write()
myfile.Close()

#print exsig.values()
#print exsig.keys()

bdtbound =  np.array([])
for key in exsig.keys():
    print key, key.split("_")[1] 
    bdtbound = np.append(bdtbound,  key.split("_")[1]   )

exsig = np.array(exsig.values())

# Create a dataset:
df=pd.DataFrame({'bdtbound' : bdtbound , 'exsig' : exsig})

# plot
fig = plt.figure()
plt.plot( 'bdtbound', 'exsig', data=df, linestyle='none', marker='o')
plt.title("Significance for RECO_VBFTOPO_JET3VETO")
plt.xlabel("dijet_mva boundary")
plt.ylabel("Significance")

fig.savefig("Significance_RECO_VBFTOPO_JET3VETO.png")


#plt.show()

