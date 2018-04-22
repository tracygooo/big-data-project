#!/bin/bash

# remove output directory
hdfs dfs -rm -r /user/hduser/weather-crime/output

# define paths used in hadoop streaming
hadoop_path="/usr/local/hadoop/bin/hadoop"
jar_path="/usr/local/hadoop/hadoop-streaming-2.7.5.jar"
mapper_path="/home/hduser/big-data-project/weather-crime/map-reduce/code/test_mapper.py"
reducer_path="/home/hduser/big-data-project/weather-crime/map-reduce/code/test_reducer.py"
input_path="/user/hduser/weather-crime/input/wc.tes"
output_path="/user/hduser/weather-crime/output"
filename1="output/weights.txt"
filename2="output/test_ave.txt"
filename3="input/descale.txt"

# define stream command
stream="$hadoop_path jar $jar_path -mapper $mapper_path -reducer $reducer_path -input $input_path -output $output_path -file $filename1 -file $filename2 -file $filename3" 

# execute hadoop streaming command
eval $stream

# output final results
hdfs dfs -cat /user/hduser/weather-crime/output/*
