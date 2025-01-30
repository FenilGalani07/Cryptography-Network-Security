# remove_vowels.py

def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in input_string if char not in vowels])
    return result

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result_string = remove_vowels(input_string)
    print(f"String after removing vowels: {result_string}")
