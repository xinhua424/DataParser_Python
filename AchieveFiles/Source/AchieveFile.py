'''

@author: v-xinhzh
Take out the specify files from a folder that has some compressed files.
'''
import zipfile;
import os,csv;
import shutil;
import sys;


#SourcePath="\\\E1118419\\";
SubSourcePath="c$\\temp\\LogArchive\\";

DestinedFolder="C:\\temp\\tempfile\\20170220\\";

# SourcePath="C:\\Work\\Chariot\\RepairLineSensorLog\\"
# DestinedFolder="C:\\Work\\Chariot\\RepairLineSensorLog\\Sensor_Log\\";

KeyFileName="Vertex.Dev_3.8.17046.01_20170216_RR_PSZ"

FileCountLimit=100000;

# if not os.path.exists(SourcePath+SubSourcePath):
#     print("The source file folder doesn't exist.");
#     exit;

#TesterName=SourcePath.split("\\")[-2]; 
 
# if not os.path.exists(DestinedFolder+TesterName):
#     os.makedirs(DestinedFolder+TesterName);
#     DestinedFolder=DestinedFolder+TesterName+"/";

filecount=0;
errors=0;

cwd=os.getcwd();    #Get the execution path.
try:
    testernamefile=open(cwd+"\\testernames.csv","rb");
    testnamereader=csv.reader(testernamefile,delimiter=",",quotechar="|");
    execdatefile=open(cwd+"\\date.csv","rb");
    execdatereader=csv.reader(execdatefile,delimiter=",",quotechar="|");
except:
    print("Error of the open files.");
    exit;

for testername in testnamereader:
    if not os.path.exists(DestinedFolder+testername[0]):
        os.makedirs(DestinedFolder+testername[0]);
        DestinedFolder=DestinedFolder+testername[0]+"/";
    for execdate in execdatereader:
        print(testername[0]);
        print(SubSourcePath);
        print(execdate[0]);
        SourceFilePath="\\\\"+testername[0]+"\\"+SubSourcePath+execdate[0]+"\\";
        if not os.path.exists(SourceFilePath):
            continue;
        for paths,dirs,files in os.walk(SourceFilePath, False):
            for OneZipFile in files:
                if OneZipFile.endswith(".zip"):
                    zfile=zipfile.ZipFile(paths+"\\"+OneZipFile,"r");
                    for File in zfile.namelist():
                        if File.endswith(".err"):
                            continue;
                        else:
                            (Dirname,Filename)=os.path.split(File);
                            if (KeyFileName in File):
                                try:
                                    shutil.copy2(SourceFilePath+OneZipFile,DestinedFolder+OneZipFile);
                                    filecount+=1;
                                except:
                                    errors+=1;
                                    continue;
                if filecount>FileCountLimit:
                    break;
print("Achieve %d files with %s totally." %(filecount,KeyFileName));
print("There are total %d errors." %(errors));
