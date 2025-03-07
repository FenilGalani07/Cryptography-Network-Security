def capitalize_first_character(input_string):
    if input_string:
        return input_string[0].upper() + input_string[1:]
    return input_string

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    capitalized_string = capitalize_first_character(user_input)
    print(f"Capitalized String: {capitalized_string}")