from stats import word_count
from stats import character_count

def get_book_text(file):
    with open(file) as f:
        file_content = f.read()
        return file_content
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {word_count(book_text)} total words")
    print(character_count(book_text))

main()