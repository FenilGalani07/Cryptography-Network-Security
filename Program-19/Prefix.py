# longest_common_prefix.py

def longest_common_prefix(strs):
    if not strs:
        return ""


    prefix = strs[0]

    for string in strs[1:]:

        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

    return prefix

if __name__ == "__main__":
    input_strings = input("Enter strings separated by commas: ").split(',')
    input_strings = [s.strip() for s in input_strings]
    result_prefix = longest_common_prefix(input_strings)
    print(f"The longest common prefix is: '{result_prefix}'")
