#!/usr/bin/python
#Author: Xing Zhao
#Filter function takes seed file and raw data file
#output the data in the raw data file exclude the reference dara in seed file
#seed file include data requied to be filtered out,one line per record 
#records in the raw data file must be seperated by line
import subprocess
import sys
import os

#open file and load the list
if len(sys.argv) != 3:
  print "Usage: ./filter.py seed_file rawdata_file"
  quit()

load_list = open(str(sys.argv[1]), "r")
load_data = open(str(sys.argv[2]), "r")

filter_list = load_list.readlines()

data = load_data.readlines()
#print data
for entry in data:
   flag = 0
   for seed in filter_list:
       if seed.strip() in entry:
	  flag = 1
   if flag == 0:
       print entry
