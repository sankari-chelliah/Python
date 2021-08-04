def break_words(stuff):
    words = stuff.split()
    return words

def sort_words(stuff):
    return sorted(stuff)

def print_first_word(stuff):
    words = stuff.pop(0)
    print(words)

def print_last_word(stuff):
    words = stuff.pop(-1)
    print(words)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    #words = sentence.split()
    #print (sorted(words))
    #words1 = sorted(words)
    words1 = sort_sentence(sentence)
    print_first_word(words1)
    print_last_word(words1)
