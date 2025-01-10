def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count_words(text)
    count_characters(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    word_count = 0
    words = book.split()
    for word in words:
        word_count += 1
    print("word count: " + str(word_count))

def count_characters(book):
    char_count = {}
    for character in book:
        if character.isalpha():
            letter = character.lower()
            if letter in char_count:
                char_count[letter] += 1
            else:
                 char_count[letter] = 1
    
    char_list = []
    for letter in char_count:
        char_list.append({'letter': letter, 'count': char_count[letter]})

    def sort_on(dict):
        return dict['count']

    char_list.sort(reverse=True, key=sort_on)

    for char_dict in char_list:
        #count = char_count[letter]
        #print(char_list[1])
        print(f"The '{char_dict['letter']}' character was found {char_dict['count']} times")

main()