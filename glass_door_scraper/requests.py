# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:05:30 2020

@author: quresa9
"""

import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
HEADERS = {'Content-Type': 'application/json'}
data = {'input': data_in}
r = requests.get(URL, headers = HEADERS, json = data)
