#Class
class Tweet:
    #constructor
    def __init__(self,twitter_id,text,coordinate):
        self.twitter_id = twitter_id
        self.text = text
        self.coordinate = coordinate
    #instance method
    def get_tweet_word_count(self):
        return len(self.text.split(' '))
    
    #parameter self for send self data
    def get_character_count(self):
        return len(self.text)