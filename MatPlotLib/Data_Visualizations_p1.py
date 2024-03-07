#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:29:39 2024

@author: jitendra
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inspect
import seaborn as sns
x = [0,2,4,5,6,7,8,9,10]
y = [60,13,45,29,48,77,102,95,58]
y1 = [60,13,45,29,48,77,102,95,58]
y2 = [50,12,41,66,23,65,87,43,67]

print(plt.style.available)



#####LINE PLOTS######
#A basic line plot
'''
plt.style.use('classic')
plt.plot(x,y1)
plt.show()
'''

#Overlaying one line plot over another one
'''
plt.style.use('seaborn-whitegrid')
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
'''

#Adding a title, labels, and saving
'''
plt.style.use('seaborn-whitegrid')
plt.plot(x,y1,'-')
plt.plot(x,y2,'--')
plt.title('Average scores in a class')
plt.xlabel('Frequency')
plt.ylabel('Average marks')
plt.savefig('abc.png')
plt.show()
'''


#Adding a legend
'''
plt.style.use('seaborn-whitegrid')
plt.plot(x,y1,'-')
plt.plot(x,y2,'--')
plt.title('Average scores in a class')
plt.xlabel('Count')
plt.ylabel('Average marks')
plt.legend(['Class A','Class B'])
plt.savefig('abc.png')
plt.show()
'''
#Alternate way to use a legend
'''
plt.style.use('seaborn-whitegrid')
plt.plot(x,y1,'-',label='Class A')
plt.plot(x,y2,'--',label='Class B')
plt.title('Average scores in a class')
plt.legend()
plt.show()
'''

#Change location of legend
'''
plt.style.use('seaborn-whitegrid')
plt.plot(x,y1,'-',label='Class A')
plt.plot(x,y2,'--',label='Class B')
plt.title('Average scores in a class')
plt.legend(loc="upper left")
plt.show()
'''

#Adding colors, markers, linewidth, and annotations
'''


plt.plot(x,y1,'-',color='r',marker='o',linewidth = 6, label='Class A')
plt.plot(x,y2,'--',color='b',marker='x',label='Class B')
plt.title('Average scores in a class')
plt.legend(loc="upper left")
plt.tight_layout()
for x_val, y_val in zip(x, y1):
    label = y_val
    plt.annotate(label, (x_val, y_val),
                 textcoords="offset points",
                 xytext=(0, 10), ha="center")

for x_val, y_val in zip(x, y2):
    label = y_val
    plt.annotate(label, (x_val, y_val),
                 textcoords="offset points",
                 xytext=(0, 10), ha="right")

plt.show()
'''


#Stackplot
'''
plt.stackplot(x,y1,colors='r')
plt.stackplot(x,y2,colors='b')
plt.title('Average scores in a class')
plt.legend(['Class A','Class B'],loc="upper left")

plt.show()
'''

'''
plt.style.use('dark_background')
plt.stackplot(x,y1,colors='r')
plt.stackplot(x,y2,colors='b')
plt.title('Average scores in a class')
plt.legend(['Class A','Class B'],loc="upper left")
plt.show()
'''




#####  BAR PLOTS  ######
#Show frequency distribution of categorical variables, but can be used for other cases too

Classes = ["A","B","C","D"]
Class_Female_Counts = [21,19,20,15]

#Visualizing data of one source

'''
plt.bar(Classes, Class_Female_Counts, color='b')
plt.title("Class_Counts per each class")
plt.xlabel("Class Name")
plt.ylabel("Class_Female_Counts")


for i, y_val in enumerate(Class_Female_Counts):
    label = y_val
    plt.annotate(str(label), (i, y_val),xytext=(0, -60),
                 textcoords="offset points", ha="center")
    
    
plt.show()
'''


#Visualizing data of two sources simultaneously using a bar plot and a line plot

'''
Classes = ["A","B","C","D"]
Female_counts= [21,19,20,15]
Scores = [50,100,75,80]
plt.bar(Classes, Female_counts, color='b',label="Female_counts")
plt.plot(Classes, Scores, color='r',label="Scores")
plt.legend()
plt.show()
'''


#You can tinker with the width of the bars as well
'''
Classes = ["A","B","C","D"]
Female_counts = [21,19,20,15]
Scores = [50,100,75,80]
plt.bar(Classes, Female_counts, color='b',width = 0.2, label="Female_counts")
plt.plot(Classes, Scores, color='r',label="Scores")
plt.legend()
plt.show()
'''


#plotting multiple bars at once
'''
Classes = ["A","B","C","D"]
Female_counts = [21,19,20,15]
Male_counts = [19,20,21,18]
plt.bar(Classes, Female_counts, width=0.2, color='b',label="Female_counts")
plt.bar(Classes, Male_counts, width=0.2, color='r',label="Male_counts")
plt.legend()
plt.show()
'''
#a more useful view
'''
width = 0.2
Classes = ["A","B","C","D"]
Classes_index = np.arange(len(Classes))
Female_counts = [21,19,20,15]
Male_counts = [19,20,21,18]
plt.bar(Classes_index-width, Female_counts, width=width, color='b',label="Female_counts")
plt.bar(Classes, Male_counts, width=width, color='r',label="Male_counts")
plt.legend()
plt.show()
'''


