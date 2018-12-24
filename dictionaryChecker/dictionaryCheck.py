import json
from difflib import SequenceMatcher

# Ratio cutoff for similarity between words using SequenceMatcher algorithm
RELATED_RATIO = 0.6

# Loads dictionary
with open('data.json') as datafile:
    data = json.load(datafile)

    
# Prompts for user input
def askWord():
    word = input("Please enter the word you would like to search: \n")
    return word


word = askWord()


def isWord(w):
    if w in data:
        return True
    else:
        return False

#Checks for similarity between strings
def isCloseWord(w):
    for words in data:
        ratio = SequenceMatcher(None, words, w).ratio()
        if ratio > 0.6:
            return True
    return False


def bestWord():
    best = 'test'
    # Comparison between one arbitrary word and the user input  
    big = SequenceMatcher(None, data[best], word).ratio()
    
    # Iterate over the words in the dictionary
    for words in data:
        ratio = SequenceMatcher(None, words, word).ratio()
        if (ratio > RELATED_RATIO) and (ratio > big):
            big = ratio
            best = words
    return best


def suggestion(best):   
    yn = input('Did you mean \"%s\"? (y/n)\n' % best)
    if yn == 'y':
        return best
    elif yn == 'n':
        word = askWord()
        best = bestWord()
        suggestion(word)
    else:
        print('Please enter a valid character...\n')
        suggestion(best)


if isWord(word):
    for defs in data[word]:
        print(':' + defs)
elif isCloseWord(word):
    best = bestWord()
    word = suggestion(best)
    for defs in data[word]:
        print(':' + defs)
else:
    print('That\'s an invalid word, please try again...\n')

