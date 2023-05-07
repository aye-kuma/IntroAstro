import numpy as np
import matplotlib.pyplot as plt 

pathStars = "/Users/theo/Downloads/PulsarStars.csv"
dataStars = np.genfromtxt(pathStars, delimiter=',',  names=['period','period_dot','class'])

pathAXR = "/Users/theo/Downloads/AXRPulsar.csv"
dataAXR = np.genfromtxt(pathAXR, delimiter=',',  names=['period','period_dot','class'])

pathRadio = "/Users/theo/Downloads/RadioPulsars.csv"
dataRadio = np.genfromtxt(pathRadio, delimiter=',',  names=['period','period_dot','class'])

pathXRPulsar = "/Users/theo/Downloads/XRPulsars.csv"
dataXRPulsar = np.genfromtxt(pathXRPulsar, delimiter=',',  names=['period','period_dot','class'])

plt.scatter(np.log10(dataStars['period']),np.log10(dataStars['period_dot']), label='Neutron Star', marker="o")
plt.scatter(np.log10(dataAXR['period']),np.log10(dataAXR['period_dot']), label='Anomalous X-Ray', marker="^")
plt.scatter(np.log10(dataRadio['period']),np.log10(dataRadio['period_dot']), label='Radio Pulsar', marker="s")
plt.scatter(np.log10(dataXRPulsar['period']),np.log10(dataXRPulsar['period_dot']), label='X-Ray Pulsar', marker="d")
plt.xlabel('Barycentric Period of Pulsar (s) ')
plt.ylabel('d/dt of barycentric period (dimensionless)')
#plt.rcParams['figure.dpi'] = 300
plt.grid()
plt.legend()
plt.show()
