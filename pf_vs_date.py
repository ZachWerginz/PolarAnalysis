import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

data = pd.read_csv('PF_data1992-05-03_1999-12-30.csv')

pfNorth = np.array(data.unsfluxc_n)/100
pfSouth = np.array(data.unsfluxc_s)/100
Y = np.array(data.year)
M = np.array(data.month)
D = np.array(data.day)
date = []
max_pxf_n = np.array(data.max_pxf_n)
max_pxfc_n = np.array(data.max_pxfc_n)
max_pxf_s = np.array(data.max_pxf_s)
max_pxfc_s = np.array(data.max_pxfc_s)
visarea_n = np.array(data.visarea_n)
visarea_s = np.array(data.visarea_s)
maxarea_n = np.nanmax(visarea_n)
maxarea_s = np.nanmax(visarea_s)

#Getting Date Axis
for i in range( 0, len(Y) ):
    d = datetime.date(int(Y[i]), int(M[i]), int(D[i]) ).toordinal()
    date.append( Y[i] + (d - datetime.date(int(Y[i]), 1, 1).toordinal() )/(datetime.date(int(Y[i]) + 1, 1, 1).toordinal() - datetime.date(int(Y[i]), 1, 1).toordinal() ) )

date = np.array(date)

normflux_n = pfNorth*maxarea_n/visarea_n
normflux_s = pfSouth*maxarea_s/visarea_s

#Extract bad pixels
#ClrTh = 3.5e20
#inxNg = np.array(np.where(data.max_pxflux_n > ClrTh)[0])
#inxNs = np.array(np.where(data.max_pxflux_n <= ClrTh)[0])

#inxSg = np.array(np.where(data.max_pxflux_s > ClrTh)[0])
#inxSs = np.array(np.where(data.max_pxflux_s <= ClrTh)[0])



#Plotting Northern Hemisphere
def pf1():
    plt.subplot(211)
    plt.plot(date, normflux_n, 'b.')
    plt.plot(date, normflux_n, 'm.')
    #plt.axis([1976, 2017, -3e22, 3e22])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above $65^\circ$)')

#Plotting Southern Hemisphere
def pf2():
    plt.subplot(212)
    plt.plot(date, normflux_s, 'r.' )
    plt.plot(date, normflux_s, 'g.')
    #plt.axis([1976, 2017, -3e22, 3e22])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below $65^\circ$)')


plt.subplots_adjust(hspace = .40)
pf1()
pf2()

plt.show()
