## General description:
The goal of this project is to use Hadoop for linear regression. It contains four objects below:
 - hadoop-test 
 - word-count
 - weather-crime
 - boston

### 1. hadoop-test object
./hadoop-test: test build-in mapreduce example (pi calculation) and hdfs command 

### 2. word-count object
./word-count: word-count: utilize common word-count exam to test hadoop streaming utility that enables python script 

### 3. weather-crime object
 - ./weather-crime: apply paralleled linear regression model to combined weather and crime dataset, which are collected from NOAA and Chicago data portal respectively

 - ./weather-crime/data-cleaning: remove unneccessary features of weather and crime dataframes, merge the two datasets on 'date', convert the format of the merged dataset into Metaneural, which is the DMak format

 - ./weather-crime/map-reduce
	- run ./train_streaming.sh, paralleled linear regression - training part, obtain weights.txt
	- run ./test_streaming.sh, paralleled linear regression - testing part 

Please see ./weather-crime/data-workflow for data workflow details


### 4. boston object
./boston: apply paralleled linear regression model to commonly used Boston housing data 

The same with weather-crime object except two differences
 - No need for data-cleaning, training and testing data are directly from DMak output
 - Different features: weather-crime: 6, Boston: 13
