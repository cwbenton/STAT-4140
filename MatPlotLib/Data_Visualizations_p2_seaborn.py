#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 07:36:37 2024

@author: jitendra
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/cwbenton/MATH4140/datasets/supermarket_sales.csv")
print(df.head())
x = [0,2,4,5,6,7,8,9,10]
y = [60,13,45,29,48,77,102,95,58]
y1 = [60,13,45,29,48,77,102,95,58]
y2 = [50,12,41,66,23,65,87,43,67]



#### Using Matplotlib ######
'''
plt.style.use('classic')
plt.rcParams['font.size']=20
figs, axs = plt.subplots(2,figsize=(10,10),sharex='col',sharey='row')
axs[0].plot(x,y1,'-',color='r',label='CLass A')
axs[1].plot(x,y2,'--',color='b',label='CLass B')
axs[0].legend(loc="upper left")
axs[1].legend(loc="upper left")
plt.suptitle("Line plots",fontsize=26)
plt.show()
'''
#### Using Seaborn ######
'''
sns.set_theme()
plt.rcParams['font.size']=20
figs, axs = plt.subplots(2,figsize=(10,10),sharex='col',sharey='row')
axs[0].plot(x,y1,'-',color='r',label='CLass A')
axs[1].plot(x,y2,'--',color='b',label='CLass B')
axs[0].legend(loc="upper left")
axs[1].legend(loc="upper left")
plt.suptitle("Line plots",fontsize=26)
plt.show()
'''

#Some useful Seaborn plots

#Kernel density plot

sns.kdeplot(y1, shade=True)
sns.kdeplot(y2, shade=True)
plt.show()


#Histograms
'''
sns.histplot(y1)
sns.histplot(y2)
plt.show()
'''

#Distplots
'''
sns.distplot(y1)
sns.distplot(y2)
plt.show()
'''

#loading datasets
'''
ir = sns.load_dataset("iris")
print(ir.head())


#pairplots - help identify mutlidimensional relationships amongst samples

sns.pairplot(ir,hue='species',size=2.5)
#hue assigns different colors to different categories
plt.show()
'''


#using axes in Seaborn
'''
figs, axs = plt.subplots(2,figsize=(10,10),sharex='col',sharey='row')
sns.lineplot(x=x,y=y1,color='r',ax=axs[0])
axs[0].legend(['Line 1'],loc="upper left")
sns.lineplot(x=x,y=y2,color='b',ax=axs[1])
axs[1].legend(['Line 2'],loc="upper left")
plt.suptitle("Line plots",fontsize=26)
plt.show()
'''