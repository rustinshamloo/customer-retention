# coding='utf-8'

# QUESTION 3 - tenure.py

# Write a Python script “tenure.py” to find out how many customers who have used the service for at least k months.

import sys
import json
import requests

# get data from database
url = 'https://dsci551-hw1-b3438-default-rtdb.firebaseio.com/test.json?orderBy="tenure"&startAt=' + str(sys.argv[1])
response = requests.get(url)                      
response = response.json()
print(len(response))
