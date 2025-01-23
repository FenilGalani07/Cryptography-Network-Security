# camel_case_check.py

def is_camel_case(input_string):

    if not input_string or not input_string[0].islower():
        return False


    for char in input_string:
        if char.isupper() and input_string.index(char) != 0:
            continue
        elif char == '_':
            return False
    return True

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if is_camel_case(input_string):
        print(f"The string '{input_string}' is in Camel Case.")
    else:
        print(f"The string '{input_string}' is not in Camel Case.")