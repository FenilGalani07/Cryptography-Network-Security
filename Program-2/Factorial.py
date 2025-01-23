# factorial.py

def factorial(n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i

    return dp[n]

if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(number)
            print(f"The factorial of {number} is: {result}")
    except ValueError:
        print("Please enter a valid integer.")