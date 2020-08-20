import pytest
from service import letter_in_string, set_result_word


def test_set_result_word_parametrized(word):
    assert set_result_word(word) == '_' * len(word)

def test_letter_in_string_parametrized(word, true_letter):
    if not true_letter in word:
        pytest.skip()
    assert true_letter in letter_in_string(true_letter, word)


def test_letter_uper_in_string_parametrized(word, true_letter):
    if not true_letter in word:
        pytest.skip()
    assert true_letter in letter_in_string(true_letter.upper(), word)


def test_all_letter_in_string_parametrized(word, all_letter):
    if all_letter in word:
        pytest.skip()
    assert not all_letter in letter_in_string(all_letter, word)