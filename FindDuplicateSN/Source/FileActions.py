import os

KeyName2="UsbMassStorageTest";
KeyName3=".log";

#Delete all of the files whose name has the KeyName
def DeleteAllFiles(FilePath, KeyName):
    for path,dirs,files in os.walk(FilePath,False):
        for filename in files:
            if KeyName in filename:
                os.remove(path+"\\"+filename);
                print("Delete %s" %(path+"\\"+filename));

#Delete all of the files except the one is first created.
def DeleteOtherFiles(FilePath,KeyName):
    TheEarliestFile="";
    for path,dirs,files in os.walk(FilePath, False):
        for filename in files:
            if (KeyName in filename)&(KeyName2 in filename)&(KeyName3 in filename):
                if TheEarliestFile=="":
                    TheEarliestFile=path+"\\"+filename;
                else:
                    #compare the current file and previous file's modified time
                    CurrentFileModifiedTime=os.path.getmtime(path+"\\"+filename);
                    EarliestFileModifiedTime=os.path.getmtime(TheEarliestFile);
                    if CurrentFileModifiedTime < EarliestFileModifiedTime: #The current file is modified earlier.
                        os.remove(TheEarliestFile);
                        TheEarliestFile=path+"\\"+filename;
                    else:
                        os.remove(path+"\\"+filename);
            else:
                continue;
