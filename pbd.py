"""
Demo of bar plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt


N = 3
theta = (arccos(0),arccos(10),arccos(20))
radii = 10 * np.random.rand(N)
# width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, polar=True)
bars = ax.bar(theta, radii, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip9(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

plt.show()
