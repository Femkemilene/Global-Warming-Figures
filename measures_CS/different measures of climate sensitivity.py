# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:05:56 2019

@author: fn235
"""

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

sns.palplot(sns.color_palette("GnBu"))
sns.palplot(sns.color_palette("BuGn"))
cp = sns.color_palette("YlGn", 11)
cp = sns.color_palette("BuGn", 11)

fig = plt.figure()
ax = fig.add_subplot(111)

language = 'en'
if language == 'en':
    TCR = 'Transient climate response'
    ECS = 'Equilibrium \n climate sensitivity'
    eECS = 'Effective \n climate sensitivity'
    ESS = 'Earth system sensitivity'
    


# ==================================================================
# Putting the rectangles in place 
# ==================================================================
rect1 = matplotlib.patches.Rectangle((-200, 150), 410, 100, color=cp[3])
rect2a = matplotlib.patches.Rectangle((-200,-100), 205, 150, color=cp[5])
rect2b = matplotlib.patches.Rectangle((0,-100), 205, 150, color=cp[4])
rect3 = matplotlib.patches.Rectangle((-200,-300), 410, 100, color=cp[6])
backg = matplotlib.patches.Rectangle((-200,-300), 410, 800, color=cp[1])
#ax.add_patch(backg)
ax.add_patch(rect1)
ax.add_patch(rect2a)
ax.add_patch(rect2b)
ax.add_patch(rect3)
plt.xlim([-200, 200])
plt.ylim([-300, 250])


# =======================================================================
# Drawing my Arrows
# =======================================================================
ax.arrow(-100, 150, 0, -40, width=30, head_width=50, head_length=60, color=cp[3])
ax.arrow(-100, -100, 0, -40, width=30, head_width=50, head_length=60, color=cp[5])



# ==================================================================
# Putting black lines in place accross boxes
# ==================================================================
mpl.rcParams['lines.linewidth'] = 1

ax.hlines(-300, -200, 200)  # Bottom box
ax.hlines(-200, -200, 200)
ax.vlines(-200, -300, -200)
ax.vlines(200, -300, -200)


ax.hlines(-100, -200, -115) # Middle box
ax.hlines(-100, -85, 200)
ax.hlines(  50, -200, 200)
ax.vlines(-200, -100, 50)
ax.vlines(0, -100, 50)
ax.vlines(200, -100, 50)


ax.hlines(150, -200, -115)  #Top box
ax.hlines(150, -85, 200)  
ax.hlines(250, -200, 200)  
ax.vlines(-200, 150, 250)
ax.vlines(200, 150, 250)







# =======================================================================
# Putting the text in place
# =======================================================================
fontdictmain = {'fontsize': '14', 'color':'black'}  #'fontweight': 'bold'
fontdictsmall = {'fontsize': '11'}
ax.text(-60, -175, 'Millennia: very slow vegetation \n and ice sheet changes',  fontdict=fontdictsmall)
ax.text(-60, 100, 'Centuries: ocean also heats up', fontdict=fontdictsmall)
ax.text(-190, 20, 'Climate sensitivity may rise')
ax.text(15, 20, 'Climate sensitivity constant')
ax.text(-120, 190, TCR, fontdict=fontdictmain)
ax.text(-190, -70, ECS, fontdict=fontdictmain)
ax.text(15, -70, eECS, fontdict=fontdictmain)
ax.text(-120, -260, ESS, fontdict=fontdictmain)


# ===========================================================================
# Turning off sides
# ===========================================================================
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["top"].set_visible(False)    
ax.spines["right"].set_visible(False)   

# 


plt.tick_params(
    axis='both',       # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    left=False,         # ticks along the top edge are off
    labelbottom=False, # labels along the bottom edge are off
    labelleft = False)
plt.show()

fig.savefig('schematic_climate_sensitivity.svg', bbox_inches='tight')
fig.savefig('schematic_climate_sensitivity.png', dpi=300)

plt.show()
