#!/usr/bin/env python

import sys
import numpy as np
from numpy.linalg import inv

# number of attributes (columns) in training data
attri = 13
s = ( attri , attri )

x = np.zeros( s )
y = np.zeros( attri )

#'''
# Process each key-value pair from the mapper
for line in sys.stdin:
#f = open( 'moutput.txt' , 'r' )
#for line in f:

    # dim: index of entry; entry: value of entry
    dim , entry  = line.split('\t')

    # change data type of entry into float
    entry = float( entry )

    # sum all the entries with same indexes
    if ',' in dim:
        row , col = dim.split(',')
        row = int( row )
        col = int( col )
        x[ row , col ] += entry
    else:
        dim = int( dim )
        y[ dim ] += entry

# Compute weights of linear regression
w = np.matmul( inv( x ) , y )

for i in xrange( w.shape[ 0 ] ):

    # Two ways to print weights split by tab
    # No newline at the end of every line
    sys.stdout.write( '{}\t'.format( w[i] ) )
