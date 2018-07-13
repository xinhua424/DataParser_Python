'''

@author: v-xinhzh
Read the specify parameters from the log files in the folder and sub folder
'''
import os,csv;


SourceFolder="C:\\Work\\Chariot\\RepairLineSensorLog\\Sensor_Log\\";
SummaryFileName="Summary.csv"

KeyFileName="SensorTest";
KeyParameters=("MagCalibrationGainX","MagCalibrationGainY","MagCalibrationGainZ");

resultfile=open(SourceFolder+SummaryFileName,"wb");
csw=csv.writer(resultfile,delimiter=",",quoting=csv.QUOTE_MINIMAL);
filenum=0;

for path,dirs,files in os.walk(SourceFolder, False):
    for OneFile in files:
        if KeyFileName not in OneFile:
            continue;
        else:
#             filenum+=1;
#             if filenum>100:
#                 break;
            with open(path+"\\"+OneFile,"rb") as logfile:
                csr=csv.reader(logfile,delimiter=",",quotechar="|");
                result=[];
                for lines in csr:
                    try:
                        if KeyParameters[0] in lines[-1] and "|" in lines[-1]:
                            result.append(path.split("\\")[-1]);
                            result.append(lines[-2]);
                            result.append(lines[-1].split("|")[2]);
                        elif KeyParameters[1] in lines[-1] and "|" in lines[-1]:
                            result.append(lines[-1].split("|")[2]);
                        elif KeyParameters[2] in lines[-1] and "|" in lines[-1]:
                            result.append(lines[-1].split("|")[2]);
                            csw.writerow(result);
                            break;
                    except:
                        print(lines[-2]);
                        print(lines[-1]);
                        continue;
                            
                    
        