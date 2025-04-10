from stats import get_num_words, get_num_chars, sort_chars
import sys

def get_book_text(file):
    with open(file) as file:
        f = file.read()
    return f

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    num_chars = get_num_chars(get_book_text(book))
    num_words = get_num_words(get_book_text(book))
    sorted_chars = sort_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in sorted_chars.items():
        print(f"{k}: {v}")
    print("============= END ===============")

if __name__ == "__main__":
    main()