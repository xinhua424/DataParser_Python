'''

@author: v-xinhzh
Read all of the VNA trace data from the specified folder, combine all of the S parameter data into one csv file.
'''
import os,csv;
import itertools as IT;
import matplotlib.pyplot as plt

def plotS21(figurenum,xaxis,yaxis,ylabel,title,savefigpath):
    if len(xaxis) != len(yaxis):
        print "The array diamension is not same.";
        return;
    plt.figure(figurenum);
    plt.plot(xaxis,yaxis);
    plt.xlabel("frequency [Hz]");
    plt.ylabel(ylabel);
    plt.title(title);
    plt.grid(True);
#     plt.show();
    plt.savefig(savefigpath);
    plt.close();

RootFolder="C:\\Work\\Andromeda\\PCBA\\MB\\EV4\\RF probe engagement validation\\Rafla MB4\\";
SubRoot="";
SummaryFileName="Combined.csv"
figureindex=0;

for path,dirs,files in os.walk(RootFolder, False):
    slot1handles=[];
    slot2handles=[];
    SubRoot=path.split("\\")[-1];
    if SubRoot is "":
        break;
    for filename in files:
        if "DUT1" in filename:
            slot1handles.append(open(RootFolder+SubRoot+"\\"+ filename, 'rb'));
        if "DUT2" in filename:
            slot2handles.append(open(RootFolder+SubRoot+"\\"+ filename, 'rb'));
     
    slot1readers = [csv.reader(f, delimiter=',') for f in slot1handles];
    slot2readers = [csv.reader(f, delimiter=',') for f in slot2handles];
    
    #Deal with DUT1
    S21values=[];
    FrequencyArray=[];
    S21AverageArray=[];
    S21RippleArray=[];
    with  open(RootFolder+SubRoot+"_DUT1_"+SummaryFileName, 'wb') as slot1h:
        slot1writer = csv.writer(slot1h, delimiter=',', lineterminator='\n', )
        rowcount=0;
        for rows in IT.izip_longest(*slot1readers):
            rowcount+=1;
            if rowcount <3:
                continue;
            combined_row = [];
            FrequencyRecorded=False;
            for row in rows:
                if not FrequencyRecorded:
                    row = row[:2] # select the columns you want
                    FrequencyRecorded=True;
                    if rowcount>3:
                        FrequencyArray.append(float(row[0]));
                else:
                    row=row[1:2];
                combined_row.extend(row);
            if rowcount is 3:
                combined_row.extend(["Max","Min","Average","Ripple"]);
            else:
                S21strings=combined_row[1:];
                S21values=[float(S21SingleString) for S21SingleString in S21strings];
                S21Max=max(S21values);
                S21Min=min(S21values);
                S21Average=sum(S21values)/len(S21values);
                S21Ripple=S21Max-S21Min;
                combined_row.extend([S21Max,S21Min,S21Average,S21Ripple]);
                S21RippleArray.append(S21Ripple);
                S21AverageArray.append(S21Average);
            slot1writer.writerow(combined_row);
        figureindex+=1;
        plotS21(figureindex, FrequencyArray, S21AverageArray,"S21 Average [dB]", "Average of "+SubRoot+"_DUT1 path loss",RootFolder+SubRoot+"_DUT1_Average.png");
        figureindex+=1;
        plotS21(figureindex, FrequencyArray, S21RippleArray,"S21 Ripple [dB]", "Ripple of "+SubRoot+"_DUT1 path loss",RootFolder+SubRoot+"_DUT1_Ripple.png");
        print SubRoot+", the slot1 csv logs are combined.";
    
    # Deal with DUT2
    S21values=[];
    FrequencyArray=[];
    S21AverageArray=[];
    S21RippleArray=[];
    with  open(RootFolder+SubRoot+"_DUT2_"+SummaryFileName, 'wb') as slot2h:
        slot2writer = csv.writer(slot2h, delimiter=',', lineterminator='\n', )
        rowcount=0;
        for rows in IT.izip_longest(*slot2readers, fillvalue=""):
            rowcount+=1;
            if rowcount <3:
                continue;
            combined_row = [];
            FrequencyRecorded=False;
            for row in rows:
                if not FrequencyRecorded:
                    row = row[:2] # select the columns you want
                    FrequencyRecorded=True;
                    if rowcount>3:
                        FrequencyArray.append(float(row[0]));
                else:
                    row=row[1:2];
                combined_row.extend(row);
            if rowcount is 3:
                combined_row.extend(["Max","Min","Average","Ripple"]);
            else:
                S21strings=combined_row[1:];
                S21values=[float(S21SingleString) for S21SingleString in S21strings];
                S21Max=max(S21values);
                S21Min=min(S21values);
                S21Average=sum(S21values)/len(S21values);
                S21Ripple=S21Max-S21Min;
                S21RippleArray.append(S21Ripple);
                S21AverageArray.append(S21Average);
                combined_row.extend([S21Max,S21Min,S21Average,S21Ripple]);
            slot2writer.writerow(combined_row)
        figureindex+=1;
        plotS21(figureindex, FrequencyArray, S21AverageArray,"S21 Average [dB]", "Average of "+SubRoot+"_DUT2 path loss",RootFolder+SubRoot+"_DUT2_Average.png");
        figureindex+=1;
        plotS21(figureindex, FrequencyArray, S21RippleArray,"S21 Ripple [dB]", "Ripple of "+SubRoot+"_DUT2 path loss",RootFolder+SubRoot+"_DUT2_Ripple.png");
        print SubRoot+", the slot2 csv logs are combined.";

