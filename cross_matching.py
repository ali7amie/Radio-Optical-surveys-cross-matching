import numpy as np

# convert right ascension from Hour,Minute,Second to decimal degree
def hms2dec(hour,minute,second):

  return 15 * ( hour + minute/60 + second/3600)

# convert declination from Degree,Minute,Second to decimal degrees
def dms2dec(degree, minute, second):
  if degree < 0:
    sign = -1
  else:
    sign = 1

  return sign*(abs(degree) + minute/60 + second/3600)

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
 
# import the AT20G BSS catalog, create the structure (src_index, ra[deg], dec[deg])
def import_bss():
  bss_data = np.loadtxt('bss.dat', usecols=range(1, 7))
  result=[]
  for i in range(0,len(bss_data)):
    ra_deg=hms2dec(bss_data[i][0],bss_data[i][1],bss_data[i][2])
    dec_deg=dms2dec(bss_data[i][3],bss_data[i][4],bss_data[i][5])
    result.append((i+1,ra_deg,dec_deg))

  return np.array(result)

# import the SuperCOSMOS catalog, create the structure (src_index, ra[deg], dec[deg])
def import_super():
  super_data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  result=[]
  for i in range(0,len(super_data)):
    result.append((i+1,super_data[i][0],super_data[i][1]))

  return np.array(result)

# naive cross correlator - 1 vs all catalog
# cross-matching each sources in the two catalogs, matched sources have a separation distance < aperture
def crossmatch(cat1, cat2, aperture):
    matches = []
    no_matches = []
    for index1, ra1, dec1 in cat1:
        closest_dist = np.inf
        closest_index2 = None
        for index2, ra2, dec2 in cat2:
            dist = angular_dist(ra1, dec1, ra2, dec2)
            if dist < closest_dist:
                closest_index2 = index2
                closest_dist = dist
        
        # Ignore match if it's outside the maximum radius
        if closest_dist > aperture:
            no_matches.append(index1)
        else:
            matches.append((index1, closest_index2, closest_dist))

    return matches, no_matches