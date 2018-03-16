#!/usr/bin/env python

import numpy as np

# Read data to matrix 'mat' from 'boston.pat' 
count = 0
f = open( 'boston.pat' , 'r' )
mat = np.loadtxt( f )
row = mat.shape[ 0 ]

# X: first 13 columns 
X = mat[ : , :13 ]

# Y_real: 14th column (15th (last) column is ID)
Y_real = mat[ : , 13 ]

#for i in xrange( 0 , row ):
for i in xrange( 0 , 2 ):

    # Convert X[i] and Y_real[i] into 2-D array in order to apply transpose
    Xi = np.array( [ X[ i ] ] )
    #Yi = np.array( [ Y_real[ i ] ] )

    # transpose of Xi
    Xi_T = Xi.T

    print 'Group #{0}\n{1}\n'.format( i , Xi_T * Xi )
    print 'Group #{0}\n{1}\n'.format( row + i , Xi_T * Y_real[i] )
