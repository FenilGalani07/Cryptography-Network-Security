# armstrong.py

def is_armstrong(number):
    num_str = str(number)
    num_length = len(num_str)
    armstrong_sum = sum(int(digit) ** num_length for digit in num_str)
    return armstrong_sum == number

if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Armstrong numbers are defined for non-negative integers only.")
        else:
            if is_armstrong(number):
                print(f"{number} is an Armstrong number.")
            else:
                print(f"{number} is not an Armstrong number.")
    except ValueError:
        print("Please enter a valid integer.")