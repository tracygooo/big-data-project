#!/bin/bash

# remove output directory
hdfs dfs -rm -r /user/hduser/boston/output

# define paths used in hadoop streaming
hadoop_dir="/usr/local/hadoop/bin/hadoop"
jar_dir="/usr/local/hadoop/hadoop-streaming-2.7.5.jar"
mapper_dir="/home/hduser/big-data-project/boston/code/test_mapper.py"
reducer_dir="/home/hduser/big-data-project/boston/code/test_reducer.py"
input_dir="/user/hduser/boston/input/boston.tes"
output_dir="/user/hduser/boston/output"
filename1="output/weights.txt"
filename2="output/test_ave.txt"
filename3="input/descale.txt"

# define stream command
stream="$hadoop_dir jar $jar_dir -mapper $mapper_dir -reducer $reducer_dir -input $input_dir -output $output_dir -file $filename1 -file $filename2 -file $filename3" 

# execute hadoop streaming command
eval $stream

# output final results
hdfs dfs -cat /user/hduser/boston/output/*
