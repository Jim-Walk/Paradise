# Holds functions useful to bots. Re use slightly adjusted code
# from the poem/tests/helpers.py file

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
