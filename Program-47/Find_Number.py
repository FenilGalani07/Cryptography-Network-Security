def count_digits(number):

    return len(str(abs(number)))

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        digit_count = count_digits(user_input)
        print(f"The number of digits in {user_input} is: {digit_count}")
    except ValueError:
        print("Please enter a valid integer.")