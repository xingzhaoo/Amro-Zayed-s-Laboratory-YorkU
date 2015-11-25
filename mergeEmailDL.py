#!/usr/bin/python
__author__ = "Xing Zhao@Amro Zayed's Lab, York University"
__copyright__ = "Copyright (C) 2015 Xing Zhao@Amro Zayed's Lab, York University"
__license__ = "Public Domain"
__version__ = "1.0"

import sys
def printEmail(emailList):
    outlist = ''
    for item in emailList:
       outlist += item + "\t"
    print outlist.rstrip()
    
    #text_file.write(outlist+"\n")

emailfile = open(str(sys.argv[1]), "r")
#text_file = open(str(sys.argv[2]), "w")
#line = emailfile.readline();
oldset = ''
emailEntry = []
for line in emailfile:
    dataset = line.split()
    if len(dataset) < 2:
       continue 
    #print dataset[0]
    #print oldseti
    if ";" in dataset[0]:
	Mails = dataset[0].split(";")
	dataset[0] = Mails[0]
	del dataset[1]

    if dataset[0] == oldset:
        for item in dataset[1:]:
	    emailEntry.append(item)
    else:
        printEmail(emailEntry)
        emailEntry = []
	tempSet = list(dataset)
        
	for item in tempSet:
	   emailEntry.append(item)
    
    oldset = dataset[0]	

emailfile.close()
#text_file.close()
