# ==================================================
# Created by Jinghua to test mapreduce example
# ==================================================

#--------------------------------------------------------------------------
# Enable debug output to console (terminal output)
# http://www.hadoopadmin.co.in/bigdata/how-to-enable-debug-logging-for-hdfs/
#export HADOOP_ROOT_LOGGER=DEBUG,console

#--------------------------------------------------------------------------
# DRFA will allow the logs to go into the File Appender rather than Console -> System.err/out.
#export HADOOP_ROOT_LOGGER=WARN,DRFA

#--------------------------------------------------------------------------
printf "\n\n"
printf "Run madreduce example"
cd /usr/local/hadoop
hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.5.jar pi 2 5
#hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.5.jar pi 16 1000
printf "\n\n"

#--------------------------------------------------------------------------
# Test hdfs
printf "Testing hdfs ls command"
hdfs dfs -ls \
