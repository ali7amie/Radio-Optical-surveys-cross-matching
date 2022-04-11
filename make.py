import import_catalogs
import loop_naive_cross_matcher
import numpy_naive_cross_matcher


aperture=40/3600
Radio_catalog = import_catalogs.import_bss()
Optical_catalog = import_catalogs.import_super()

loop_naive_matches, loop_naive_no_matches = loop_naive_cross_matcher.crossmatch(Radio_catalog, Optical_catalog, aperture)

numpy_naive_matches, numpy_naive_no_matches, time2 = numpy_naive_cross_matcher.crossmatch(Radio_catalog, Optical_catalog, aperture)
