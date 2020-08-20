import random

def get_word():
    word_list = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    return random.choice(word_list)

def set_result_word(string):
    return '_' * len(string)

def letter_in_string(letter, string, res_string=''):
    res = list(set_result_word(string) if len(res_string) == 0 else res_string)
    for i, l in enumerate(string):
        if l == letter.lower():
            res[i] = l
    return ''.join(res)

