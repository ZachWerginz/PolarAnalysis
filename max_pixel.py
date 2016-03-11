import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

data = pd.read_csv('imb85_PF_1976-01-13_1993-04-09.csv')
pfNorth = []
pfSouth = []
maxNorth = []
maxSouth = []

for i in range(len(data) ):
    maxNorth.append( data.iat[i, 15] )
    maxSouth.append( data.iat[i, 25] )
    pfNorth.append( abs(data.iat[i, 10]) )
    pfSouth.append( abs(data.iat[i, 20]) )

xmin = min( [min(maxNorth), min(maxSouth)] )
xmax = max( [max(maxNorth), max(maxSouth)] )

ymin = min( [min(pfNorth), min(pfSouth)] )
ymax = max( [max(pfNorth), max(pfSouth)] )

xmin = xmin - .3*xmin
xmax = xmax + .3*xmax
ymin = ymin - .3*ymin
ymax = ymax + .3*ymax

#Plotting Northern Hemisphere
def pf1():
    plt.subplot(211)
    plt.plot(maxNorth, pfNorth, 'bo')
    plt.axis([-xmin, xmax, ymin, ymax])
    plt.xlabel('Max Pixel Flux')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above 65^o)')

#Plotting Southern Hemisphere
def pf2():
    plt.subplot(212)
    plt.plot(maxSouth, pfSouth, 'ro' )
    plt.axis([-xmin, xmax, ymin, ymax])
    plt.xlabel('Max Pixel Flux')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below 65^o)')


plt.subplots_adjust(hspace = .40)
pf1()
pf2()

plt.show()
