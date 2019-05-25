#!/usr/bin/python3

import tweepy
import config
import src.Grabber as Grabber
import src.util as util
import sys, time

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
API = tweepy.API(auth)

# Sometimes a section is outside of a book, and then we return blank
# sometimes a section is at the end of the book, and then we need to know
# so we can break the loop

if __name__ == '__main__':
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            debug = True
            print('Running in debug mode')
    print('Running bot')
    g = Grabber.Grabber()
    verse = ''
    i = 0
    while True:
        print('Bot has completed', i, 'readings')
        newest_verse = util.get_most_recent_verse()
        book_num, sec = g.get_bk_sec(newest_verse)
        while book_num < 13:
            verse = g.get_verse(book_num, sec)
            # Essentially a do while to make sure we include
            # the book header
            if verse.split('\n')[0].strip() == 'THE ARGUMENT':
                verse = 'BOOK ' + str(book_num) + '\n' + verse
                if debug:
                    print(verse)
                    time.sleep(5)
                else:
                    API.update_status(verse)
                    time.sleep(1800)
            while verse != '' and not util.book_end(verse):
                sec += 1
                verse = g.get_verse(book_num, sec)
                if debug:
                    print(verse)
                else:
                    API.update_status(verse)
                    time.sleep(1800)
                # Poem End
                if verse.split('\n')[0].strip() == 'THE END':
                    book_num = 1
                    break
                # Most books have this string in their last phrase,
                # as in, the end of the sixth book
            book_num += 1
            sec = 1
        i += 1
