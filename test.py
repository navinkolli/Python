# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:27:42 2017

@author: navin
"""
#import sys
"""
import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("train.csv")
 #Reading the dataset in a dataframe using Pandas
 
#df.head(10)
#print(df.describe())
print(df.head(10))
#df['Property_Area'].value_counts()
temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print ('\n Frequency Table for Credit History:\n')
print (temp1)

print ('\nProbility of getting loan for each Credit History class:\n' )
print (temp2)
"""
import pandas as pd
import numpy as np
import matplotlib as plt
list_x= [1,2,3,5]
j=1
list_y=[0]
for i in range(0,len(list_x)):
    if(i==0 or i%2 ==0):
        print(list_x[i])
        list_y = [].append
     
"""for i,index in enumerate(list_x):
    if(i==0 or i%2 ==0):
     print(list_x[i])     
     #print(list_x[j])
     #j=j+2 """
     
        
        
    
    