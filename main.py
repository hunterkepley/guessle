import nltk
import re

def main():
    nltk.download('words')
    all_words = nltk.corpus.words.words()
    
    word = word_entry(1)
    check = check_word(word)
    guesses = compile_guesses(all_words, word, check)
    print_guesses(guesses)

def word_entry(n):
    while True:
        word = input(f"Enter word {n}: ")
        if len(word) == 5:
            return word
        print("Length of word is not 5, please enter a 5 letter word")

def check_word(word):
    print(word.upper())
    print("\nEnter (G)reen, (Y)ellow, or (N)ot for each character:\n")
    result = []
    for c in word.upper():
        inp = input(f"{c}: ").lower()
        if inp != 'g' and inp != 'y' and inp !='n':
            inp = 'n'
        result.append(inp)
    return result

def compile_guesses(all_words, word, check):
    yellows = []
    nots = []
    re_str = r'^'
    for i, c in enumerate(word):
        if check[i] == 'g': # Green (match)
            re_str += c
        elif check[i] == 'y': # Yellow (in word)
            yellows.append(c)
            re_str += r'\w'
        else: # Unknown (any character)
            nots.append(c)
            re_str += r'\w'
    re_str += r'$'

    r = re.compile(re_str)

    matched_words = list(filter(r.match, all_words))

    for y in yellows:
        matched_words = list(filter(lambda x: y in x, matched_words))

    for n in nots:
        matched_words = list(filter(lambda x: n not in x, matched_words))
        
    return matched_words

def print_guesses(guesses):
    print("\nGuesses: ")
    print("------------------------------")
    for g in guesses:
        print(g, end=' ')
    print("\n------------------------------")
        

if __name__ == "__main__":
    main()
