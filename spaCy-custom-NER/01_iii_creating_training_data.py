''' Part of the Custom NER Label v2 architecture.
Objective: to create a spaCy-compatible dataset for training a custom spaCy NER model.

NOTE 
01_ii deals with scraping and cleaning; for proximity to data, the codes are placed within 'spaCy-custom-NER/spaCy-custom-NER_data/a_gathering-cleaning_v2' and named 'query.py' and 'cl_01_delete_repetition.py' respectively; 'config.py' is used for connecting to the Twitter API. 
The output data of scraped, cleaned tweets is inside 'spaCy-custom-NER/spaCy-custom-NER_data/b_building-set'.

Zekai Zhang, 1 August 2022
'''

import re
import spacy
import random
import json

test_input = ""

def load_data(file):
    with open(file, "r", encoding="utf-8") as f: 
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f: 
        json.dump(data, f, indent=4)

def test_model(model, text):
    doc = nlp(text)
    results = []
    entities = []

    for ent in doc.ents:
        entities.append((ent.start_char, ent.end_char, ent.label_))
        # print(training_data)

    if len(entities)>0:
        results = [text, {"entities": entities}]
        # print(results)
        
    return(results)

# TRAIN_DATA = [(text, {"entities": [(start_index, end_index, label)]})]

nlp = spacy.load("urban_location_ner/street_ner_ruler")
cleaned_tweets = "spaCy-custom-NER_data/a_gathering-cleaning_v2/data_cleaned/cleaned_final.txt"
real_output = "spaCy-custom-NER_data/c_train-set_STREET/steet_training_v2.json"
TRAIN_DATA = []

with open (cleaned_tweets, "r") as f:
    tweets = f.readlines()

    for tweet in tweets:
        tweet = tweet.strip().replace("\n", "")
        results = test_model(nlp, tweet)
        # print(tweet)
        if results != []:
            # print(results)
            TRAIN_DATA.append(results)

# entry_index = int(input("Access an entry in the training set (#1-#1261): "))           
# print(TRAIN_DATA[entry_index-1])

save_data(real_output, TRAIN_DATA)