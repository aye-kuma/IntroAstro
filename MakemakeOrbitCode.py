import numpy as np
import matplotlib.pyplot as plt

def AreaT(a,b,theta1, theta2):
    area = 0.5 * a * b * np.sin((theta2- theta1) * np.pi/180)
    return area
    
# Was comparing the two to see if I needed to know side C in order to get the area 

def AreaTri(a,b,theta1, theta2):
    c = np.sqrt(a**2 + b**2 - 2*a*b*np.cos((theta2 - theta1) * np.pi/180))
    s = 0.5 * (a + b + c)
    area = np.sqrt(s* (s-a) * (s-b) * (s-c))
    return area

A1 = 45.4059866936633
A2 = 41.0339992084371

B1 = 38.2108754299483
B2 = 40.0084524609087

C1 = 40.0372279443707
C2 = 38.4302797996442

D1 = 51.7185730369357
D2 = 52.6509625044766

thetaA1 = 260.5437
thetaA2 = 302.4433

thetaB1 = 0.0256
thetaB2 = 47.6182

thetaC1 = 311.4853
thetaC2 = 343.0647

thetaD1 = 151.3121
thetaD2 = 170.9338

print(AreaT(A1,A2,thetaA1,thetaA2))
print(AreaTri(A1,A2,thetaA1,thetaA2))

print(AreaT(C1, C2, thetaC1, thetaC2))
print(AreaTri(C1, C2, thetaC1, thetaC2))

print(AreaT(B1, B2, thetaB1, thetaB2))
print(AreaTri(B1, B2, thetaB1, thetaB2))

print(AreaT(D1, D2, thetaD1, thetaD2))
print(AreaTri(D1, D2, thetaD1, thetaD2))


"""pathMakemake = "/Users/theo/Downloads/MakemakeVector.txt"
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
plt.show()"""
