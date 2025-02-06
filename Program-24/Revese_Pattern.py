# reverse_pattern.py

def print_reverse_pattern(n):
    for i in range(1, n + 1):

        print(' ' * (n - i), end='')

        print((str(i) + ' ') * i)

if __name__ == "__main__":
    try:
        size = int(input("Enter the number of rows for the pattern: "))
        print_reverse_pattern(size)
    except ValueError:
        print("Please enter a valid integer.")
