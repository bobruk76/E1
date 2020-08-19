from service import get_word

set_word = ''
result_word = ''
def main():
    set_word = get_word()
    result_word = '_' * len(set_word)
    while True:
        letter = input("Введите букву:")
        print('{} -- {}'.format(set_word,result_word))

if __name__ == '__main__':
    main()
