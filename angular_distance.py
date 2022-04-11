
import numpy as np

# compute the angular distance between two compared sources
def angular_dist(ra1,dec1,ra2,dec2):

  # convert degrees to radians
  r1=np.radians(ra1)
  r2=np.radians(ra2)
  d1=np.radians(dec1)
  d2=np.radians(dec2)

  # compute the angular distance  
  a=(np.sin(np.abs(d1-d2)/2))**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b))

  # convert back to degrees
  return np.degrees(d)


def angular_distance_rad(r1, d1, r2, d2):
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return 2*np.arcsin(np.sqrt(a + b))