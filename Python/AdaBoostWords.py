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
Gender, Num_the, Num_i, Num_and, Num_him, Num_of = [], [], [], [], [], []

with open( "data.txt", "r" ) as f :
	header1 = f.readline()

	for line in f:
		l = line.split(',')
		Gender.append(str(l[0]))
		Num_the.append(float(l[10]))
		Num_i.append(float(l[11]))
		Num_and.append(float(l[12]))
		Num_him.append(float(l[13]))
		Num_of.append(float(l[14]))
	f.close()

for i in range(0,len(Gender)):
	if Gender[i] == 'female':
		Gender[i]=0
	elif Gender[i]== 'male':
		Gender[i]=1

trainlen = int(np.floor(len(Gender)/2))


Data_Train_l = np.array(Gender[0:trainlen])
Data_Train = np.column_stack((Num_the[0:trainlen], Num_i[0:trainlen], Num_and[0:trainlen], Num_him[0:trainlen], Num_of[0:trainlen]))



Data_Test_l = np.array(Gender[trainlen:-1])
Data_Test = np.column_stack(( Num_the[trainlen:-1], Num_i[trainlen:-1], Num_and[trainlen:-1], Num_him[trainlen:-1], Num_of[trainlen:-1]))



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

print 'Num_the \t \t = %.4g ' % pram[0]
print 'Num_i \t \t \t = %.4g ' % pram[1]
print 'Num_and  \t \t = %.4g ' % pram[2]
print 'Num_him  \t \t = %.4g ' % pram[3]
print 'Num_of \t \t \t = %.4g ' % pram[4]


BLT_m = BLT[Data_Test_l==0]
BLT_f = BLT[Data_Test_l==1]

b = np.linspace(-0.02,0.02)

plt.hist(BLT_m,normed=True,bins=b,color='b',label='men',alpha=0.5)
plt.hist(BLT_f,normed=True,bins=b,color='r',label='women',alpha=0.5)
plt.legend()
plt.xlabel('AdaBoost score',fontsize=20)
plt.ylabel('Occurence',fontsize=20)
plt.title('AdaBoost decision tree result words',fontsize=25)
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.show()

# scores: 0.621913080988
# Parameter importance:

# Num_the 	 	 = 0.175 
# Num_i 	 	 = 0.19 
# Num_and  	 	 = 0.16 
# Num_him  	 	 = 0.275 
# Num_of 	 	 = 0.2 
