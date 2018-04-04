#!/usr/bin/env python

'''
Compute 
    mean square error (MSE)
    mean average error (MAE)
    q^2
    Q^2
    ...
'''

import numpy as np
import sys

#target_sum = 0
#predict_sum = 0
diff = 0
diff_square = 0
count = 0

for line in sys.stdin:

    count += 1

    # y_t-target, y_p-prediction
    y_t , y_p = line.split('\t')
    y_t = float( y_t )
    y_p = float( y_p )

    #target_sum += y_t
    #predict_sum += y_p
    diff += abs( y_p - y_t )
    diff_square += pow( y_p - y_t , 2 )

#count = float( count )

# Mean average error
MAE = diff / count

# Mean square error
MSE = pow( diff_square / count , 0.5 )
print "MAE = {}\tMSE = {}".format( MAE , MSE )
