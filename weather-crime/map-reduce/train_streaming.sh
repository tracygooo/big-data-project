#!/bin/bash

# remove output directory
hdfs dfs -rm -r /user/hduser/weather-crime/output

# define paths used in hadoop streaming
hadoop_path="/usr/local/hadoop/bin/hadoop"
jar_path="/usr/local/hadoop/hadoop-streaming-2.7.5.jar"
mapper_path="/home/hduser/big-data-project/weather-crime/map-reduce/code/train_mapper.py"
reducer_path="/home/hduser/big-data-project/weather-crime/map-reduce/code/train_reducer.py"
input_path="/user/hduser/weather-crime/input/wc.pat"
output_path="/user/hduser/weather-crime/output"

# define stream command
stream="$hadoop_path jar $jar_path -mapper $mapper_path -reducer $reducer_path -input $input_path -output $output_path" 

# execute hadoop streaming command
eval $stream

hdfs dfs -copyToLocal weather-crime/output/part-00000 /home/hduser/big-data-project/weather-crime/map-reduce/output/weights.txt
