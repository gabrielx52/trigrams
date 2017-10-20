"""Test module for trigrams module."""
# import pytest

TEST_DATA = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
TEST_DATA_2 = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
TEST_DICT = {'a': 1, 'b': 2, 'c': 3}


def test_text_loader():
    """Test text_loader function from trigrams module."""
    from trigrams import text_loader
    assert text_loader('text/text_test.txt').startswith(TEST_DATA)


def test_text_stripper():
    """Test text_stripper function from trigrams module."""
    from trigrams import text_loader, text_stripper
    assert text_stripper(text_loader('text/text_test.txt'))\
        .startswith(TEST_DATA_2)


def test_list_maker():
    """Test list_maker function from trigrams module."""
    from trigrams import text_loader, text_stripper, list_maker
    assert type(list_maker(text_stripper(text_loader(
        'text/text_test.txt')))) is list


def test_dict_maker():
    """Test dict_maker function from trigrams module."""
    from trigrams import text_loader, text_stripper, list_maker, dict_maker
    assert type(dict_maker(list_maker(text_stripper(
        text_loader('text/text_test.txt'))))) is dict


def test_random_dictionary_key():
    """Test random_dictionary_key function from trigrams module."""
    from trigrams import random_dictionary_key
    assert random_dictionary_key(TEST_DICT) in TEST_DICT


def test_main():
    """Test trigrams main function."""
    import trigrams
    assert len(trigrams.main('text/text_test.txt', 5).split(' ')) == 5
