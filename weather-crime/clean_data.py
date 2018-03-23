#!/usr/bin/env python

'''
Drop useless features, selected interested features
    For weather data, four features ('DATE' , 'TEMP' , 'PRCP' , 'SNOW') are selected 
    For crime data, five features ('Date' , 'Community Area' , 'FBI Code' , 'Domestic', 'Arrest') are kept

Merge cleaned weather and crime data on feature 'Date'
'''

import pandas as pd


#----------------------Clean weather data--------------------------------------#

# Read weather data 
weather_df = pd.read_csv( "data/weather.csv" , sep = "," , parse_dates = ['DATE'] )

# Add Column 'TEMP', median value of TMAX and TMIN
weather_df[ 'TEMP' ] = ( weather_df[ 'TMAX' ] + weather_df[ 'TMIN' ]) / 2.0 

# Select attributes: DATE, TEMP, PRCP, SNOW
weather_df = weather_df[ [ 'DATE' , 'TEMP' , 'PRCP' , 'SNOW' ] ]

# Change column name
weather_df.columns = [ 'Date' , 'Temp' , 'Prcp' , 'Snow' ]
weather_df[ 'Date' ] = pd.to_datetime( weather_df.Date )

# Output cleaned weather data to csv file
weather_df.to_csv( 'cleaned_weather.csv' )


#----------------------Clean crime data--------------------------------------#

# Read crime data
crime_df = pd.read_csv( "data/crime.csv" , sep = "," , parse_dates = ['Date'] )
print( 'Read crime data done!')

# Select attributes: Date, Community Area, FBI Code, Domestic, Arrest 
crime_df = crime_df[ [ 'Date' , 'Community Area' , 'FBI Code' , 'Domestic', 'Arrest' ] ]
print( 'Select crime attributes done!')

# Sort by date
crime_df[ 'Date' ] = pd.to_datetime( crime_df.Date )
crime_df = crime_df.sort_values('Date')
print( 'Sorted crime date by date done!')

# Remove time, keep only date
temp = pd.DatetimeIndex( crime_df[ 'Date' ] )
crime_df[ 'Date' ] = temp.date
crime_df[ 'Date' ] = pd.to_datetime( crime_df.Date )
print( 'Removed time from datetime done!' )

# Output cleaned crime data to csv file
crime_df.to_csv( 'cleaned_crime.csv' )
print( 'Outputed cleaned crime data done!')


#----------------------Merge weather and crime data----------------------------#

# Merge crime and weather data frames 
combine_df = pd.merge( weather_df , crime_df , how = 'outer' , on = 'Date' ) 
print( 'Merged crime and weather data done!')

# Output merged data to csv file
combine_df.to_csv( 'combined.csv' )
print( 'Outputed combined data done!')
