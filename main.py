import sys
from stats import *

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

words = count_words(get_book_text(sys.argv[1]))
char_dict = count_characters(get_book_text(sys.argv[1]))
sorted_dict = sort_dict(char_dict)

print("============ BOOKBOT ============")
print(f"Analyzing book fount at {sys.argv[1]}")
print("----------- Word Count ----------")
print(f"Found {words} total words")
print("--------- Character Count -------")
for pair in sorted_dict:
    print(f"{pair["char"]}: {pair["num"]}")
print("============== END ==============")
