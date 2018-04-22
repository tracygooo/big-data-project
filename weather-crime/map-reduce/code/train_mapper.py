#!/usr/bin/env python

import sys
import numpy as np

# number of attributes
attri = 6 

for line in sys.stdin:
    # Split line into a list
    ls = line.split()
    la = np.asarray( ls , dtype = np.float32 )

    # First 13 elements
    x = la[ 0:attri:1 ]

    # 14th element
    y = la[ attri ]

    for i in xrange( attri ):
        print( '{}\t{}'.format( i , x[i] * y ) )
        for j in xrange( attri ):
            print( '{},{}\t{}'.format( i , j , x[i] * x[j] ) )
