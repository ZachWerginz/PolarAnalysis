import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

#Plot Northern Hemisphere
def pf1(c):
    plt.subplot(211)
    plt.plot(Date, pfNorth, color = c, marker = '.', linestyle = 'None')
    plt.xlabel('Year')
    plt.ylabel('Polar Field (G)')
    plt.title('North Pole (above $65^\circ$)')

#Plot Southern Hemisphere
def pf2(c):
    plt.subplot(212)
    plt.plot(Date, pfSouth, color = c, marker = '.', linestyle = 'None')
    plt.xlabel('Year')
    plt.ylabel('Polar Field (G)')
    plt.title('South Pole (below $65^\circ$)')

#Date initialization
def date_init():
    Year = np.array(data.Year)
    Month = np.array(data.Month)
    Day = np.array(data.Day)
    date = []
    for i in range( 0, len(Year) ):
        d = datetime.date(int(Year[i]), int(Month[i]), int(Day[i]) ).toordinal()
        date.append( Year[i] + (d - datetime.date(int(Year[i]), 1, 1).toordinal() )/(datetime.date(int(Year[i]) + 1, 1, 1).toordinal() - datetime.date(int(Year[i]), 1, 1).toordinal() ) )
    date = np.array(date)
    return date
    
data = pd.read_csv("WSO_Polar_Field_Nov-2015.csv")

pfNorth = np.array(data.NPF)
pfSouth = np.array(data.SPF)

Date = date_init()

pf1('blue');
pf2('red');
plt.subplots_adjust(hspace = .40)

plt.show()
