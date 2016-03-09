import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

data = pd.read_csv('1PF_data1976-01-13_1993-04-09.csv')
pfNorth = []
pfSouth = []
Y = []
M = []
D = []
date = []

for i in range(len(data)):
    Y.append(data.iat[i,1])
    M.append(data.iat[i,2])
    D.append(data.iat[i,3])
    pfNorth.append(data.iat[i,10])
    pfSouth.append(data.iat[i,19])

#Getting Date Axis
for i in range( 0, len(Y) ):
    d = datetime.date(int(Y[i]), int(M[i]), int(D[i]) )
    date.append(d.toordinal()/365)

#Plotting Northern Hemisphere
def pf1():
    plt.subplot(211)
    plt.plot(date, pfNorth, 'bo')
    plt.axis([1976, 1993.5, -1e23, 1e23])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above 65^o)')

#Plotting Southern Hemisphere
def pf2():
    plt.subplot(212)
    plt.plot(date, pfSouth, 'ro')
    plt.axis([1976, 1993.5, -1e23, 1e23])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below 65^o)')


plt.subplots_adjust(hspace = .40)
pf1()
pf2()

plt.show()
