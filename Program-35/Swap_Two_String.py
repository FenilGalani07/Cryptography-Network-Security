# swap_strings.py

def swap_strings(str1, str2):
    print("Before swapping:")
    print("String 1:", str1)
    print("String 2:", str2)

    str1, str2 = str2, str1

    print("After swapping:")
    print("String 1:", str1)
    print("String 2:", str2)

if __name__ == "__main__":
    try:
        string1 = input("Enter the first string: ")
        string2 = input("Enter the second string: ")
        swap_strings(string1, string2)
    except Exception as e:
        print("An error occurred:", e)