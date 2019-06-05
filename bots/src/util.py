# Holds functions useful to bots. Re use slightly adjusted code
# from the poem/tests/helpers.py file

import re
# Check if this verse is the end of the book
def book_end(verse):
    if verse == '':
        return False
    for line in verse.split('\n'):
        if 'Book.' in line.split():
            return True
    return False

def count_roundels(text):
    roundels = 0
    lines = 0
    for line in text:
        lines += 1
        for char in line:
            if char == '°':
                roundels += 1
    return roundels

# Counts gloss in gloss.txt
def count_gloss(text):
    counter = 0
    for line in text:
        counter += 1
        for char in line:
            if "/" == char:
                counter += 1
    return counter

# Returns 0 if equal number of open and close brackets
# Returns +ve val if more close than open
# Returns -ve val if more open than close
def count_brackets(text):
    open_b = 0
    close_b = 0
    for char in text:
        if char == '(':
            open_b += 1
        if char == ')':
            close_b += 1
    return close_b - open_b

# Takes a line from a foot note file and gives back the line number 
# it refers too. Returns -1 if there is none
# Hard case: 6.37–41) often applied to Satan.   [reject this]
def legit_foot_num(text):
    foot_num = -1
    char_digit = re.compile('\d+')
    prose_n = re.compile('\d+,\d+') # Matches 24,00
    ref_n = re.compile('\d+\.\d+') # Matches 1.7
    bib_ref = re.compile('\d+:') # Matches 12:etc
    semic_ref = re.compile('\d+;') # Matches 12;etc
    if char_digit.match(text):
        niave = char_digit.match(text).group()
        foot_num = int(niave)
        # if there's not the right number of bracktets
        if count_brackets(text) > 0:
            foot_num = -1
        # some lines are just line numbers, and should be ignored
        elif ref_n.match(text):
            foot_num = -1
        elif len(niave) == len(text):
            foot_num = -1
        # Matches '1556.'
        elif len(niave) +1  == len(text):
            foot_num = -1
        elif prose_n.match(text):
            foot_num = -1
        elif bib_ref.match(text):
            foot_num = -1
        elif semic_ref.match(text):
            foot_num = -1

    return foot_num


