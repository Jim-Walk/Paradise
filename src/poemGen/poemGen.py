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
        pf += [text.pop(0)]
        ## TODO, if text[0] is a number and roundels now > 0, pop all lines
        ## that are a number or blank, then get gloss
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
    if roundels < 0:
        roundels = 0
    if roundels == 0 or text == []:
        return getGloss(text, pf, gloss, roundels)

    if text[0] != '\n' and NONDIGIT.match(text[0]) and '.' not in text[0]:
        # good chance that this word is gloss, but is it two or one?
        line = text.pop(0)
        if " / " in line:
            roundels -= 2
            gloss += [line]
            return combGloss(text, pf, gloss, roundels)
        else:
            roundels -= 1
            gloss += [line]
            return combGloss(text, pf, gloss, roundels)
    else:
        text.pop(0)
        return combGloss(text, pf, gloss, roundels)

