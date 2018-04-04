#!/usr/bin/env python

'''
Compute 
    mean square error (MSE)
    mean average error (MAE)
    q^2
    Q^2

    For a good model, q^2 and Q^2 should be close to 0
    ...
'''

import numpy as np
import sys

# Read averages of target and predicted responses
f_ave = open( 'test_ave.txt' , 'r' )
ave = np.loadtxt( f_ave )
t_ave = ave[ 0 ]
p_ave = ave[ 1 ]
f_ave.close()

# Read standard deviation for descaling (MSE and MAE need)
f_des = open( 'descale.txt' , 'r' )
des_array = np.loadtxt( f_des )
des_std = des_array[ 1 ]
f_des.close()

#------------------ Accumulate following items---------------------------
# prediction - target
pt = 0

# square of ( prediction - target )
pt_2 = 0

# square of ( prediction - prediction_average )
p_pave_2 = 0

# square of ( target - target_average )
t_tave_2 = 0

# multiplication of ( prediction - prediction_ave) and ( target - target_ave)
ppa_tta = 0

# number of instances tested
count = 0

#------------------ Accumulate following items - end---------------------------

for line in sys.stdin:

    if( 'ave' in line):
        tmp , t_comma_p = line.split( '\t' )
        t_ave , p_ave = t_comma_p.split( ',' )
        continue

    count += 1

    # y_t-target, y_p-prediction
    y_t , y_p = line.split('\t')

    y_t = float( y_t )
    y_p = float( y_p )

    pt += abs( y_p - y_t )
    pt_2 += pow( y_p - y_t , 2 )
    p_pave_2 += pow( y_p - p_ave , 2 )
    t_tave_2 += pow( y_t - t_ave , 2 )
    ppa_tta += ( y_p - p_ave ) * ( y_t - t_ave )


# Mean average error
MAE = pt / count
MAE = MAE * des_std

# Mean square error
MSE = pow( pt_2 / count , 0.5 )
MSE = MSE * des_std

# Pearson Correlation Coefficient, r^2
r2 = pow( ppa_tta , 2 ) / ( p_pave_2 * t_tave_2 )

# R^2
R2 = 1.0 - pt_2 / t_tave_2

# q^2, Q^2
q2 = 1 - r2
Q2 = 1 - R2

print "MAE = {}\nMSE = {}\nq^2 = {}\nQ^2 = {}\n".format( MAE , MSE , q2 , Q2 )
