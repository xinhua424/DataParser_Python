'''

@author: v-xinhzh
Parse the test logs generated JDM1 TS, merge the useful information in one CSV file
'''
import os,csv;

#Modify SourceFolder as the log file path.
#Please use \\ in the path string, rather than \.
SourceFolder="C:\\Work\\Cardinal\\MonInline\\20160909\\";
SummaryFileName="Summary.csv"

SuffixName=".csv";


resultfile=open(SourceFolder+SummaryFileName,"wb");
csw=csv.writer(resultfile,delimiter=",",quoting=csv.QUOTE_MINIMAL);
result=("MACHINE NAME","TEST_MEASUREMENT NAME","LOWER LIMIT","UPPER LIMIT","SERIAL NUMBER","VALUE","SubFolder");
csw.writerow(result);
filenum=0;

for path,dirs,files in os.walk(SourceFolder, False):
    for OneFile in files:
        if SuffixName not in OneFile:
            continue;
        else:
#             filenum+=1;
#             if filenum>100:
#                 break;
            with open(path+"\\"+OneFile,"rb") as logfile:
                csr=csv.reader(logfile,delimiter=",",quotechar="|");
                for lines in csr:
                    try:
                        if lines[0]!="TSRID" and lines[5] != "" and lines[14]!="" and (lines[17]!="" or lines[18]!=""):
                            #Test name is not null
                            #Measurement name is not null
                            #Low limit is not null
                            #High limit is not null
                            result=[];
                            result.append(lines[4]);    #Machine Name
                            result.append(lines[5]+"_"+lines[14]);   #Measurement name
                            result.append(lines[17]);   #Low limit
                            result.append(lines[18]);   #Upper limit
                            result.append(lines[1]);    #Serial number
                            result.append(lines[15]);   #Value
                            #result.append(lines[7]);    #Error code
                            result.append(path.split("\\")[-3]);    #Subfolder name
                            csw.writerow(result);
                            continue;
                    except:
                        continue;
                               
print("End");
print("The test result has been explored.");
                    
        
