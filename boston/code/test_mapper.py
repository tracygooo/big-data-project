#!/usr/bin/env python

#---------------------------------------------------------
#Using weights obtained from training data, compute predicted response
#Output target and predicted response as input of reducer
#---------------------------------------------------------


import numpy as np
import sys

# number of attributes
attri = 13

# Read weights to array 'w'
#f_weight = open( '/user/hduser/boston/input/weights.txt' , 'r' )
f_weight = open( 'weights.txt' , 'r' )
w = np.loadtxt( f_weight )
# w = np.array([-0.0940579058469, 0.128322469148, -0.00578034364991, 0.101799511318, -0.230212306852, 0.244139399789,  0.0182279904518, -0.342488378616, 0.278580425242,  -0.245897085046, -0.229638684728, 0.0715963743274, -0.394478860359])


# Open test data file
# f_test = open( '../input/boston.tes' , 'r' )

#for line in f_test:
for line in sys.stdin:

    # Split line into a list
    ls = line.split()
    la = np.asarray( ls , dtype = np.float32 )

    # First 13 elements
    x = la[ 0:attri:1 ]

    # Target
    y_t = la[ attri ]

    # Predicted response
    y_p = np.matmul( w.T , x )

    # Print target and prediction for reducer
    print( '{}\t{}'.format( y_t , y_p ) )
