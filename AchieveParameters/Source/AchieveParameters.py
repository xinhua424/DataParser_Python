'''

Achive key parameters from *.txt files in a specified folder.
This is requested by Pal H.
@author: Shawn Zhang
'''

import csv
import os

SourceFolder="C:\\Work\\Cardinal\\log\\A31152410375542A\\";
ResultFilePaht="C:\\Work\\Cardinal\\log\\A31152410375542A\\";

if not os.path.exists(ResultFilePaht):
    os.makedirs(ResultFilePaht);
    
KeyParameter=("RC_PathA_Alpha_Saved","RC_PathA_Beta_Saved","RC_PathB_Alpha_Saved","RC_PathB_Beta_Saved");
# ResultString=["DUT_SN","Repeat_Time"];
ResultString=["Repeat_Time"];
for a in KeyParameter:
    ResultString.append(a);

resultfile=open(ResultFilePaht+"Result.csv","wb");
csw=csv.writer(resultfile,delimiter=",",quoting=csv.QUOTE_MINIMAL);
csw.writerow(ResultString);

for paths,dirs,files in os.walk(SourceFolder, False):
    for onelog in files:
        if onelog.endswith(".txt"):
            logfile=open(SourceFolder+"\\"+onelog,"rb");
            logreader=csv.reader(logfile,delimiter=":");
            temp=onelog[:-4].split("-");
            ResultString=[];
#             ResultString.append(temp.pop(2));
            ResultString.append(temp.pop(1));
            for oneline in logreader:
                if oneline.__len__()>1 and KeyParameter[0] in oneline[0]:
                    ResultString.append(oneline[1].replace(" ","").split("(")[0]);
                elif oneline.__len__()>1 and KeyParameter[1] in oneline[0]:
                    ResultString.append(oneline[1].replace(" ","").split("(")[0]);
                elif oneline.__len__()>1 and KeyParameter[2] in oneline[0]:
                    ResultString.append(oneline[1].replace(" ","").split("(")[0]);
                elif oneline.__len__()>1 and KeyParameter[3] in oneline[0]:
                    ResultString.append(oneline[1].replace(" ","").split("(")[0]);
                    csw.writerow(ResultString);
                else:
                    continue;
                