# Process text files and upload to running web server
#! /usr/bin/env python3
import os
import requests

# Assign directory
directory = "/data/feedback/"
dictionary = {}

# Iterate over files in the text directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    # Open the files and create a dictionary
    with open(f, 'r') as text:
        for indx, line in enumerate(text):
            if indx == 0:
                stripped = line.strip()
                dictionary["title"] = stripped
            if indx == 1:
                stripped = line.strip()
                dictionary["name"] = stripped
            if indx == 2:
                stripped = line.strip()
                dictionary["date"] = stripped
            if indx == 3:
                stripped = line.strip()
                dictionary["feedback"] = stripped
    
    # Send the dictionary to the server and record the response
    response = requests.post("http://34.136.32.86/feedback/", data=dictionary)
    response.raise_for_status() 
