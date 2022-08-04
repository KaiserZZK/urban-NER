'''
Part of the Custom NER Label v2 architecture: DATA CLEANING

Objective: initial cleaning by getting rid of repeated tweets 
e.g. the tweet "Pop out of the 59th Street subway stop, walk across Lexington Avenue and hang a left to step back into peak-pandemic time https://t.co/otywjqujEb" appears in searches for both "STREET" and "AVENUE"

output a txt file for training, similar to 'hp.txt' used in '04_01_customizing_spacy.py'

'cleaned_01.txt': removed repetition
'cleaned_02.txt': removed hashtags and changed all characters to lowercase

Zekai Zhang, 29 July 2022
'''

def write_data(file, input):
    with open(file, 'a+') as filehandler:
        filehandler.write(input)

import re
import os

tweets = {} # Dictionary of subfixes

path = "data_uncleaned"
os.chdir(path)

for file in os.listdir():
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:

            # results = line.strip()
            # print(results) # Simply read in the entire line for data 
            # streets.append(results)

            tweet = line.strip().replace('#', '').lower()
            if tweet not in tweets and tweet != '':
                tweets[tweet] = 1
                write_data("cleaned_test_01.txt", tweet+'\n')
