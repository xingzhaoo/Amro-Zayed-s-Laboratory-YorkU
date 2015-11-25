# Amro-Zayed-s-Laboratory-YorkU

msToDhConc.py
It runs the ms and passes the ms result into dh. After dh produces the result, it extracts the Tajma and p value from the dh result.

To use this program, ensure the dh package which stores all DH files and msdir package which stores MS files are under the same directory as this program.

Before you run the program, you need to give the ms paramters in a config file such as "myfile.txt"
A example in "myfile.txt" can be "msdir/ms 22 100000 -t 11" 
*(Read ms paper if you never use ms. http://home.uchicago.edu/rhudson1/source/mksamples/msdir/msdoc.pdf)

To run the program, use ./msToDhConc.py myfile.txt N > outfile
N is the numer of processors you want to run for this program
outfile is where the result stores to.
