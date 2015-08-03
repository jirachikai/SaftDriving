from readData import readAllData
import csv
from Preprocess import *
from FeatureExtraction import FE
data = readAllData("H:\TaxiNetwork\DriverSafty\DriverSafty\data_7_31\data")
afterFilters = []
extractor = FE()
for d in data:
    afterFilter = lowPassFilter(data[d]["a1"],0.01)
    afterFilters.append(afterFilter)
    spice = splitData(afterFilter)
    title = extractor.getTitle()
    w = csv.writer(open(d,"wb"))
    w.writerow(title)
    for section in spice:
        w.writerow(extractor.extract(section))
print len(afterFilters)