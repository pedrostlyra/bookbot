def get_number_of_words(text):
    number_of_words = 0
    words = text.split()
    for word in words:
        number_of_words += 1
    return number_of_words

def generate_dictionary(text):
    char_dictionary = {}
    letters = list(text.lower())
    for letter in letters:
        if char_dictionary.get(letter) is not None:
            char_dictionary[letter] = 0
        else:
            char_dictionary[letter] = 0
    for charachter in char_dictionary:
        num_chars = 0
        for char in letters:
            if char == charachter:
                num_chars += 1
                char_dictionary[charachter] = num_chars

    return char_dictionary

def sort_dict(dictionary):
    new_list = []
    for char in dictionary:
        if char.isalpha() == True:
            new_list.append({"charact": char, "count":dictionary[char]})
            new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(dict):
    return dict["count"]