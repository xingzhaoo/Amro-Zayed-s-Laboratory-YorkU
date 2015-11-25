#!/usr/bin/python
__author__ = "Xing Zhao@Amro Zayed's Lab, York University"
__copyright__ = "Copyright (C) 2015 Xing Zhao@Amro Zayed's Lab, York University"
__license__ = "Public Domain"
__version__ = "1.0"

import sys
import os
import subprocess
import multiprocessing
from multiprocessing import Pool
import tempfile
#import time
#local functiona
#chunk the msSample into N process list
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
      out.append(seq[int(last):int(last + avg)])
      last += avg

    return out


#individual sample from dh output
def extractTP(sample):
    if not sample:
       return

    #split each sample into lines
    lines = sample.strip().splitlines()
    tup = () # store taj, p values
    taj = []
    p = []
    #scan through each line to extract the values
    for line in lines:
        if not line:
           continue
        if 'Tajima' in line:
           taj = line.split(' = ')
        if 'p-value' in line:
           p = line.split(' = ')
    #end of each sample to collect tup values
    if taj and p:
       tup = (taj[1], p[1])
    if len(tup)== 2:
       return tup


#process the list contains chucked samples
def dhToMsProcess(sampleList):
    #restore the list back to String
    eachMsOut = ""
    for line in sampleList:
        eachMsOut += "//" + line
    #write to vFile in memory

    fd, vfPath = tempfile.mkstemp()
    os.write(fd, eachMsOut)
    #print fd
    #print vfPath

    #DH part start
    #cmooand line for Dh, make sure this file is with dh directory
    cmd_dh = ['java', '-cp', '.:dh/dh.jar', 'dh.Readms', vfPath, nsam]
    p_dh = subprocess.Popen(cmd_dh, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    dhOut, err = p_dh.communicate()

    os.close(fd)
    os.remove(vfPath)

    samples = dhOut.strip().split('\\') #split dh output into samples
    #pharse samplies
    records = [] # list to store (T,p)values from each sample

    for eachSample in samples[1:]:
        if eachSample:
           records.append(extractTP(eachSample))

    return records

#program start
#start_time = time.time()

if __name__ == '__main__':
   
   if len(sys.argv) < 2:
      sys.exit("Your configuration file for 'ms' is required!")

   PROCESS = 0

   if len(sys.argv) < 3:
     # print "All CPUs will be used."
      PROCESS = multiprocessing.cpu_count()
   else:
      PROCESS = int(sys.argv[2])
     # print "%d CPU(s) will be used." % (PROCESS)


   #MS part start
   #open the ms config file and read the 1st line
   conf_file = open(str(sys.argv[1]), "r")
   #extract the parameters set for ms
   cmd_ms = conf_file.readline().strip().split()
   #get the nsam
   nsam = cmd_ms[1]
   #cmd_ms = ['msdir/ms', '4', '2', '-t', '5.0']
   p_ms = subprocess.Popen(cmd_ms, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   msOut, err = p_ms.communicate()

   #split the output from ms
   msSampleList = msOut.split("//")

   #parallel starts
   if PROCESS < 1 or PROCESS > multiprocessing.cpu_count():
      PROCESS = multiprocessing.cpu_count()
   
   dhProcArray = chunkIt(msSampleList[1:], PROCESS)

   pool = Pool(processes=PROCESS)
   #TASK = [(samples[x]) for x in range(1,len(samples))]
   results = [pool.apply_async(dhToMsProcess, args=(slist,)) for slist in dhProcArray]


   i = 1
   print "Run\tTajimaD\tp"
   for recordList in results:
       for tup in recordList.get():
           if tup:
              print  "%d\t%f\t%f" % (i, float(tup[0]), float(tup[1]))
              i += 1

   pool.close()
   pool.join()

  # print "---%s---minutes" % ((time.time() - start_time)/60)
