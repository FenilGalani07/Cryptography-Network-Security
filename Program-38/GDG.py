# gcd.py

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        result = gcd(num1, num2)
        print(f"The GCD of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid integers.")