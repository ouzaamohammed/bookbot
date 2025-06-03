from stats import get_num_words, get_count_characters, get_sorted_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    count_characters = get_count_characters(text)
    sorted_count_characters_list = get_sorted_char_counts(count_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count_char in sorted_count_characters_list:
        if count_char["char"].isalpha():
            print(f"{count_char["char"]}: {count_char["num"]}")
    print("============= END ===============")

main()
