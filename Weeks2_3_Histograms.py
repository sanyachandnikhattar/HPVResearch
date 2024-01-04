import matplotlib.pyplot as plt #use anaconda environment to get this to work
import numpy as np
import pandas as pd #importing a library

#Weeks 2-3
file_path = 'hpvdata.csv'
hpvdata = pd.read_csv(file_path, low_memory = False)
new_df = hpvdata

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