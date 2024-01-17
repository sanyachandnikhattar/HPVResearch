import matplotlib.pyplot as plt #use anaconda environment to get this to work
import numpy as np
import pandas as pd #importing pandas library
from scipy.stats import ttest_ind #ttest
import scipy.stats as stats
from tabulate import tabulate #for tables
#hi

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
#equal variance depends on personal opinion — is variance small or variance large --> if under 1 of difference, variance not that large
#keep rules consistent throughout analysis: if differentiating by decimal place, keep that throughout
res = stats.ttest_ind(Group1Male['HPV_VAX_attitu_s35'].dropna(), Group2Female['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #syntax for t-test
print (res)
#print (res.pvalue)
print ("\n")

Flag = True
#if abs(np.var(Group1Male)-np.var(Group2Female))>1: #threshold is 1
# Flag = False

#Section 1 Question 5 Questions 1, 2, 3, 4
new_df = hpvdata[hpvdata['sec1_q5'] != -999]

sec1q5Median = new_df['sec1_q5'].median(numeric_only=True)
print ("Section 1 Question 5 Median: ")
print(sec1q5Median)
sec1q5Mean = new_df['sec1_q5'].mean(numeric_only=True)
print ("Section 1 Question 5 Mean: ")
print (sec1q5Mean)
print ("\n")
print(new_df['sec1_q5'].value_counts())
print ("\n")
Group1 = new_df[new_df['sec1_q5']==1]
Group2 = new_df[new_df['sec1_q5']==2]
Group3 = new_df[new_df['sec1_q5']==3]
Group4 = new_df[new_df['sec1_q5']==4]
print (np.nanvar(Group1['HPV_VAX_attitu_s35'])) #36.05705497885428
print (np.nanvar(Group2['HPV_VAX_attitu_s35'])) #35.024184117687525
print (np.nanvar(Group3['HPV_VAX_attitu_s35'])) #40.3724509220702
print (np.nanvar(Group4['HPV_VAX_attitu_s35'])) #31.504805843906187
#run 6 t-tests: 1 and 2, 1 and 3, 1 and 4, 2 and 3, 2 and 4, 3 and 4 --> Upper Triangular Matrix
res2 = stats.ttest_ind(Group1['HPV_VAX_attitu_s35'].dropna(), Group2['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 2
res3 = stats.ttest_ind(Group1['HPV_VAX_attitu_s35'].dropna(), Group3['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 3
res4 = stats.ttest_ind(Group1['HPV_VAX_attitu_s35'].dropna(), Group4['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 4
res2_3 = stats.ttest_ind(Group2['HPV_VAX_attitu_s35'].dropna(), Group3['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 3
res2_4 = stats.ttest_ind(Group2['HPV_VAX_attitu_s35'].dropna(), Group4['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 4
res3_4 = stats.ttest_ind(Group3['HPV_VAX_attitu_s35'].dropna(), Group4['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 4
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
print ("\n")
print(new_df['sec1_q6'].value_counts())
print ("\n")
#needs multiple t-tests
Group1q6 = new_df[new_df['sec1_q6']==1] #full-time
Group2q6 = new_df[new_df['sec1_q6']==2] #part-time
Group3q6 = new_df[new_df['sec1_q6']==3] #casual laborer
Group4q6 = new_df[new_df['sec1_q6']==4] #self-employed
Group5q6 = new_df[new_df['sec1_q6']==5] #looking for work
Group6q6 = new_df[new_df['sec1_q6']==6] #not employed, not looking for work

#Finding Variance
print (np.nanvar(Group1q6['HPV_VAX_attitu_s35'])) #36.952036651395254
print (np.nanvar(Group2q6['HPV_VAX_attitu_s35'])) #34.5146484375
print (np.nanvar(Group3q6['HPV_VAX_attitu_s35'])) #42.3069617941412
print (np.nanvar(Group4q6['HPV_VAX_attitu_s35'])) #38.17392045454546
print (np.nanvar(Group5q6['HPV_VAX_attitu_s35'])) #37.422335600907026
print (np.nanvar(Group6q6['HPV_VAX_attitu_s35'])) #33.630232096806175

#Printing the T-Tests of All S1Q6 Questions Against One Another
res2 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group2q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 2
res3 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group3q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 3
res4 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group4q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 4
res5 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group5q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 1 against 5
res6 = stats.ttest_ind(Group1q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 6
res2_3 = stats.ttest_ind(Group2q6['HPV_VAX_attitu_s35'].dropna(), Group3q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 3
res2_4 = stats.ttest_ind(Group2q6['HPV_VAX_attitu_s35'].dropna(), Group4q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 4
res2_5 = stats.ttest_ind(Group2q6['HPV_VAX_attitu_s35'].dropna(), Group5q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 5
res2_6 = stats.ttest_ind(Group2q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 2 against 6
res3_4 = stats.ttest_ind(Group3q6['HPV_VAX_attitu_s35'].dropna(), Group4q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 4
res3_5 = stats.ttest_ind(Group3q6['HPV_VAX_attitu_s35'].dropna(), Group5q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 5
res3_6 = stats.ttest_ind(Group3q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 6
res4_5 = stats.ttest_ind(Group4q6['HPV_VAX_attitu_s35'].dropna(), Group5q6['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 4 against 5
res4_6 = stats.ttest_ind(Group4q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 4 against 6
res5_6 = stats.ttest_ind(Group5q6['HPV_VAX_attitu_s35'].dropna(), Group6q6['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 5 against 6
print (res2)
print ("\n")
print (res3)
print ("\n")
print (res4)
print ("\n")
print (res5)
print ("\n")
print (res6)
print ("\n")
print (res2_3)
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
print ("\n") #space before looking at value counts + variance
print (new_df['sec1_q7'].value_counts())
print ("\n")
Group1q7 = new_df[new_df['sec1_q7']==1] #single
Group2q7 = new_df[new_df['sec1_q7']==2] #cohabitating
Group3q7 = new_df[new_df['sec1_q7']==3] #married
Group4q7 = new_df[new_df['sec1_q7']==4] #widowed
Group5q7 = new_df[new_df['sec1_q7']==5] #divorced/separated
print (np.nanvar(Group1q7['HPV_VAX_attitu_s35'])) #36.10735532720389
print (np.nanvar(Group2q7['HPV_VAX_attitu_s35'])) #12.666666666666666
print (np.nanvar(Group3q7['HPV_VAX_attitu_s35'])) #38.21758692517224
print (np.nanvar(Group4q7['HPV_VAX_attitu_s35'])) #45.625
print (np.nanvar(Group5q7['HPV_VAX_attitu_s35'])) #32.13811728395061
res2 = stats.ttest_ind(Group1q7['HPV_VAX_attitu_s35'].dropna(), Group2q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 2
res3 = stats.ttest_ind(Group1q7['HPV_VAX_attitu_s35'].dropna(), Group3q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 3
res4 = stats.ttest_ind(Group1q7['HPV_VAX_attitu_s35'].dropna(), Group4q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 4
res5 = stats.ttest_ind(Group1q7['HPV_VAX_attitu_s35'].dropna(), Group5q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 5
res2_3 = stats.ttest_ind(Group2q7['HPV_VAX_attitu_s35'].dropna(), Group3q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 3
res2_4 = stats.ttest_ind(Group2q7['HPV_VAX_attitu_s35'].dropna(), Group4q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 4
res2_5 = stats.ttest_ind(Group2q7['HPV_VAX_attitu_s35'].dropna(), Group5q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 5
res3_4 = stats.ttest_ind(Group3q7['HPV_VAX_attitu_s35'].dropna(), Group4q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 4
res3_5 = stats.ttest_ind(Group3q7['HPV_VAX_attitu_s35'].dropna(), Group5q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 5
res4_5 = stats.ttest_ind(Group4q7['HPV_VAX_attitu_s35'].dropna(), Group5q7['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 4 against 5
print (res2)
print ("\n")
print (res3)
print ("\n")
print (res4)
print ("\n")
print (res5)
print ("\n")
print (res2_3)
print ("\n")
print (res2_4)
print ("\n")
print (res2_5)
print ("\n")
print (res3_4)
print ("\n")
print (res3_5)
print ("\n")
print (res4_5)
print ("\n")

#Section 1 Question 8
new_df = hpvdata[hpvdata['sec1_q8'] != -999]
sec1q8Median = new_df['sec1_q8'].median(numeric_only=True)
print ("Section 1 Question 8 Median: ")
print(sec1q8Median)
sec1q8Mean = new_df['sec1_q8'].mean(numeric_only=True) #exclude negative values with new_df
print ("Section 1 Question 8 Mean: ")
print (sec1q8Mean)
print ("\n") #space before looking at value counts + variance
print (new_df['sec1_q8'].value_counts())
print ("\n")
Group1q8 = new_df[new_df['sec1_q8']==1] #allowed savings
Group2q8 = new_df[new_df['sec1_q8']==2] #little savings
Group3q8 = new_df[new_df['sec1_q8']==3] #only met savings
Group4q8 = new_df[new_df['sec1_q8']==4] #insufficient
Group5q8 = new_df[new_df['sec1_q8']==5] #really insufficient
print (np.nanvar(Group1q8['HPV_VAX_attitu_s35'])) #43.95061728395062
print (np.nanvar(Group2q8['HPV_VAX_attitu_s35'])) #43.09061224489796
print (np.nanvar(Group3q8['HPV_VAX_attitu_s35'])) #36.79488990279706
print (np.nanvar(Group4q8['HPV_VAX_attitu_s35'])) #39.85220310085779
print (np.nanvar(Group5q8['HPV_VAX_attitu_s35'])) #35.6592923553719
res2 = stats.ttest_ind(Group1q8['HPV_VAX_attitu_s35'].dropna(), Group2q8['HPV_VAX_attitu_s35'].dropna(), equal_var = True) #group 1 against 2
res3 = stats.ttest_ind(Group1q8['HPV_VAX_attitu_s35'].dropna(), Group3q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 3
res4 = stats.ttest_ind(Group1q8['HPV_VAX_attitu_s35'].dropna(), Group4q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 4
res5 = stats.ttest_ind(Group1q8['HPV_VAX_attitu_s35'].dropna(), Group5q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 5
res2_3 = stats.ttest_ind(Group2q8['HPV_VAX_attitu_s35'].dropna(), Group3q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 3
res2_4 = stats.ttest_ind(Group2q8['HPV_VAX_attitu_s35'].dropna(), Group4q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 4
res2_5 = stats.ttest_ind(Group2q8['HPV_VAX_attitu_s35'].dropna(), Group5q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 5
res3_4 = stats.ttest_ind(Group3q8['HPV_VAX_attitu_s35'].dropna(), Group4q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 4
res3_5 = stats.ttest_ind(Group3q8['HPV_VAX_attitu_s35'].dropna(), Group5q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 5
res4_5 = stats.ttest_ind(Group4q8['HPV_VAX_attitu_s35'].dropna(), Group5q8['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 3 against 5
print (res2)
print ("\n")
print (res3)
print ("\n")
print (res4)
print ("\n")
print (res5)
print ("\n")
print (res2_3)
print ("\n")
print (res2_4)
print ("\n")
print (res2_5)
print ("\n")
print (res3_4)
print ("\n")
print (res3_5)
print ("\n")
print (res4_5)
print ("\n")

#Section 1 Question 9
new_df = hpvdata[hpvdata['sec1_q9'] != -999]
sec1q9Median = new_df['sec1_q9'].median(numeric_only=True)
print ("Section 1 Question 9 Median: ")
print(sec1q9Median)
sec1q9Mean = new_df['sec1_q9'].mean(numeric_only=True) #data frame already initialized to exclude -999, so use new_df
print ("Section 1 Question 9 Mean: ")
print (sec1q9Mean)
Group1q9 = new_df[new_df['sec1_q9']==1] #city (urban)
Group2q9 = new_df[new_df['sec1_q8']==2] #trading center (town)
Group3q9 = new_df[new_df['sec1_q8']==3] #village (rural)
print ("\n")
print (new_df['sec1_q9'].value_counts()) #value counts for statistically significant pairings
print ("\n")
print (np.nanvar(Group1q9['HPV_VAX_attitu_s35'])) #41.31609977324263
print (np.nanvar(Group2q9['HPV_VAX_attitu_s35'])) #43.09061224489796
print (np.nanvar(Group3q9['HPV_VAX_attitu_s35'])) #36.79488990279706
print ("\n")
#none of the groups' variance absolute value differences <1, so equal variance false
res2 = stats.ttest_ind(Group1q9['HPV_VAX_attitu_s35'].dropna(), Group2q9['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 2
res3 = stats.ttest_ind(Group1q9['HPV_VAX_attitu_s35'].dropna(), Group3q9['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 1 against 3
res2_3 = stats.ttest_ind(Group2q9['HPV_VAX_attitu_s35'].dropna(), Group3q9['HPV_VAX_attitu_s35'].dropna(), equal_var = False) #group 2 against 3
print (res2)
print (res3)
print (res2_3)
print ("\n")

#Section 1 Question 10
new_df = hpvdata[hpvdata['sec1_q10'] != -999] #exclude -999 decline to answer
sec1q10Median = new_df['sec1_q10'].median(numeric_only=True)
print ("Section 1 Question 10 Median: ")
print(sec1q10Median)
sec1q10Mean = new_df['sec1_q10'].mean(numeric_only=True)
print ("Section 1 Question 10 Mean: ")
print (sec1q10Mean)
Group1q10 = new_df[new_df['sec1_q10']==1] #at home 
Group2q10 = new_df[new_df['sec1_q10']==2] #not at home
print ("\n")
print (new_df['sec1_q10'].value_counts())
print ("\n")
#getting variance to see if equal variance
print (np.nanvar(Group1q10['HPV_VAX_attitu_s35'])) #38.24462544423242
print (np.nanvar(Group2q10['HPV_VAX_attitu_s35'])) #37.75120628914195
#variance difference <1, so equal variance
print("\n")
res2 = stats.ttest_ind(Group1q10['HPV_VAX_attitu_s35'].dropna(), Group2q10['HPV_VAX_attitu_s35'].dropna(), equal_var=True) #group 1 against group 2
print (res2)
print ("\n")

#Section 1 Question 11 #1 — receiving and sending text-based SMS messages
#--> 2 Groups: No or Yes
new_df = hpvdata[hpvdata['sec1_q11_1'] != -999]
sec1q11_1Median = new_df['sec1_q11_1'].median(numeric_only=True)
print ("Section 1 Question 11 #1 (Receive and send SMS Messages) Median: ")
print(sec1q11_1Median)
sec1q11_1Mean = new_df['sec1_q11_1'].mean(numeric_only=True)
print ("Section 1 Question 11 #1 Mean: ")
print (sec1q11_1Mean)
print ("\n")
Group1q11_1 = new_df[new_df['sec1_q11_1'] == 0] #no, can't receive and send SMS
Group2q11_1 = new_df[new_df['sec1_q11_1'] == 1] #yes, can receive and send SMS
#checking variance to see what the setting should be for t-test
print (np.nanvar(Group1q11_1['HPV_VAX_attitu_s35'])) #21.950617283950617
print (np.nanvar(Group2q11_1['HPV_VAX_attitu_s35'])) #38.17871500822665
#variance not equal (>1 difference)
print ("\n")
res2 = stats.ttest_ind(Group1q11_1['HPV_VAX_attitu_s35'].dropna(), Group2q11_1['HPV_VAX_attitu_s35'].dropna(), equal_var=False)
#group 1 (no for sending text sms) against group 2 (yes for sending text sms)
print (res2) #statistically insignificant, p > 0.05
print ("\n")


#Section 1 Question 11 #2 — taking photos
new_df = hpvdata[hpvdata['sec1_q11_2'] != -999]
sec1q11_2_Median = new_df['sec1_q11_2'].median(numeric_only=True)
print ("Section 1 Question 11 #2 (Take Photos) Median: ")
print(sec1q11_2_Median)
sec1q11_2Mean = new_df['sec1_q11_2'].mean(numeric_only=True)
print ("Section 1 Question 11 #2 Mean: ")
print (sec1q11_2Mean)
print ("\n") #space between median/mean and variance values
print (new_df['sec1_q11_2'].value_counts())
print ("\n")
Group1q11_2 = new_df[new_df['sec1_q11_2'] == 0] #no, cannot take photos
Group2q11_2 = new_df[new_df['sec1_q11_2'] == 1] #yes, can take photos
#checking variance to verify what the equal variance settings should be
print (np.nanvar(Group1q11_2['HPV_VAX_attitu_s35'])) #34.71809917355372
print (np.nanvar(Group2q11_2['HPV_VAX_attitu_s35'])) #38.28651102994887
#variance not equal (>1 difference)
print ("\n")
res2 = stats.ttest_ind(Group1q11_2['HPV_VAX_attitu_s35'].dropna(), Group2q11_2['HPV_VAX_attitu_s35'].dropna(), equal_var=False)
#group 1 (cannot take photos) against group 2 (can take photos)
print (res2) #statistically significant, p < 0.05 (~0.02)
print ("\n")


#Section 1 Question 11 #3 — receiving and sending SMS with photos
new_df = hpvdata[hpvdata['sec1_q11_3'] != -999]
sec1q11_3Median = new_df['sec1_q11_3'].median(numeric_only=True)
print ("Section 1 Question 11 #3 (Receive and send SMS with Photos) Median: ")
print(sec1q11_3Median)
sec1q11_3Mean = new_df['sec1_q11_3'].mean(numeric_only=True)
print ("Section 1 Question 11 #3 Mean: ")
print (sec1q11_3Mean)
print ("\n")
Group1q11_3 = new_df[new_df['sec1_q11_3'] == 0] #no, cannot receive SMS with photos
Group2q11_3 = new_df[new_df['sec1_q11_3'] == 1] #yes, can receive SMS with photos
#checking variance
print (np.nanvar(Group1q11_3['HPV_VAX_attitu_s35'])) #35.7637109375
print (np.nanvar(Group2q11_3['HPV_VAX_attitu_s35'])) #38.49447706122449
#variance not equal (>1 difference)
print ("\n")
res2 = stats.ttest_ind(Group1q11_3['HPV_VAX_attitu_s35'].dropna(), Group2q11_3['HPV_VAX_attitu_s35'].dropna(), equal_var=False)
#group 1 (cannot send SMS with photos) against group 2 (can send SMS with photos)
print (res2) #statistically insignificant, p > 0.05 (~0.6)
print ("\n")

#Section 1 Question 11 #4 — mobile banking
new_df = hpvdata[hpvdata['sec1_q11_4'] != -999]
sec1q11_4Median = new_df['sec1_q11_4'].median(numeric_only=True)
print ("Section 1 Question 11 #4 Median (Receive and send money (banking)): ")
print(sec1q11_4Median)
sec1q11_4Mean = new_df['sec1_q11_4'].mean(numeric_only=True)
print ("Section 1 Question 11 #4 Mean: ")
print (sec1q11_4Mean)
print ("\n")
Group1q11_4 = new_df[new_df['sec1_q11_4'] == 0] #no, cannot do mobile banking
Group2q11_4 = new_df[new_df['sec1_q11_4'] == 1] #yes, can do mobile banking
#checking variance
print (np.nanvar(Group1q11_4['HPV_VAX_attitu_s35'])) #34.5701540274387
print (np.nanvar(Group2q11_4['HPV_VAX_attitu_s35'])) #38.488022988398505
#variance not equal (>1 difference)
#NOTICE: similar variance values in yes/no groups so far from sec1q11_2 to sec1q11_4 variance 
print ("\n")
res2 = stats.ttest_ind(Group1q11_4['HPV_VAX_attitu_s35'].dropna(), Group2q11_4['HPV_VAX_attitu_s35'].dropna(), equal_var=False)
#group 1 (cannot mobile bank) against group 2 (can mobile bank)
print (res2) #statistically insignificant, p > 0.05 (~0.67) (similar p-value to section 1 q11 _3)
print ("\n")

#Section 1 Question 11 #5 — Messaging Apps
new_df = hpvdata[hpvdata['sec1_q11_5'] != -999]
sec1q11_5Median = new_df['sec1_q11_5'].median(numeric_only=True)
print ("Section 1 Question 11 #5 Median (Use Messaging Apps): ")
print(sec1q11_5Median)
sec1q11_5Mean = new_df['sec1_q11_5'].mean(numeric_only=True)
print ("Section 1 Question 11 #5 Mean: ")
print (sec1q11_5Mean)
print ("\n")
print (new_df['sec1_q11_5'].value_counts())
print ("\n")
Group1q11_5 = new_df[new_df['sec1_q11_5'] == 0] #no, cannot use messaging apps
Group2q11_5 = new_df[new_df['sec1_q11_5'] == 1] #yes, can use messaging apps 
#checking variance
print (np.nanvar(Group1q11_5['HPV_VAX_attitu_s35'])) #32.79198799233994
print (np.nanvar(Group2q11_5['HPV_VAX_attitu_s35'])) #38.625317631935594
#variance not equal (~6 difference, >1 difference)
print ("\n")
res2 = stats.ttest_ind(Group1q11_5['HPV_VAX_attitu_s35'].dropna(), Group2q11_5['HPV_VAX_attitu_s35'].dropna(), equal_var=False)
#group 1 (cannot use messaging apps) against group 2 (can use messaging apps)
print (res2) #statistically significant (p ~= 0.007, p < 0.05)
print ("\n")

#Section 1 Question 11 #6 — Use Social Media Apps
new_df = hpvdata[hpvdata['sec1_q11_6'] != -999]
sec1q11_6Median = new_df['sec1_q11_6'].median(numeric_only=True)
print ("Section 1 Question 11 #6 Median (Use Social Media Apps): ")
print(sec1q11_6Median)
sec1q11_6Mean = new_df['sec1_q11_6'].mean(numeric_only=True)
print ("Section 1 Question 11 #6 Mean: ")
print (sec1q11_6Mean)
print ("\n")
print (new_df['sec1_q11_6'].value_counts())
print ("\n")
Group1q11_6 = new_df[new_df['sec1_q11_6'] == 0] #no, cannot use social media apps
Group2q11_6 = new_df[new_df['sec1_q11_6'] == 1] #yes, can use social media apps
#checking variance
print (np.nanvar(Group1q11_6['HPV_VAX_attitu_s35'])) #34.5155859375
print (np.nanvar(Group2q11_6['HPV_VAX_attitu_s35'])) #38.53278824489796
#variance not equal (~4 difference, >1 difference)
print ("\n")
res2 = stats.ttest_ind(Group1q11_6['HPV_VAX_attitu_s35'].dropna(), Group2q11_6['HPV_VAX_attitu_s35'].dropna(), equal_var=False)
#group 1 (cannot use social media apps) against group 2 (can use social media apps)
print (res2) #statistically significant (p ~=0.02, p < 0.05)
print ("\n")

#Section 1 Question 11 #7
new_df = hpvdata[hpvdata['sec1_q11_7'] != -999]
sec1q11_7Median = new_df['sec1_q11_7'].median(numeric_only=True)
print ("Section 1 Question 11 #7 Median (Watch Videos): ")
print(sec1q11_7Median)
sec1q11_7Mean = new_df['sec1_q11_7'].mean(numeric_only=True)
print ("Section 1 Question 11 #7 Mean: ")
print (sec1q11_7Mean)
print ("\n")
Group1q11_7 = new_df[new_df['sec1_q11_7'] == 0] #no, cannot watch videos
Group2q11_7 = new_df[new_df['sec1_q11_7'] == 1] #yes, can watch videos
#checking variance
print (np.nanvar(Group1q11_7['HPV_VAX_attitu_s35'])) #37.98615510204081
print (np.nanvar(Group2q11_7['HPV_VAX_attitu_s35'])) #38.04263250405625
#variance equal (~0.06 difference, <1 difference)
print ("\n")
res2 = stats.ttest_ind(Group1q11_7['HPV_VAX_attitu_s35'].dropna(), Group2q11_7['HPV_VAX_attitu_s35'].dropna(), equal_var = True)
#group 1 (cannot watch videos) against group 2 (can watch videos)
print (res2)
#0.25070767055934357 is p-value --> statistically insignificant (p>0.05)
print ("\n")

#Section 1 Question 11 #8
new_df = hpvdata[hpvdata['sec1_q11_8'] != -999]
sec1q11_8Median = new_df['sec1_q11_8'].median(numeric_only=True)
print ("Section 1 Question 11 #8 Median (Listen to an Audio File/Recording): ")
print(sec1q11_8Median)
sec1q11_8Mean = new_df['sec1_q11_8'].mean(numeric_only=True)
print ("Section 1 Question 11 #8 Mean: ")
print (sec1q11_8Mean)
print ("\n")
Group1q11_8 = new_df[new_df['sec1_q11_8'] == 0] #no, listen to audio files
Group2q11_8 = new_df[new_df['sec1_q11_8'] == 1] #yes, can listen to audio files
#checking variance
print (np.nanvar(Group1q11_8['HPV_VAX_attitu_s35'])) #34.52846880907372
print (np.nanvar(Group2q11_8['HPV_VAX_attitu_s35'])) #39.091738744647195
#variance not equal (difference ~=4.5, >1)
print ("\n")
res2 = stats.ttest_ind(Group1q11_8['HPV_VAX_attitu_s35'].dropna(), Group2q11_8['HPV_VAX_attitu_s35'].dropna(), equal_var = False)
#group 1 (cannot watch videos) against group 2 (can watch videos)
print (res2)
#0.7324055447568049 is p-value --> statistically insignificant (p>0.05)
print ("\n")
