from scipy import signal
def lowPassFilter(data,freq = 0.01):
    b,a = signal.butter(3,freq,'low')
    sf = signal.filtfilt(b,a,data)
    return sf

def isZero(p1,p2):
    if p1>=0.0 and p2<=0.0:
        return True
    elif p1<=0.0 and p2>=0.0:
        return True
    return False

def splitData(data,step=100):
    start = 0
    end = 0
    d = []
    for i in xrange(len(data)-1):
        if isZero(data[i],data[i+1]):
            if end -start >=step:
                d.append(data[start:end])
            start = end
        else:
            end = i
    return d