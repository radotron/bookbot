def get_book_text(file_path):  # ✅ Better function name
    with open(file_path, "r") as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


def sort_on(item):
    return item["count"]  # ✅ Fixed key name to match what's created


def sort_characters(char_counts):
    new_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # Only count alphabetical characters
            new_list.append({"char": char, "count": count})

    new_list.sort(reverse=True, key=sort_on)
    return new_list