def count_character_occurrences(input_string, character):

    count = 0


    for char in input_string:

        if char == character:
            count += 1

    return count


if __name__ == "__main__":

    user_string = input("Enter a string: ")

    user_character = input("Enter the character to count: ")

    if len(user_character) != 1:
        print("Please enter a single character.")
    else:

        occurrences = count_character_occurrences(user_string, user_character)
        print(f"The character '{user_character}' occurs {occurrences} times in the string.")