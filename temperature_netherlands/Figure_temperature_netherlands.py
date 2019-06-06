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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import heapq


data = pd.read_fwf('labrijn_ea.dat',skiprows=20)

'Figure 1: simple graph of yearly temperatures'

fig2,ax2 = plt.subplots()
data.rename(columns={'Unnamed: 0': 'yr'},inplace=True)
data.set_index('yr')
data['Year'] = data['Year']/10
ax2.plot(data['yr'],data['Year'],linewidth=0.8, label='jaargemiddelde')
ax2.set_xlabel('jaar')
ax2.set_ylabel(r'Temperatuur ($\degree$C)')
ax2.set_title('Gemiddelde jaartemperatuur De Bilt')

#compute the lowess smoothed average temperature
smoothed = sm.nonparametric.lowess(data['Year'], data['yr'],frac=(15/len(data)), it=1)
ax2.plot(data['yr'][1:-1],smoothed[:,1],color='red',linewidth=2.5,label='gewogen 15-jarig gemiddelde')
ax2.legend(fontsize=14,loc=0)
fig2.savefig('Jaargemiddelde_De_Bilt.svg', bbox_inches='tight')
fig2.savefig('Jaargemiddelde_De_Bilt.png', bbox_inches='tight',dpi=300)







'Figure 2; that artsy figure Ed Hawkins started'
fig, ax = plt.subplots()
minimum = heapq.nsmallest(5,data['Year'][1:-1])[-1]
maximum = heapq.nlargest(2,data['Year'][1:-1])[-1]

ax.imshow([data['Year']], aspect='auto',cmap='coolwarm',vmin=minimum,vmax=maximum)

ax.axis('off')
fig.tight_layout()
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
bbox = fig.bbox_inches.from_bounds(0.01, 1, 5.95, 2.0)
fig.savefig('MeanT_EdHawkinslike.png', bbox_inches=bbox,dpi=500)


fig, ax3 = plt.subplots()
ax3.imshow([data['Year'][-120:-1]], aspect='auto',cmap='coolwarm')
ax3.axis('off')
fig.savefig('MeanT_EdHawkinslike_last120yr.png', bbox_inches='tight',dpi=500)




