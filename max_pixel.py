import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

data = pd.read_csv('t4_PF_data1976-01-13_1993-04-09.csv')

pfNorth = np.array(data.sfluxc_n)
pfSouth = np.array(data.sfluxc_s)
max_pxflux_n = np.array(data.max_pxflux_n)
max_pxflux_s = np.array(data.max_pxflux_s)
max_pxf_n = np.array(data.max_pxf_n)
max_pxfc_n = np.array(data.max_pxfc_n)
max_pxf_s = np.array(data.max_pxf_s)
max_pxfc_s = np.array(data.max_pxfc_s)

ClrTh = 3.5e20
inxNg = np.array(np.where(max_pxflux_n > ClrTh)[0])
inxNs = np.array(np.where(max_pxflux_n <= ClrTh)[0])

inxSg = np.array(np.where(max_pxflux_s > ClrTh)[0])
inxSs = np.array(np.where(max_pxflux_s <= ClrTh)[0])

#Plotting Northern Hemisphere
def pf1():
    plt.subplot(211)
    plt.plot(max_pxflux_n[inxNs], pfNorth[inxNs], 'b.')
    plt.plot(max_pxflux_n[inxNg], pfNorth[inxNg], 'm.')
    plt.xlabel('Max abs Unsigned Pixel Flux')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above $65^\circ$)')

#Plotting Southern Hemisphere
def pf2():
    plt.subplot(212)
    plt.plot(max_pxflux_s[inxSs], pfSouth[inxSs], 'r.' )
    plt.plot(max_pxflux_s[inxSg], pfSouth[inxSg], 'g.' )
    plt.xlabel('Max abs Unsigned Pixel Flux')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below $65^\circ$)')

#Northern Hemisphere Pixel Flux and Field
def pf3():
    plt.figure(1)
    plt.plot(max_pxflux_n[inxNg], max_pxfc_n[inxNg], 'b.')
    plt.plot(max_pxflux_n[inxNs], max_pxfc_n[inxNs], 'm.')
    plt.xlabel('Max abs Unsigned Pixel Flux')
    plt.ylabel('Max Pixel Field')
    plt.title('North Pole (above $65^\circ$)')

#Southern Hemisphere Pixel Flux and Field
def pf4():
    plt.figure(2)
    plt.plot(max_pxflux_s[inxSg], max_pxfc_s[inxSg], 'r.')
    plt.plot(max_pxflux_s[inxSs], max_pxfc_s[inxSs], 'g.')
    plt.xlabel('Max abs Unsigned Pixel Flux')
    plt.ylabel('Max Pixel Field')
    plt.title('South Pole (above $65^\circ$)')
plt.subplots_adjust(hspace = .40)
#pf1()
#pf2()
pf3()
pf4()

plt.show()
