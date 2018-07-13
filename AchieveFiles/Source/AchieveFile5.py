'''

@author: v-xinhzh
Copy the specify files in the compressed file from a folder.
'''
import zipfile;
import os;
#import shutil;


# Tester station name
TesterStationName="CRA1";

#Inline station
#MyTesters={"E1118419","E1003133","MS2435619","E1118416","E1118395","E1118519","MS3943653","MS3509839"};

#UT station
#MyTesters={"MS5342381","MS5342148","MS5342392","MS5342159","MS4004521"};

#Mura station
MyTesters={"E1569149","E1568893","E1122897","E1569089","E1569081","E1568871","E1122896","E1568253","E1568788","E1569059","E1122925","E1002343"};

TestDate={"2017-08-26","2017-08-27","2017-08-28","2017-08-29","2017-08-30","2017-08-31","2017-09-01","2017-09-02","2017-09-03","2017-09-04","2017-09-05","2017-09-06","2017-09-07","2017-09-08","2017-09-09","2017-09-10",};

SubSourcePath="c$\\temp\\LogArchive\\";


# SourcePath="C:\\Work\\Chariot\\RepairLineSensorLog\\"
# DestinedFolder="C:\\Work\\Chariot\\RepairLineSensorLog\\Sensor_Log\\";

KeyFileName="HighOrderHarmonicDistortionTest";

FileCountLimit=1000000;

filecount=0;
errors=0;

for TesterName in MyTesters:
    for mydate in TestDate:
        SourceFilePath="\\\\"+TesterName+"\\"+SubSourcePath+mydate+"\\";
        #DestinedFolder="D:\\Dummy Data\\20170220\\123\\"+TesterName+"\\";
        #SourceFilePath="D:\\Dummy Data\\20170220\\E11xxx\\Archieve\\"+mydate+"\\";
        DestinedFolder="C:\\temp\\tempfile\\20170911\\"+TesterStationName+"\\"+TesterName+"\\";
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
                            
                            if (KeyFileName in File):
                                Dirname,myFileName=os.path.split(File);
                                try:
                                    zfile.extract(myFileName, DestinedFolder);
                                    print("Extract the log file: "+myFileName);
                                    filecount+=1;
                                except:
                                    print("Error happens on "+DestinedFolder+myFileName);
                                    errors+=1;
                                    continue;
                            
    if filecount>FileCountLimit:
        break;
print("Achieve %d files with %s totally." %(filecount,KeyFileName));
print("There are total %d errors." %(errors));
