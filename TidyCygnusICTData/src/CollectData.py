'''

@author: v-xinhzh
Read the specify parameters from the log files in the folder and sub folder
'''
import os,csv;
#from token import EQUAL

#Modify SourceFolder as the log file path.
#Please use \\ in the path string, rather than \.
SourceFolder="C:\\Work\\Cygnus\\PCBA\\20161205\\ICT 5X3 CSV\\";
testername="TPTICTPT171";

for path,dirs,files in os.walk(SourceFolder, False):
    for OneFile in files:
        if "Reworked" in OneFile and ".csv" in OneFile:
            continue;
        resultfile=open(path+"\\"+OneFile.replace(".csv","")+"_Reworked.csv","wb");
        csw=csv.writer(resultfile,delimiter=",",quoting=csv.QUOTE_MINIMAL);
        with open(path+"\\"+OneFile,"rb") as logfile:
            csr=csv.reader(logfile,delimiter=",",quotechar="|");
            for lines in csr:
                result=[];
                try:
                    for item in lines:
                        if "#1" in item:
                            item=item.replace("#1","");
                        if "#2" in item:
                            item=item.replace("#2","");    
                        if "#3" in item:
                            item=item.replace("#3",""); 
                        if "#4" in item:
                            item=item.replace("#4",""); 
                        if testername in item:
                            item=item+"_"+path.split("\\")[-1];
                        result.append(item);
                    csw.writerow(result);
                except:
                    print("Errors.");
                    continue;
        
print("End");
print("The FTF test result has been explored.");
                    
        
