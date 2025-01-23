# count_words.py

def count_words(string):

    words = string.split()
    return len(words)

if __name__ == "__main__":
    try:
        input_string = input("Enter a string: ")
        word_count = count_words(input_string)
        print(f"The number of words in the string is: {word_count}")
    except Exception as e:
        print("An error occurred:", e)