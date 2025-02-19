# pyramid_pattern.py

def print_pyramid_pattern(n):
    for i in range(n):

        print(' ' * (n - i - 1), end='')

        print('*' * (2 * i + 1))

if __name__ == "__main__":
    try:
        rows = int(input("Enter the number of rows for the pyramid pattern: "))
        print_pyramid_pattern(rows)
    except ValueError:
        print("Please enter a valid integer.")
