# Check if this verse is the end of the book
def book_end(verse):
    if verse == '':
        return False
    for line in verse.split('\n'):
        if 'Book.' in line.split():
            return True
    return False

