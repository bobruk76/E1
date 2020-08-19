import random

def get_word():
    word_list = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    return random.choice(word_list)

def letter_in_string(letter, string, res_string):
    res = ''
    for i, l in enumerate(string):
        res += string[i] if string[i] == letter else res_string[i]
    return res

