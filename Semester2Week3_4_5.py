import matplotlib.pyplot as plt #use anaconda environment to get this to work
import numpy as np
import pandas as pd #importing pandas library
from scipy.stats import ttest_ind #ttest
import scipy.stats as stats
from tabulate import tabulate #for tables
#hi

file_path = 'hpvdata.csv'
hpvdata = pd.read_csv(file_path, low_memory = False)
hpvdata = hpvdata.dropna(subset=['HPV_VAX_attitu_s35']) #to debyg
hpvdata.describe()
new_df = hpvdata

print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'],hpvdata['sec1_q4']))
#pseudocode: section 1 question 4 correlation against HPV VAX attitu s35
#x = np.arange(len(new_df['sec1q_4'])) 
#error 
#Traceback (most recent call last.. KeyError: 'sec1q_4' --> how to fix? 


#Beginning of Week 2 Work
#Correlation Analysis:
#   for loop against all: 
#       1. Section 1 Questions (DONE)
#       2. Section 6 Questions
#       3. Section 8 Questions
#       4. Section 11 Questions
#**find top 10 variables with highest correlation to HPV VAX ATTITU s35**

#how do we deal with NaN
#how do we automate

#for (sec1q4 --> sec1q11_8)

#sec1q5
#hpvdata_cleaned = hpvdata.dropna()
#x = np.arange(len(new_df['sec1_q5']))
#print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q5'].dropna())) #how do we drop nan?
#method 1: column numbers in array, iterate over array/list
#method 2: automatically get the data frame everytime you are going through the CSV file 
# y should be the section 1 question 4 relative to HPV VAX ATTITU s35

#sec1q6
#x = np.arange(len(new_df['sec1_q6'])) #length because pandas wants to deal with a singular(?) amount
#np.set_printoptions(precision=8)
#print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q6']))

#sec1q7
#new_df = hpvdata[hpvdata['sec1_q7'] != -999]
#print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q7'])) 
#why still printing nan? don't see nan in the csv file


# Replace -999 with NaN in the 'sec1_q7' column
#hpvdata['sec1_q7'].replace(-999, np.nan, inplace=True)
# Drop rows with NaN values in 'sec1_q7'
#hpvdata_cleaned = hpvdata.dropna(subset=['sec1_q7'])
# Calculate correlation coefficient
#correlation = np.corrcoef(hpvdata_cleaned['HPV_VAX_attitu_s35'], hpvdata_cleaned['sec1_q7'])
#print(correlation)


# Convert NaN values to a string with desired precision
#correlation_str = np.array_str(correlation, precision=4)
#print(correlation_str)

#sec1q8
x = np.arange(len(new_df['sec1_q8']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q8'].dropna()))

#sec1q9
x = np.arange(len(new_df['sec1_q9']))
print(np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q9']))

#sec1q10
x = np.arange(len(new_df['sec1_q10']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q10']))

#sec1q11_1
x = np.arange(len(new_df['sec1_q11_1']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_1']))

#sec1q11_2
x = np.arange(len(new_df['sec1_q11_2']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_2']))

#sec1q11_3
x = np.arange(len(new_df['sec1_q11_3']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_3']))

#sec1q11_4
x = np.arange(len(new_df['sec1_q11_4']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_4']))

#sec1q11_5
x = np.arange(len(new_df['sec1_q11_5']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_5']))

#sec1q11_6
x = np.arange(len(new_df['sec1_q11_6']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_6']))

#sec1q11_7
x = np.arange(len(new_df['sec1_q11_7']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_7']))

#sec1q11_8
x = np.arange(len(new_df['sec1_q11_8']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_8']))

#2 1's in matrix: correlation of variable with itself
#value on diagonal: correlation between a and b = correlation between b and a
#value close to 0 --> no correlation; closer to 1: high positive correlation
#close to -1: high negative correlation