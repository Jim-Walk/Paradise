import re

BOOKS = re.compile('BOOK \d')

class Grabber():

    poem = ""
    book_idxs = [0]

    def __init__(self):
        with open('../poem/poem.txt') as poem_f:
            self.poem = poem_f.readlines()
        i = 0
        book = 1
        # Create a list of indexes where each book starts
        while book < 13:
            if self.poem[i].strip() == 'BOOK ' + str(book):
                book += 1
                self.book_idxs += [i]
            i += 1

    def get_verse(self, bk, sec):
        i = self.book_idxs[bk] + 1
        char_limit = 190
        char_count = 0; sec_count = 0
        while sec_count < sec:
            verse = ''
            while char_count < char_limit:
                if i >= len(self.poem):
                    break
                if BOOKS.match(self.poem[i]):
                    break
                char_i = 0
                while char_i < len(self.poem[i]):
                    verse += self.poem[i][char_i]
                    char_count += 1
                    char_i += 1
                i += 1
            sec_count += 1
            char_count = 0

        return verse
