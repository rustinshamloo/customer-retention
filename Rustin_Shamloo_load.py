

# QUESTION 1 - load.py

import pandas as pd
import json
import requests
import csv

# upload csv and convert to pandas df
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# filter to keep only senior customers
df = df[df['SeniorCitizen'] != 0]

# extract only cID, churn, and tenure columns
df2 = df[['customerID', 'Churn', 'tenure']].copy()

# # set cID as index and sort
df2 = df2.set_index('customerID')
df2 = df2.sort_index()

# convert to JSON with cID as parent 
data = df2.to_json(orient = 'index')
data

# put into firebase
#url = 'https://dsci551-hw1-b3438-default-rtdb.firebaseio.com/test.json'
#response = requests.put(url, data)


