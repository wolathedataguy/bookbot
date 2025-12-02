import sys
from stats import get_num_words, count_characters, book_report


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]
    
word_count = get_num_words(filepath)
char_count = count_characters(filepath)
report_stats = book_report(filepath)

first_part  = f"""============ BOOKBOOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
{word_count}
--------- Character Count -------"""
print(first_part)
for item in report_stats:
    if item['char'].isalpha(): 
        char_stat = f"{item['char']}: {item['num']}"
        print(char_stat)
ending_part = "============ END ==============="
print(ending_part)
