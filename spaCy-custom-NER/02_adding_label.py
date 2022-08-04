''' Part of the Custom NER Label v2 architecture.
Objective: to create a custom NER based on the NYC street names dataset
"spaCy-custom-NER_data/streets.json" 

Zekai Zhang, 28 July 2022
'''

# Adding a new pipe to a blank model 

import spacy

nlp = spacy.blank("en") # Creating a blank model 
# print(nlp.pipe_names) # prints blank result since NO pipe has been added yet 

''' adding a pipe in spaCy 3.x
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("ner", name="street_ner", before="ner")
'''

''' in Tutorial 9.2; the way for spaCy 2.x
ner = nlp.create_pipe("ner")
#ner.add_label("STREET")
'''
nlp.create_pipe("ner")

ner = nlp.add_pipe("ner", name="street_ner") # Adding a PIPE within the MODEL
ner.add_label("STREET")
# Documentation referred: https://spacy.io/api/entityrecognizer#add_label
''' The desired output in meta.json:
"labels":{
    "street_ner":[
      "STREET"
    ]
  },
'''

# print(nlp.pipe_names)

nlp.to_disk("urban_location_ner") # Saving the newly created model