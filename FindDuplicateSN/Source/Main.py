'''
Created on Sep 28, 2015

@author: v-xinhzh@microsoft.com
Remove the duplicated test of same DUTs, keep the first test by the modified time.
'''
import os
import FileActions
from __builtin__ import raw_input


SourceFolder=os.getcwd();
#SourceFolder="C:\\Work\\Chariot\\20150929\\data";
Dictionary_DUTs={};
print("The current folder is: "+SourceFolder);

#Get all of the files.
for path,dirs,files in os.walk(SourceFolder, False):
    for filename in files:
        if("UsbMassStorageTest" in filename)&(".log" in filename):
            temp=filename.split('_');
            SN=temp[1].split('.')[0];
            if(SN in Dictionary_DUTs):
                Dictionary_DUTs[SN]+=1;
            else:
                Dictionary_DUTs[SN]=1;
print("There are total %s DUTs before running the filter." %(Dictionary_DUTs.__len__()));

#Remove all of the files that are duplicated more than twice.
for SN,duplicate in Dictionary_DUTs.items():
    if(duplicate>3):
        #delete the files.
        FileActions.DeleteAllFiles(SourceFolder, SN);
        Dictionary_DUTs.__delitem__(SN);
    elif (duplicate>1)&(duplicate<=3):
        FileActions.DeleteOtherFiles(SourceFolder, SN);
        Dictionary_DUTs[SN]=1;

#Write the dictionary to the csv file
#Csv_Writer=csv.writer(open("SN_Result2.csv",'wb'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL);
#fileHeader=["SN","Quantity"];
#Csv_Writer.writerow(fileHeader);
#for key, value in Dictionary_DUTs.items():
#    Csv_Writer.writerow([key,str(value)]);

print("There are %s DUTs left are running filter." %(Dictionary_DUTs.__len__()));
#Hold on the console.
print("Please press Enter to return...");
a=raw_input();
