import pickle

def gen_word_dict(): #Creates a dictionary list
    with open('words_alpha.txt') as word_dict:
        return [word.strip('\n') for word in word_dict.readlines()]


with open('app/api/word_dict','wb') as outfile:
    pickle.dump(gen_word_dict(),outfile)

    