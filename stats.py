def get_word_count(book_text):
    words = book_text.split()
    return len(words)


def get_char_count_dict(book_text):
    chars = {}
    for char in book_text.lower():
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1
    return chars


def get_sorted_char_list(char_count_dict):
    char_list = []
    for char, count in char_count_dict.items():
        char_list.append({"char": char, "num": count})

    def get_count(dictionary):
        return dictionary["num"]

    char_list.sort(key=get_count, reverse=True)
    return char_list
