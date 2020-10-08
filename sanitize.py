from __future__ import division
import math               # Import MATH libraries (for extended MATH functions)
from array import array   # Import the concept of arrays (needed in TGraphErrors
from subprocess import call
import os
import commands


indir = '~/Dropbox/Project2 Anvendt Statestik/gammel' #/Users/rikkedagrandlv/Desktop/AnvStat/Project2/blogs'# path
for filenames in os.walk(indir): #loops over each file
    for f in filenames[2]: # I'm not sure why [2] is needed but it works
        
        call(['./sanitizeNew.sh',f])

