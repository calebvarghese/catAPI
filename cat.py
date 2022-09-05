#!/usr/bin/python3

# We need these to handle API requests and json
import requests
import json
import random

# This hits the fact end point then puts the requests json into a python dictionary object
response = requests.get("https://catfact.ninja/fact/")
resp_fact = response.json()

# This grabs the 'fact' from the dictionary
print("New Fact:\n\n" + resp_fact.get('fact') + "\n")

num = random.randint(1,34)
#this grabs a nested directory of facts
list_response = requests.get('https://catfact.ninja/facts?page={}'.format(num))
resp_fact_list = list_response.json()

print("Daily Facts:\n")
for x in resp_fact_list['data']:
    print(x['fact'] + "\n")
    
