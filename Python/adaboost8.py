#!/usr/bin/env python
#coding: UTF8

from __future__ import division
from array import array
from math import sqrt
from math import pi
import numpy as np
import scipy
from scipy.stats import norm
import matplotlib.pyplot as plt

from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

logdata=False

Data = []
Gender, Age, Job, Zodiac, AvgPostLength, AvgWordLength, AvgPostFrequency, NumURL, NumInternetWords, NumAdjectives, Num_the, Num_i, Num_and, Num_him, Num_of = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
with open( "data.txt", "r" ) as f :
	header1 = f.readline()

	for line in f:
		l = line.split(',')
		Gender.append(str(l[0]))
		Age.append(int(l[1]))
		Job.append(str(l[2]).strip())
		Zodiac.append(str(l[3]))
		AvgPostLength.append(float(l[4]))
		AvgWordLength.append(float(l[5]))
		AvgPostFrequency.append((float(l[6])))
		NumURL.append(float(l[7]))
		NumInternetWords.append(float(l[8]))
		NumAdjectives.append(float(l[9]))
		Num_the.append(float(l[10]))
		Num_i.append(float(l[11]))
		Num_and.append(float(l[12]))
		Num_him.append(float(l[13]))
		Num_of.append(float(l[14]))
	f.close()

ujob = []
with open("uniquejobs.txt") as f:
	for line in f:
		string = line.strip(',\r\n')
		string.rstrip(' ')
		ujob.append(string)

ujobnum = np.linspace(0,len(ujob)-1,len(ujob),endpoint=True)

for j in range(0,len(Job)):
	for u in range(0,len(ujob)):
		if Job[j] == ujob[u]:
			Job[j]=ujobnum[u]


for i in range(0,len(Gender)):
	if Gender[i] == 'female':
		Gender[i]=0
	elif Gender[i]== 'male':
		Gender[i]=1

if logdata==True:
	for i in range(0,len(Gender)):
		if AvgPostFrequency[i]!=0:
			AvgPostFrequency[i]=np.log(AvgPostFrequency[i])
		else:
			continue
		if AvgPostLength[i]!=0:
			AvgPostLength[i]=np.log(AvgPostLength[i])
		else:
			continue
		if NumInternetWords[i]!=0:
			NumInternetWords[i]=np.log(NumInternetWords[i])
		else:
			continue


trainlen = int(np.floor(len(Gender)/2))


Data_Train_l = np.array(Gender[0:trainlen])
Data_Train = np.column_stack((Age[0:trainlen], Job[0:trainlen], AvgPostLength[0:trainlen], AvgWordLength[0:trainlen], AvgPostFrequency[0:trainlen], NumURL[0:trainlen], NumInternetWords[0:trainlen], NumAdjectives[0:trainlen]))

Data_Test_l = np.array(Gender[trainlen:-1])
Data_Test = np.column_stack((Age[trainlen:-1], Job[trainlen:-1], AvgPostLength[trainlen:-1], AvgWordLength[trainlen:-1], AvgPostFrequency[trainlen:-1], NumURL[trainlen:-1], NumInternetWords[trainlen:-1], NumAdjectives[trainlen:-1]))


###################################################################
# Source
# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier
#
###################################################################

clf = AdaBoostClassifier(n_estimators=500)
clf.fit(Data_Train,Data_Train_l)
print 'scores:', clf.score(Data_Test,Data_Test_l)
BLT = clf.decision_function(Data_Test)


print 'Parameter importance:\n'
pram = clf.feature_importances_


print 'Age \t \t \t = %.4g ' % pram[0]
print 'Job \t \t \t = %.4g ' % pram[1]
print 'AvgPostLength  \t \t = %.4g ' % pram[2]
print 'AvgWordLength  \t \t = %.4g ' % pram[3]
print 'AvgPostFrequency  \t = %.4g ' % pram[4]
print 'NumURL  \t \t = %.4g ' % pram[5]
print 'NumInternetWords  \t = %.4g ' % pram[6]
print 'NumAdjectives  \t \t = %.4g ' % pram[7]

# B = []
# for i in range(0,len(BLT)):
# 	B.append(BLT[i][1])
# B = np.array(B)

# print B

BLT_f = BLT[Data_Test_l==0]
BLT_m = BLT[Data_Test_l==1]

b = np.linspace(-0.01,0.01)
#b = np.linspace(-0.0,1)

plt.hist(BLT_m,normed=True,bins=b,color='b',label='Men',alpha=0.5)
plt.hist(BLT_f,normed=True,bins=b,color='r',label='Women',alpha=0.5)
plt.legend()
plt.xlabel('AdaBoost score',fontsize=20)
plt.ylabel('Occurence',fontsize=20)
plt.title('AdaBoost decision tree result',fontsize=25,fontweight='bold')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.subplots_adjust(bottom=0.2)
axes = plt.gca()
axes.set_xlim([-0.01,0.01])
plt.show()


# scores: 0.633991157123
# Parameter importance:

# Age 	 	 	 		 = 0.03 
# Job 	 	 	 		 = 0.15 
# AvgPostLength  	 	 = 0.186 
# AvgWordLength  	 	 = 0.17 
# AvgPostFrequency  	 = 0.092 
# NumURL  	 	 		 = 0.152 
# NumInternetWords  	 = 0.1 
# NumAdjectives  	 	 = 0.12


# Nu med Log af ting

# scores: 0.633236277364
# Parameter importance:

# Age 	 	 	 		 = 0.046 
# Job 	 	 	 		 = 0.152 
# Log AvgPostLength  	 = 0.132 
# AvgWordLength  	 	 = 0.166 
# Log AvgPostFrequency   = 0.14 
# NumURL  	 	 		 = 0.126 
# Log NumInternetWords   = 0.122 
# NumAdjectives  	 	 = 0.116 



