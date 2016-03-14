import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

data = pd.read_csv('PF_data1976-01-13_1993-04-09.csv')

pfNorth = []
pfSouth = []
Y = []
M = []
D = []
date = []

#print (data.head())
for i in range(len(data)):
    Y.append(data.loc[i,"year"])
    M.append(data.loc[i,"month"])
    D.append(data.loc[i,"day"])
    pfNorth.append(data.loc[i,"sflux_n"])
    pfSouth.append(data.loc[i,"sflux_s"])

#Getting Date Axis
for i in range( 0, len(Y) ):
    d = datetime.date(int(Y[i]), int(M[i]), int(D[i]) ).toordinal()
    date.append( Y[i] + (d - datetime.date(int(Y[i]), 1, 1).toordinal() )/(datetime.date(int(Y[i]) + 1, 1, 1).toordinal() - datetime.date(int(Y[i]), 1, 1).toordinal() ) )

date = np.array(date)
pfNorth = np.array(pfNorth)
pfSouth = np.array(pfSouth)
#Extract bad pixels
ClrTh = 2.5e20
inxNg = np.array(np.where(data.max_pxflux_n > ClrTh)[0])
inxNs = np.array(np.where(data.max_pxflux_n <= ClrTh)[0])

inxSg = np.array(np.where(data.max_pxflux_s > ClrTh)[0])
inxSs = np.array(np.where(data.max_pxflux_s <= ClrTh)[0])



#Plotting Northern Hemisphere
def pf1():
    plt.subplot(211)
    plt.plot(date[inxNs], pfNorth[inxNs], 'b.')
    plt.plot(date[inxNg], pfNorth[inxNg], 'm.')
    plt.axis([1976, 1993.5, -1e23, 1e23])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above 65^o)')

#Plotting Southern Hemisphere
def pf2():
    plt.subplot(212)
    plt.plot(date[inxSs], pfSouth[inxSs], 'r.' )
    plt.plot(date[inxSg], pfSouth[inxSg], 'g.')
    plt.axis([1976, 1993.5, -1e23, 1e23])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below 65^o)')


plt.subplots_adjust(hspace = .40)
pf1()
pf2()

plt.show()
