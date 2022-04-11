import numpy as np
import angular_distance


 
# naive cross matcher - compute distance between each src in catalog A and all sources in catalog B - matching is based on a given aperture[degree]

def crossmatch(cat1, cat2, aperture):
    matches = []
    no_matches = []
    for index1, ra1, dec1 in cat1:
        closest_dist = np.inf
        closest_index2 = None
        for index2, ra2, dec2 in cat2:
            dist = angular_distance.angular_dist(ra1, dec1, ra2, dec2)
            if dist < closest_dist:
                closest_index2 = index2
                closest_dist = dist
        
        # Ignore match if it's outside the maximum radius
        if closest_dist > aperture:
            no_matches.append(index1)
        else:
            matches.append((index1, closest_index2, closest_dist))

    return matches, no_matches









