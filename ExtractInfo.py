from __future__ import division
from ROOT import *        # Import ROOT libraries (to use ROOT)
from math import *        # Import MATH libraries (for extended MATH functions)
from array import array   # Import the concept of arrays (needed in TGraphErrors
from subprocess import call
import os
import commands
#Import the xml reader:
try : 
	import xml.etree.cElementTree as ET #Use this one
except ImportError: 
	import xml.etree.ElementTree as ET  #If above fails, use this one :) 

#Define lists to fill data into: 
#Info from filename
filespecs = []
#Dates and blogs
filecontent = []

indir = 'newblogs/'# path
for filenames in os.walk(indir): #loops over each file
	for f in filenames[2]: # I'm not sure why [2] is needed but it works
		infoStr = f.split('.') # Splits the filename into colums: 0:number 1:gender 2:age 3:work 4:zodiac 5:xml
		filename = f
		#Fills lists with info from filename
		Gender = [] ; Gender = infoStr[1]
		Age = [] ; Age = infoStr[2]
		Work = [] ; Work = infoStr[3]
		Zodiac = [] ; Zodiac = infoStr[4]

		filespecs.append([Gender, Age, Work, Zodiac])
		print filespecs[-1]
		#Extract data
		dates = []
		posts = []
		print f
		tree = ET.ElementTree(file='newblogs/'+f) 
		root = tree.getroot() #Now all information from the file is in this variable

		for date in root.iter('date'): #Iterate over all children of root called "date"
			dates.append(date.text) #Save dates to the list
		for post in root.iter('post'): #Iterate over all children of root called "post"
			posts.append(post.text) #Save postss to the list
		filecontent.append([dates,posts])

print filespecs[-1], filecontent[-1]

raw_input( ' ... Press enter to exit ... ' )












