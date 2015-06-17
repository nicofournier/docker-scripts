#!/usr/bin/env python

print('start')
import matplotlib
print('before Agg')
matplotlib.use('Agg')
from obspy.core import read
print('before importing')
st = read('http://examples.obspy.org/RJOB_061005_072159.ehz.new')
print('before plotting')
st.plot(outfile='/scripts/00-plot.png')
print('after plotting')
