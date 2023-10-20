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
res = stats.ttest_ind(hpvdata['sec1_q4'].dropna(), hpvdata['HPV_VAX_attitu_s35'].dropna(), equal_var = True)
print (res)
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
sec1q6Mean = hpvdata['sec1_q6'].mean(numeric_only=True) #check how to exclude negative value
print ("Section 1 Question 6 Mean: ")
print (sec1q6Mean)
print ("\n")

#Section 1 Question 7
new_df = hpvdata[hpvdata['sec1_q7'] != -999]
sec1q7Median = hpvdata['sec1_q7'].median(numeric_only=True)
print ("Section 1 Question 7 Median: ")
print(sec1q7Median)
sec1q7Mean = hpvdata['sec1_q7'].mean(numeric_only=True)
print ("Section 1 Question 7 Mean: ") #check how to exclude negative value
print (sec1q7Mean)
print ("\n")

#Section 1 Question 8
new_df = hpvdata[hpvdata['sec1_q8'] != -999]
sec1q8Median = hpvdata['sec1_q8'].median(numeric_only=True)
print ("Section 1 Question 8 Median: ")
print(sec1q8Median)
sec1q8Mean = hpvdata['sec1_q8'].mean(numeric_only=True) #check how to exclude negative value
print ("Section 1 Question 8 Mean: ")
print (sec1q8Mean)
print ("\n")

#Section 1 Question 9
new_df = hpvdata[hpvdata['sec1_q9'] != -999]
sec1q9Median = hpvdata['sec1_q9'].median(numeric_only=True)
print ("Section 1 Question 9 Median: ")
print(sec1q9Median)
sec1q9Mean = hpvdata['sec1_q9'].mean(numeric_only=True)
print ("Section 1 Question 9 Mean: ")
print (sec1q9Mean)
print ("\n")

#Section 1 Question 10
new_df = hpvdata[hpvdata['sec1_q10'] != -999]
sec1q10Median = hpvdata['sec1_q10'].median(numeric_only=True)
print ("Section 1 Question 10 Median: ")
print(sec1q10Median)
sec1q10Mean = hpvdata['sec1_q10'].mean(numeric_only=True)
print ("Section 1 Question 10 Mean: ")
print (sec1q10Mean)
print ("\n")

#Section 1 Question 11 #1
new_df = hpvdata[hpvdata['sec1_q11_1'] != -999]
sec1q11_1Median = hpvdata['sec1_q11_1'].median(numeric_only=True)
print ("Section 1 Question 11 #1 (Receive and send SMS Messages) Median: ")
print(sec1q11_1Median)
sec1q11_1Mean = hpvdata['sec1_q11_1'].mean(numeric_only=True)
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
sec1q11_3Mean = hpvdata['sec1_q11_3'].mean(numeric_only=True)
print ("Section 1 Question 11 #3 Mean: ")
print (sec1q11_3Mean)
print ("\n")

#Section 1 Question 11 #4
new_df = hpvdata[hpvdata['sec1_q11_4'] != -999]
sec1q11_4Median = hpvdata['sec1_q11_4'].median(numeric_only=True)
print ("Section 1 Question 11 #4 Median (Receive and send money (banking)): ")
print(sec1q11_4Median)
sec1q11_4Mean = hpvdata['sec1_q11_4'].mean(numeric_only=True)
print ("Section 1 Question 11 #4 Mean: ")
print (sec1q11_4Mean)
print ("\n")

#Section 1 Question 11 #5
new_df = hpvdata[hpvdata['sec1_q11_5'] != -999]
sec1q11_5Median = hpvdata['sec1_q11_5'].median(numeric_only=True)
print ("Section 1 Question 11 #5 Median (Use Messaging Apps): ")
print(sec1q11_5Median)
sec1q11_5Mean = hpvdata['sec1_q11_5'].mean(numeric_only=True)
print ("Section 1 Question 11 #5 Mean: ")
print (sec1q11_5Mean)
print ("\n")

#Section 1 Question 11 #6
new_df = hpvdata[hpvdata['sec1_q11_6'] != -999]
sec1q11_6Median = hpvdata['sec1_q11_6'].median(numeric_only=True)
print ("Section 1 Question 11 #6 Median (Use Social Media Apps): ")
print(sec1q11_6Median)
sec1q11_6Mean = hpvdata['sec1_q11_6'].mean(numeric_only=True)
print ("Section 1 Question 11 #6 Mean: ")
print (sec1q11_6Mean)
print ("\n")

#Section 1 Question 11 #7
new_df = hpvdata[hpvdata['sec1_q11_7'] != -999]
sec1q11_7Median = hpvdata['sec1_q11_7'].median(numeric_only=True)
print ("Section 1 Question 11 #7 Median (Watch Videos): ")
print(sec1q11_7Median)
sec1q11_7Mean = hpvdata['sec1_q11_7'].mean(numeric_only=True)
print ("Section 1 Question 11 #7 Mean: ")
print (sec1q11_7Mean)
print ("\n")

