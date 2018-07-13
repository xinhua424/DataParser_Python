'''

@author: v-xinhzh
Read the specify parameters from the log files in the folder and sub folder
'''
import os,csv;


SourceFolder="C:\\Work\\Cardinal\\SiT station\\20160215\\NHK\\";
SummaryFileName="Summary.csv"

KeyFileName="AudioTest";
# KeyParameters=("Level");
KeyParameter="Level";

resultfile=open(SourceFolder+SummaryFileName,"wb");
csw=csv.writer(resultfile,delimiter=",",quoting=csv.QUOTE_MINIMAL);
filenum=0;

for path,dirs,files in os.walk(SourceFolder, False):
    for OneFile in files:
        if KeyFileName not in OneFile:
            continue;
        else:
#             filenum+=1;
#             if filenum>100:
#                 break;
            with open(path+"\\"+OneFile,"rb") as logfile:
                csr=csv.reader(logfile,delimiter=",",quotechar="|");
                for lines in csr:
                    if KeyParameter in lines[-1]:
                        result=[];
                        result.append(lines[-1].split("|")[-6]);
                        result.append(lines[-1].split("|")[-4]);
                        result.append(lines[-1].split("|")[-5]);
                        csw.writerow(result);
                print("End");             
                            
                    
        