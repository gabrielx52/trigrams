"""Story maker using trigrams with existing txt files."""


def main(file):
    """."""
    dict_maker(list_maker(text_stripper(text_loader(file))))
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
    trigram_dict = {}
    for idx in range(len(word_list) - 1):
        key_word = ' '.join([word_list[idx], word_list[idx + 1]])
        print(key_word)
        if key_word in trigram_dict:
            trigram_dict[key_word].append(word_list[idx + 2])
        else:
            try:
                trigram_dict[key_word] = [word_list[idx + 2]]
            except IndexError:
                pass
    return trigram_dict
