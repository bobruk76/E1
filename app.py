from service import get_word, letter_in_string

def main():
    points = 0
    set_word = get_word()
    result_word = '_' * len(set_word)
    print('{} -- {}'.format(set_word, result_word))
    while set_word != result_word and points < 4:
        letter = input("Введите букву:")
        if letter in set_word:
            result_word = letter_in_string(letter, set_word, result_word)
        else:
            points += 1

        print('{} Штрафных очков:{}'.format(result_word, points))
    if points < 4:
        print('Вы выиграли!')
    else:
        print('Вы проиграли!')

if __name__ == '__main__':
    main()
