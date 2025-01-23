# find_word.py

def find_word_in_string(string, word):

    if word in string:
        return f"The word '{word}' is found in the string."
    else:
        return f"The word '{word}' is not found in the string."

if __name__ == "__main__":
    try:
        input_string = input("Enter a string: ")
        word_to_find = input("Enter the word to find: ")

        result = find_word_in_string(input_string, word_to_find)
        print(result)
    except Exception as e:
        print("An error occurred:", e)