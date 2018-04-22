#!/usr/bin/env python

#---------------------------------------------------------
#Using weights obtained from training data, compute predicted response
#Output target and predicted response as input of reducer
#---------------------------------------------------------


import numpy as np
import sys

# number of attributes
attri = 6 

# Read weights to array 'w'
f_weight = open( 'weights.txt' , 'r' )
w = np.loadtxt( f_weight )

target_sum = 0
predict_sum = 0
count = 0

# Open test data file
#f_test = open( '../input/boston.tes' , 'r' )

#for line in f_test:
for line in sys.stdin:
    
    # Counting number of testing instances
    count += 1

    # Split line into a list
    ls = line.split()
    la = np.asarray( ls , dtype = np.float32 )

    # Attributes
    x = la[ 0:attri:1 ]

    # Target
    y_t = la[ attri ]
    target_sum += y_t

    # Predicted response
    y_p = np.matmul( w.T , x )
    predict_sum += y_p

    # Print target and prediction for reducer
    print( '{}\t{}'.format( y_t , y_p ) )
#f_test.close()

target_ave = target_sum / count
predict_ave = predict_sum / count
#print( '{}\t{},{}'.format( '00ave' , target_ave , predict_ave ) )

#path = '/home/hduser/big-data-project/boston/code/'
#of = open( path + 'test_ave.txt' , 'w' )
of = open( 'test_ave.txt' , 'w' )
of.write( '# Average of testing data: Target and Prediction\n' )
of.write( '{}\t{}'.format( target_ave , predict_ave ) )
of.close()
