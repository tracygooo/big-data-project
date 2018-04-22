#!/usr/bin/env python

#--------------------------------------------------------------
# Descale weights obtained by training part based on stats.txt
#-------------------------------------------------------------

import numpy as np

# number of attributes
attri = 13 

# Read weights to wt
f_weight = open( '../output/weights.txt' , 'r' )
wt = np.loadtxt( f_weight )
f_weight.close()

# Read mean and standard deviation to f_stats
# stats.txt: 
    # 1st col: ID 
    # 2nd col: Mean
    # 3rd col: Standard deviation
    # First 13 lines: x
    # 14th line: response y
f_stats = open( '../input/stats.txt')
stat = np.loadtxt( f_stats )
f_stats.close()

x_mean = stat[ 0:attri , 1 ]
x_std = stat[ 0:attri , 2 ]
y_mean = stat[ attri , 1 ]
y_std = stat[ attri , 2 ]

# Descaled weights
wt_des = np.zeros( wt.shape[0] + 1 )
# Constant term, the last element of 'wt_des'
wt_des_cnt = 0
for i in np.arange( x_mean.shape[0] ) :
    wt_des[ i ] = wt[ i ] * y_std / x_std[ i ]
    wt_des_cnt += -y_std * wt[ i ] * x_mean[ i ] / x_std[ i ]

wt_des_cnt += y_mean
wt_des[ wt_des.shape[0] - 1 ] = wt_des_cnt

f_wt_des = open( '../output/weights_descaled.txt' , 'w' )
#f_wt_des.write( wt_des )
np.savetxt( f_wt_des , wt_des , delimiter = '\t' )
f_wt_des.close()

print 'Scaled weights are\n {}'.format( wt )
print 'Descaled weights are\n {}'.format( wt_des )
