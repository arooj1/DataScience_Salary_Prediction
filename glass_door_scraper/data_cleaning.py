# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:43:16 2020

@author: quresa9
"""

import pandas as pd
# read both datasets
df1 = pd.read_csv('glassdoor.csv')
df2 = pd.read_csv('glassdoor_canada.csv')

## Join both datasets
df = pd.concat([df1,df2])


# Remove columns with complete b-1 values : Competitors, Headquarters  
# Remove unwanted columns with complete -1 values

df = df.drop(['Competitors', 'Headquarters'], axis = 1)

'''
Salary parsing
    - Remove all rows with 'Salary Estimate' == '-1'.
    - Remove text '(Glassdoor estimate)'
    - Replace CA$, K with a blank space
    - 'per hour' make a separate column 
    - 'CAD to US $' make a separate column
    - extract min , max and average salary. Make sure the data type of these columns is 'integer'
    
 '''
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
salary_minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$',''))

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['currency'] = df['Salary Estimate'].apply(lambda x: 'CAD' if 'ca' in x.lower() else 'US')
df['employer_provided' ] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary;' in x.lower() else 0)

min_hr = salary_minus_Kd.apply(lambda x: x.lower().replace('ca','').replace('per hour','').replace('employer provided salary',''))
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['average_salary'] = (df.min_salary+df.max_salary)/2


# company name [text only]
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1 )


# State field [1] if Currency == 'US', otherwise [0] (It belongs to Canada as we just have two currencies). 
df['job_region-state'] = df.apply(lambda x: x['Location'] if x['currency'] == 'CAD' else x['Location'].split(',')[1], axis = 1)
df['job_region-state'].value_counts()


#age of the company
df['age'] = df['Founded'].apply(lambda x: x if x <0 else 2020 - x)

#parsing of job description (python, etc.)
# python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

# R studio
df['r_studio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

# SQL
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() or 'mysql' in x.lower() else 0)

# Cloud 
df['cloud_yn'] = df['Job Description'].apply(lambda x: 1 if 'Google Cloud Platform' in x.lower() or 'GCP' in x.lower()  or 'aws' in x.lower() or 'azure' in x.lower() else 0)
df['cloud_yn'].value_counts()

# Excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() in x.lower() else 0)
# BigQuery
df['bigquery_yn'] = df['Job Description'].apply(lambda x: 1 if 'bigquery' in x.lower() in x.lower() else 0)
# Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv', index=False)

#pd.read_csv('salary_data_cleaned.csv')