import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

#Plot Northern Hemisphere
def pf1(c):
    plt.subplot(211)
    plt.plot(date, normflux_n, color = c, marker = '.', linestyle = 'None')
    plt.axis([1976, 2017, -3e22, 3e22])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above $65^\circ$)')

#Plot Southern Hemisphere
def pf2(c):
    plt.subplot(212)
    plt.plot(date, normflux_s, color = c, marker = '.', linestyle = 'None')
    plt.axis([1976, 2017, -3e22, 3e22])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below $65^\circ$)')


files = ["PF_data1976-01-13_1993-04-11.csv", "PF_data1992-04-21_1999-12-30.csv", "PF_data1996-01-01_2011-04-11.csv","PF_data2010-04-08_2016-04-08.csv"]
#files = ["PF_data1976-01-13_1993-04-09.csv", "PF_data1976-01-13_1993-04-11.csv"]
carr = ['red', 'yellow', 'green', 'blue']
#data = [pd.read_csv(files[0]), pd.read_csv(files[1]), pd.read_csv(files[2]), pd.read_csv(files[3])]
data = []
j = 0

for num in files:
    data.append(pd.read_csv(num))

for file in data:
    Y = np.array(file.year)
    M = np.array(file.month)
    D = np.array(file.day)
    date = []
    visarea_n = np.array(file.visarea_n)
    visarea_s = np.array(file.visarea_s)
    maxarea_n = np.nanmax(file.visarea_n)
    maxarea_s = np.nanmax(file.visarea_s)
    pfNorth = np.array(file.sfluxc_n)
    pfSouth = np.array(file.sfluxc_s)

    #Getting Date Axis
    for i in range( 0, len(Y) ):
        d = datetime.date(int(Y[i]), int(M[i]), int(D[i]) ).toordinal()
        date.append( Y[i] + (d - datetime.date(int(Y[i]), 1, 1).toordinal() )/(datetime.date(int(Y[i]) + 1, 1, 1).toordinal() - datetime.date(int(Y[i]), 1, 1).toordinal() ) )

    date = np.array(date)
    pfNorth = np.array(pfNorth)
    pfSouth = np.array(pfSouth)

    normflux_n = pfNorth*maxarea_n/visarea_n
    normflux_s = pfSouth*maxarea_s/visarea_s

    plt.subplots_adjust(hspace = .40)
    pf1(carr[j])
    pf2(carr[j])
    j = j + 1






plt.show()
