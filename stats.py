def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_text):
    word_count = file_text.split()
    return len(word_count)

def count_characters(file_text):
    char_dict = dict()
    for char in file_text:
        charlow = char.lower()
        if charlow in char_dict:
            char_dict[charlow] += 1
        else:
            char_dict[charlow] = 1
    return char_dict

def sort_dict(unsorted_dict):
    new_list = list()
    for pair in unsorted_dict:
        if pair.isalpha():
            new_list.append({"char": pair, "num": unsorted_dict[pair]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(dict):
    return dict["num"]
