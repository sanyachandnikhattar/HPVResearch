import matplotlib.pyplot as plt #use anaconda environment to get this to work
import numpy as np
import pandas as pd #importing pandas library
from scipy.stats import ttest_ind #ttest
import scipy.stats as stats
from tabulate import tabulate #for tables

file_path = 'hpvdata.csv'
hpvdata = pd.read_csv(file_path, low_memory = False)
hpvdata.describe()
new_df = hpvdata

#Section 1 Question 4 Group 1: Male vs. Female
new_df = hpvdata[hpvdata['sec1_q4'] != -999]
sec1q4Median = new_df['sec1_q4'].median(numeric_only=True)
print ("Section 1 Question 4 Median: ")
print(sec1q4Median)
sec1q4Mean = new_df['sec1_q4'].mean(numeric_only=True)
print ("Section 1 Question 4 Mean: ")
print (sec1q4Mean)
new_df = hpvdata[hpvdata['HPV_VAX_attitu_s35'] != -999]
Group1Male= new_df[new_df['sec1_q4']==1]
Group2Female = new_df[new_df['sec1_q4']==2]
print (np.nanvar(Group1Male['HPV_VAX_attitu_s35'])) #finding variance for male 
#printing everything bet section 1 question 4, dropna doesn't actually drop NaN
print (np.nanvar(Group2Female['HPV_VAX_attitu_s35'])) #finding variance for female
res = stats.ttest_ind(Group1Male['HPV_VAX_attitu_s35'].dropna(), Group2Female['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #syntax for t-test
print (res)
#print (res.pvalue)
print ("\n")

Flag = True
#if abs(np.var(Group1Male)-np.var(Group2Female))>1: #threshold is 1
#  Flag = False

#Section 1 Question 5 Questions 1, 2, 3, 4, 5
new_df = hpvdata[hpvdata['sec1_q5'] != -999]
sec1q5Median = new_df['sec1_q5'].median(numeric_only=True)
print ("Section 1 Question 5 Median: ")
print(sec1q5Median)
sec1q5Mean = new_df['sec1_q5'].mean(numeric_only=True)
print ("Section 1 Question 5 Mean: ")
print (sec1q5Mean)
#print(new_df['sec1_q5'].value_counts())
Group1 = new_df[new_df['sec1_q5']==1]
Group2 = new_df[new_df['sec1_q5']==2]
Group3 = new_df[new_df['sec1_q5']==3]
Group4 = new_df[new_df['sec1_q5']==4]
#run 6 t-tests: 1 and 2, 1 and 3, 1 and 4, 2 and 3, 2 and 4, 3 and 4
res2 = stats.ttest_ind(Group1['HPV_VAX_attitu_s35'].dropna(), Group2['HPV_VAX_attitu_s35'], equal_var = True) #group 1 against 2
res3 = stats.ttest_ind(Group1['HPV_VAX_attitu_s35'].dropna(), Group3['HPV_VAX_attitu_s35'], equal_var = True) #group 1 against 3
res4 = stats.ttest_ind(Group1['HPV_VAX_attitu_s35'].dropna(), Group4['HPV_VAX_attitu_s35'], equal_var = True) #group 1 against 4
res2_3 = stats.ttest_ind(Group2['HPV_VAX_attitu_s35'].dropna(), Group3['HPV_VAX_attitu_s35'], equal_var = True) #group 2 against 3
res2_4 = stats.ttest_ind(Group2['HPV_VAX_attitu_s35'].dropna(), Group4['HPV_VAX_attitu_s35'], equal_var = True) #group 2 against 4
res3_4 = stats.ttest_ind(Group3['HPV_VAX_attitu_s35'].dropna(), Group4['HPV_VAX_attitu_s35'], equal_var = True) #group 3 against 4
print (res2)
print ("\n")
print (res3)
print ("\n")
print (res4)
print ("\n")
print (res2_3)
print ("\n")
print (res2_4)
print ("\n")
print (res3_4)
print ("\n")

#Section 1 Question 6
new_df = hpvdata[hpvdata['sec1_q6'] != -999]
sec1q6Median = new_df['sec1_q6'].median(numeric_only=True)
print ("Section 1 Question 6 Median: ")
print(sec1q6Median)
sec1q6Mean = new_df['sec1_q6'].mean(numeric_only=True) #exclude negative values with new_df
print ("Section 1 Question 6 Mean: ")
print (sec1q6Mean)
res = stats.ttest_ind(new_df['sec1_q6'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
#needs multiple t-tests
Group1q6 = new_df[new_df['sec1_q6']==1] #full-time
Group2q6 = new_df[new_df['sec1_q6']==2] #part-time
Group3q6 = new_df[new_df['sec1_q6']==3] #casual laborer
Group4q6 = new_df[new_df['sec1_q6']==4] #self-employed
Group5q6 = new_df[new_df['sec1_q6']==5] #looking for work
Group6q6 = new_df[new_df['sec1_q6']==6] #not employed, not looking for work
res2 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group2q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 1 against 2
res3 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group3q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 1 against 3
res4 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group4q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 1 against 4
res5 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group5q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 1 against 5
res6 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 1 against 4
res2_3 = stats.ttest_ind(Group2q6['HPV_VAX_attitu_s35'].dropna(), Group3q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 2 against 3
res2_4 = stats.ttest_ind(Group2q6['HPV_VAX_attitu_s35'].dropna(), Group4q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 2 against 4
res2_5 = stats.ttest_ind(Group2q6['HPV_VAX_attitu_s35'].dropna(), Group5q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 2 against 5
res2_6 = stats.ttest_ind(Group2q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 2 against 6
res3_4 = stats.ttest_ind(Group3q6['HPV_VAX_attitu_s35'].dropna(), Group4q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 3 against 4
res3_5 = stats.ttest_ind(Group3q6['HPV_VAX_attitu_s35'].dropna(), Group5q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 3 against 5
res3_6 = stats.ttest_ind(Group3q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 3 against 6
res4_5 = stats.ttest_ind(Group4q6['HPV_VAX_attitu_s35'].dropna(), Group5q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 4 against 5
res4_6 = stats.ttest_ind(Group4q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 4 against 6
res5_6 = stats.ttest_ind(Group5q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 5 against 6
print (res2)
print ("\n")
print (res3) #significant, p-value 1.359
print ("\n")
print (res4)
print ("\n")
print (res5)
print ("\n")
print (res6)
print ("\n")
print (res2_3) #almost significant, p-value 7.1310452
print ("\n")
print (res2_4)
print ("\n")
print (res2_5)
print ("\n")
print (res2_6)
print ("\n")
print (res3_4)
print ("\n")
print (res3_5)
print ("\n")
print (res3_6)
print ("\n")
print (res4_5)
print ("\n")
print (res4_6)
print ("\n")
print (res5_6)
print ("\n")

#Section 1 Question 7
new_df = hpvdata[hpvdata['sec1_q7'] != -999]
sec1q7Median = new_df['sec1_q7'].median(numeric_only=True)
print ("Section 1 Question 7 Median: ")
print(sec1q7Median)
sec1q7Mean = new_df['sec1_q7'].mean(numeric_only=True)
print ("Section 1 Question 7 Mean: ") #exclude negative values with new_df
print (sec1q7Mean)
res = stats.ttest_ind(new_df['sec1_q7'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
#check: negative value still being produced, how do we fix this?
print (res)
print ("\n")

#Section 1 Question 8
new_df = hpvdata[hpvdata['sec1_q8'] != -999]
sec1q8Median = new_df['sec1_q8'].median(numeric_only=True)
print ("Section 1 Question 8 Median: ")
print(sec1q8Median)
sec1q8Mean = new_df['sec1_q8'].mean(numeric_only=True) #exclude negative values with new_df
print ("Section 1 Question 8 Mean: ")
print (sec1q8Mean)
res = stats.ttest_ind(new_df['sec1_q8'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 9
new_df = hpvdata[hpvdata['sec1_q9'] != -999]
sec1q9Median = new_df['sec1_q9'].median(numeric_only=True)
print ("Section 1 Question 9 Median: ")
print(sec1q9Median)
sec1q9Mean = new_df['sec1_q9'].mean(numeric_only=True) #data frame already initialized to exclude -999, so use new_df
print ("Section 1 Question 9 Mean: ")
print (sec1q9Mean)
res = stats.ttest_ind(new_df['sec1_q9'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 10
new_df = hpvdata[hpvdata['sec1_q10'] != -999]
sec1q10Median = new_df['sec1_q10'].median(numeric_only=True)
print ("Section 1 Question 10 Median: ")
print(sec1q10Median)
sec1q10Mean = new_df['sec1_q10'].mean(numeric_only=True)
print ("Section 1 Question 10 Mean: ")
print (sec1q10Mean)
res = stats.ttest_ind(new_df['sec1_q10'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 11 #1
new_df = hpvdata[hpvdata['sec1_q11_1'] != -999]
sec1q11_1Median = new_df['sec1_q11_1'].median(numeric_only=True)
print ("Section 1 Question 11 #1 (Receive and send SMS Messages) Median: ")
print(sec1q11_1Median)
sec1q11_1Mean = new_df['sec1_q11_1'].mean(numeric_only=True)
print ("Section 1 Question 11 #1 Mean: ")
print (sec1q11_1Mean)
res = stats.ttest_ind(new_df['sec1_q11_1'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 11 #2
new_df = hpvdata[hpvdata['sec1_q11_2'] != -999]
sec1q11_2_Median = new_df['sec1_q11_2'].median(numeric_only=True)
print ("Section 1 Question 11 #2 (Take Photos) Median: ")
print(sec1q11_2_Median)
sec1q11_2Mean = new_df['sec1_q11_2'].mean(numeric_only=True)
print ("Section 1 Question 11 #2 Mean: ")
print (sec1q11_2Mean)
res = stats.ttest_ind(new_df['sec1_q11_2'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 11 #3
new_df = hpvdata[hpvdata['sec1_q11_3'] != -999]
sec1q11_3Median = new_df['sec1_q11_3'].median(numeric_only=True)
print ("Section 1 Question 11 #3 (Receive and send SMS with Photos) Median: ")
print(sec1q11_3Median)
sec1q11_3Mean = new_df['sec1_q11_3'].mean(numeric_only=True)
print ("Section 1 Question 11 #3 Mean: ")
print (sec1q11_3Mean)
res = stats.ttest_ind(new_df['sec1_q11_3'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 11 #4
new_df = hpvdata[hpvdata['sec1_q11_4'] != -999]
sec1q11_4Median = new_df['sec1_q11_4'].median(numeric_only=True)
print ("Section 1 Question 11 #4 Median (Receive and send money (banking)): ")
print(sec1q11_4Median)
sec1q11_4Mean = new_df['sec1_q11_4'].mean(numeric_only=True)
print ("Section 1 Question 11 #4 Mean: ")
print (sec1q11_4Mean)
res = stats.ttest_ind(new_df['sec1_q11_4'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 11 #5
new_df = hpvdata[hpvdata['sec1_q11_5'] != -999]
sec1q11_5Median = new_df['sec1_q11_5'].median(numeric_only=True)
print ("Section 1 Question 11 #5 Median (Use Messaging Apps): ")
print(sec1q11_5Median)
sec1q11_5Mean = new_df['sec1_q11_5'].mean(numeric_only=True)
print ("Section 1 Question 11 #5 Mean: ")
print (sec1q11_5Mean)
res = stats.ttest_ind(new_df['sec1_q11_5'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 11 #6
new_df = hpvdata[hpvdata['sec1_q11_6'] != -999]
sec1q11_6Median = new_df['sec1_q11_6'].median(numeric_only=True)
print ("Section 1 Question 11 #6 Median (Use Social Media Apps): ")
print(sec1q11_6Median)
sec1q11_6Mean = new_df['sec1_q11_6'].mean(numeric_only=True)
print ("Section 1 Question 11 #6 Mean: ")
print (sec1q11_6Mean)
res = stats.ttest_ind(new_df['sec1_q11_6'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 11 #7
new_df = hpvdata[hpvdata['sec1_q11_7'] != -999]
sec1q11_7Median = new_df['sec1_q11_7'].median(numeric_only=True)
print ("Section 1 Question 11 #7 Median (Watch Videos): ")
print(sec1q11_7Median)
sec1q11_7Mean = new_df['sec1_q11_7'].mean(numeric_only=True)
print ("Section 1 Question 11 #7 Mean: ")
print (sec1q11_7Mean)
res = stats.ttest_ind(new_df['sec1_q11_7'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")

#Section 1 Question 11 #8
new_df = hpvdata[hpvdata['sec1_q11_8'] != -999]
sec1q11_8Median = new_df['sec1_q11_8'].median(numeric_only=True)
print ("Section 1 Question 11 #8 Median (Listen to an Audio File/Recording): ")
print(sec1q11_8Median)
sec1q11_8Mean = new_df['sec1_q11_8'].mean(numeric_only=True)
print ("Section 1 Question 11 #8 Mean: ")
print (sec1q11_8Mean)
res = stats.ttest_ind(new_df['sec1_q11_8'], new_df['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #syntax for t-test
print (res)
print ("\n")