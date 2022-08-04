Part of the Custom NER Label v2 architecture.
Objective: to account for possible ways which the street name expressions in tweets varies from the "official" expression 

Zekai Zhang, 28 July 2022
----------------------------------------------------------

EXPRESSION VARIATIONS
----------------------------------------------------------
IGNORE upper/lower cases;
NO SPACING 

a. "St" (covering 1st and 2nd search attempt)
BASIC FORM
    "W 66th St"
VARIATIONS
    see the text as 5 separata parts (ignore upper/lower cases):
        (W)+( )+(66th)+( )+(St)
        each part has the following possible variations:
        1) W OR West OR W.
        2) ( ) OR ()
        3) 66th OR 66 
            Good thing is that entries in the original dataset already inlude subfixes like "nd" "st" "rd" so just remove the 
        4) * same as (2)*
        5) St OR Street OR St.
        --> 72 total possible combinations

b. "Ave" (covering 3rd search attempt)
    1) 66th OR 66
    2) ( ) OR () 
    3) ave or ave. or avenue

c. Pl-s are usually fine (covering 4th search attempt)

d. Blvd-s are usually fine (covering 5th search attempt)

e. Pkwy-s are usually fine (covering 8th search attempt)


