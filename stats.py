def get_num_words(text):
    return len(text.split())

def get_count_characters(text):
    count_characters = {}
    for char in text:
        char = char.lower()
        if char not in count_characters:
            count_characters[char] = 1
        else:
            count_characters[char] += 1
    return count_characters

def sort_on(dict):
    return dict["num"]

def get_sorted_char_counts(count_chars):
    count_chars_list = []
    for key in count_chars:
        count_chars_list.append({"char": key, "num": count_chars[key]})
    count_chars_list.sort(reverse=True, key=sort_on)
    return count_chars_list
