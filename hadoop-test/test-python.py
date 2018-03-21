#!/usr/bin/python

from snakebite.client import Client
client = Client('localhost', 50070)
for x in client.ls(['/']):
	print x
