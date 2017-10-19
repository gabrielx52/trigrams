"""Story maker using trigrams with existing txt files."""


def main(path_to_source_file, number_of_words):
    """."""
    pass


def text_loader(text_file):
    """Load text file and return data."""
    with open(text_file, "r") as my_file:
        data = my_file.read()
    return data


def text_stripper(text_data):
    """Strip newline character and punctuation."""
    no_new_lines = text_data.replace('\n', ' ').replace('-', ' ')
    stripped_text = ''.join([char for char in no_new_lines
                             if char.isalpha() or char == ' '])
    return stripped_text


def list_maker(stripped_text):
    """Convert text data into list of words in same order."""
    word_list = [word for word in stripped_text.split(' ') if word.isalpha()]
    return word_list


def dict_maker(word_list):
    """Make dict with trigram key value pairs."""
    
