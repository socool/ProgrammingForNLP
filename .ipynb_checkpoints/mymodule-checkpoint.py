import random

def tokenize_text(text):
    return text.split(' ')

def shuffle_text(text):
    character_list = list(text)
    random.shuffle(character_list)
    return ''.join(character_list)