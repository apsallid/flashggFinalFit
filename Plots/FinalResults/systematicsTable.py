#!/usr/bin/env python

import numpy as np
import ROOT as r
from optparse import OptionParser

#Some input is needed which can be found by 
#opening with vi the two datacards and 
#printing by trial and error to find the 
#range in the VBFTag categories of the official analysis
#minlengthofofficialarray=79
minofrangeofofficialarray=100
maxofrangeofofficialarray=133
readfileafterofofficial=225

#minlengthofourcurrentarray=2
#minofrangeofourcurrentarray=2
#maxofrangeofourcurrentarray=78

readfileafterofourcurrent=73

'''
#def process(words, minlen, minrange, maxrange, official):
def process(words, minlen, minrange, maxrange):
    arr = np.array(words)
    #Find the number you should put when 
    #printing only VBFTag categories of the official analysis (trial and error)
    #First run with bin as argument instead of sys name.
    #OBSERVE HERE: Uncomment below when -s "bin" and comment below that
    #print arr
        
    if len(arr) > minlen:  
        #print (arr[minrange:maxrange].astype(float) - 1)
        #Print the min and max values
        #print arr[minrange:maxrange].astype(float)
        #print "Maximum value for ", arr[0], " is ", np.amax( abs(arr[minrange:maxrange].astype(float) - 1 ) )
        minmaxarr = arr[minrange:maxrange].astype(float) - 1 
        minmaxarr = abs( np.ma.masked_equal(minmaxarr, -1) )
        minmaxarr = abs( np.ma.masked_equal(minmaxarr, 0) * 100.)
        #Find the relevant official value
        offarr = np.array(findrelevantlineinofficial(words[0]))
        minmaxarroff = offarr[minofrangeofofficialarray:maxofrangeofofficialarray].astype(float) - 1 
        minmaxarroff = abs( np.ma.masked_equal(minmaxarroff, -1) )
        minmaxarroff = abs( np.ma.masked_equal(minmaxarroff, 0) * 100.)
        #print "Official array " , offarr
        #print minmaxarroff
        
        #
        if len(offarr) > minlengthofofficialarray:
            minmaxarroff = offarr[minofrangeofofficialarray:maxofrangeofofficialarray].astype(float) - 1 
            minmaxarroff = abs( np.ma.masked_equal(minmaxarroff, 0) * 100.)
        
        for offline in official[readfileafterofofficial:]:
            if arr[0] in offline: 
                offarr = np.array(offline)
                minmaxarroff = arr[minofrangeofofficialarray:maxofrangeofofficialarray].astype(float) - 1 
                minmaxarroff = abs( np.ma.masked_equal(minmaxarroff, 0) * 100.)
        #       

        if len(offarr) != 0:
            print " & ", arr[0], " & ", "%.1f" % np.amin( minmaxarr ), "-",  "%.1f" % np.amax( minmaxarr ), " & ", "%.1f" % np.amin( minmaxarroff ), "-",  "%.1f" % np.amax( minmaxarroff ), " \\\\"
        else : 
            print " & ", arr[0], " & ", np.amin( minmaxarr ), "-",  np.amax( minmaxarr ), " \\\\"
            
'''
parser = OptionParser()
parser.add_option("-i","--infilename", help="The datacard txt file")
parser.add_option("-f","--officialfilename", help="The official datacard txt file")
parser.add_option("-d","--indatfile", help="The photonCatSyst.dat file produce by calcPhotonSystConsts.cpp code")
parser.add_option("-g","--officialdatfile", help="The official photonCatSyst.dat file produce by calcPhotonSystConsts.cpp code")
parser.add_option("-s","--systematicname", help="The specific systematic you are working")

(options,args)=parser.parse_args()

