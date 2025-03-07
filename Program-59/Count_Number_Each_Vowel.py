def count_vowels(input_string):

    vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    input_string = input_string.lower()

    # Count each vowel in the string
    for char in input_string:
        if char in vowels_count:
            vowels_count[char] += 1

    return vowels_count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    vowel_counts = count_vowels(user_input)

    print("Vowel counts:")
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count}")