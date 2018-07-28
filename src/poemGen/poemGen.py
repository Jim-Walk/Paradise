import re, codecs, sys
sys.setrecursionlimit(50000)
NONDIGIT = re.compile("\D")

# Takes poem text as an array of strings, returns a tuple of parsed text
# (pf, gloss) where pf is the poem and footnotes and gloss is the gloss

def parseGloss(text):
    return getGloss(text, [], [], 0)

# text, pf, gloss = []
# roundels = int

def getGloss(text, pf, gloss, roundels):
    # when there is no more text to process we are  finished
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
    if roundels == 0 or text == []:
        return getGloss(text, pf, gloss, roundels)
    if text[0] != '\n' and NONDIGIT.match(text[0]) and '.' not in text[0]:
        # good chance that this word is gloss, but is it more than one?
        if text[0] == "movement / bearing\n":
            import pdb; pdb.set_trace()
        roundels -= 1
        line = text.pop(0)
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

