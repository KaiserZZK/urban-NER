Part of the Custom NER Label v2 architecture.
Objective: to build a training set with tweets from Twitter

Zekai Zhang, 28 July 2022
----------------------------------------------------------

The intermediate step between 02_adding_label.py and 03_training_model.py;
following DHG 04 Part 01-03 in the NER playlist by Python Tutorials for Digital Humanities

0   A "dictionary" of a cleaned list of street names [DONE]
0.5 Modify the dictionary by adding variants based on observation from sampled tweets <04 01> []

1   DATA GATHERING [FINISHED]
1.1 Determine Twitter scraping search keywords [DONE]   
1.2 Get raw training data from Twitter using tweepy, 1st batch [DONE]
1.3 *Review data, refine search keywords if necessary [DONE]
1.4 Iterate [DONE]
(Min. training set size: ~2000; ideal: ~4000)

2   DATA CLEANING []
2.1 Delete repeated tweets []

3   Cultivate scraped data to create training set <04 02> []
* make "failed" text into validation set e.g. "@NYC_DOT Double Parking of cars in Junction Blvd. in Jackson Heights. This is a recurrent issue that blocks a two way street during Friday, Saturday and Sunday. This issue is along Junction Blvd in Jackson Heights between 34 Av and Roosevelt Av."--which technically should be containing location information but does not correspond to the catalogue

transition from 04.03 to 09 03 (it does seem that the training data obtained at the end of 09 02 would suffice? )
