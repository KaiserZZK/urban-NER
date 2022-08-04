''' Part of the Custom NER Label v2 architecture.
Objective: using rule-based NER to clean data and generate an exhaustive dictionary for building the training set 
to be more specific, the list of streets in 'streets.json' will be taken as the input, then a set of rules will be generated to ultimately account for ALL occurrences/variations of street names
May refer to '01_i_variations'

Zekai Zhang, 30 July 2022
'''

import re
import spacy
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import json

test_input = "spaCy-custom-NER_data/b_building-set/test_input.json"
test_output_dictionary = "spaCy-custom-NER_data/b_building-set/test_output_9.json"
test_output_set = ""

real_input = "spaCy-custom-NER_data/streets.json" 
real_output = ""

modified_names = []

def load_data(file):
    with open(file, "r", encoding="utf-8") as f: 
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f: 
        json.dump(data, f, indent=4)

def generate_name_variations(file): 
    street_names = load_data(file) 
    
    for name in street_names: 
        modified_names.append(name)

    for name in street_names:
        name = name.lower()

        words = name.strip().split()
        street_type = words[-1]

        if street_type=="st":
            add_all_st_variations(name)

        if street_type=="ave":
            add_all_ave_variations(name)

        if street_type=="rd":
            add_all_rd_variations(name)

    modified_names.sort()
    # print(len(modified_names))
    return(modified_names)

def add_all_st_variations(name): 
    parts = re.split(r'(\s+)', name)
    # print('%s%s%s' %(parts, ', length = ', len(parts)))

    last_part = ['st', 'street', 'st.']
    
    ''' CASE 1 -> length==5: "W 66th St"; NO edgecases?
    PSEUDOCODE
    create x separate lists (x being length of the list)
    add to the possible part variation to each list as the elements 
    x nested loops, iterate through each list within every loop  
    '''
    if len(parts)==5 and parts[2][0:-2].isnumeric():
        if parts[0]=='w':
            part1 = ['w', 'west', 'w.']
        else:
            part1 = ['e', 'east', 'e.']
        part2 = ['', ' ']
        part3 = [parts[2], parts[2][0:-2]]
        part4 = ['', ' ']

        # all_variations = []

        for var1 in part1:
            for var2 in part2:
                for var3 in part3:
                    for var4 in part4:
                        for var5 in last_part:
                            modified_names.append(var1+var2+var3+var4+var5)  

        # print(all_variations)
        # print(len(all_variations))
        # print('e 124st' in all_variations)    

    ''' CASE 2 -> length==3: "129th St"; edgecases: "Edgewater St"
    check whether the first 2 or 3 characters in the first part are digits
    '''
    if len(parts)==3: 
        if parts[0][0:-2].isnumeric():
            part1 = [parts[0], parts[0][0:-2]]
            part2 = ['', ' ']

            # all_variations_2 = []
            
            for var1 in part1:
                for var2 in part2:
                    for var3 in last_part:
                        modified_names.append(var1+var2+var3)

        else: 
            variation = ''
            for i in range(0,len(parts)-1):
                variation += parts[i]
            for var in last_part:
                modified_names.append(variation+var)
        
        # print(all_variations_2)
        # print(len(all_variations_2))
        # print('2nd street' in all_variations_2)
        
    ''' CASE 3 -> various other lengths: "Yacht Club Cove St"
    unlikely to have variations other than the ones for St
    '''
    if len(parts)!=3 and len(parts)!=5: 
        # all_variations_3 = []
        variation = ''
        for i in range(0,len(parts)-1):
            variation += parts[i]
        for var in last_part:
            modified_names.append(variation+var)

        # print(all_variations_3)
        # print(len(all_variations_3))
        # print('2nd street' in all_variations_3)

def add_all_ave_variations(name):
    parts = re.split(r'(\s+)', name)
    # print('%s%s%s' %(parts, ', length = ', len(parts)))

    last_part = ['ave', 'avenue', 'ave.']

    # all_variations = []

    if parts[0][0:-2].isnumeric():
        part1 = [parts[0], parts[0][0:-2]]
        variation = ''
        for i in range(1,len(parts)-1):
            variation += parts[i]
        for var1 in part1:
            for var in last_part:
                modified_names.append(var1+variation+var)

    else:
        variation = ''
        for i in range(0,len(parts)-1):
            variation += parts[i]
        for var in last_part:
            modified_names.append(variation+var)

    # print(all_variations)
    # print(len(all_variations))
    # print('2nd street' in all_variations)

def add_all_rd_variations(name):
    parts = re.split(r'(\s+)', name)
    # print('%s%s%s' %(parts, ', length = ', len(parts)))

    last_part = ['rd', 'road', 'rd.']

    # all_variations = []

    if parts[0][0:-2].isnumeric():
        part1 = [parts[0], parts[0][0:-2]]
        variation = ''
        for i in range(1,len(parts)-1):
            variation += parts[i]
        for var1 in part1:
            for var in last_part:
                modified_names.append(var1+variation+var)

    else:
        variation = ''
        for i in range(0,len(parts)-1):
            variation += parts[i]
        for var in last_part:
            modified_names.append(variation+var)

def create_training_data(input_file, entity_type):
    streets = generate_name_variations(input_file)
    patterns = []
    edge_cases = ["i st", "a st", "5th", "6th", "a street", "1st", "1 st", "31st", "21st", "61st", "33st"]


    for street in streets:

        if street not in edge_cases:
            pattern = {
                        "label": entity_type,
                        "pattern": street
                        }
            patterns.append(pattern)

    return (patterns)

def generate_rules(patterns):
    nlp = English() 
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(patterns)
    nlp.to_disk("urban_location_ner/street_ner_ruler")

def test_model(model, text):
    doc = nlp(text)
    results = []
    for ent in doc.ents:
        results.append(ent.text)
    return(results)

patterns = create_training_data(real_input, "STREET")
# print(patterns)
generate_rules(patterns)
# save_data(test_output, modified_names)

nlp = spacy.load("urban_location_ner/street_ner_ruler")

cleaned_tweets_test = "spaCy-custom-NER_data/b_building-dictionary/ruler_test_input.txt"
cleaned_tweets = "spaCy-custom-NER_data/a_gathering-cleaning_v2/data_cleaned/cleaned_final.txt"

cleaned_tweet_test_output = "spaCy-custom-NER_data/b_building-dictionary/ruler_test_output_6.json"
cleaned_tweet_output = "spaCy-custom-NER_data/b_building-dictionary/ruler_test_output_2.json"

street_information  = {}
# streets_mentioned = []

with open (cleaned_tweets, "r") as f:
    tweets = f.readlines()

    for tweet in tweets:
        tweet = tweet.strip().replace("\n", "")
        results = test_model(nlp, tweet)
        streets_mentioned = []
        # print(tweet)

        for result in results:
            streets_mentioned.append(result)
        if len(streets_mentioned) != 0:
            street_information[tweet] = streets_mentioned


# print(street_information)
save_data(cleaned_tweet_test_output, street_information)

# print(len(tweets))