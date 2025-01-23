# prime.py

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Negative numbers are not considered prime.")
        else:
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")