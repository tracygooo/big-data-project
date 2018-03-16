#!/usr/bin/env python

import sys
import numpy as np
from numpy.linalg import inv

row = 400
attri = 13
s = ( attri , attri )

X = np.zeros( s )
Y = np.zeros( attri )

#'''
# Process each key-value pair from the mapper
for line in sys.stdin:

    # Get the key and value from the current line
    key , value = line.split( '\t' )
    key = int( key )
    value = float( value )
    if( key < row ):
        X += value
    else:
        Y += value

print inv( X ) * Y 
#'''
