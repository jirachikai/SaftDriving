import os,csv
from readData import readAllData
#data = readAllData("H:\TaxiNetwork\DriverSafty\DriverSafty\CurveLabeledData")
def Merge(folder,target):
    allTitle = True
    t = csv.writer(open(target,"w"))
    for file in os.listdir(folder):
        path = folder + "/" + file
        f = csv.reader(open(path))
        title = True
        for line in f:
            if title:
                if allTitle:
                    t.writerow(line)
                    allTitle = False
                title = False
            else:
                t.writerow(line)

Merge("H:\TaxiNetwork\DriverSafty\DriverSafty\CurveLabeledData","CurveWeka.csv")