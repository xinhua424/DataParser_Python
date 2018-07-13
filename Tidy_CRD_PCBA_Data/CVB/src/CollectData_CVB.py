'''

@author: v-xinhzh
Read the specify parameters from the log files in the folder and sub folder
'''
import os,csv;
from token import EQUAL

#Modify SourceFolder as the log file path.
#Please use \\ in the path string, rather than \.
SourceFolder="C:\\Work\\Campo\\20160709\\FTF\\";
SummaryFileName="Summary.csv"

KeyFileName=".csv";
KeyParameters=("Pk1 Force ","Cf/Cr");

#LOWLIMIT=225;
#UPPERLIMIT=375;

resultfile=open(SourceFolder+SummaryFileName,"wb");
csw=csv.writer(resultfile,delimiter=",",quoting=csv.QUOTE_MINIMAL);
result=("MACHINE NAME","TEST_MEASUREMENT NAME","LOWER LIMIT","UPPER LIMIT","SERIAL NUMBER","VALUE","ErrorCode");
csw.writerow(result);
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
                    try:
                        if KeyParameters[0] == lines[-6]:
                            result=[];
                            result.append(lines[4]);    #Machine Name
                            result.append(lines[-6]);   #Measurement name
                            result.append(lines[-3]);   #Low limit
                            result.append(lines[-2]);   #Upper limit
                            result.append(lines[1]);    #Serial number
                            result.append(lines[15]);   #Value
                            result.append(lines[7]);    #Error code
                            csw.writerow(result);
                            continue;
                        if KeyParameters[1] == lines[-6]:
                            result=[];
                            result.append(lines[4]);    #Machine Name
                            result.append(lines[-6]);   #Measurement name
                            result.append(lines[-3]);   #Low limit
                            result.append(lines[-2]);   #Upper limit
                            result.append(lines[1]);    #Serial number
                            result.append(lines[15]);   #Value
                            result.append(lines[7]);    #Error code
                            csw.writerow(result);                       
                            break;
                    except:
                        continue;
                               
print("End");
print("The FTF test result has been explored.");
                    
        
