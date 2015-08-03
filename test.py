from scipy.optimize import leastsq,curve_fit
import numpy as np
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,10,5,6])
def func(x,a,b):
    return a*x+b

#def residuals(p, y, x):
#    return y-func(x,p)

p0=[0, 0]
print curve_fit(func,x,y)
