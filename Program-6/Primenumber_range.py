# prime_range.py

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        if start < 0 or end < 0:
            print("Please enter non-negative integers for the range.")
        elif start > end:
            print("Start of the range should be less than or equal to the end.")
        else:
            prime_numbers = find_primes_in_range(start, end)
            print(f"Prime numbers between {start} and {end}: {prime_numbers}")
    except ValueError:
        print("Please enter valid integers.")