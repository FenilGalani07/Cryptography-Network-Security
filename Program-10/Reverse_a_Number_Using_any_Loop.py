# reverse_number.py

def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num

if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            print("Please enter a positive integer.")
        else:
            reversed_num = reverse_number(number)
            print(f"The reversed number is: {reversed_num}")
    except ValueError:
        print("Please enter a valid integer.")