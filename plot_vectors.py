"""
Demo of bar plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt
import loadData as ld
import Recommendations as rec

def dispVectors(movie,num=5):
    ld.loadMovies()
    ld.loadRatings()
    recom=rec.topMatches(ld.RatingsDB,movie,n=200)
    #theta = np.linspace(0.0, np.pi/2, N)
    theta = {}
    radii = np.random.rand(num)

    for i in range(0,num):
    	theta[i] = np.arccos(recom[int(radii[i]*100)][0])
	radii[i] = 10
	print ( theta[i] )

    ax = plt.subplot(111, polar=True)
    bars = ax.bar(theta, radii, bottom=0.0)

    # Use custom colors and opacity
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.3)
        bar.set_width(0.2)

    plt.show()
