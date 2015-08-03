from dtw import dtw
from readData import readData, readAllData
from Preprocess import lowPassFilter
def valid(var,mean,DelVar = 0.001,DelMean = 0.5):
    if var >= DelVar or abs(mean)>DelMean:
        return True
    return False

def merge(d,vars,means):
    start = 0
    flag = True
    end = 0
    newD = []
    split = []
    for i in xrange(len(vars)):
        candidate = valid(vars[i],means[i])
        if flag and candidate:
            start = i
            flag = False
        elif (not flag) and candidate:
            end = i+1
        elif (not flag) and (not candidate):
            if start<end:
                print start,end
                split.append([start,end])
            flag = True
        else:
            continue
    start = [0,0]
    for p in split:
        if start[1]+1 == p[0]:
            start[1] = p[1]
        else:
            if start[1]-start[0]>5:
                l = []
                for i in range(start[0],start[1]):
                    l.extend(d[i][0])
                newD.append(l)
            start = p
    if start[1]-start[0]>5:
        l = []
        for i in range(start[0],start[1]):
            l.extend(d[i][0])
        newD.append(l)
    return newD

def isZero(p1,p2):
    if p1>=0.0 and p2<=0.0:
        return True
    elif p1<=0.0 and p2>=0.0:
        return True
    return False

def splitData2(data,step = 200):
    start = 0
    end = 0
    d = []
    for i in xrange(len(data)-1):
        if isZero(data[i],data[i+1]):
            print start,end
            if end -start >=step:
                d.append(data[start:end])
            start = end
        else:
            end = i
    if end -start >=step:
        d.append(data[start:end])
    return d

data = readData("data/turn/Turn1.csv")
sf = lowPassFilter(data["AX"],0.02)
#d,vars,means = splitData(sf.tolist())
#newD = merge(d,vars,means)
#print len(newD)
#for line in newD:
#    print len(line)
newD = splitData2(sf)
for line in newD:
    print len(line)
data = readData("data/turn/Turn3.csv")
sf = lowPassFilter(data["AX"],0.02)
for line in splitData2(sf):
    newD.append(line)
for line in newD:
    sim = []
    for line2 in newD:
        dist, cost, path = dtw(line, line2)
        sim.append(dist)
    print sim
#Visualize(sf,newD)


