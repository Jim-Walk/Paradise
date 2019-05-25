import re
import tweepy
import config
import time

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
API = tweepy.API(auth)

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

    def get_most_recent_verse(self):
        tweet_list = API.user_timeline(count=1, tweet_mode='extended')
        return tweet_list[0]._json['full_text']

    # Returns book and section of the most recent tweet
    def get_recent_bk_sec(self):
        bk = 1
        sec = 1
        recent_verse = self.get_most_recent_verse()
        verse = ''
        while recent_verse.strip() != verse.strip():
            verse = self.get_verse(bk,sec)
            if verse == '':
                break
            sec += 1
            for line in verse.split('\n'):
                line = line.strip()
                if BOOKS.match(line):
                    bk += 1
        return bk, sec


    # return verse for given book and section.
    # if section is not in book then we return a blank
    def get_verse(self, bk, sec):
        i = self.book_idxs[bk] + 1
        char_limit = 190
        char_count = 0; sec_count = 0
        sec_in_book = True
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

