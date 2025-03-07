def trim_whitespace(input_string):

    return input_string.strip()

if __name__ == "__main__":
    user_input = input("Enter a string with leading and/or trailing whitespace: ")
    trimmed_string = trim_whitespace(user_input)
    print(f"Trimmed String: '{trimmed_string}'")