'''

@author: v-xinhzh
Read the specify parameters from the log files in the folder and sub folder
'''
import os,csv;
from token import EQUAL

#Modify SourceFolder as the log file path.
#Please use \\ in the path string, rather than \.
#SourceFolder="C:\\Work\\Cardinal\\SiT station\\Calibration\\LED calibration\\IRCalibration0906\\";
SourceFolder="C:\\Work\\Cardinal\\SiT station\\Calibration\\LED calibration\\IRCalibration0906_new IR meter\\";
SummaryFileName="Summary.csv"

KeyFileName=".csv";
KeyParameterA0="Fit Polynomial IR Table Visible Intensity - A0";
KeyParameterA1="Fit Polynomial IR Table Visible Intensity - A1";
KeyParameterA2="Fit Polynomial IR Table Visible Intensity - A2";

#LOWLIMIT=225;
#UPPERLIMIT=375;

for path,dirs,files in os.walk(SourceFolder, False):
    for OneFile in files:
        if KeyFileName not in OneFile:
            continue;
        else:
            with open(path+"\\"+OneFile,"rb") as logfile:
                csr=csv.reader(logfile,delimiter=",",quotechar="|");
                for lines in csr:
                    try:
                        if KeyParameterA0 == lines[14]:
                            a0=lines[15];
                            continue;
                        if KeyParameterA1 == lines[14]:
                            a1=lines[15];
                            continue;
                        if KeyParameterA2 == lines[14]:
                            a2=lines[15];
                            break;
                    except:
                        continue;
            print(OneFile.split("_")[0],float(a0)+float(a1)*0.3+float(a2)*0.3*0.3);                   
print("End");
                    
        
