'''
customized spaCy Named Entity Recognition (NER) that extracts the specific
urban location information from a tweet.
<Example>
Input: "URBAN FLOODING north side of NYC here is I95 near the CT border."
Output: I95 tagged as 'location'.

APPROACH 1: small traing dataset 
'''

# Possible 1st step: remove hashtag

TRAIN_DATA = [
('RBAN FLOODING north side of NYC here is I95 near the CT border.', {'entities': [(41, 44, 'road')]}),

    
]