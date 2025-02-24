# isomorphic_strings.py

def are_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    mapping = {}
    mapped_values = set()

    for char1, char2 in zip(str1, str2):
        if char1 in mapping:
            if mapping[char1] != char2:
                return False
        else:
            if char2 in mapped_values:
                return False
            mapping[char1] = char2
            mapped_values.add(char2)

    return True

if __name__ == "__main__":
    try:
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")

        if are_isomorphic(str1, str2):
            print(f"The strings '{str1}' and '{str2}' are isomorphic.")
        else:
            print(f"The strings '{str1}' and '{str2}' are not isomorphic.")
    except Exception as e:
        print("An error occurred:", e)
