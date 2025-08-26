from stats import get_book_text, count_characters, sort_characters, count_words
import sys


def print_report(book_path, text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_counts = sort_characters(char_counts)

    for item in sorted_counts:
        print(f"{item['char']}: {item['count']}")  # ✅ Fixed key name

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path).lower()  # ✅ Better function name
    print_report(book_path, text)


if __name__ == "__main__":
    main()