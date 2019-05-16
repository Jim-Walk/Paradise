# Helper functions for poem gen, mainly used by
# the test suite
# counts the number of roundels, or ° in each line 
# of the string array it is given

import codecs

def count_roundels(text):
    roundels = 0
    lines = 0
    for line in text:
        lines += 1
        for char in line:
            if char == '°':
                roundels += 1
    print('Found ', roundels, '°s in ', lines, 'lines')
    return roundels

def count_gloss(text):
    counter = 0
    for line in text:
        counter += 1
        for char in line:
            if "/" == char:
                counter += 1
    return counter

