# remove_duplicates.py

def remove_duplicates(input_string):

    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result_string = remove_duplicates(input_string)
    print(f"String after removing duplicates: {result_string}")
