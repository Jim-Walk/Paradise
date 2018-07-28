#!/usr/bin/python3

import pytest, codecs, copy
from tests.helpers import countRoundels, count_gloss
from src.poemGen.poemGen import parseGloss

FILE = 'raw.txt'

# checks that we have the same number of roundels afterwards 
# that we do before
def test_count_roundels():
    with codecs.open(FILE, 'r', encoding='utf8') as text:
        txt = text.readlines()

    pf, gloss = parseGloss(copy.copy(txt))

    assert countRoundels(txt) == countRoundels(pf)

# There should be less lines in the poem and footnotes array
# than in the raw text array

def test_number_of_lines():
    with codecs.open(FILE, 'r', encoding='utf8') as raw:
        text = raw.readlines()

    pf, gloss = parseGloss(copy.copy(text))
    assert countRoundels(pf) == count_gloss(gloss)

