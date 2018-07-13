'''

@author: v-xinhzh
Take out the specify files from a folder that has some compressed files.
'''
import zipfile;
import os;


SourcePath="C:\\Work\\Peregrine\\Vertex sensor log10.09-10.16.zip"
DestinedFolder="C:\\Work\\Peregrine\\Vertex sensor log10.09-10.16\\";

# SourcePath="C:\\Work\\Chariot\\RepairLineSensorLog\\"
# DestinedFolder="C:\\Work\\Chariot\\RepairLineSensorLog\\Sensor_Log\\";

KeyFileName="SensorTest"

FileCountLimit=100000;

if not os.path.exists(DestinedFolder):
    os.makedirs(DestinedFolder);

filecount=0;
errors=0;
for paths,dirs,files in os.walk(SourcePath, False):
    for OneZipFile in files:
        if OneZipFile.endswith(".zip"):
            zfile=zipfile.ZipFile(paths+"\\"+OneZipFile,"r");
            for File in zfile.namelist():
                if File.endswith("/"):
                    continue;
                else:
                    (Dirname,Filename)=os.path.split(File);
                    if (KeyFileName in File) and (File.endswith(".log")):
                        print "Decompressing " + Filename + " on " + Dirname;
                        try:
                            zfile.extract(File, DestinedFolder);
                            filecount+=1;
                        except:
                            errors+=1;
                            continue;
        if filecount>FileCountLimit:
            break;
    if filecount>FileCountLimit:
        break;
print("Achieve %d files with %s totally." %(filecount,KeyFileName));
print("There are total %d errors." %(errors));
        