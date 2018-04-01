#!/usr/bin/env python

import sys
import numpy as np
from numpy.linalg import inv

row = 400
attri = 13
s = ( attri , attri )

x = np.zeros( s )
y = np.zeros( attri )

mat = "" 

#'''
# Process each key-value pair from the mapper
for line in sys.stdin:
#f = open( 'moutput.txt' , 'r' )
#for line in f:

    dim , entry  = line.split('\t')
    entry = float( entry )
    if ',' in dim:
        row , col = dim.split(',')
        row = int( row )
        col = int( col )
        x[ row , col ] += entry
    else:
        dim = int( dim )
        y[ dim ] += entry

#print( 'x = {}'.format( x ) )
#print( 'y = {}'.format( y ) )

beta = np.matmul( inv( x ) , y )
print( 'Fitted weights  = {}'.format( beta ) )
