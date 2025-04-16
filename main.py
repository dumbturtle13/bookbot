import sys
from stats import get_num_words, get_char_counts, sort_char_counts

# Проверяем, передали ли аргумент с путём к книге
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Завершаем программу с кодом ошибки 1

def main():
    path = sys.argv[1]  # Берём путь к книге из аргументов
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    with open(path) as f:
        file_contents = f.read()

    word_count = get_num_words(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_counts = get_char_counts(file_contents)
    sorted_chars = sort_char_counts(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
