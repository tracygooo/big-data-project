#!/usr/bin/env python

'''
Direct linear regression for boston data (No split for mapper and reducer)

Used to check results of hadoop streaming
'''

import numpy as np
from sklearn import preprocessing
from numpy.linalg import inv

# Read data to matrix 'mat' from 'boston.pat' 
f = open( 'input/boston.pat' , 'r' )
mat = np.loadtxt( f )
row = mat.shape[ 0 ]

# X: first 13 columns 
X_org = mat[ : , :13 ]
X_scaled = preprocessing.scale( X_org )
#xscaler = preprocessing.StandardScaler().fit( X_org )

# Add last column with ones for bias (omega_0)
X0 = np.ones( row )
X0 = np.array( [ X0 ] )
X = np.concatenate( ( X_scaled , X0.T ) , axis = 1 )

# Y_real: 14th column (15th (last) column is ID)
Y_real = mat[ : , 13 ]
Y_real_scaled = preprocessing.scale( Y_real )

# Convert Y-real to 2-D array
Y_real = np.array( [ Y_real_scaled ] )

XTX = np.matmul( X.T , X )
XTY =  np.matmul(  X.T , Y_real.T )

omega = np.matmul( inv( XTX ) , XTY )
print( 'omega = {}'.format( omega ) )
