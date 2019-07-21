from itertools import permutations as pt
import pickle

    
def gen_words(letters): #Creates a word list from letters passed
    words=[''.join(item) for item in pt(letters)]
    return list(set(words))


def word_check(word_list,word_dict):# Checks out for meaningful words
    element = [item for item in word_list if item in word_dict]
    return element


def gen_word_dict(): # loads the dictionary list
    with open('app/api/word_dict','rb') as infile:
        word_dict = pickle.load(infile)

    return word_dict
