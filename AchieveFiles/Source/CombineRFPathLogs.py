'''

@author: v-xinhzh
Read all of the VNA trace data from the specified folder, combine all of the S parameter data into one csv file.
'''
import os,csv;
import itertools as IT;


RootFolder="C:\\Work\\Andromeda\\PCBA\\MB\\EV4\\RF probe engagement validation\\Rafla MB6\\";
SubRoot="Board No7 PxLB to WiFi0";
SubSourceFolderName="DUT2";
SummaryFileName="Combined.csv"

for path,dirs,files in os.walk(RootFolder+SubRoot+"\\"+SubSourceFolderName, False):
    handles = [open(RootFolder+SubRoot+"\\"+SubSourceFolderName+"\\"+ filename, 'rb') for filename in files]    
    readers = [csv.reader(f, delimiter=',') for f in handles]
    with  open(RootFolder+SubRoot+"_"+SubSourceFolderName+"_"+SummaryFileName, 'wb') as h:
        writer = csv.writer(h, delimiter=',', lineterminator='\n', )
        for rows in IT.izip_longest(*readers, fillvalue=['']*2):
            combined_row = []
            FrequencyRecorded=False;
            for row in rows:
                if not FrequencyRecorded:
                    row = row[:2] # select the columns you want
                    FrequencyRecorded=True;
                else:
                    row=row[1:2];
                combined_row.extend(row)
#                 if len(row) == 2:
#                     combined_row.extend(row)
#                 else:
#                     combined_row.extend(['']*2)
            writer.writerow(combined_row)
        print "The csv logs are combined.";
