import scipy.constants as const
import numpy as np
from astropy.coordinates import SkyCoord, EarthLocation
import math
import matplotlib.pyplot as plt
import astropy.units as u



obs = EarthLocation(lat=53*u.deg+28*u.arcmin+49*u.arcsec,
                    lon=10*u.deg+14*u.arcmin+23*u.arcsec)
phi = obs.lat
N = np.arange(365)
omega = 2*math.pi/365.24
ecl = math.radians(23.44)
delta = -np.arcsin(math.sin(ecl) * np.cos(omega * (N+10)))
h = np.arccos(-np.tan(delta) * math.tan(phi.radian))
T = (np.degrees(2*h)/360) * u.sday.to(u.h)


# betelgeuse = SkyCoord.from_name('Betelgeuse')

# print(betelgeuse)
# print(const.G)