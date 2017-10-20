"""Test module for trigrams module."""
# import pytest

TEST_DATA = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
TEST_DATA_2 = "Lorem ipsum dolor sit amet consectetur adipiscing elit"


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
