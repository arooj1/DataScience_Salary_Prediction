# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:32:24 2020

@author: quresa9
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# read both datasets

df= pd.read_csv('salary_data_cleaned.csv')
df.columns
# Extract columns required as features for model building
