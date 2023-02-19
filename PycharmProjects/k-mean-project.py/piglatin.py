import sys
print(sys.path)
print(dir())

def piglatin_converter(text):
    vowels = 'aeiou'
    if text[0] in vowels:
        pig_word = text + 'way'
        return pig_word
    else:
        pig_word = text[1:] + text[0] + 'ay'
        return pig_word

word = input('Give a word: ')
pig_word = piglatin_converter(word.lower())
print(pig_word)


