'''

@author: v-xinhzh
Take out the log files (end with .log) from a folder.
'''
import os;
import shutil;


FileCountLimit=100000;

filecount=0;
errors=0;


SourceFilePath="\\\\Tcsbu01\\SiteUsers\\N6 4F\\Calgary 5x3 log\\";

MainDestinedFolder="C:\\temp\\tempfile\\20170320\\";
if not os.path.exists(SourceFilePath):
    print("The source file folder doesn't exist.");
    exit;

if not os.path.exists(MainDestinedFolder):
    os.makedirs(MainDestinedFolder);

for paths,dirs,files in os.walk(SourceFilePath, False):
    DirArray=paths.split("\\");
    try:
        DestinedFolder=MainDestinedFolder+DirArray[6]+"\\"+DirArray[7];
    except:
        print(paths);
        exit;
    if not os.path.exists(DestinedFolder):
        os.makedirs(DestinedFolder);
    
    for OneLogFile in files:
        if OneLogFile.endswith(".log"):
            shutil.copy2(paths+"\\"+OneLogFile,DestinedFolder+"\\"+OneLogFile);
            #print(OneLogFile + "is archieved from "+paths);
            filecount+=1;
        if filecount>FileCountLimit:
            break;
print("There are %d files are archieved."%(filecount));
print("There are total %d errors." %(errors));
