from stats import get_num_words, count_chars, sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    diccionario = count_chars(text)
    diccionario = sort_dict(diccionario)
    for i in diccionario:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")



main()