#EXERCISE: Try out a bar chart and a line plot using the following data:
'''
experience = [1,2,3,4,5,6,7]
data_scientist_sal = [90450,10540,12540,13654,16854,25640,356435]
data_analyst_sal = [78543, 89342, 10436, 11564, 13654, 15764, 20465]
'''

######  PIE CHARTS  #####

grades = [43,65,34,76]

'''
plt.pie(grades)
plt.show()
'''
'''
Classes = ['A','B','C','D']
plt.pie(grades,labels = Classes)
plt.title("Average marks per Class")
plt.show()
'''

#changing the start angle
'''
Classes = ['A','B','C','D']
plt.pie(grades,labels = Classes, startangle= 180)
plt.title("Average marks per Class")
plt.show()
'''


#helps highlight one pie

'''
Classes = ['A','B','C','D']
explodes = [0.2,0,0,0]
plt.pie(grades,labels = Classes, startangle= 180, explode = explodes)
plt.title("Average marks per Class")
plt.show()
'''

#change the size of the figure and labels
'''
plt.figure(figsize=(40,40)) 
plt.rcParams['font.size'] = 60
Classes = ['A','B','C','D']
explodes = [0.2,0,0,0]
plt.pie(grades,labels = Classes, startangle= 180, explode = explodes)
plt.title("Average marks per Class")
plt.legend(title="Classes",loc="upper left")
plt.show()
'''

#manually adding colors
'''
plt.figure(figsize=(20,20)) 
plt.rcParams['font.size'] = 40
Classes = ['A','B','C','D']
explodes = [0.2,0,0,0]
colors = ["b","g","y","hotpink"]
plt.pie(grades,labels = Classes, startangle= 180, explode = explodes, colors = colors)
plt.title("Average marks per Class")
'''

#add percentages
'''
plt.figure(figsize=(20,20)) 
plt.rcParams['font.size'] = 40
Classes = ['A','B','C','D']
explodes = [0.2,0,0,0]
colors = ["b","g","y","hotpink"]
plt.pie(grades,labels = Classes, startangle= 180, explode = explodes, colors = colors, autopct = "% 1.1f %%")
plt.title("Average marks per Class")
'''


######   HISTOGRAMS  #####
# A graph showing the frequency distribution of continuous variables


df = pd.read_csv("/Users/cwbenton/MATH4140/datasets/supermarket_sales.csv")
print(df.head())
'''
bins=pd.cut(df["gross income"],5)
print(bins)

plt.hist(df["gross income"],bins=5,color="blue",edgecolor="black")
plt.show()
'''
'''
plt.figure(figsize=(20,20)) 
plt.rcParams['font.size'] = 40
sales_median = df["gross income"].median()
sales_mean = df["gross income"].mean()

plt.hist(df["gross income"],bins=5,color="blue",edgecolor="black")
plt.axvline(sales_median, color="gray", label="Salary Median", linewidth=10)
plt.axvline(sales_mean, color="green", label="Salary Mean", linewidth=10)
plt.title("Gross income distribution")
plt.xlabel("income")
plt.ylabel("counts")
plt.legend(loc = "upper right")
plt.show()

'''

###### SCATTER PLOTS  ######

'''
#used to plot data points on horizontal and vertical axis in the attempt to show how much one variable is affected by another.
#change style to grid

#scatterplot along with a color map
#plt.scatter(df["Rating"],df["gross income"],color='r')

plt.scatter(df["Rating"], df["Quantity"], color='b', marker='o')
plt.title("Ratings vs. Gross Income")
plt.xlabel("Ratings")
plt.ylabel("Gross Income")
plt.legend(["Grodd Income", "Quantity"], loc="upper left")
plt.show()
'''



####### BOX PLOTS #########
'''
#Depicts numerical data through quartiles
plt.figure(figsize=(5,5)) 
plt.rcParams['font.size'] = 10
plt.boxplot(df["gross income"])
#plt.boxplot(df["gross income"],notch=True)
#plt.boxplot(df["gross income"],notch=True,showfliers=False)
#plt.boxplot(df["gross income"],notch=True,showfliers=False,vert=False)
plt.title("Box Plot of incomes")
plt.ylabel("incomes")
plt.show()
'''



####### VIOLIN PLOTS #######
#Shows probability density of data at different values

'''
plt.figure(figsize=(20,20))
plt.rcParams['font.size']=40

plt.violinplot(df["gross income"], showmedians=True, quantiles=[0,0.25,0.50,0.75])
plt.title("Violin Plot of incomes")
plt.ylabel("gross incomes")
plt.show()

#Find out all the parameters of a function

import inspect
print(inspect.signature(plt.violinplot))


###Let us try a few of these options

plt.violinplot(df["gross income"])
plt.title("Violin Plot of incomes")
plt.ylabel("gross incomes")
'''






