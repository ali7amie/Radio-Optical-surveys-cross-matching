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







