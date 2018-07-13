'''

@author: v-xinhzh
Take out the specify files from a folder that has some compressed files.
'''
import zipfile;
import os;
import shutil;


# Tester station name
TesterStationName="CRA1";

#Inline station
#MyTesters={"E1118419","E1003133","MS2435619","E1118416","E1118395","E1118519","MS3943653","MS3509839"};

#UT station
#MyTesters={"MS5342381","MS5342148","MS5342392","MS5342159","MS4004521"};

#Mura station
MyTesters={"E1569149","E1568893","E1122897","E1569089","E1569081","E1568871","E1122896","E1568253","E1568788","E1569059","E1122925","E1002343"};

TestDate={"2017-02-17","2017-02-18","2017-02-19"};

SubSourcePath="c$\\temp\\LogArchive\\";


# SourcePath="C:\\Work\\Chariot\\RepairLineSensorLog\\"
# DestinedFolder="C:\\Work\\Chariot\\RepairLineSensorLog\\Sensor_Log\\";

KeyFileName="AudioHohd";

FileCountLimit=100000;

filecount=0;
errors=0;

for TesterName in MyTesters:
    for mydate in TestDate:
        SourceFilePath="\\\\"+TesterName+"\\"+SubSourcePath+mydate+"\\";
        #DestinedFolder="D:\\Dummy Data\\20170220\\123\\"+TesterName+"\\";
        #SourceFilePath="D:\\Dummy Data\\20170220\\E11xxx\\Archieve\\"+mydate+"\\";
        DestinedFolder="C:\\temp\\tempfile\\20170901\\"+TesterStationName+"\\"+TesterName+"\\";
        if not os.path.exists(SourceFilePath):
            print("The source file folder "+mydate+" doesn't exist.");
            continue;
        
        if not os.path.exists(DestinedFolder):
            os.makedirs(DestinedFolder);
        
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
                                    shutil.copy2(SourceFilePath+OneZipFile,DestinedFolder+"\\"+OneZipFile);
                                    print(OneZipFile + " is archieved from "+SourceFilePath);
                                    filecount+=1;
                                except:
                                    errors+=1;
                                    continue;
                if filecount>FileCountLimit:
                    break;
print("Achieve %d files with %s totally." %(filecount,KeyFileName));
print("There are total %d errors." %(errors));
