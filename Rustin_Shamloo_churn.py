# coding='utf-8'
# QUESTION 2 - churn.py

# Write a Python script “churn.py” to find the first k (senior) customers who have churned. 
# Only need to return IDs of first k customers (ordered by their IDs).

import sys
import json
import requests

# request from firebase users who have churned
lst = []
url = 'https://dsci551-hw1-b3438-default-rtdb.firebaseio.com/test.json?orderBy="Churn"&equalTo="Yes"&limitToFirst='+str(sys.argv[1])
response = requests.get(url)
response = response.json()
        
# return k customer IDs aka keys
c = 0
for k in response.keys():
    if c < int(sys.argv[1]):
        lst.append(k)
        lst = sorted(lst)
    c+=1
print(lst) 
