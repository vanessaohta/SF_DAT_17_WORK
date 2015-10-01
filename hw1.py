'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 9/30/2015
'''
#Vanessa's homework

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_17/master/hw/data/police-killings.csv')
killings.head()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race
killings.columns
killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace=True)

# 2. Show the count of missing values in each column
killings.isnull().sum() 

# 3. replace each null value in the dataframe with the string "Unknown"
killings.fillna(value='Unknown') 

# 4. How many killings were there so far in 2015?
killings.year.value_counts()

# 5. Of all killings, how many were male and how many female?
killings.gender.value_counts()

# 6. How many killings were of unarmed people?
killings.armed[killings.armed == 'No'].value_counts()

# 7. What percentage of all killings were unarmed?
killings.armed.value_counts() / killings.shape[0]

# 8. What are the 5 states with the most killings?
killings.state.value_counts(sort = True).head(5)

# 9. Show a value counts of deaths for each race
killings.race.value_counts()

# 10. Display a histogram of ages of all killings
killings.age.hist(bins=40)

# 11. Show 6 histograms of ages by race
killings.age.hist(by=killings.race, sharex=True, sharey=True)
print;
#need to label 

# 12. What is the average age of death by race?
killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month
killings.month_num = killings.month.replace({
        'January':1,
        'February':2,
        'March':3,
        'April':4,
        'May':5,
        'June':6
            })         
            
ax = killings.month_num.value_counts().sort_index().plot(kind='bar')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Police Killings')
print;

###################
### Less Morbid ###
###################

majors = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_17/master/hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)
del majors['Employed_full_time_year_round']
del majors['Major_code']
majors.columns

# 2. Show the count of missing values in each column
majors.isnull().sum()

# 3. What are the top 10 highest paying majors?
# Using the median as the indicator for pay 
top_ten_majors = majors.sort_index(by = 'Median', ascending=False).head(10) 
print top_ten_majors[['Major','Median']].sort_index(by = 'Median', ascending=False)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
top_ten_majors[['Major','Median']].sort_index(by = 'Median', ascending=False).plot(kind='bar', title = 'Top 10 Highest Paying Majors')
#I know this isn't labeled correctly but I couldn't get it before class today! I will fix it later!

print top_ten_majors['Major']

# 5. What is the average median salary for each major category?
majors.columns
majors.groupby('Major_category').Median.mean()

# 6. Show only the top 5 paying major categories
majors.groupby('Major_category').Median.mean().order(ascending = False).head(5)

# 7. Plot a histogram of the distribution of median salaries
majors.Median.hist(bins=40)

# 8. Plot a histogram of the distribution of median salaries by major category
majors.groupby('Major_category').Median.mean().hist()
#this is also wrong and Ineed to fix it sorry!!

# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?
majors[['Major','Unemployment_rate']].sort_index(by = 'Unemployment_rate', ascending=False).head(10)


# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?
majors.groupby('Major_category').Unemployment_rate.mean().order(ascending = False).head(10)

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the employment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042
majors[['Major','Total', 'Employed','Unemployment_rate']].head(10)
majors['sample_employment_rate'] = majors.Employed / majors.Total
majors[['Major','Total', 'Employed','sample_employment_rate']].head(10)

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
majors['sample_unemployment_rate'] = 1 - majors['sample_employment_rate']
majors[['Major','Total', 'Employed','sample_employment_rate', 'sample_unemployment_rate']].head(10)