#Section 1 Question 11 #8
new_df = hpvdata[hpvdata['sec1_q11_8'] != -999]
sec1q11_8Median = hpvdata['sec1_q11_8'].median(numeric_only=True)
print ("Section 1 Question 11 #8 Median (Listen to an Audio File/Recording): ")
print(sec1q11_8Median)
sec1q11_8Mean = hpvdata['sec1_q11_8'].mean(numeric_only=True)
print ("Section 1 Question 11 #8 Mean: ")
print (sec1q11_8Mean)
print ("\n")

#histograms for binary variables and population
#section 1 question 4: male or female
plt.xlabel('Gender')
genderScale = ('Male', 'Female')
x_positions1q4 = [1, 2]
plt.xticks (x_positions1q4, genderScale)
plt.ylabel('Population')
plt.title('Distribution of Gender')
plt.hist(new_df['sec1_q4'], edgecolor = 'black')
plt.show()

#section 1 question 5: highest level of school completed
educationScale = ('Primary', 'Secondary', 'Higher', 'No School')
x_positions1q5 = [1, 2, 3, 4]
plt.xlabel ('Education Level Gradient')
plt.xticks(x_positions1q5, educationScale)
plt.ylabel ('Population')
plt.title ('Highest Level of School Completed')
plt.hist(new_df['sec1_q5'], edgecolor = 'black')
#ask what 1, 2, 3, 4 stands for to add labels later
plt.show()

#section 1 question 6: current employment status
new_df = hpvdata[hpvdata['sec1_q6']!= -999]
plt.hist(new_df['sec1_q6'], bins = 12, edgecolor = 'black')
employmentScale = ('Full-Time', 'Part-Time', 'Casual', 'Self-Employed', 'Searching', 'Not Searching')
x_positions1q6 = [1, 2, 3, 4, 5, 6]
plt.xlabel ('Gradient from Full-Time Employment to Unemployed')
plt.xticks (x_positions1q6, employmentScale)
plt.ylabel ('Population')
plt.title ('Current Employment Status')
#ask what 1, 2, 3, 4, 5, -999 stands to add labels later
plt.show()

#section 1 question 7: current marital status
#hpvdatasec1q7 = pd.read_csv('hpvdata.csv', usecols = ['sec1_q7'], low_memory = False)
new_df = hpvdata[hpvdata['sec1_q7'] != -999]
plt.hist(new_df['sec1_q7'], range=[1, 5], bins = 5, edgecolor = 'black')
#ask what 1, 3, 4, 5, -999 means to add labels later
maritalScale = ('Single', 'Cohabitating/Partnered', 'Married', 'Widowed', 'Divorced/Separated')
x_positions1q7 = [1, 2, 3, 4, 5]
plt.xlabel('Gradient from Single to Divorced/Separated')
plt.xticks(x_positions1q7, maritalScale)
plt.ylabel('Population')
plt.title('Current Marital Status')
plt.show()

#section 1 question 8: household income over the past 12 months
new_df = hpvdata[hpvdata['sec1_q8'] != -999]
plt.hist(new_df['sec1_q8'], range=[1, 5], bins = 10, edgecolor = 'black')
#ask what 1, 3, 4, 5, -999 means to add labels later
incomeScale = ('Significant Savings', 'Slight Savings', 'Met Expenses', 'Insufficient', 'Insufficient and Borrowing')
x_positions1q8 = [1, 2, 3, 4, 5]
plt.xlabel('Income Gradient')
plt.xticks(x_positions1q8, incomeScale)
plt.ylabel('Population')
plt.title('Household Income Over Past 12 Months')
plt.show()

#section 1 question 9: description of living area at present
new_df = hpvdata[hpvdata['sec1_q9'] != -999] #exclude -999 prefer not to answer
plt.hist(new_df['sec1_q9'], range = [1, 3], bins = 6, edgecolor = 'black')
residenceArea = ('City (urban)', 'Trading Center (town)', 'Village (rural)')
x_positions1q9 = [1, 2, 3]
plt.xlabel('Residence Gradient')
plt.xticks(x_positions1q9, residenceArea)
plt.ylabel ('Population')
plt.title ('Description of Living Area at Present')
plt.show()

#section 1 question 10: where are you now while doing this survey
new_df = hpvdata[hpvdata['sec1_q10'] != -999] #exclude -999 prefer not to answer
plt.hist(new_df['sec1_q10'], range = [1, 2], bins = 4, edgecolor = 'black')
homeBinary = ('I am at home right now', 'I am not at home right now')
x_positions1q10 = [1, 2]
plt.xlabel ('Location Binary')
plt.xticks(x_positions1q10, homeBinary)
plt.ylabel ('Population')
plt.title ('Location at Time of Interview')
plt.show()

