''' Part of the Custom NER Label v2 architecture.
Objective: to build a dataset for training a model that recognizes street names in NYC, primarily using automated web scraping
1) to clean and format street name data parsed from geographic.org
2) extract subfixes to provide keywords for Twitter scraping

Zekai Zhang, 28 July 2022
'''

''' Data Source 1: plain list, without any metadata
https://geographic.org/streetview/usa/ny/new_york.html
https://geographic.org/streetview/usa/ny/bronx.html
https://geographic.org/streetview/usa/ny/brooklyn.html
https://geographic.org/streetview/usa/ny/queens.html
https://geographic.org/streetview/usa/ny/staten_island.html
'''

import json
import glob

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return(data)

def write_data(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

import re
streets = [] # Array
subfixes = {} # Dictionary of subfixes

with open("spaCy-custom-NER_data/streets.txt", "r") as f:
    lines = f.readlines()
    for line in lines:

        results = line.strip()
        # print(results) # Simply read in the entire line for data 
        streets.append(results)

        words = line.strip().split()
        subfix = words[-1]
        if subfix in subfixes:
            subfixes[subfix] += 1
        else:
            subfixes[subfix] = 1
        subfixes = dict(sorted(subfixes.items(), key=lambda subfixes: subfixes[1], reverse=True))

# print(streets)
print(subfixes)

# write_data("streets.json", streets)
write_data("spaCy-custom-NER_data/street_subfixes.txt", subfixes)