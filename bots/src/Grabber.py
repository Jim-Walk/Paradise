import re
import time
import src.util as util

BOOKS = re.compile('BOOK \d')

# Grabber gets things from the poem text to post
class Grabber():

    poem = ""
    gloss = ""
    book_idxs = [0]

    def __init__(self):
        with open('../poem/poem.txt') as poem_f:
            self.poem = poem_f.readlines()
        with open('../poem/gloss.txt') as gloss_f:
            self.gloss = gloss_f.readlines()
        i = 0
        book = 1
        # Create a list of indexes where each book starts
        while book < 13:
            if self.poem[i].strip() == 'BOOK ' + str(book):
                book += 1
                self.book_idxs += [i]
            i += 1


    # Returns book and section of a given verse
    def get_bk_sec(self, recent_verse):
        bk = 1
        sec = 1
        verse = self.get_verse(bk,sec)
        while recent_verse.strip() != verse.strip():
            # Check if we are outside a book
            if verse == '':
                bk += 1
                sec = 1
                verse = self.get_verse(bk,sec)
                if verse == '':
                    break
            sec += 1
            for line in verse.split('\n'):
                line = line.strip()
                if BOOKS.match(line):
                    bk += 1
                    sec = 1
            verse = self.get_verse(bk,sec)
        return bk, sec


    # return verse for given book and section.
    # if section is not in book then we return a blank
    def get_verse(self, bk, sec):
        if bk > 12:
            return ''
        i = self.book_idxs[bk] + 1
        char_limit = 190
        char_count = 0; sec_count = 0
        sec_in_book = True
        verse = ''
        while sec_count < sec and sec_in_book:
            verse = ''
            while char_count < char_limit:
                if i >= len(self.poem):
                    break
                if BOOKS.match(self.poem[i]):
                    # if this section is the last book
                    # the current verse  is the end of the book, 
                    # we can return it safely
                    if verse != '':
                        for line in verse.split('\n'):
                            if 'Book.' in line.split():
                                return verse
                    sec_in_book = False
                    break
                char_i = 0
                while char_i < len(self.poem[i]):
                    verse += self.poem[i][char_i]
                    char_count += 1
                    char_i += 1
                i += 1
            sec_count += 1
            char_count = 0

        if sec_in_book:
            return verse
        else:
            return ''

    def get_gloss(self, verse):
        verse_r = util.count_roundels(verse.split('\n'))
        if verse_r == 0:
            return ''

        # Get first non blank line from verse
        for match_line in verse.split('\n'):
            if match_line != '':
                break

        # Count how many roundels in we've had in the poem so far
        roundels = 0
        for line in self.poem:
            if line.strip() == match_line.strip():
                break
            if '°' in line:
                roundels += 1

        # Count off corresponding number of words from
        # the gloss, using roundels-1 to fix an off by one
        i = 0
        while i < roundels:
            if "/" in self.gloss[i]:
                i += 1
            i += 1
        # Add as many gloss words as needed by verse
        gloss = ''
        while verse_r > 0:
            gloss += self.gloss[i]
            if "/" in self.gloss[i]:
                verse_r -= 1
            i += 1
            verse_r -= 1

        return gloss

