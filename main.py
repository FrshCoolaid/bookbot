import sys
from stats import get_num_words, get_num_char, sorted_chars_dict

def main():
    if len(sys.argv) > 1:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book)
    num_char = get_num_char(text)
    number = get_num_words(text)
    sorted_chars = sorted_chars_dict(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        num = item ["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()    

main()