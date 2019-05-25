import tweepy

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
API = tweepy.API(auth)

# Check if this verse is the end of the book
def book_end(verse):
    if verse == '':
        return False
    for line in verse.split('\n'):
        if 'Book.' in line.split():
            return True
    return False

def get_most_recent_verse():
    tweet_list = API.user_timeline(count=1, tweet_mode='extended')
    return tweet_list[0]._json['full_text']
