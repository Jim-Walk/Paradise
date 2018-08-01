#!/usr/bin/python3

import pytest, codecs, copy, re
from tests.helpers import count_roundels, count_gloss
from src.poemGen.poemGen import parseGloss, parse_footnotes

FILE = 'raw.txt'

# checks that we have the same number of roundels afterwards 
# that we do before
def test_count_roundels():
    with codecs.open(FILE, 'r', encoding='utf8') as text:
        txt = text.readlines()

    pf, gloss = parseGloss(copy.copy(txt))

    assert count_roundels(txt) == count_roundels(pf)

# There should be equal number of roundels in pf, that there is to the number
# of lines in the gloss, less two due to edge cases

def test_number_of_lines():
    with codecs.open(FILE, 'r', encoding='utf8') as raw:
        text = raw.readlines()

    pf, gloss = parseGloss(text)
    assert count_roundels(pf) -2 == count_gloss(gloss)

def test_count_roundels_pf():
    with codecs.open(FILE, 'r', encoding='utf8') as raw:
        text = raw.readlines()

    pf, gloss = parseGloss(text)
    poem, footnotes = parse_footnotes(copy.copy(pf))

    assert count_roundels(pf) == count_roundels(poem)

def test_12_books():
    with codecs.open(FILE, 'r', encoding='utf8') as raw:
        text = raw.readlines()

    pf, gloss = parseGloss(text)
    poem, footnotes = parse_footnotes(pf)
    books = re.compile('BOOK \d')
    counter = 0
    for line in poem:
        if books.match(line):
            counter += 1
    assert counter == 12
