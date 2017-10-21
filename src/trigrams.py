"""Story maker using trigrams with existing txt files."""
from __future__ import print_function
import random
import textwrap


def main(file_path, num_of_words):
    """Story making function."""
    text_loaded = text_loader(file_path)
    stripped_text = text_stripper(text_loaded)
    word_list = list_maker(stripped_text)
    word_dict = dict_maker(word_list)
    starting_key = random_dictionary_key(word_dict)
    new_story = trigram_story_maker(word_dict, starting_key, num_of_words)
    print(textwrap.fill(new_story, 70), end='.\n\n\t\t\t~FIN\n\n')
    return textwrap.fill(new_story, 70)


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
        if key_word in trigram_dict:
            trigram_dict[key_word].append(word_list[idx + 2])
        else:
            try:
                trigram_dict[key_word] = [word_list[idx + 2]]
            except IndexError:
                pass
    return trigram_dict


def random_dictionary_key(dictionary):
    """Get random key from a dictionary."""
    random_key = random.choice(list(dictionary.keys()))
    return random_key


def trigram_story_maker(word_dict, starting_key, number_of_words):
    """Generate trigram story."""
    story_list = starting_key.split(' ')
    for i in range(number_of_words - 2):
        key_word = " ".join([story_list[i], story_list[i + 1]])
        if key_word in word_dict:
            story_list.append(random.choice(word_dict[key_word]))
        else:
            break
    new_book = ' '.join(story_list)
    return new_book

if __name__ == "__main__":  # pragma: no cover
    import sys
    main(sys.argv[1], int(sys.argv[2]))
