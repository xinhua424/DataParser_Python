'''

@author: v-xinhzh
Take out the specify files from a folder that has some compressed files.
'''
import zipfile;
import os;

SourcePath="D:\\Dummy Data\\20170222\\"
DestinedRootFolder="C:\\Temp\\tempfile\\20170222\\";

# SourcePath="C:\\Work\\Chariot\\RepairLineSensorLog\\"
# DestinedFolder="C:\\Work\\Chariot\\RepairLineSensorLog\\Sensor_Log\\";

FileCountLimit=100000;

filecount=0;
errors=0;
for paths,dirs,files in os.walk(SourcePath, False):
    for OneZipFile in files:
        if OneZipFile.endswith(".zip"):
            zfile=zipfile.ZipFile(paths+"\\"+OneZipFile,"r");
            for File in zfile.namelist():
                if not File.endswith(".err"):
                    continue;
                else:
                    Dirname,ErrorFileName=os.path.split(File);
                    ExpectedLogFile=ErrorFileName.split(".err")[0]+".log";
                    PathList=paths.split("\\");
                    DestinedFolder=DestinedRootFolder+PathList[-2]+"\\"+PathList[-1]+"\\";
                    try:
                        zfile.extract(ExpectedLogFile, DestinedFolder);
                        zfile.extract(ErrorFileName,DestinedFolder);
                        print("Extract the log file: "+ErrorFileName);
                        filecount+=1;
                    except:
                        print("Error happens on "+DestinedFolder+ExpectedLogFile);
                        errors+=1;
                        continue;
        if filecount>FileCountLimit:
            break;
    if filecount>FileCountLimit:
        break;
print("Achieve %d files with totally." %(filecount));
print("There are total %d errors." %(errors));