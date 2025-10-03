from stats import get_book_text , count_word , count , sorted_count
import sys

def main():
    if len(sys.argv) < 2 : 
        print(" - 'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    
    #print(count(book_text))
    sorted_list = sorted_count(count(book_text))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found",count_word(book_text),"total words")
    for dic in sorted_list:
        for key , value in dic.items():
            print(key+":",value)
    
if __name__ == "__main__":
    main()