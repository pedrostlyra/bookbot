from stats import get_number_of_words
from stats import generate_dictionary
from stats import sort_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_number_of_words(book_text)
    char_dictionary = generate_dictionary(book_text)
    print(f"============ BOOKBOT ============\n")
    print(f"Analyzing book found at {sys.argv[1]}...\n")
    print(f"----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print(f"--------- Character Count -------\n")
    dict_list = sort_dict(char_dictionary)
    for dicti in dict_list:
        print(f"{dicti['charact']}: {dicti['count']}\n") 
    print(f"============= END ===============")

main()