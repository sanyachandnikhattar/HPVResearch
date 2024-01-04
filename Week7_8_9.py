import matplotlib.pyplot as plt #use anaconda environment to get this to work
import numpy as np
import pandas as pd #importing a library
from scipy.stats import ttest_ind #ttest
import scipy.stats as stats
from tabulate import tabulate #for tables

file_path = 'hpvdata.csv'
hpvdata = pd.read_csv(file_path, low_memory = False)
new_df = hpvdata

#looking at t-test, not p-test
#printing tables

#Section 1 Question 4
new_df = hpvdata[hpvdata['sec1_q4'] != -999]
#new_df = new_df.apply(str())
#sec1q4Median = np.nanmedian(new_df)
sec1q4Median = hpvdata['sec1_q4'].median(numeric_only=True)
print ("Section 1 Question 4 Median: ")
print(sec1q4Median)
sec1q4Mean = hpvdata['sec1_q4'].mean(numeric_only=True)
print ("Section 1 Question 4 Mean: ")
print (sec1q4Mean)
#sec1q4 = hpvdata['sec1_q4']
attitudeQuestionMean = hpvdata['HPV_VAX_attitu_s35'].mean(numeric_only=True)
#ttest_ind(sec1q4, attitudeQuestion, equal_var = False)
#print (ttest_ind)
#res = stats.ttest_ind(hpvdata['sec1_q4'].dropna(), hpvdata['HPV_VAX_attitu_s35'].dropna(), equal_var = True)
#print (res) #this t-test is comparing all of section 1 question 4 against attitude 
#rather than SEPARATED GROUPS AND THEIR CORRESPONDING ATTITUDES AGAINST EACH OTHER --> this is what we need!
print ("\n")

#Section 1 Question 5
new_df = hpvdata[hpvdata['sec1_q5'] != -999]
#sec1q4Median = np.nanmedian(new_df)
sec1q5Median = hpvdata['sec1_q5'].median(numeric_only=True)
print ("Section 1 Question 5 Median: ")
print(sec1q5Median)
sec1q5Mean = hpvdata['sec1_q5'].mean(numeric_only=True)
print ("Section 1 Question 5 Mean: ")
print (sec1q5Mean)
print ("\n")

#Section 1 Question 6
new_df = hpvdata[hpvdata['sec1_q6'] != -999]
sec1q6Median = hpvdata['sec1_q6'].median(numeric_only=True)
print ("Section 1 Question 6 Median: ")
print(sec1q6Median)
sec1q6Mean = new_df['sec1_q6'].mean(numeric_only=True) #exclude negative values with new_df
print ("Section 1 Question 6 Mean: ")
print (sec1q6Mean)
print ("\n")

#Section 1 Question 7
new_df = hpvdata[hpvdata['sec1_q7'] != -999]
sec1q7Median = hpvdata['sec1_q7'].median(numeric_only=True)
print ("Section 1 Question 7 Median: ")
print(sec1q7Median)
sec1q7Mean = new_df['sec1_q7'].mean(numeric_only=True)
print ("Section 1 Question 7 Mean: ") #exclude negative values with new_df
print (sec1q7Mean)
print ("\n")

#Section 1 Question 8
new_df = hpvdata[hpvdata['sec1_q8'] != -999]
sec1q8Median = hpvdata['sec1_q8'].median(numeric_only=True)
print ("Section 1 Question 8 Median: ")
print(sec1q8Median)
sec1q8Mean = new_df['sec1_q8'].mean(numeric_only=True) #exclude negative values with new_df
print ("Section 1 Question 8 Mean: ")
print (sec1q8Mean)
print ("\n")

#Section 1 Question 9
new_df = hpvdata[hpvdata['sec1_q9'] != -999]
sec1q9Median = hpvdata['sec1_q9'].median(numeric_only=True)
print ("Section 1 Question 9 Median: ")
print(sec1q9Median)
sec1q9Mean = new_df['sec1_q9'].mean(numeric_only=True) #exclude negative values with new_df
print ("Section 1 Question 9 Mean: ")
print (sec1q9Mean)
print ("\n")

#Section 1 Question 10
new_df = hpvdata[hpvdata['sec1_q10'] != -999]
sec1q10Median = hpvdata['sec1_q10'].median(numeric_only=True)
print ("Section 1 Question 10 Median: ")
print(sec1q10Median)
sec1q10Mean = new_df['sec1_q10'].mean(numeric_only=True) #new_df already initialized to exclude -999, so use that
print ("Section 1 Question 10 Mean: ")
print (sec1q10Mean)
print ("\n")

