# -*- coding: utf-8 -*-
"""
author: Femke Nijsse

Shared under Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)

You are free to:
Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material
for any purpose, even commercially. 

Under the following terms:
Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original. 
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import matplotlib as mpl
mpl.rcParams['font.size'] = 15

language_version='German'
if language_version=='English':
    title = 'historical CO$_2$ level'
    ice_age = 'Ice age \n cycles'
    indust= 'Industrial revolution starts'
    co2con = 'CO$_2$ concentration (ppmv)'
    thyrago = 'Thousands of years ago'
    year = 'year (CE)'
    
if language_version=='Dutch':
    title = r'Historisch niveau CO$_2$'
    ice_age = 'IJstijd- \n cycli'
    indust= 'Begin industriële revolutie'
    co2con = 'CO$_2$ concentratie (ppmv)'
    thyrago = 'Duizenden jaar geleden'
    year = 'jaar (CE)'
    
    
if language_version=='German':
    #Not really German yet
    title = r'Historische CO$_2$-Konzentration'
    ice_age = 'Eiszeit- \n Zyklen'
    indust= 'Beginn der Industriellen Revolution'
    co2con = 'CO$_2$-Konzentration (ppmv)'
    thyrago = 'Tausende Jahre zuvor'
    year = 'Jahr (n.Chr.)'
    
    


"""
Import Vostok, Dome C and Taylor data 800 kyr 
"""


xls = pd.ExcelFile('CO2_800kyr.xls')
df1 = pd.read_excel(xls, 'CO2 611-800KYr')
df2 = pd.read_excel(xls, 'Vostok-TD-Dome C',skiprows=6)
df3 = pd.read_excel(xls, 'Composite CO2',skiprows=6)

df3.columns = ['yr', 'CO2']
df3['yr']= df3['yr']+1950 #convert to CE units
df_domeC = df3[df3.yr > 391896]

df_Vostok = df2.iloc[:,5:7]
df_Vostok.columns = ['yr', 'CO2']
df_Vostok['yr']=df_Vostok['yr']+1950

df_Taylor = df2.iloc[:,8:10]
df_Taylor.columns = ['yr', 'CO2']
df_Taylor['yr'] = df_Taylor['yr']+1950

df_domeC2 = df2.iloc[:183,1:3]
df_domeC2.columns = ['yr', 'CO2']
df_domeC2['yr'] = df_domeC['yr']+1950



"""
Import Law Dome ice core data sets
"""
skiprowsa = list(range(22))+list(range(54,467))
skiprowsb = list()
df_lawdome = pd.read_table('lawdome_combined.dat',skiprows=skiprowsa, \
                           names=('code','analysisdate', 'ice age', 'yr','CO2'))
df_lawdome_all = pd.read_table('lawdome_combined.dat',skiprows=273, \
                           names=('yr','CO2', 'smoothed', '-','_','.'))





"""
Import Mauna Loa data
"""

df_mlo = pd.read_csv('monthly_in_situ_co2_mlo.csv',skiprows=54)
df_mlo=df_mlo[['  Yr','CO2filled']]
df_mlo.columns = ['yr', 'CO2']
df_mlo = df_mlo[df_mlo.yr != '1958']
df_mlo = df_mlo[df_mlo.yr != '2018']
df_mlo = df_mlo.drop([0,1])

#Take yearly averages
yeararray = np.arange(1959,2018)
co2matrix = np.zeros((len(yeararray),2))
for n in yeararray:
    jan_yr_n = 12*(n-1959)
    dec_yr_n = 12*(n-1959)+12
    mon = df_mlo.iloc[jan_yr_n:dec_yr_n,1]
    meanmon = np.mean([float(item) for item in mon])        
    co2matrix[n-1959]=np.array([n,meanmon])
    


"""
Make the plot
"""

#Initialise
fig,ax = plt.subplots()

ax.set_title(title)


#Add data
ax.plot(co2matrix[:,0]/1000,co2matrix[:,1],'k',linewidth=1.5)
ax.plot(df_lawdome_all['yr']/1000,df_lawdome_all['CO2'],'C2',linewidth=2.0)
ax.plot(df_Taylor['yr']/1000,df_Taylor['CO2'],'C1',linewidth=1)
ax.plot(df_Vostok['yr']/1000,df_Vostok['CO2'],'C0',linewidth=1)
ax.plot(df_domeC['yr']/1000,df_domeC['CO2'], 'C9',linewidth=1)
ax.plot(df_domeC2['yr']/1000,df_domeC2['CO2'], 'C9',linewidth=1)


#Add box for inset
xy_elli_low = (0.935,0.45)
width_elli,height_elli = 0.04,0.54
xy_elli_high = (xy_elli_low[0],xy_elli_low[1]+height_elli)
xy_inset_low = (0.89,0.725)
xy_inset_high = (0.89,0.945)

ax.add_patch(
    patches.Ellipse(
        (xy_elli_low[0]+0.5*width_elli,xy_elli_low[1]+0.5*height_elli),   # (x,y)
        width_elli,          # width
        height_elli,          # height
        fill=False,
        alpha=0.8,
        transform=ax.transAxes,
        linewidth=0.8
    )
)

    
#Adding the lines connecting inset figure to oval
xy_elli_low_centre = (xy_elli_low[0]+0.5*width_elli,xy_elli_low[1]-0.02)
xy_elli_high_centre = (xy_elli_high[0]+0.5*width_elli,xy_elli_high[1])


ax.annotate("", xy=xy_elli_low_centre, xytext=xy_inset_low,
             arrowprops=dict(arrowstyle="-",alpha=0.9,linewidth=0.8),
             xycoords='axes fraction')
ax.annotate("", xy=xy_elli_high_centre, xytext=xy_inset_high,
             arrowprops=dict(arrowstyle="-",alpha=0.9,linewidth=0.8),
             xycoords='axes fraction')



#Mark-up

ax.set_xlabel(thyrago)
ax.set_ylabel(co2con)
ax.invert_xaxis()
ax.yaxis.tick_right()
ax.tick_params(axis='both', which='major', labelsize=14)
ax.yaxis.set_label_position("right")
ax.set_facecolor((0.94, 0.94, 0.94))


#Inset figure
axins = inset_axes(ax, 3.7,0.7, bbox_to_anchor=(360, 250))
axins.plot(df_lawdome_all['yr'], df_lawdome_all['CO2'],'C2', linewidth=2.2)
axins.plot(co2matrix[:,0], co2matrix[:,1], 'k', linewidth=2.2)


axins.set_xlabel(year, fontsize=13, labelpad=-0.2)
axins.tick_params(labelsize=13, direction='in')

# sub region of the original image
x1, x2, y1, y2 = 1000, 2025, 260, 420
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

# fix the number of ticks on the inset axes
axins.yaxis.get_major_locator().set_params(nbins=4)
axins.xaxis.get_major_locator().set_params(nbins=5)


ax.text(0.15,0.37,ice_age, size=12, ha="center", 
         transform=ax.transAxes)

axins.annotate(indust, xy=(1750, 295), xytext=(1200, 370),
            arrowprops=dict(facecolor='black', alpha=0.7, arrowstyle='->'),fontsize=12,
            )


plt.draw()

fig_name = 'CO2_{}.svg'.format(language_version)
plt.savefig(fig_name, bbox_inches='tight')



