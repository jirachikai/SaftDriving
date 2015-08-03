from readData import readAllData
from Preprocess import lowPassFilter
from Visualize import Visualize
import copy
data = readAllData("H:\TaxiNetwork\DriverSafty\DriverSafty\data_7_31\data")
X = {}
for d in data:
    X[d] = copy.copy(data[d]["a1"])
    X[d] = lowPassFilter(X[d])
del data


