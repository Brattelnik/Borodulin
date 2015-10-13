__author__ = 'Ivan'

import math
import pylab
from matplotlib import mlab

xmin = -20.0
xmax = 20.0

dx = 0.01
xlist = mlab.frange (xmin, xmax, dx)

pylab.ion()

for n in range (50):
        ylist = [math.sin (x + n / 2.0) for x in xlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()

pylab.close()