from stats import get_num_words
from stats import get_num_characters
from stats import dic_sorter
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    counted = get_num_words(book_content)
    char_counts = get_num_characters(book_content)
    sorted_chars = dic_sorter(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {counted} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()

