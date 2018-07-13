'''
Purpose: Find files in a folder that contains some compressed files. The compressed file may contains the files we want.
Print the path of the destined files.
@author: v-xinhzh
'''
import zipfile,os;

SourcePath="C:\\Work\\Chariot\\RepairLineSensorLog\\";
KeyWord="8580754157";

for paths,dirs,files in os.walk(SourcePath, False):
    for OneZipFile in files:
        if not OneZipFile.endswith(".zip"):
            continue;
        else:
            zfile=zipfile.ZipFile(paths+"\\"+OneZipFile,"r");
            for File in zfile.namelist():
                if File.endswith("/"):
                    continue;
                else:
                    (Dirname,Filename)=os.path.split(File);
                    if (KeyWord in File) and (File.endswith(".log")):
                        print("The file contains %s is in %s" %(KeyWord,paths+"\\"+Dirname+OneZipFile));
                        break;