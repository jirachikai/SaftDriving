import numpy as np
import matplotlib.pyplot as pl
def Visualize(wave,title):
    axis_x = np.linspace(0,1,num=len(wave))
    pl.plot(axis_x,wave)
    pl.title(title)
    pl.axis('tight')
    pl.show()