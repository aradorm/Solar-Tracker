import numpy as np
import ephem

location=ephem.Observer() #observer - heliostat location
location.lon = '34:47:38.95'
location.lat = '31:15:32'
location.elevation = 260
sun=ephem.Sun(location)

ColAlt = 0
ColAz = 0.5*np.pi

S = np.array([np.sin(sun.alt),np.cos(sun.alt)*np.sin(sun.az),np.cos(sun.alt)*np.cos(sun.az)])
C = np.array([np.sin(ColAlt),np.cos(ColAlt)*np.sin(ColAz),np.cos(ColAlt)*np.cos(ColAz)])
M=((S+C)*(2+2*np.dot(2*S,C)))**-0.5

HAlt=np.arcsin(M[1])
HAz=np.arcsin(M[2]/np.cos(HAlt))
print(M)