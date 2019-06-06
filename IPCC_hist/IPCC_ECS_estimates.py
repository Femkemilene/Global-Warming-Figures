# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:46:41 2019

@author: fn235
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import AutoMinorLocator

font = {'size'   : 15}                  
matplotlib.rc('font', **font)                                      # Sets font size

ipcc_reports =    [['FAR', np.nan, 1.5, 2.5,    4.5, np.nan,  'informal'],
                   ['SAR', np.nan, 1.5, np.nan, 4.5, np.nan, 'informal'],
                   ['TAR', np.nan, 1.5, np.nan, 4.5, np.nan, 'informal'],
                   ['AR4', 1.5,    2.0, 3.0,    4.5, np.nan, 'formal'],
                   ['AR5', 1.0,    1.5, np.nan, 4.5, 6.0,    'formal']]

mod_name, minmin, minecs, bestecs, maxecs, maxmax, markup = zip(*ipcc_reports)

lw = 10
fig, ax = plt.subplots()                                          # Initialise graph
mod_range = range(len(ipcc_reports))
mark_up_dict = {'informal_dashed': 
                    {'linestyles': (0, [1.8, 0.7, 1.8, 0.7]), 'colors': 'C0', 'linewidth': lw, 'alpha': 0.65}, 
                'informal':
                    {'linestyles': 'solid', 'colors': 'C0', 'linewidth': lw, 'alpha': 0.55}, 
                'formal':
                    {'linestyles': 'solid', 'colors': 'C0', 'linewidth': lw, 'alpha': 1.0},
                'extremes':
                    {'alpha': 0.287, 'linewidth': lw},
                'informal_extremes': 
                    {'alpha': 0.2, 'linewidth': lw}}


for n in mod_range:
    ax.vlines(n+0.5, minmin[n], minecs[n], **mark_up_dict['extremes'])     # The mininum values
    ax.vlines(n+0.5, maxecs[n], maxmax[n], **mark_up_dict['extremes'])     # The maximum values
    ax.vlines(n+0.5, minecs[n], maxecs[n], **mark_up_dict[markup[n]])      # The likely range
    if np.isnan(maxmax[n]):
        ax.annotate("", xy=(0.49 + n, 6.6), xytext=(0.49 + n, maxecs[n]-0.05), alpha=0.3,
                     arrowprops=dict(arrowstyle="->", alpha=0.3))
        ax.annotate("?", xy=(0.53 + n, 4.75), xytext=(0.53 + n, 4.75), alpha=0.4)
    if np.isnan(minmin[n]):
        ax.annotate("", xy=(0.49 + n, 0.6), xytext=(0.49 + n, minecs[n]), alpha=0.3,
                     arrowprops=dict(arrowstyle="->", alpha=0.3))
        ax.annotate("?", xy=(0.53 + n, 1.1), xytext=(0.53 + n, 1), alpha=0.4)
ax.set_xticks((np.arange(6)))
ax.set_xticklabels(mod_name)

deg = r'${}^{\circ}$C'
deg_list = ['0.0'+deg, '1.5' + deg, '3.0'+deg, '4.5'+deg, '6.0'+deg]

ax.set_yticks(np.arange(0, 6.5, 1.5))
ax.set_yticklabels(deg_list, fontsize=14)

ax.set_title('Equilibrium climate sensitivity', pad=10, alpha=0.9)

ax.yaxis.grid()
plt.minorticks_on()
minor_locator = AutoMinorLocator(3)
ax.yaxis.set_minor_locator(minor_locator)
ax.grid(axis='y', which='minor', color='gray', alpha=0.1)


# Create offset transform by 5 points in x direction
dx = 36/72.; dy = 0/72. 
offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

# apply offset transform to all x ticklabels.
for label in ax.xaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)



ax.tick_params(axis='both', labelcolor='black')
ax.tick_params(axis='y', which='both', left=False)
ax.tick_params(axis='x', which='minor', bottom=False)


ax.spines["bottom"].set_color('gray')
ax.spines["left"].set_color('gray')
ax.spines["left"].set_visible(False)
#ax.spines["bottom"].set_visible(False)
ax.spines["top"].set_visible(False)    
ax.spines["right"].set_visible(False)    

plt.ylim(0, 6.0 + 0.9)        
plt.xlim(-0.2, 5.2)

plt.savefig('ECS_assessments_IPCC.svg', bbox_inches = 'tight' )