######## TIME SERIES ########
'''
plt.figure(figsize=(5,5)) 
plt.rcParams['font.size'] = 10
df1 = df.sample(5) #Chooses 5 random observations from the dataframe
plt.plot_date(df1.Date,df1.Rating)
plt.title("Time Series")
plt.show()
#plt.xticks(rotation='vertical')
'''

'''
df1 = df.sample(5)
df1 = df1.sort_values(by="Date") #Sort by date so the x-axis is in order.
plt.plot_date(df1.Date,df1.Rating,marker='o',linestyle="solid")
plt.title("Time Series")
plt.show()
'''

###### MULTIPLE SUB PLOTS ######
'''
plt.figure(figsize=(20,20))
plt.rcParams['font.size']=40
plt.title("Box plot vs Violin plot", fontsize=50)

plt.subplot(2,1,1) #I want 2 subplots and put this at row 1 and column 1.
plt.violinplot(df["gross income"])
plt.ylabel("gross income")

plt.subplot(2,1,2) #I want 2 subplots and put this at row 1 column 2.
plt.boxplot(df["gross income"])
plt.ylabel("gross income")
#plt.suptitle("Box plot vs Violin plot", fontsize=50)
plt.show()
'''

##### Plotting using ax instead of plt ######

plt.figure(figsize=(20,20))
plt.rcParams['font.size']=10
figs, axs = plt.subplots(6)

# axs[0] refers to the first subplot
axs[0].violinplot(df["gross income"])
axs[0].set_ylabel("gross income")

# axs[1] refers to the second subplot
axs[1].boxplot(df["gross income"])
axs[1].set_ylabel("gross income")

plt.suptitle("Box plot vs Violin plot", fontsize=25)
plt.show()


#You can also create subplots in several rows

'''
plt.style.use('seaborn-whitegrid')
plt.rcParams['font.size']=10
figs, axs = plt.subplots(2,3,figsize=(10,10))
#figs, axs = plt.subplots(2,3,figsize=(10,10),sharex='col',sharey='row')

# axs[0,0] refers to the subplot at row 1 column 1
axs[0,0].violinplot(df["gross income"])
axs[0,0].set_ylabel("gross income")

# axs[1,0] refers to the subplot at row 2 column 1
axs[1,0].boxplot(df["gross income"])
axs[1,0].set_ylabel("gross income")

plt.suptitle("Box plot vs Violin plot", fontsize=25)
'''

#annotating individual points using arrows
'''
plt.style.use('seaborn-whitegrid')
plt.rcParams['font.size']=10
figs, axs = plt.subplots(2,3,figsize=(10,10),sharex='col',sharey='row')
Classes = ["A","B","C","D"]
Female_counts= [21,19,20,15]
Scores = [50,100,75,80]
axs[0,1].bar(Classes, Female_counts, color='b',label="Female_counts")
axs[1,1].plot(Classes, Scores, color='r',label="Scores")
axs[1,1].annotate('local maximum', xy=(1, 100), xytext=(-1.5, 85),arrowprops=dict(facecolor='black', shrink=0.05))
axs[0,1].legend()
axs[1,1].legend()
plt.show()
'''


###### CUSTOMIZING TICKS ######
    
#Major ticks and minor ticks



#hiding the ticks
'''
plt.style.use('classic')
plt.rcParams['font.size']=20
figs, axs = plt.subplots(2,figsize=(10,10),sharex='col',sharey='row')
axs[0].plot(x,y1,'-',color='r',label='CLass A')
axs[1].plot(x,y2,'--',color='b',label='CLass B')
axs[0].legend(loc="upper left")
axs[1].legend(loc="upper left")
plt.suptitle("Line plots",fontsize=26)
axs[0].xaxis.set_major_locator(plt.NullLocator())
axs[1].yaxis.set_major_formatter(plt.NullFormatter())
axs[1].xaxis.set_major_locator(plt.NullLocator())
axs[0].yaxis.set_major_formatter(plt.NullFormatter())
plt.show()
'''

#Changing the number of ticks
'''
plt.style.use('classic')
plt.rcParams['font.size']=20
figs, axs = plt.subplots(2,figsize=(10,10),sharex='col',sharey='row')
axs[0].plot(x,y1,'-',color='r',label='CLass A')
axs[1].plot(x,y2,'--',color='b',label='CLass B')
axs[0].legend(loc="upper left")
axs[1].legend(loc="upper left")
plt.suptitle("Line plots",fontsize=26)
axs[0].xaxis.set_major_locator(plt.MaxNLocator(3))
axs[0].yaxis.set_major_locator(plt.MaxNLocator(3))
axs[1].xaxis.set_major_locator(plt.MaxNLocator(3))
axs[1].yaxis.set_major_locator(plt.MaxNLocator(3))
plt.show()
'''

###### Color Maps ######
'''
classes = np.random.randint(0,4,1000)
#plt.scatter(df["Rating"],df["gross income"])
#plt.scatter(df["Rating"],df["gross income"],c=classes)
plt.scatter(df["Rating"],df["gross income"],c=classes,cmap="Blues")

plt.show()
'''

df2 = df[['gross income','Rating','Quantity']]
sns.heatmap(df2.corr(),annot=True,cmap='Blues') #Heat Maps
plt.show()


























