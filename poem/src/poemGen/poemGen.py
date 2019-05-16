import re, codecs, sys
sys.setrecursionlimit(50000)
import pdb

# regexes are global variable so they are only created once
# and always in scope

NONDIGIT = re.compile("\D")
DIGITS = re.compile("\d")
BOOKS = re.compile("BOOK \d")
BOOK_HEAD = re.compile("Book \d")

# Takes poem text as an array of strings, returns a tuple of parsed text
# (pf, gloss) where pf is the poem and footnotes and gloss is the gloss

def parseGloss(text):
    return getGloss(text, [], [], 0)

# text, pf, gloss = []
# roundels = int

def getGloss(text, pf, gloss, roundels):
    # when there is no more text to process we are finished
    if text == []:
        return pf, gloss

    elif roundels == 0:
        for char in text[0]:
            if char == '°':
                roundels += 1

        # This helps avoid seg faults, as we need to ensure the text array
        # always decreases after counting the roundels in a line
        line = text.pop(0)
        pf += [line]
        # if not not a digit, i.e. it is a digit

        # in an edge case, some lines with roundels start with a number,
        # and are then followed by more line numbers, before the poem starts
        # again.
        # if not not a digit, i.e. it is a digit
        if not NONDIGIT.match(line):
            while not NONDIGIT.match(text[0]) or text[0] == '\n':
                pf += [text.pop(0)]
        return getGloss(text, pf, gloss, roundels)

    elif roundels > 0 and text[0] == '\n':
        return combGloss(text, pf, gloss, roundels)

    elif roundels > 0 and text[0] != '\n':
        for char in text[0]:
            if char == '°':
                roundels += 1
        pf += [text.pop(0)]
        return getGloss(text, pf, gloss, roundels)

def combGloss(text, pf, gloss, roundels):
    if roundels == 0:
        return getGloss(text, pf, gloss, roundels)

    if text[0] != '\n' and NONDIGIT.match(text[0]) and '.' not in text[0]:
        # good chance that this word is gloss, but is it more than one?

        # this corrects for two edge cases, where a line has two roundels but
        # only one gloss
        if text[0] == "more careless\n" or (text[0] == "always\n" and text[2] == "this time\n"):
            roundels -= 1

        roundels -= 1
        line = text.pop(0)
        # normally if there are x roundels in one line, there will be x glosses,
        # seperated by a slash
        for char in line:
            if '/' == char:
                roundels -= 1
        gloss += [line]
        return combGloss(text, pf, gloss, roundels)
        #else:
        #    roundels -= 1
        #    gloss += [line]
        #    return combGloss(text, pf, gloss, roundels)
    else:
        text.pop(0)
        return combGloss(text, pf, gloss, roundels)

def parse_footnotes(text):
    return get_feet(text, [], [])

def get_feet(text, poem, feet):
    if text == []:
        return poem, feet

    # Special case to grab the arguement
    # Catch that last little blank line to make line numbers easier later
    if BOOKS.match(text[0]):
        poem += [text.pop(0)]; poem += [text.pop(0)]
        while not NONDIGIT.match(text[0]) or text[0] == '\n':
            del text[0]
        while text[0] != '\n':
            poem += [text.pop(0)]
        poem += [text.pop(0)]

    if BOOK_HEAD.match(text[0]):
        del text[0]

    if NONDIGIT.match(text[0]):
        return comb_poem(text, poem, feet)

    if not NONDIGIT.match(text[0]):
        return comb_feet(text, poem, feet)

def comb_poem(text, poem, feet):
    if text == []:
        return get_feet(text, poem, feet)
    if text[0] == '\n':
        text.pop(0)
        return get_feet(text, poem, feet)
    else:
        poem += [text.pop(0)]
        return comb_poem(text, poem, feet)

def comb_feet(text, poem, feet):
    if text == []:
        return get_feet(text, poem, feet)
    if text[0] == '\n':
        return sweep_line_numbers(text, poem, feet)
    else:
        feet += [text.pop(0)]
        return comb_feet(text, poem, feet)


def sweep_line_numbers(text, poem, feet):
    if text[0] == "BOOK 1\n" and text[2] == "180\n":
        import pdb; pdb.set_trace()
    if BOOK_HEAD.match(text[1]):
        del text[1]
    if NONDIGIT.match(text[0]) and text[0] != '\n':
        poem += [text.pop(0)]
        return get_feet(text, poem, feet)
    else:
        while text[0] == '\n' or DIGITS.match(text[0]):
            del text[0]
        return get_feet(text, poem, feet)


