import matplotlib.pyplot as plt #use anaconda environment to get this to work
import numpy as np
import pandas as pd #importing pandas library
from scipy.stats import ttest_ind #ttest
import scipy.stats as stats

file_path = 'hpvdata.csv'
hpvdata = pd.read_csv(file_path, low_memory = False)
hpvdata = hpvdata.dropna(subset=['HPV_VAX_attitu_s35', 'sec6_q67', 'sec8_q89', 'sec11_q156', 'sec11_q157', 'sec11_q160']) #to debug
#excluding the correlation analysis for: (1) sec11_q170, sec11_q159
hpvdata.describe()
new_df = hpvdata

#Correlation Analysis:
#   for loop against all: 
#       1. Section 1 Questions (DONE)
#       2. Section 6 Questions (DONE)
#       3. Section 8 Questions (DONE)
#       4. Section 11 Questions (DONE)
#**find top 10 variables with highest correlation to HPV VAX ATTITU s35**

#how do we deal with NaN
#how do we automate

#for (sec1q4 --> sec1q11_8)
print ("Section 1 Questions")
#sec1q4
x = np.arange(len(new_df['sec1_q4']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q4'].dropna()))
print ("\n")

#sec1q5
x = np.arange(len(new_df['sec1_q5']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q5'].dropna()))
print ("\n")

#sec1q6
x = np.arange(len(new_df['sec1_q6']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q6'].dropna()))
print ("\n")

#sec1q7
print ("sec1q7, MISSED")
x = np.arange(len(new_df['sec1_q7']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q7'].dropna()))
print ("\n")

#sec1q8
x = np.arange(len(new_df['sec1_q8']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q8'].dropna()))
print ("\n")

#sec1q9
x = np.arange(len(new_df['sec1_q9']))
print(np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q9']))
print ("\n")

#sec1q10
x = np.arange(len(new_df['sec1_q10']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q10']))
print ("\n")

#sec1q11_1
x = np.arange(len(new_df['sec1_q11_1']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_1']))
print ("\n")

#sec1q11_2
x = np.arange(len(new_df['sec1_q11_2']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_2']))
print ("\n")

#sec1q11_3
x = np.arange(len(new_df['sec1_q11_3']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_3']))
print ("\n")

#sec1q11_4
x = np.arange(len(new_df['sec1_q11_4']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_4']))
print ("\n")

#sec1q11_5
x = np.arange(len(new_df['sec1_q11_5']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_5']))
print ("\n")

#sec1q11_6
x = np.arange(len(new_df['sec1_q11_6']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_6']))
print ("\n")

#sec1q11_7
x = np.arange(len(new_df['sec1_q11_7']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_7']))
print ("\n")

#sec1q11_8
x = np.arange(len(new_df['sec1_q11_8']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec1_q11_8']))
print ("\n")

#2 1's in matrix: correlation of variable with itself
#value on diagonal: correlation between a and b = correlation between b and a
#value close to 0 --> no correlation; closer to 1: high positive correlation
#close to -1: high negative correlation

#for (sec6_q67 --> sec6_q76)
#note: sec6_q67 --> sec6_q74 one section, sec6_q75 --> sec6_q76 second section


print ("Section 6 Questions:") #showing nan again

#sec6_q67
x = np.arange(len(new_df['sec6_q67']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q67']))
print ("\n")

#sec6_q68
x = np.arange(len(new_df['sec6_q68']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q68']))
print ("\n")

#sec6_q69
x = np.arange(len(new_df['sec6_q69']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q69']))
print ("\n")

#sec6_q70
x = np.arange(len(new_df['sec6_q70']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q70']))
print ("\n")

#sec6_q71
x = np.arange(len(new_df['sec6_q71']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q71']))
print ("\n")

#sec6_q72
x = np.arange(len(new_df['sec6_q72']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q72']))
print ("\n")

#sec6_q73
x = np.arange(len(new_df['sec6_q73']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q73'])) #typo
print ("\n")

#sec6_q74
x = np.arange(len(new_df['sec6_q74']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q74']))
print ("\n")
print ("\n")
#end of group in baseline spreadsheet

#sec6_q75
x = np.arange(len(new_df['sec6_q75']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q75']))
print ("\n")

#sec6_q76
x = np.arange(len(new_df['sec6_q75']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec6_q76']))
print ("\n")
print ("\n")

#section 8 questions — sec8q89 --> sec8q93
print ("Section 8 Questions")
x = np.arange(len(new_df['sec8_q89']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec8_q89']))
print ("\n")

x = np.arange(len(new_df['sec8_q90']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec8_q90']))
print ("\n")

x = np.arange(len(new_df['sec8_q91']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec8_q91']))
print ("\n")

x = np.arange(len(new_df['sec8_q92']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec8_q92']))
print ("\n")

x = np.arange(len(new_df['sec8_q93']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec8_q93']))
print ("\n")

#section 11 questions - sec11q156 --> sec11q170
print ("Section 11 Questions")
x = np.arange(len(new_df['sec11_q156']))
print (len(new_df['sec11_q156']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec11_q156']))
print ("\n")

x = np.arange(len(new_df['sec11_q157']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec11_q157']))
print ("\n")

x = np.arange(len(new_df['sec11_q158']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec11_q158']))
print ("\n")

x = np.arange(len(new_df['sec11_q159']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec11_q159']))
print ("\n")

# COVID QUESTIONS — LAST TWO QUESTIONS IN SURVEY
x = np.arange(len(new_df['sec11_q160']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec11_q160']))
print ("\n")

x = np.arange(len(new_df['sec11_q170']))
print (np.corrcoef(hpvdata['HPV_VAX_attitu_s35'], hpvdata['sec11_q170']))
print ("\n")
#note: sec11_q160, sec11_q170 are COVID sections

print (len(hpvdata)) #1032 , then 1017