#Section 1 Question 11 #1
new_df = hpvdata[hpvdata['sec1_q11_1'] != -999]
sec1q11_1Median = hpvdata['sec1_q11_1'].median(numeric_only=True)
print ("Section 1 Question 11 #1 (Receive and send SMS Messages) Median: ")
print(sec1q11_1Median)
sec1q11_1Mean = new_df['sec1_q11_1'].mean(numeric_only=True)
print ("Section 1 Question 11 #1 Mean: ")
print (sec1q11_1Mean)
print ("\n")

#Section 1 Question 11 #2
new_df = hpvdata[hpvdata['sec1_q11_2'] != -999]
sec1q11_2_Median = hpvdata['sec1_q11_2'].median(numeric_only=True)
print ("Section 1 Question 11 #2 (Take Photos) Median: ")
print(sec1q11_2_Median)
sec1q11_2Mean = hpvdata['sec1_q11_2'].mean(numeric_only=True)
print ("Section 1 Question 11 #2 Mean: ")
print (sec1q11_2Mean)
print ("\n")

#Section 1 Question 11 #3
new_df = hpvdata[hpvdata['sec1_q11_3'] != -999]
sec1q11_3Median = hpvdata['sec1_q11_3'].median(numeric_only=True)
print ("Section 1 Question 11 #3 (Receive and send SMS with Photos) Median: ")
print(sec1q11_3Median)
sec1q11_3Mean = new_df['sec1_q11_3'].mean(numeric_only=True)
print ("Section 1 Question 11 #3 Mean: ")
print (sec1q11_3Mean)
print ("\n")

#Section 1 Question 11 #4
new_df = hpvdata[hpvdata['sec1_q11_4'] != -999]
sec1q11_4Median = hpvdata['sec1_q11_4'].median(numeric_only=True)
print ("Section 1 Question 11 #4 Median (Receive and send money (banking)): ")
print(sec1q11_4Median)
sec1q11_4Mean = new_df['sec1_q11_4'].mean(numeric_only=True)
print ("Section 1 Question 11 #4 Mean: ")
print (sec1q11_4Mean)
print ("\n")

#Section 1 Question 11 #5
new_df = hpvdata[hpvdata['sec1_q11_5'] != -999]
sec1q11_5Median = hpvdata['sec1_q11_5'].median(numeric_only=True)
print ("Section 1 Question 11 #5 Median (Use Messaging Apps): ")
print(sec1q11_5Median)
sec1q11_5Mean = new_df['sec1_q11_5'].mean(numeric_only=True)
print ("Section 1 Question 11 #5 Mean: ")
print (sec1q11_5Mean)
print ("\n")

#Section 1 Question 11 #6
new_df = hpvdata[hpvdata['sec1_q11_6'] != -999]
sec1q11_6Median = hpvdata['sec1_q11_6'].median(numeric_only=True)
print ("Section 1 Question 11 #6 Median (Use Social Media Apps): ")
print(sec1q11_6Median)
sec1q11_6Mean = new_df['sec1_q11_6'].mean(numeric_only=True)
print ("Section 1 Question 11 #6 Mean: ")
print (sec1q11_6Mean)
print ("\n")

#Section 1 Question 11 #7
new_df = hpvdata[hpvdata['sec1_q11_7'] != -999]
sec1q11_7Median = hpvdata['sec1_q11_7'].median(numeric_only=True)
print ("Section 1 Question 11 #7 Median (Watch Videos): ")
print(sec1q11_7Median)
sec1q11_7Mean = new_df['sec1_q11_7'].mean(numeric_only=True)
print ("Section 1 Question 11 #7 Mean: ")
print (sec1q11_7Mean)
print ("\n")

#Section 1 Question 11 #8
new_df = hpvdata[hpvdata['sec1_q11_8'] != -999]
sec1q11_8Median = hpvdata['sec1_q11_8'].median(numeric_only=True)
print ("Section 1 Question 11 #8 Median (Listen to an Audio File/Recording): ")
print(sec1q11_8Median)
sec1q11_8Mean = new_df['sec1_q11_8'].mean(numeric_only=True)
print ("Section 1 Question 11 #8 Mean: ")
print (sec1q11_8Mean)
print ("\n")