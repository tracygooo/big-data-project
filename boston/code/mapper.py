#!/usr/bin/env python

import sys
import numpy as np

for line in sys.stdin:
    # Split line into a list
    ls = line.split()
    la = np.asarray( ls , dtype = np.float32 )

    # First 13 elements
    xi = la[ 0:13:1 ]

    # 14th element
    yi = la[ 13 ]

    # Convert X[i] and Y_real[i] into 2-D array in order to apply transpose
    xi = np.array( [xi] )

    # transpose of Xi
    xi_T = xi.T

    XTX = np.matmul( xi_T , xi )
    XTY =   xi_T * yi

    print '1\t{}'.format( XTX )
    print '2\t{}'.format( XTY )
