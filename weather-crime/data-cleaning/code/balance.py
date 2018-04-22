#!/usr/bin/python

'''
In dmak.csv, data is unblanced for the attribute 'Arrest'
when executing df['Arrest'].value_counts(), the result is shown below,
    2:  215044 
    1:  51591
This script will down-sample the majority class '2' (Not arrested)
'''

import pandas as pd
import numpy as np
from sklearn.utils import resample

# Read dmak.csv to data frame
df = pd.read_csv( '../data/cleaned/dmak.csv' , sep = '\t' )

# Seperate majority and minority classes
df_maj = df[ df.Arrest == 2 ]
df_min = df[ df.Arrest == 1 ]

# Downsample majority class
df_maj_down = resample(df_maj,
                       replace=False,    #sample without replacement
                       n_samples=51591,  #to match minority class
                       random_state=123) #reproducible results

# Convert downsampled majority class from numpy array to dataframe
df_maj_down = pd.DataFrame( data = df_maj_down )
df_maj_down.columns = [ 'Temp' , 'Prcp' , 'Snow' , 'Community Area' , 'FBI Code' , 'Domestic', 'Arrest' , 'ID' ]

# Combine minority class with downsampled majority class
df_down = pd.concat( [ df_maj_down , df_min ] )

# Change data types of below three columns from float to int
df_down['Arrest'] = df_down['Arrest'].astype(int)
df_down['Community Area'] = df_down['Community Area'].astype(int)
df_down['FBI Code'] = df_down['FBI Code'].astype(int)

# Shuffle the majority and minority classes
df_down = df_down.sample( frac = 1 , replace = True )

# Drop messy column 'ID'
df_down.drop( 'ID' , axis = 1 , inplace = True )

# Add a new ID column to match format of dMak software
row = df_down.shape[ 0 ]
df_down[ 'ID' ] = np.arange( 1 , row + 1 , 1 , dtype = int )

# Output changed data frame in dmak.csv
df_down.to_csv( '../data/cleaned/dmak_balanced.csv', sep = '\t' , header = False , index = False )
