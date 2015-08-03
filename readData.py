import os,csv
def readData(f):
    f = csv.reader(open(f))
    data = {}
    title = []
    for line in f:
        if not title:
            title = line
            for l in title:
                data[l] = []
        else:
            for i in xrange(len(title)):
                data[title[i]].append(float(line[i]))
    return data

def readAllData(folder):
    data = {}
    for file in os.listdir(folder):
        path = folder + "/" + file
        data[file] = readData(path)
    return data
