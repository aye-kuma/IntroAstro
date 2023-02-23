import numpy as np
import matplotlib.pyplot as plt

pathArtemisE = "/Users/theo/Downloads/ArtemisEarthOrbit.txt"
dataArtemisE = np.genfromtxt(pathArtemisE, skip_header=157, skip_footer=48, delimiter=',', names=['JDTDB', 'Calendar Date', 'X','Y','Z'])

pathMoon = "/Users/theo/Downloads/MoonOrbit.txt"
dataMoon = np.genfromtxt(pathMoon, skip_header=50 , skip_footer=48 , delimiter=',', names=['JDTDB','Calendar Date','X','Y','Z'])

plt.scatter(0,0,s=30,color='blue')
plt.scatter(dataMoon['X'],dataMoon['Y'],color='grey',s=2)
plt.scatter(dataArtemisE['X'],dataArtemisE['Y'],s=2,color='red')
plt.grid()
plt.show()

