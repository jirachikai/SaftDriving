import numpy as np
from scipy.optimize import leastsq,curve_fit

class FE(object):
    def getTitle(self):
        return  [
            "mean",
            "var",
            "calculus",
            "maxAbs",
            "deltaT",
            "median",
            "gradientF",
            "gradientS",
            "bS",
            "label"
        ]
    
    def extract(self,list):
        r = [
            self.__mean(list),
            self.__var(list),
            self.__sum(list),
            self.__maxAbs(list),
            self.__deltaT(list),
            self.__median(list)
        ]
        for i in self.__fitting(list):
            r.append(i)
        return r


    def __mean(self,list):
        return np.mean(list)

    def __var(self,list):
        return np.var(list)

    def __sum(self,list):
        return sum(list)

    def __maxAbs(self,list):
        s = self.__sum(list)
        if s <= 0:
            return abs(min(list))
        else:
            return max(list)

    def __deltaT(self,list):
        return len(list)

    def __median(self,list):
        return np.median(list)

    def __fitting(self,l):
        func = lambda x,a,b: a*x+b
        residuals = lambda p, y, x: y-func(x,p)
        s = self.__sum(l)
        l = l.tolist()
        if s <= 0:
            i = l.index(min(l))
        else:
            i = l.index(max(l))

        frt = np.array(l[:i])
        snd = np.array(l[i:])
        if len(frt)<5:
            opt_parmsF = [0.0,0.0]
        else:
            opt_parmsF, parm_covF = curve_fit(func, [i for i in xrange(len(frt))], frt)
        if len(snd)<5:
            opt_parmsS = [0.0,0.0]
        else:
            opt_parmsS, parm_covS = curve_fit(func, [i for i in xrange(len(snd))], snd)
        return opt_parmsF[0], opt_parmsS[0], opt_parmsS[1]

