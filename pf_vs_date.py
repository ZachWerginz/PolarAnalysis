import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

deg_lim = 75

data1 = pd.read_csv('PF_data1996-01-01_2011-04-11.csv')
data2 = pd.read_csv('PF_1996-04-14_2011-04-11_uncertainty.csv')

pfNorth_IDL = np.abs(np.array(data1.sfluxc_n))
pfSouth_IDL = np.abs(np.array(data1.sfluxc_s))
pfNorth_PY = np.array(data2.sfluxc_n_v)
pfSouth_PY = np.array(data2.sfluxc_s_v)
Y = np.array(data1.year)
M = np.array(data1.month)
D = np.array(data1.day)
date = []
#max_pxf_n = np.array(data.max_pxf_n)
#max_pxfc_n = np.array(data.max_pxfc_n)
#max_pxf_s = np.array(data.max_pxf_s)
#max_pxfc_s = np.array(data.max_pxfc_s)
visarea_n_IDL = np.array(data1.visarea_n)
visarea_s_IDL = np.array(data1.visarea_s)
visarea_n_PY = np.array(data2.visarea_n_v)
visarea_s_PY = np.array(data2.visarea_s_v)
#maxarea_n = np.nanmax(visarea_n)
#maxarea_s = np.nanmax(visarea_s)
maxarea = 2*np.pi*6.95508e10**2*(1-np.cos(np.deg2rad(90-deg_lim)))

#Getting Date Axis
for i in range( 0, len(Y) ):
    d = datetime.date(int(Y[i]), int(M[i]), int(D[i]) ).toordinal()
    date.append( Y[i] + (d - datetime.date(int(Y[i]), 1, 1).toordinal() )/(datetime.date(int(Y[i]) + 1, 1, 1).toordinal() - datetime.date(int(Y[i]), 1, 1).toordinal() ) )

date = np.array(date)

ind1 = np.unique(data1.mdi_i, return_index=True)
ind2 = np.unique(data2.md, return_index=True)

mask1 = np.in1d(ind1[0], ind2[0])
mask2 = np.in1d(ind2[0], ind1[0])



normflux_n_IDL = pfNorth_IDL*maxarea/visarea_n_IDL
normflux_s_IDL = pfSouth_IDL*maxarea/visarea_s_IDL
normflux_n_PY = pfNorth_PY*maxarea/visarea_n_PY
normflux_s_PY = pfSouth_PY*maxarea/visarea_s_PY




#Extract bad pixels
#ClrTh = 3.5e20
#inxNg = np.array(np.where(data.max_pxflux_n > ClrTh)[0])
#inxNs = np.array(np.where(data.max_pxflux_n <= ClrTh)[0])

#inxSg = np.array(np.where(data.max_pxflux_s > ClrTh)[0])
#inxSs = np.array(np.where(data.max_pxflux_s <= ClrTh)[0])



#Plotting Northern Hemisphere
def pf1():
    plt.subplot(211)
    plt.plot(normflux_n_IDL[ind1[1][mask1]], normflux_n_PY[ind2[1][mask2]], 'b.')
    #plt.axis([1996, 2011, 0, 1.5e22])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('North Pole (above $65^\circ$)')

#Plotting Southern Hemisphere
def pf2():
    plt.subplot(212)
    plt.plot(normflux_s_IDL[ind1[1][mask1]], normflux_s_PY[ind2[1][mask2]], 'r.')
    #plt.axis([1996, 2011, 0, 1.5e22])
    plt.xlabel('Year')
    plt.ylabel('Total Signed Flux (Mx)')
    plt.title('South Pole (below $65^\circ$)')


plt.subplots_adjust(hspace = .40)
pf1()
pf2()

plt.show()
