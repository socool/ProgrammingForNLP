import spacy

LANG_TO_PROCESSOR = {
    'en':spacy.load('en',disable=['parser','ner']),
    'fr':spacy.load('fr',disable=['parser','ner'])
}

class CorpusAnalyzer:
    def __init__(self,file_name,language):
        self.file_name = file_name
        self.language = language
        data_file = open(file_name)
        self.sentences = []
        processor = LANG_TO_PROCESSOR[self.language]
        
        for line in data_file:
            self.sentences.append(list(processor(line.strip())))
    
    def get_num_sentences(self):
        return len(self.sentences)