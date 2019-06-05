import re
import time
from src.util import count_roundels, legit_foot_num

BOOKS = re.compile('BOOK \d')

# Grabber gets things from the poem text to post
class Grabber():

    poem = ""
    gloss = ""
    foot = ""
    book_idxs = [0]
    arg_idxs = [0]
    foot_idxs = [0]

    def __init__(self):
        with open('../poem/poem.txt') as poem_f:
            self.poem = poem_f.readlines()
        with open('../poem/gloss.txt') as gloss_f:
            self.gloss = gloss_f.readlines()
        with open('../poem/footnotes.txt') as foot_f:
            self.foot = foot_f.readlines()
        i = 0
        book = 1
        # Create a list of indexes where each book starts in the poem
        while book < 13:
            if self.poem[i].strip() == 'BOOK ' + str(book):
                book += 1
                self.book_idxs += [i]
                while self.poem[i-1] != '\n':
                    i += 1
                self.arg_idxs += [i]
            i += 1
        # Create a list of indexes where each book starts in the footnotes
        # Not a perfect match due to non standard footnotes, but good enough
        i = 0
        book = 1
        c = 1
        most_recent_foot = -1
        while book < 13 and i < len(self.foot):
            line = self.foot[i].strip()
            if most_recent_foot <= legit_foot_num(line):
                most_recent_foot = legit_foot_num(line)
            else:
                if legit_foot_num(line) > 0:
                    c += 1
                    if c > 1:
                        self.foot_idxs += [i]
                        book += 1
                        most_recent_foot = -1
                        c = 0
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
            return '', -1
        i = self.book_idxs[bk] + 1
        char_limit = 190
        char_count = 0; sec_count = 0
        verse = ''
        lineN = 1
        while sec_count < sec:
            verse = ''
            while char_count < char_limit:
                if i >= len(self.poem):
                    break
                if BOOKS.match(self.poem[i]):
                    break
                # Add to verse from line
                verse += self.poem[i]
                char_count += len(self.poem[i])
                i += 1
                if i < len(self.poem):
                    if self.poem[i] != '\n' or self.poem[i].strip() != '':
                        lineN += 1
            sec_count += 1
            char_count = 0

        if sec_count == sec:
            return verse, self.book_idxs[bk] + lineN - self.arg_idxs[bk]
        else:
            return '', -1

    def get_gloss(self, verse):
        verse_r = count_roundels(verse.split('\n'))
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

    def get_footnote(self, bk, lineN):
        if lineN < 0:
            return ''
        return 'Please implement'

