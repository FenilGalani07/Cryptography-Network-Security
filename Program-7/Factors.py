# factors.py

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer: "))
        if number < 1:
            print("Please enter a positive integer greater than 0.")
        else:
            factors = find_factors(number)
            print(f"Factors of {number}: {', '.join(map(str, factors))}")
    except ValueError:
        print("Please enter a valid integer.")