'''
def findrelevantlineinofficial(syst): 
    offwords = []
    #Create official lines
    with open(options.officialfilename) as f:
        officiallines = f.read().splitlines()
        #OBSERVE HERE: We loop only to the systematic values portion of the files
        #or else it will crash (find the number with vi)
        for line in officiallines[readfileafterofofficial:]:
        #OBSERVE HERE: When running with -s "bin" find the range uncomment below not above    
        #for line in lines:
            if not syst in line: continue
            if "/" in line: offwords = line.replace("-","0.").replace("/"," ").split()
            else: offwords = line.replace("-","0.").split()
    
    #print offwords     
    return offwords  
'''

nuisancesyst = {}
nuisancesystofficial = {}

allothersyst = {}
allothersystofficial = {}

nuisancesystfromdat = {}
nuisancesystfromofficialdat = {}

'''
def processnuisance(words):
    arr = np.array(words)

with open(options.infilename) as f:
    lines = f.read().splitlines()
    #OBSERVE HERE: We loop only to the systematic values portion of the files
    #or else it will crash (find the number with vi)
    #for line in lines[readfileafterofofficial:]:
    for line in lines[readfileafterofourcurrent:]:
    #OBSERVE HERE: When running with -s "bin" find the range uncomment below not above    
    #for line in lines:
        if not "all" in options.systematicname:
            if not options.systematicname in line: continue
        if "/" in line: words=line.replace("-","").replace("/"," ").split()
        else: words=line.replace("-","").split()
        #process(words, minlengthofofficialarray, minofrangeofofficialarray, maxofrangeofofficialarray, offwords)
        #process(words, minlengthofourcurrentarray, minofrangeofourcurrentarray, maxofrangeofourcurrentarray, offwords)
        process(words, minlengthofourcurrentarray, minofrangeofourcurrentarray, maxofrangeofourcurrentarray)

'''
#################################################################################
# First part : Reading the files and saving them in dictionaries. 
#################################################################################
print "The datacard of our analysis"
with open(options.infilename) as f:
    lines = f.read().splitlines()
    #Now on an atttempt for nuisance parameters
    for line in lines:
        if not "nuisance" in line: continue
        words=line.split()
        nuisancesyst[words[0]] = words[1:]
        #print nuisancesyst[words[0]]
    #OBSERVE HERE: We loop only to the systematic values portion of the files
    #or else it will crash (find the number with vi)
    for line in lines[readfileafterofourcurrent:]:
    #OBSERVE HERE: When running with -s "bin" find the range uncomment below not above    
    #for line in lines:
        if not "all" in options.systematicname:
            if not options.systematicname in line: continue
        if "/" in line: words=line.replace("-","1.0").replace("/"," ").split()
        else: words=line.replace("-","1.0").split()
        if len(words) == 0: continue
        #print words
        allothersyst[words[0]] = words[1:]
        #print allothersyst[words[0]]
 
#################################################################################
print "Going to official datacard"
#Create official lines
with open(options.officialfilename) as f:
    officiallines = f.read().splitlines()
    for line in officiallines:
        if not "nuisance" in line: continue
        words=line.split()
        nuisancesystofficial[words[0]] = words[1:]
        #print nuisancesystofficial[words[0]]
    #OBSERVE HERE: We loop only to the systematic values portion of the files
    #or else it will crash (find the number with vi)
    for line in officiallines[readfileafterofofficial:]:
        if not "all" in options.systematicname:
            if not options.systematicname in line: continue
        if "/" in line: offwords = line.replace("-","1.0").replace("/"," ").split()
        else: offwords = line.replace("-","1.0").split()
        if len(offwords) == 0: continue
        #OBSERVE HERE: 
        #Find the number you should put when 
        #printing only VBFTag categories of the official analysis (trial and error)
        #First run with bin as argument instead of sys name.
        allothersystofficial[offwords[0]] = offwords[minofrangeofofficialarray:maxofrangeofofficialarray]
        #print allothersystofficial[offwords[0]]
        
