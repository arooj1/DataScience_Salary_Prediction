# @author Arooj Ahmed Qureshi

import scrapper as gl
import pandas as pd 

path = "D:\job_applications-2020\DEC_JAN_2021\SharpestMinds\ds_salary_proj\chromedriver\chromedriver"
slp_time = 15
records = 500

df = gl.get_jobs('data scientist',records,False,path, slp_time)

df.to_csv('glassdoor_canada.csv', index=False)
