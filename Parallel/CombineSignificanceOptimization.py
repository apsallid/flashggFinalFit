import glob
import re
import numpy as np
import operator
import math
from decimal import Decimal
import ROOT as r
from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile

c1 = TCanvas( 'c1', 'Expected Significance (Asimov)', 200, 10, 800, 800 )
h1f = TH1F( 'h1f', 'Expected Significance (Asimov)', 50, 1.8, 2.3 )
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
       found = m.group(1)
       print found
    with open(fname) as f: 
        for line in f:
            if "Significance:" in line:
                exsig[found] = float(line.split()[1])
                #print float(line.split()[1])
                print exsig[found]
                h1f.Fill(float(line.split()[1]))
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


for key in exsig: 
   if exsig[key] <= 11.:
       exsigbelowthreshold[key] = exsig[key]


#print exsig, expval

print max(exsig.iteritems(), key=operator.itemgetter(1))[0]


print "maximum expected significance ", max(exsig.values()) , " for " , max(exsig, key=exsig.get)

#print "maximum expected significance for none zero pval ", max(exsignozeropval.values()) , " for " , max(exsignozeropval, key=exsignozeropval.get)

#print "maximum expected significance for below 11 sig  ", max(exsigbelowthreshold.values()) , " for " , max(exsigbelowthreshold, key=exsigbelowthreshold.get)

h1f.Draw()
c1.Update()

c1.SaveAs('expsignificance_nosys.png', 'png')

myfile = TFile( 'expsignificancenosys.root', 'RECREATE' )
h1f.Write()
myfile.Close()