#################################################################################
print "The dat file of our analysis"
with open(options.indatfile) as f:
    lines = f.read().splitlines()
    for line in lines:
        words=line.split()
        if len(words) < 3 or ("autogenerated" in line) or ("rate_change" in line): continue
        if words[0] not in nuisancesystfromdat:
            #Take only the rate_change column
            nuisancesystfromdat[words[0]] = words[3:4]
        else: 
            #We need extend here not append
            nuisancesystfromdat[words[0]].extend( words[3:4] )
        if (len(nuisancesystfromdat[words[0]]) < 1): continue
    #print nuisancesystfromdat

#################################################################################
print "The official dat file of our analysis"
with open(options.officialdatfile) as f:
    lines = f.read().splitlines()
    for line in lines:
        words=line.split()
        if (len(words) == 0) or ("autogenerated" in line) or ("rate_change" in line): continue
        if words[0] not in nuisancesystfromofficialdat:
            #Take only the rate_change column
            nuisancesystfromofficialdat[words[0]] = words[3:4]
        else: 
            #We need extend here not append
            nuisancesystfromofficialdat[words[0]].extend( words[3:4] )
        if len(nuisancesystfromofficialdat[words[0]]) < 1 : continue
    #print nuisancesystfromofficialdat


#################################################################################
# Second part : Connect the two datacards and dat files
#################################################################################
# First for the nuisance we read it from the dat file produced by the 
# calcPhotonSystConsts.cpp code. For the moment I do not have an official dat 
# file. However, in order to have the code ready I read my dat file twice. 
for sys, info in nuisancesystfromdat.items():
    for sysoff, infooff in nuisancesystfromofficialdat.items():
        if sys != sysoff: continue
        if len(info) == 0 or "diphotonCat" in sys or '=' in sys: continue
        #print info
        nuisancesystfromdatarr = np.array( info ).astype(float)
        nuisancesystfromofficialdatarr = np.array( infooff  ).astype(float)
        # HACK to avoid too large values
        #nuisancesystfromdatarr = nuisancesystfromdatarr[ nuisancesystfromdatarr < 0.1  ] 
        #nuisancesystfromofficialdatarr = nuisancesystfromofficialdatarr[ nuisancesystfromofficialdatarr < 0.1 ]
        #print nuisancesystfromdatarr
        # For now since I do not have the official I will not print the official column
        #print " & CMS_hgg_nuisance_", sys, " & ", "%.1f" % (np.amax( nuisancesystfromdatarr ) * 100.), " & ",  "%.1f" % (np.amax( nuisancesystfromofficialdatarr ) * 100.), " \\\\"
        print " & CMS_hgg_nuisance_", sys, " & ", "%.1f" % (np.amax( nuisancesystfromdatarr ) * 100.), " & ", " Need official dat file \\\\"
                
for sys, info in allothersyst.items():
    for sysoff, infooff in allothersystofficial.items():
        if sys != sysoff: continue
        
        allothersystarr = np.array( info )
        # [1:] below is because we do not want the lnN element. 
        minmaxarr = allothersystarr[1:].astype(float) - 1 
        #minmaxarr = abs( np.ma.masked_equal(minmaxarr, -1) )
        minmaxarr = abs( np.ma.masked_equal(minmaxarr, 0) * 100.)

        allothersystoffarr = np.array( infooff  )
        minmaxarroff = allothersystoffarr[1:].astype(float) - 1 
        #minmaxarroff = abs( np.ma.masked_equal(minmaxarroff, -1) )
        minmaxarroff = abs( np.ma.masked_equal(minmaxarroff, 0) * 100.)

        print " & ", sys, " & ", "%.1f" % np.amin( minmaxarr ), "-",  "%.1f" % np.amax( minmaxarr ), " & ", "%.1f" % np.amin( minmaxarroff ), "-",  "%.1f" % np.amax( minmaxarroff ), " \\\\"

        #print " & ", sys, " & ", float(info[2]) * 100., " & ", float(infooff[2]) * 100.


