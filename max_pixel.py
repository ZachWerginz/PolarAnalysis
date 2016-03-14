import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

data = pd.read_csv('PF_data1976-01-13_1993-04-09.csv')

pfNorth = np.array(data.sflux_n)
pfSouth = np.array(data.sflux_s)
max_pxflux_n = np.array(data.max_pxflux_n)
max_pxflux_s = np.array(data.max_pxflux_s)

ClrTh = 2.5e20
inxNg = np.array(np.where(max_pxflux_n > ClrTh)[0])
inxNs = np.array(np.where(max_pxflux_n <= ClrTh)[0])

inxSg = np.array(np.where(max_pxflux_s > ClrTh)[0])
inxSs = np.array(np.where(max_pxflux_s <= ClrTh)[0])

#Plotting Northern Hemisphere
def pf1():
    plt.subplot(211)
    plt.plot(max_pxflux_n[inxNs], pfNorth[inxNs], 'b.')
    plt.plot(max_pxflux_n[inxNg], pfNorth[inxNg], 'm.')
    plt.xlabel('Max abs Unsigned Pixel')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above 65^o)')

#Plotting Southern Hemisphere
def pf2():
    plt.subplot(212)
    plt.plot(max_pxflux_s[inxSs], pfSouth[inxSs], 'r.' )
    plt.plot(max_pxflux_s[inxSg], pfSouth[inxSg], 'g.' )
    plt.xlabel('Max abs Unsigned Pixel')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below 65^o)')


plt.subplots_adjust(hspace = .40)
pf1()
pf2()

plt.show()
