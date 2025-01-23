# palindrome.py

def is_palindrome(number):

    num_str = str(number)
    return num_str == num_str[::-1]

if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Negative numbers are not considered palindromes.")
        else:
            if is_palindrome(number):
                print(f"{number} is a palindrome.")
            else:
                print(f"{number} is not a palindrome.")
    except ValueError:
        print("Please enter a valid integer.")