'''

@author: v-xinhzh
Take out the specify files from a folder that has some compressed files.
'''
import zipfile;
import os;
import shutil;


# Tester station name
TesterStationName="CRA1";

MyTesters={"MS5416652","MS40044710"};

#TestDate={"2017-04-17","2017-04-18","2017-04-19"};

SubSourcePath="c$\\temp\\LogArchive\\";

#===============================================================================
# SourcePath="E:\\Temp data\\20170512\\"
# DestinedFolder="E:\Temp data\20170512a\\";
#===============================================================================

KeyFileName="FanTest";

FileCountLimit=100000;

filecount=0;
errors=0;

for TesterName in MyTesters:
        #=======================================================================
        #  DestinedFolder="E:\\Temp data\\20170512a\\";
        #  SourceFilePath="E:\\Temp data\\20170512\\";
        #=======================================================================
        SourceFilePath="\\\\"+TesterName+"\\"+SubSourcePath+"\\";
        DestinedFolder="C:\\temp\\Shawn\\20170512\\"+TesterStationName+"\\"+TesterName+"\\";
        if not os.path.exists(SourceFilePath):
            print("The source file path {"+SourceFilePath+"} doesn't exist.");
            continue;
        
        if not os.path.exists(DestinedFolder):
            os.makedirs(DestinedFolder);
        
        for paths,dirs,files in os.walk(SourceFilePath, False):
            for OneZipFile in files:
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
