def sort_words(input_string):

    words = input_string.split()
    words.sort()
    return words

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    sorted_words = sort_words(user_input)

    print("Sorted words in alphabetical order:")
    print(", ".join(sorted_words))