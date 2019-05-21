#!/usr/bin/python3

import tweepy
import config
import src.Grabber
import time

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
API = tweepy.API(auth)

if __name__ == '__main__':
    print('Running bot')
    g = Grabber.Grabber()
    verse = ''
    i = 0
    while True:
        print('Bot has completed', i, 'readings')
        for book_num in range(1,13):
            sec = 1
            verse = g.get_verse(book_num, sec)
            if verse.split('\n')[0].strip() == 'THE ARGUMENT':
                verse = 'BOOK ' + str(book_num) + '\n' + verse
                API.update_status(verse)
                time.sleep(1800)
            while verse != '':
                sec += 1
                verse = g.get_verse(book_num, sec)
                API.update_status(verse)
                time.sleep(1800)
                if verse.split('\n')[0].strip() == 'THE END':
                    break
