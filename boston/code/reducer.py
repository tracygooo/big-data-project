#!/usr/bin/env python

import sys
import numpy as np
from numpy.linalg import inv

row = 400
#attri = 14
attri = 13
s = ( attri , attri )

X = np.zeros( s )
Y = np.zeros( attri )

mat = "" 

#'''
# Process each key-value pair from the mapper
for line in sys.stdin:

    # Get the key and value from the current line
    if '[[' in line:

        if ']' in line:
            line = line.replace( ']' , '];' )
        
        key , mat = line.split('\t')
        key = int( key )

    elif ']]' not in line:

        if ']' in line:
            # Add ';' after ']' to make np.matrix convert string type 'mat' to 2-D array 'mat'
            line = line.replace( ']' , '];' )
        mat += line

    else: # this line contains ']]'
        mat += line
        #print 'mat = {}'.format( mat )
        mat = np.matrix( mat )
        if ( key == 1 ) :
            X += mat
        else:
            #print 'key = {}'.format( key )
            #print 'mat = {}'.format( mat )
            
            # Convert 2-D array to 1-D
            mat = np.ravel( mat )
            Y += mat
        mat = "" 

beta = np.matmul( inv( X ) , Y )
print( 'Fitted weights  = {}'.format( beta ) )
#print ( 'Y = {}'.format( Y ) )
#print ( 'Y.shape = {}'.format( Y.shape ) )
#print ( 'inv( X ).shape = {}'.format( inv( X ).shape ) )
