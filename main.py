import sys
from stats import get_word_count, get_char_count_dict, get_sorted_char_list


def get_book_text(books_path):
    with open(books_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    books_path = sys.argv[1]
    book_text = get_book_text(books_path)
    num_words = get_word_count(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {books_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_count_dict = get_char_count_dict(book_text)
    sorted_char_list = get_sorted_char_list(char_count_dict)
    for char_dict in sorted_char_list:
        print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
