
def get_book_text(path :str) -> str:
    with open(path) as f:
        return f.read()
    
def get_num_words(path: str) -> str:
    content = get_book_text(path)
    return f'Found {len((content.split()))} total words'

def count_characters(filepath):
    texts = list(get_book_text(filepath).lower())
    characters = set(texts)
    char_dict = {}
    for char in characters:
        char_count = 0
        for text in texts:
            if text == char:
                char_count += 1
        char_dict[char] = char_count
    return char_dict

def sort_on(items):
    return items["num"]

def book_report(filepath : str) -> list:
    char_counter = count_characters(filepath)
    char_list = []
    for char, count in char_counter.items():
        Character_details = {}
        Character_details["char"] = char
        Character_details["num"] = count
        char_list.append(Character_details)
        
    char_list.sort(reverse = True, key = sort_on)

    return char_list 

    