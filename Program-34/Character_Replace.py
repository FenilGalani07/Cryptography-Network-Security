# replace_character.py

def replace_character(string, index, new_char):
    if index < 0 or index >= len(string):
        return "Index out of range"


    new_string = string[:index] + new_char + string[index + 1:]
    return new_string

if __name__ == "__main__":
    try:
        original_string = input("Enter the original string: ")
        index = int(input("Enter the index of the character to replace: "))
        new_char = input("Enter the new character: ")

        result = replace_character(original_string, index, new_char)
        print("Resulting string:", result)
    except ValueError:
        print("Please enter a valid integer for the index.")
