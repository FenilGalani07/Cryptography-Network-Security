# multiplication_table.py

def print_multiplication_table(number):
    print(f"Multiplication Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        number = int(input("Enter a number to print its multiplication table: "))
        print_multiplication_table(number)
    except ValueError:
        print("Please enter a valid integer.")