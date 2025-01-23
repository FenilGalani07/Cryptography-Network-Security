# count_digits.py

def count_digits(number):

    if number < 0:
        number = -number

    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

if __name__ == "__main__":
    try:
        number = int(input("Enter an integer: "))
        if number == 0:
            print("The number of digits in 0 is: 1")
        else:
            digit_count = count_digits(number)
            print(f"The number of digits in {number} is: {digit_count}")
    except ValueError:
        print("Please enter a valid integer.")