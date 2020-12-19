"""
@author: bonniema

This code helps you get relevant information from each job card, and then iterate through all job cards on one page.
Then go to the next page
"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

options = webdriver.ChromeOptions()
    
#Uncomment the line below if you'd like to scrape without a new Chrome window every time.
#options.add_argument('headless')

#Change the path to where chromedriver is in your home folder.
#driver = webdriver.Chrome(executable_path="D:\job_applications-2020\DEC_JAN_2021\SharpestMinds\ds_salary_proj/chromedriver", options=options)
driver = webdriver.Chrome(executable_path=path, options=options)
driver.set_window_size(1120, 1000)
#let the driver wait 3 seconds to locate the element before exiting out
driver.implicitly_wait(3) 

titles=[]
companies=[]
locations=[]
links =[]
reviews=[]
salaries = []
descriptions=[]


for i in range(0,20):
    
    job_card = driver.find_elements_by_xpath('//div[contains(@class,"clickcard")]')
    
    for job in job_card:
       
    #.  not all companies have review
        try:
            review = job.find_element_by_xpath('.//span[@class="ratingsContent"]').text
        except:
            review = "None"
        reviews.append(review)
   #.   not all positions have salary
        try:
            salary = job.find_element_by_xpath('.//span[@class="salaryText"]').text
        except:
            salary = "None"
    #.  tells only to look at the element       
        salaries.append(salary)
        
        try:
            location = job.find_element_by_xpath('.//span[contains(@class,"location")]').text
        except:
            location = "None"
    #.  tells only to look at the element       
        locations.append(location)
        
        try:
            title  = job.find_element_by_xpath('.//h2[@class="title"]//a').text
        except:
            title = job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="title")
        titles.append(title)
        links.append(job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="href"))
        companies.append(job.find_element_by_xpath('.//span[@class="company"]').text)
        
    
    try:
        next_page = driver.find_element_by_xpath('//a[@aria-label={}]//span[@class="pn"]'.format(i+2))
        next_page.click()

    except:
        next_page = driver.find_element_by_xpath('//a[@aria-label="Next"]//span[@class="np"]')
        next_page.click()
    #except:
        #next_page = driver.find_element_by_xpath('//a[.//span[contains(text(),"Next")]]')
        #next_page.click()
        
    
    print("Page: {}".format(str(i+2)))