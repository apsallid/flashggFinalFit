#ifndef InitialFit_h 
#define InitialFit_h

#include <iostream>
#include <vector>
#include <string>
#include <map>

#include "RooAbsReal.h"
#include "RooGaussian.h"
#include "RooAddPdf.h"
#include "RooGenericPdf.h"
#include "RooPolynomial.h"
#include "RooDataSet.h"
#include "RooDataHist.h"
#include "RooRealVar.h"
#include "RooFitResult.h"

class InitialFit {

  public:

    InitialFit(RooRealVar *massVar, RooRealVar *MHvar, int mhLow, int mhHigh, std::vector<int> skipMasses, bool binnedFit, int bins);
    InitialFit(RooRealVar *BDTVar, RooRealVar *MHvar, int mhLow, int mhHigh, float minBDT, float maxBDT, std::vector<int> skipMasses, bool binnedFit, int bins);
    ~InitialFit();

    void buildSumOfGaussians(std::string name, int nGaussians, bool recursive=false, bool forceFracUnity=false);
    void buildBDTpdf(std::string name);
    void loadPriorConstraints(std::string filename, float constraintValue);
    void saveParamsToFile(std::string filename);
    void saveParamsToFileAtMH(std::string filename, int setMH);
    void saveBDTParamsToFileAtMH(std::string filename, int setMH);
    std::map<int,std::map<std::string,RooRealVar*> > getFitParams();
		void printFitParams();
    void setDatasets(std::map<int,RooDataSet*> data);
    void setDatasetsSTD(std::map<int,RooDataSet*> data);
    void addDataset(int mh, RooDataSet *data);
    void runFits(int ncpu);
    void runFitsBDT(int ncpu);
    void plotFits(std::string name, std::string rvwn="");
    void plotFitsBDT(std::string name, std::string bdtg="");
    void setVerbosity(int v);

    void setFitParams(std::map<int,std::map<std::string,RooRealVar*> >& pars );
  private:

    RooRealVar *mass;
    RooRealVar *BDTG;
    RooRealVar *MH;
    std::map<int,RooAddPdf*> sumOfGaussians;
    std::map<int,RooGenericPdf*> BDTpdf; 
    std::map<int,RooDataSet*> datasets; 
    std::map<int,RooDataSet*> datasetsSTD; 
    std::map<int,std::map<std::string,RooRealVar*> > fitParams;
    std::map<int,std::map<std::string,RooRealVar*> > fitParamsBDT; 
    std::map<int,std::map<std::string,RooAbsReal*> > fitUtils;
    std::map<int,std::map<std::string,RooGaussian*> > initialGaussians;
    std::map<int,RooFitResult*> fitResults;
    std::map<int,RooFitResult*> fitResultsBDT;
    int mhLow_;
    int mhHigh_;
    float minBDT_;
    float maxBDT_;
		std::vector<int> skipMasses_;
    std::vector<int> allMH_;
    std::vector<int> getAllMH();
		bool skipMass(int mh);
    int verbosity_;
    bool binnedFit_;
    int bins_;

};

#endif
