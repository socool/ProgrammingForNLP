class TextContainer:
    
    STOP_WORD_LIST = set(['a','a','the','in','of'])
    #add variable convention
    text = ''
    source = ''
    
    def __init__(self):
        pass
    
    def get_word_count(self):
        return len(self.text.split(' '))
    
    def get_text_without_stop_words(self):
        return [x for x in self.text.split(' ')if x not in self.STOP_WORD_LIST]
    
class Tweeter(TextContainer):
    STOP_WORD_LIST = set(['in','of'])
    def __init__(self,text,user_id,location):
        self.text = text
        self.user_id = user_id
        self.location = location

class SubTitleLine(TextContainer):
    def __init__(self,text,timestamp,source):
        self.text = text
        self.timestamp = timestamp
        self.source = source