''' jsra
'''

import spacy
import json
import random
from spacy.training import Example


training_data_file = "spaCy-custom-NER_data/c_train-set_STREET/steet_training_FINAL.json"


def load_data(file):
    with open(file, "r", encoding="utf-8") as f: 
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f: 
        json.dump(data, f, indent=4)

def train_spacy(TRAIN_DATA, iterations):
    nlp = spacy.blank("en")
    ner = nlp.create_pipe("ner")
    nlp.add_pipe("ner", name="street_ner")
    ner.add_label("STREET")

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "street_ner"]

    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()

        for itn in range(iterations):
            print(f"Starting iteration {str(itn)}")
            random.shuffle(TRAIN_DATA)
            losses = {}

            example = []

            for text, annotations in TRAIN_DATA:
                doc = nlp.make_doc(text)
                example.append(Example.from_dict(doc, annotations))

                nlp.update(example, drop = 0.2, sgd = optimizer,losses = losses)
                # nlp.update( [text], [annotations], drop = 0.2, sgd = optimizer,losses = losses)

            print(losses)

    return (nlp)
    
'''
        for batch in batches:
            texts, annotations = zip(*batch)
            
            example = []
            # Update the model with iterating each text
            for i in range(len(texts)):
                doc = nlp.make_doc(texts[i])
                example.append(Example.from_dict(doc, annotations[i]))
            
            # Update the model
            nlp.update(example, drop=0.5, losses=losses)


'''

TRAIN_DATA = load_data(training_data_file)
# print(TRAIN_DATA[0])
TEST_TRAIN_DATA = TRAIN_DATA[0:100]

random.shuffle(TRAIN_DATA)
# print(TRAIN_DATA[0])

# nlp = train_spacy(TEST_TRAIN_DATA, 5)
nlp = train_spacy(TRAIN_DATA, 100)

nlp.to_disk("spaCy-custom-NER_data/d_trained-models/street_ner_model_v1")

'''
# SMALL TEST 1: 100 entries, 5 iterations
test_validation_text_1 = "Haahaa University is located at the intersction of 1999th street and #hoohooavenue." # "1999th street" detected
test_validation_text_2 = "Haahaa University is located at the intersction of 1999th street and #hoohoo avenue." # SUCCESS
test_validation_text_3 = "Haahaa University is located at the intersction of w1999st and the hoohoo." # FAIL

test_validation_text = test_validation_text.lower().replace('#', '')
# print(test_validation_text)

doc = nlp(test_validation_text)

for ent in doc.ents:
    print(ent.text, ent.label_)
'''