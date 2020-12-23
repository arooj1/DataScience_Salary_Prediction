# DATA SCIENCE SALARY ESTIMATOR PROJECT
## PURPOSE
The idea is to create a data science project from scratch. It will comprise of the following stages:

## CODE
- Python Version 3.7
- Packages: Pandas, Selenium, Matplotlib, Pickle, Numpy, Scikit-Learn, Flask
- For Web Framework: requirements.txt

## INSPIRATION
https://www.youtube.com/watch?v=fhi4dOhmW-g&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=3

## RESOURCES 
#### Data Acquisition
- https://github.com/arapfaik/scraping-glassdoor-selenium
- https://chromedriver.chromium.org/downloads  

#### Statistical Analysis 
- https://www.w3schools.com/datascience/ds_linear_regression_pvalue.asp 
#### Productionization
- https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Project Planning
Analyze salaries of **Data Scientists** across NORTH AMERICA using glassdoor data. 

### 1-Data Acquisition
A little twist. Instead of acquiring 1000 job data from the USA, I did 500 from the USA and 500 from Canada as Canada is my home country :)
#### Data Acquired
<List all columns>
#### Take Aways
There are a few steps to be careful of.
##### CHROME DRIVER
-	Chrome webdriver version. Make sure it is compatible with your system. 

-	In the code, change the driver path for your system. 

### 2-Data Cleaning
Following Data Cleaning steps are applied:
-  Remove columns with complete b-1 values : Competitors, Headquarters  
- Salary parsing
    - Remove all rows with `'Salary Estimate' == '-1'`.
    - Remove text `'(Glassdoor estimate)'`
    - Replace `CA$`, `K` with a blank space
    - `'per hour'` make a separate column 
    - `CAD` & US `$` make a separate column
    - extract `min` , `max` and `average` salary. Make sure the data type of these columns is 'integer'

- company name [text only]
- State field (if the country is US) otherwise city (Canada). 
- Age of the company 
- Parsing job desciption to extract key skill requirements
    - For the analysis purposes, we extracted the following:
    	- Language (python, R-studio, SQL)
    	- Cloud computing (GCP, AWS, AZURE)
    	- Analaysis (Excel)
    	- Big Data (Hadoop)

#### Take Aways 
It is recommned to work on a separate branch for data cleaning.     	

### 3-Exploratory Data Analysis (EDA)

`Jupyter-Notebook` is used for this purposes rather than `spider`

## FURTHER TASKS
The following tasks can be initiated to further explore the salary estimation project:

#### Exploratory Data Analysis - Canada alone or USA 
The present project has a combined study on Canada and USA jobs. It could have been exclusively for USA and for Canada. That could be an interesting exploration. 

#### Explore Few More Regression Models
