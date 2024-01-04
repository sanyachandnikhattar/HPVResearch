import matplotlib.pyplot as plt #use anaconda environment to get this to work
import numpy as np
import pandas as pd #importing a library

file_path = 'hpvdata.csv'
hpvdata = pd.read_csv(file_path, low_memory = False)
new_df = hpvdata

#Week 6
#comparing the section 1 questions with section 5 question 61: have you ever talked about hpv/cervical cancer vaccination with other parents

#Section 1 Question 4 No
new_df = hpvdata[hpvdata['sec1_q4'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude ['sec1_q4'], bins = 4, edgecolor = 'black')
genderOptionsLow = ('Male', 'Female')
x_positions1q4low = [1, 2]
plt.xlabel ('Gender Identity (Binary)')
plt.xticks (x_positions1q4low, genderOptionsLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Gender and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 4 Yes
new_df = hpvdata[hpvdata['sec1_q4'] != -999]
high_attitude=new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist(high_attitude ['sec1_q4'], bins = 4, edgecolor = 'black')
genderOptionsHigh = ('Male', 'Female')
x_positions1q4high = [1, 2]
plt.xlabel ('Gender Identity (Binary)')
plt.xticks (x_positions1q4high, genderOptionsHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Gender and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 5 No
new_df = hpvdata[hpvdata['sec1_q5'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude ['sec1_q5'], bins = 8, edgecolor = 'black')
educationScaleLow = ('Primary', 'Secondary', 'Higher', 'No School')
x_positions1q5low = [1, 2, 3, 4]
plt.xlabel ('Education Level')
plt.xticks (x_positions1q5low, educationScaleLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Education Level and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 5 Yes
new_df = hpvdata[hpvdata['sec1_q5'] != -999]
high_attitude=new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist(high_attitude ['sec1_q5'], bins = 8, edgecolor = 'black')
educationScaleHigh = ('Primary', 'Secondary', 'Higher', 'No School')
x_positions1q5high = [1, 2, 3, 4]
plt.xlabel ('Education Level')
plt.xticks (x_positions1q5high, educationScaleHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Education Level and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 6 No
new_df = hpvdata[hpvdata['sec1_q6']!= -999] #exclude -999 b/c skews distribution
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude ['sec1_q6'], bins = 12, edgecolor = 'black')
employmentScaleLow = ('Full-Time', 'Part-Time', 'Casual', 'Self-Employed', 'Searching', 'Not Searching')
x_positions1q6low = [1, 2, 3, 4, 5, 6]
plt.xlabel ('Gradient from Full-Time Employment to Unemployed')
plt.xticks (x_positions1q6low, employmentScaleLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Employment Status and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 6 Yes
new_df = hpvdata[hpvdata['sec1_q6'] != -999] #exclude -999 b/c skews distribution
high_attitude=new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist(high_attitude['sec1_q6'], bins = 12, edgecolor = 'black')
employmentScaleHigh = ('Full-Time', 'Part-Time', 'Casual', 'Self-Employed', 'Searching', 'Not Searching')
x_positions1q6high = [1, 2, 3, 4, 5, 6]
plt.xlabel ('Gradient from Full-Time Employment to Unemployed')
plt.xticks (x_positions1q6high, employmentScaleHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Employment Status and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 7 No
new_df = hpvdata[hpvdata['sec1_q7']!= -999] #exclude -999 b/c skews distribution
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude ['sec1_q7'], bins = 10, edgecolor = 'black')
maritalScaleLow = ('Single', 'Cohabitating/Partnered', 'Married', 'Widowed', 'Divorced/Separated')
x_positions1q7low = [1, 2, 3, 4, 5]
plt.xlabel('Marital Status')
plt.xticks(x_positions1q7low, maritalScaleLow)
plt.ylabel('Population of Lower s5q61 Score')
plt.title('Distribution of Marital Status and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 7 Yes
new_df = hpvdata[hpvdata['sec1_q7']!=-999] #exclude -999 b/c skews distribution
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist(high_attitude ['sec1_q7'], bins = 10, edgecolor = 'black')
maritalScaleHigh = ('Single', 'Cohabitating/Partnered', 'Married', 'Widowed', 'Divorced/Separated')
x_positions1q7high = [1, 2, 3, 4, 5]
plt.xlabel('Marital Status')
plt.xticks(x_positions1q7high, maritalScaleHigh)
plt.ylabel('Population of Higher s5q61 Score')
plt.title('Distribution of Marital Status and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 8 No
new_df = hpvdata[hpvdata['sec1_q8'] != -999] #exclude -999 b/c skews distribution
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude['sec1_q8'], bins = 10, edgecolor = 'black')
incomeScaleLow = ('Significant Savings', 'Slight Savings', 'Met Expenses', 'Insufficient', 'Insufficient and Borrowing')
x_positions1q8low = [1, 2, 3, 4, 5]
plt.xlabel('Household Income Over Past 12 Months')
plt.xticks(x_positions1q8low, incomeScaleLow)
plt.ylabel('Population of Lower s5q61 Score')
plt.title('Distribution of Past Year Income and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 8 Yes
new_df = hpvdata[hpvdata['sec1_q8']!=-999] #exclude -999 b/c skews distribution
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist(high_attitude['sec1_q8'], bins = 10, edgecolor = 'black')
incomeScaleHigh = ('Significant Savings', 'Slight Savings', 'Met Expenses', 'Insufficient', 'Insufficient and Borrowing')
x_positions1q8high = [1, 2, 3, 4, 5]
plt.xlabel('Household Income Over Past 12 Months')
plt.xticks(x_positions1q8high, incomeScaleHigh)
plt.ylabel('Population of Higher s5q61 Score')
plt.title('Distribution of Past Year Income and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 9 No
new_df = hpvdata[hpvdata['sec1_q9'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude['sec1_q9'], bins = 6, edgecolor = 'black')
residenceAreaLow = ('City (Urban)', 'Trading Center', 'Village (Rural)')
x_positions1q9low = [1, 2, 3]
plt.xlabel('Area of Residence')
plt.xticks(x_positions1q9low, residenceAreaLow)
plt.ylabel('Population of Lower s5q61 Score')
plt.title('Distribution of Residency and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 9 Yes
new_df = hpvdata[hpvdata['sec1_q9'] != -999] #don't need to exclude -999, isn't there
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist (high_attitude['sec1_q9'], bins = 6, edgecolor = 'black')
residenceAreaHigh = ('City (Urban)', 'Trading Center', 'Village (Rural)')
x_positions1q9high = [1, 2, 3]
plt.xlabel ('Area of Residence')
plt.xticks (x_positions1q9high, residenceAreaHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title('Distribution of Residency and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 10 No
new_df = hpvdata[hpvdata['sec1_q10'] != -999] #exclude -999, prefer not to answer
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist (low_attitude['sec1_q10'], bins = 4, edgecolor = 'black')
currentLocationLow = ('At Home', 'Not at Home Right Now')
x_positions1q10low = [1, 2]
plt.xlabel ('Current Location During Interview')
plt.xticks (x_positions1q10low, currentLocationLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Location and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 10 Yes
new_df = hpvdata[hpvdata['sec1_q10'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist (high_attitude['sec1_q10'], bins = 4, edgecolor = 'black')
currentLocationHigh = ('At Home', 'Not at Home Right Now')
x_positions1q10high = [1, 2]
plt.xlabel ('Current Location During Interview')
plt.xticks (x_positions1q10high, currentLocationHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Location and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #1 No
new_df = hpvdata[hpvdata['sec1_q11_1'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist (low_attitude['sec1_q11_1'], bins = 4, edgecolor = 'black')
SMSLow = ('No', 'Yes')
x_positions1q11_1_low = [0, 1]
plt.xlabel ('I can send and receive text-based SMS messages on my phone')
plt.xticks (x_positions1q11_1_low, SMSLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Text-Based SMS Confidence and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #1 Yes
new_df = hpvdata[hpvdata['sec1_q11_1'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist (high_attitude['sec1_q11_1'], bins = 4, edgecolor = 'black')
SMSHigh = ('No', 'Yes')
x_positions1q11_1_high = [0, 1]
plt.xlabel ('I can send and receive text-based SMS messages on my phone')
plt.xticks (x_positions1q11_1_high, SMSHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Text-Based SMS Confidence and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #2 No
new_df = hpvdata[hpvdata['sec1_q11_2'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist (low_attitude['sec1_q11_2'], bins = 4, edgecolor = 'black')
PhotosLow = ('No', 'Yes')
x_positions1q11_2_low = [0, 1]
plt.xlabel ('I can take photos on my phone')
plt.xticks (x_positions1q11_2_low, PhotosLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Phone Photography Proficiency and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #2 Yes
new_df = hpvdata[hpvdata['sec1_q11_2'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist (high_attitude['sec1_q11_2'], bins = 4, edgecolor = 'black')
PhotosHigh = ('No', 'Yes')
x_positions1q11_2_high = [0, 1]
plt.xlabel ('I can take photos on my phone')
plt.xticks (x_positions1q11_2_high, PhotosHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Phone Photography Proficiency and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()


#Section 1 Question 11 #3 No
new_df = hpvdata[hpvdata['sec1_q11_3'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist (low_attitude['sec1_q11_3'], bins = 4, edgecolor = 'black')
SMS2Low = ('No', 'Yes')
x_positions1q11_3_low = [0, 1]
plt.xlabel ('I can send and receive SMS messages with photos on my phone')
plt.xticks (x_positions1q11_3_low, SMS2Low)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Photo-Based SMS Proficiency and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #3 Yes
new_df = hpvdata[hpvdata['sec1_q11_3'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist (high_attitude['sec1_q11_3'], bins = 4, edgecolor = 'black')
SMS2High = ('No', 'Yes')
x_positions1q11_3_high = [0, 1]
plt.xlabel ('I can send and receive SMS messages with photos on my phone')
plt.xticks (x_positions1q11_3_high, SMS2High)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Photo-Based SMS Proficiency and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #4 No
new_df = hpvdata[hpvdata['sec1_q11_4'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist (low_attitude['sec1_q11_4'], bins = 4, edgecolor = 'black')
moneyLow = ('No', 'Yes')
x_positions1q11_4_low = [0, 1]
plt.xlabel ('I can send and receive money (banking)')
plt.xticks (x_positions1q11_4_low, moneyLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Mobile Banking Proficiency and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #4 Yes
new_df = hpvdata[hpvdata['sec1_q11_4'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist (high_attitude['sec1_q11_4'], bins = 4, edgecolor = 'black')
moneyHigh = ('No', 'Yes')
x_positions1q11_4_high = [0, 1]
plt.xlabel ('I can send and receive money (banking)')
plt.xticks (x_positions1q11_4_high, moneyHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Mobile Banking Proficiency and Increased Disccussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #5 No
new_df = hpvdata[hpvdata['sec1_q11_5'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist (low_attitude['sec1_q11_5'], bins = 4, edgecolor = 'black')
messagingAppsLow = ['No', 'Yes']
x_positions1q11_5_low = [0, 1]
plt.xlabel ('I can use messaging apps (Whatsapp, Facebook, Messenger, etc.)')
plt.xticks (x_positions1q11_5_low, messagingAppsLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Mobile Messaging App Proficiency and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #5 Yes
new_df = hpvdata[hpvdata['sec1_q11_5'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist (high_attitude['sec1_q11_5'], bins = 4, edgecolor = 'black')
messagingAppsHigh = ['No', 'Yes']
x_positions1q11_5_high = [0, 1]
plt.xlabel ('I can use messaging apps (Whatsapp, Facebook, Messenger, etc.)')
plt.xticks (x_positions1q11_5_high, messagingAppsHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Mobile Messaging App Proficiency and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #6 No
new_df = hpvdata[hpvdata['sec1_q11_6'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist (low_attitude['sec1_q11_6'], bins = 4, edgecolor = 'black')
socialMediaAppsLow = ['No', 'Yes']
x_positions1q11_6_low = [0, 1]
plt.xlabel ('I can use social media apps (Facebook, Twitter, Instagram, etc.)')
plt.xticks (x_positions1q11_6_low, socialMediaAppsLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Mobile Social Media App Proficiency and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #6 Yes
new_df = hpvdata[hpvdata['sec1_q11_6'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist(high_attitude['sec1_q11_6'], bins = 4, edgecolor = 'black')
socialMediaAppsHigh = ['No', 'Yes']
x_positions1q11_6_high = [0, 1]
plt.xlabel ('I can use social media apps (Facebook, Twitter, Instagram, etc.')
plt.xticks (x_positions1q11_6_high, socialMediaAppsHigh)
plt.ylabel ('Population of Higher s5q61 Score')
plt.title ('Distribution of Mobile Social Media App Proficiency and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()


#Section 1 Question 11 #7 No
new_df = hpvdata[hpvdata['sec1_q11_7'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude['sec1_q11_7'], bins = 4, edgecolor = 'black')
youTubeLow = ['No', 'Yes']
x_positions1q11_7_low = [0, 1]
plt.xlabel ('I can watch videos e.g. on Youtube')
plt.xticks (x_positions1q11_7_low, youTubeLow)
plt.ylabel ('Population of Lower s5q61 Score')
plt.title ('Distribution of Mobile Video App Proficiency and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #7 Yes
new_df = hpvdata[hpvdata['sec1_q11_7'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude['sec1_q11_7'], bins = 4, edgecolor = 'black')
youTubeHigh = ['No', 'Yes']
x_positions1q11_7_high = [0, 1]
plt.xlabel ('I can watch videos e.g. on Youtube')
plt.xticks (x_positions1q11_7_high, youTubeHigh)
plt.ylabel ('Population of Higher S35 Score')
plt.title ('Distribution of Mobile Video App Proficiency and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #8 No
new_df = hpvdata[hpvdata['sec1_q11_8'] != -999]
low_attitude=new_df[new_df['sec5_q61']<=np.nanmedian(new_df['sec5_q61'])]
plt.hist(low_attitude['sec1_q11_8'], bins = 4, edgecolor = 'black')
audioFileLow = ['No', 'Yes']
x_positions1q11_8_low = [0, 1]
plt.xlabel ('I can listen to an audio file/recording (music, podcast, etc.)')
plt.xticks (x_positions1q11_8_low, audioFileLow)
plt.ylabel ('Population of Lower S35 Score')
plt.title ('Distribution of Mobile Audio File Proficiency and Decreased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()

#Section 1 Question 11 #8 Yes
new_df = hpvdata[hpvdata['sec1_q11_8'] != -999]
high_attitude = new_df[new_df['sec5_q61']>np.nanmedian(new_df['sec5_q61'])]
plt.hist(high_attitude['sec1_q11_8'], bins = 4, edgecolor = 'black')
audioFileHigh = ['No', 'Yes']
x_positions1q11_8_high = [0, 1]
plt.xlabel ('I can listen to an audio file/recording (music, podcast, etc.)')
plt.xticks (x_positions1q11_8_high, audioFileHigh)
plt.ylabel ('Population of Higher S35 Score')
plt.title ('Distribution of Mobile Audio File Proficiency and Increased Discussion About Cervical Cancer/HPV Vaccination with Other Parents')
plt.show()
#End of Week 6
