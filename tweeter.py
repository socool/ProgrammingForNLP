class Tweeter:
    def __init__(self,text,user_id,location):
        self.text = text
        self.user_id = user_id
        self.location = location

class SubTitleLine:
    def __init__(self,text,timestamp,source):
        self.text = text
        self.timestamp = timestamp
        self.source = source
    def get_text_without_stop_words(self):
        pass
    
    def get_word_count(self):
        pass