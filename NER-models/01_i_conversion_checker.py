import re
import spacy
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import json

ipt = "spaCy-custom-NER_data/streets.json" 
opt = "spaCy-custom-NER_data/b_building-set/test_output_4.json"

modified_names = []

def load_data(file):
    with open(file, "r", encoding="utf-8") as f: 
        data = json.load(f)
    return (data)

def check_missing(input_file, output_file): 
    check_inside = load_data(output_file)
    check_against = load_data(input_file)

    all_output = []

    for entry in check_against:
        all_output.append(entry)

    for entry in check_inside:
        if entry not in all_output:
            print (entry + "NOT FOUND")

    print("ALL GREEN")

check_missing(opt, ipt)
    