import numpy as np
import matplotlib.pyplot as plt

pathMakemake = "/Users/theo/Downloads/MakemakeVector.txt"
dataMakemake = np.genfromtxt(pathMakemake, skip_header=50, skip_footer=48, delimiter=',', names=['JDTDB', 'Calendar Date', 'X','Y','Z'])

pathEarth = "/Users/theo/Downloads/EarthSolOrbit.txt"
dataEarth = np.genfromtxt(pathEarth, skip_header= 54, skip_footer= 48, delimiter=',', names=['JDTDB', 'Calendar Date', 'X', 'Y', 'Z'])

plt.plot(dataMakemake['X'],dataMakemake['Y'], color='red', label='Makemake' )
plt.plot(dataEarth['X'], dataEarth['Y'], color='blue', label='Earth')
plt.scatter(0,0,s=20,color='orange', label = 'Sun')
plt.title('Orbit of Makemake Comet')
plt.xlabel('AU')
plt.ylabel('AU')
plt.legend()
plt.grid()
plt.show()


