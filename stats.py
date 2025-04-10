def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words

def get_num_chars(book_text):
    book = book_text.lower()
    chars_dict = {}

    for char in book:
        if char.isalpha():
            chars_dict[char] = chars_dict.get(char, 0) + 1

    return chars_dict

def sort_chars(book_dict):
    return dict(sorted(book_dict.items(), key=lambda item: item[1], reverse=True))