#section 1 question 11, 1: can you send and receive sms messaging on your phone
new_df = hpvdata[hpvdata['sec1_q11_1'] != -999] #excluding both -999 
plt.hist (new_df['sec1_q11_1'], range = [0, 1], bins = 4, edgecolor = 'black')
phoneUsage1 = ('No', 'Yes') #0 is no, 1 is yes -->check
x_positions1q11_1 = [0, 1]
plt.xticks (x_positions1q11_1, phoneUsage1)
plt.ylabel ('Population')
plt.title ('I Can Use SMS Messaging to Send and Receive Texts')
plt.show()

#section 1 question 11, 2: can you take photos on your phone
new_df = hpvdata[hpvdata['sec1_q11_2'] != -999] #excluding both -999
#to exclude 888, make second data frame to exclude second value
plt.hist (new_df['sec1_q11_2'], range = [0, 1], bins = 4, edgecolor = 'black')
phoneUsage2 = ('No', 'Yes')
x_positions1q11_2 = [0, 1]
plt.xticks (x_positions1q11_2, phoneUsage2)
plt.ylabel ('Population')
plt.title ('I Can Use My Phone to Take Photos')
plt.show()

#section 1 question 11, 3: can you recieve and send SMS messages with photos
new_df = hpvdata[hpvdata['sec1_q11_3'] != -999] #excluding both -999
plt.hist (new_df['sec1_q11_1'], range = [0, 1], bins = 4, edgecolor = 'black')
phoneUsage3 = ('No', 'Yes')
x_positions1q11_3 = [0, 1]
plt.xticks (x_positions1q11_3, phoneUsage1)
plt.ylabel ('Population')
plt.title ('I can recieve and send SMS messages with photos')
plt.show()

#section 1 question 11, 4: can you recieve and send money (banking)
new_df = hpvdata[hpvdata['sec1_q11_4'] != -999] #excluding both -999
plt.hist (new_df['sec1_q11_1'], range = [0, 1], bins = 4, edgecolor = 'black')
phoneUsage4 = ('No', 'Yes')
x_positions1q11_4 = [0, 1]
plt.xticks (x_positions1q11_4, phoneUsage4)
plt.ylabel ('Population')
plt.title ('I can recieve and send money (banking)')
plt.show()

#section 1 question 11, 5: can you use messaging apps (WhatsApp, Facebook messenger)
new_df = hpvdata[hpvdata['sec1_q11_5'] != -999] #excluding both -999
plt.hist (new_df['sec1_q11_5'], range = [0, 1], bins = 4, edgecolor = 'black')
phoneUsage1 = ('No', 'Yes')
x_positions1q11_5 = [0, 1]
plt.xticks (x_positions1q11_5, phoneUsage1)
plt.ylabel ('Population')
plt.title ('I can use messaging apps (WhatsApp, Facebook Messenger)')
plt.show()


#section 1 question 11, 6: can you use social media apps (Facebook, Twitter, Instagram)
new_df = hpvdata[hpvdata['sec1_q11_6'] != -999] #excluding both -999
plt.hist (new_df['sec1_q11_6'], range = [0, 1], bins = 4, edgecolor = 'black')
phoneUsage1 = ('No', 'Yes')
x_positions1q11_6 = [0, 1]
plt.xticks (x_positions1q11_6, phoneUsage1)
plt.ylabel ('Population')
plt.title ('I can use social media apps (Facebook, Twitter, Instagram)')
plt.show()

#section 1 question 11, 7: can you watch videos such as on YouTube
new_df = hpvdata[hpvdata['sec1_q11_7'] != -999] #excluding both -999
plt.hist (new_df['sec1_q11_7'], range = [0, 1], bins = 4, edgecolor = 'black')
phoneUsage1 = ('No', 'Yes')
x_positions1q11_7 = [0, 1]
plt.xticks (x_positions1q11_7, phoneUsage1)
plt.ylabel ('Population')
plt.title ('I can watch videos on YouTube')
plt.show()

#section 1 question 11, 8: can you listen to an audio file/recording (music, podcast, etc.)
new_df = hpvdata[hpvdata['sec1_q11_8'] != -999] #excluding both -999
plt.hist (new_df['sec1_q11_8'], range = [0, 1], bins = 4, edgecolor = 'black')
phoneUsage1 = ('No', 'Yes')
x_positions1q11_8 = [0, 1]
plt.xticks (x_positions1q11_8, phoneUsage1)
plt.ylabel ('Population')
plt.title ('I can listen to an audio file/recording (music, podcast, etc.)')
plt.show()
#end of Weeks 2-3

