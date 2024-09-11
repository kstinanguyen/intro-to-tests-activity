from main import count_a_letter
import pytest

def test_sentence_is_empty():
    sentence = ""
    letter = "a"
    result = count_a_letter(sentence, letter)
    assert result == None

def test_letter_is_not_a_letter():
    sentence = "@pple"
    letter = "@"
    result = count_a_letter(sentence, letter)
    assert result == None

def test_sentence_with_letter_in_it():
    sentence = "Tasty apple"
    letter = "a"
    result = count_a_letter(sentence, letter)
    assert result == 2

def test_when_there_are_two_letter_inputs():
    sentence = "Tasty apple"
    letter = "aa"
    if not count_a_letter(sentence, letter):
        assert "Input a single letter"

def test_when_letter_input_is_left_empty():
    sentence = "Tasty apple"
    letter = ""
    if not count_a_letter(sentence, letter):
        assert "Input a single letter"

# def test_demo_two():
    # num_1 = 18
    # num_2 = 24

    # result = num_1 + num_2

    # assert result == 42
# Delete the demo tests and add your tests here 