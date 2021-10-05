#!/usr/bin/env python3

import tweepy
import config
import src.Grabber as Grabber
import src.Verse as Verse
import src.util as util
import sys, time

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
PL_API = tweepy.API(auth)

# Sometimes a section is outside of a book, and then we return blank
# sometimes a section is at the end of the book, and then we need to know
# so we can break the loop
def get_most_recent_verse():
    tweet_list = PL_API.user_timeline(count=1, tweet_mode='extended')
    return tweet_list[0]._json['full_text']


def main():
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            debug = True
            print('Running in debug mode')
    print('Running bot')
    while True:
        v = Verse.Verse(get_most_recent_verse())
        for v in v.gen_verses():
            if debug:
                print(v.verse)
            else:
                #tweet_id = PL_API.update_status(v.verse)
                #time.sleep(5)
                #GLOSS_API.update_status(verse.gloss)
                #FOOT_API.update_status(verse.foot)
                time.sleep(1800)

if __name__ == '__main__':
    main()
