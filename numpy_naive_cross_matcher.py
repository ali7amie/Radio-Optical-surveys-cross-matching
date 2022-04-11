import numpy as np
import angular_distance
import time

 
# naive cross matcher - compute distance between each src in catalog A and all sources in catalog B - matching is based on a given aperture[degree]

def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  max_radius = np.radians(max_radius)
  
  matches = []
  no_matches = []

  # Convert coordinates to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  ra2s = cat2[:,0]
  dec2s = cat2[:,1]

  for id1, (ra1, dec1) in enumerate(cat1):
    dists = angular_distance.angular_dist_rad(ra1, dec1, ra2s, dec2s)
    min_id = np.argmin(dists)
    min_dist = dists[min_id]
    if min_dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id, np.degrees(min_dist)))
    
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken








