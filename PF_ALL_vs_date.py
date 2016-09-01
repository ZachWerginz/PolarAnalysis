"""This is a script that reads in h5 files and plots the instruments
each a different color."""
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from uncertainty import Measurement as M

#Plot Northern Hemisphere
def pf1(c):
    plt.subplot(211)
    plt.plot(date, normflux_n, color = c, marker = '.', linestyle = 'None')
    plt.axis([dt.datetime(1976,1,1), dt.datetime(2016,7,5), -3e22, 3e22])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above $65^\circ$)')

#Plot Southern Hemisphere
def pf2(c):
    plt.subplot(212)
    plt.plot(date, normflux_s, color = c, marker = '.', linestyle = 'None')
    plt.axis([dt.datetime(1976,1,1), dt.datetime(2016,7,5), -3e22, 3e22])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below $65^\circ$)')


files = ['512.h5', 'SPMG.h5', 'MDI.h5', 'hmi.h5']
#files = ["PF_data1976-01-13_1993-04-09.csv", "PF_data1976-01-13_1993-04-11.csv"]
carr = ['red', 'yellow', 'green', 'blue']
#data = [pd.read_csv(files[0]), pd.read_csv(files[1]), pd.read_csv(files[2]), pd.read_csv(files[3])]
j = 0

for f in files:
    hdf = pd.read_hdf(f)
    date = hdf['date']
    visarea_n = np.array([x.v for x in hdf['visarea_n'].values])
    visarea_s = np.array([x.v for x in hdf['visarea_s'].values])
    maxarea = 2*np.pi*6.95508e10**2*(1-np.cos(np.deg2rad(90-75))) 
    pfNorth = np.array([x.v for x in hdf['sfluxc_n'].values])
    pfSouth = np.array([x.v for x in hdf['sfluxc_s'].values])
    normflux_n = pfNorth*maxarea/visarea_n
    normflux_s = pfSouth*maxarea/visarea_s
    plt.subplots_adjust(hspace = .40)
    pf1(carr[j])
    pf2(carr[j])
    j = j + 1

plt.show()
