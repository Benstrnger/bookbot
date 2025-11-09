def get_num_words(text):
    text = text.split()
    return f"Found {len(text)} total words"

def count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict(chars_dict):
    # Step 1: Convert dictionary into list of {"char": c, "num": n}
    lista_dict = []
    for c, n in chars_dict.items():
        lista_dict.append({"char": c, "num": n})

    # Step 2: Helper function for sorting key
    def get_num(item):
        return item["num"]

    # Step 3: Sort list in place (descending order)
    lista_dict.sort(key=get_num, reverse=True)

    # Step 4: Return the sorted list
    return lista_dict

