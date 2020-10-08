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


Data = []
Gender, Age, Job, Zodiac, AvgPostLength, AvgWordLength, AvgPostFrequency, NumURL, NumInternetWords, NumAdjectives, Num_the, Num_i, Num_and, Num_him, Num_of = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
with open( "data.txt", "r" ) as f :
	header1 = f.readline()

	for line in f:
		l = line.split(',')
		Gender.append(str(l[0]))
		Age.append(int(l[1]))
		Job.append(str(l[2]))
		Zodiac.append(str(l[3]))
		AvgPostLength.append(float(l[4]))
		AvgWordLength.append(float(l[5]))
		AvgPostFrequency.append(float(l[6]))
		NumURL.append(float(l[7]))
		NumInternetWords.append(float(l[8]))
		NumAdjectives.append(float(l[9]))
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
	if type(Job[j])=='str':

for i in range(0,len(Gender)):
	if Gender[i] == 'female':
		Gender[i]=0
	elif Gender[i]== 'male':
		Gender[i]=1

trainlen = int(np.floor(len(Gender)/2))


Data_Train_l = np.array(Gender[0:trainlen])
Data_Train = np.column_stack((Age[0:trainlen], Job[0:trainlen], AvgPostLength[0:trainlen], AvgWordLength[0:trainlen], AvgPostFrequency[0:trainlen], NumURL[0:trainlen], NumInternetWords[0:trainlen], NumAdjectives[0:trainlen]))



Data_Test_l = np.array(Gender[trainlen:-1])
Data_Test = np.column_stack((Age[trainlen:-1], , Job[trainlen,-1],AvgPostLength[trainlen:-1], AvgWordLength[trainlen:-1], AvgPostFrequency[trainlen:-1], NumURL[trainlen:-1], NumInternetWords[trainlen:-1], NumAdjectives[trainlen:-1]))



###################################################################
# Source
# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier
#
###################################################################

clf = AdaBoostClassifier(n_estimators=200)
clf.fit(Data_Train,Data_Train_l)
print 'scores:', clf.score(Data_Test,Data_Test_l)
BLT = clf.decision_function(Data_Test)

print 'Parameter importance:\n'
pram = clf.feature_importances_


print 'Age \t \t \t = %.4g ' % pram[0]
print 'Age \t \t \t = %.4g ' % pram[1]
print 'AvgPostLength  \t \t = %.4g ' % pram[2]
print 'AvgWordLength  \t \t = %.4g ' % pram[3]
print 'AvgPostFrequency  \t = %.4g ' % pram[4]
print 'NumURL  \t \t = %.4g ' % pram[5]
print 'NumInternetWords  \t = %.4g ' % pram[6]
print 'NumAdjectives  \t \t = %.4g ' % pram[7]


BLT_m = BLT[Data_Test_l==0]
BLT_f = BLT[Data_Test_l==1]


plt.hist(BLT_m,color='b',label='men',alpha=0.5,bins=100)
plt.hist(BLT_f,color='r',label='women',alpha=0.5,bins=100)
plt.legend()
plt.show()