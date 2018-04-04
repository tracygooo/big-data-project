#!/bin/bash

# remove output directory
hdfs dfs -rm -r /user/hduser/boston/output

# define paths used in hadoop streaming
hadoop_dir="/usr/local/hadoop/bin/hadoop"
jar_dir="/usr/local/hadoop/hadoop-streaming-2.7.5.jar"
mapper_dir="/home/hduser/big-data-project/boston/code/train_mapper.py"
reducer_dir="/home/hduser/big-data-project/boston/code/train_reducer.py"
input_dir="/user/hduser/boston/input/boston.pat"
output_dir="/user/hduser/boston/output"

# define stream command
stream="$hadoop_dir jar $jar_dir -mapper $mapper_dir -reducer $reducer_dir -input $input_dir -output $output_dir" 

# execute hadoop streaming command
eval $stream

hdfs dfs -copyToLocal boston/output/part-00000 /home/hduser/big-data-project/boston/code/weights.txt
