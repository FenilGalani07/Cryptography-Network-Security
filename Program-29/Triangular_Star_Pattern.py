# diamond_pattern.py

def print_diamond_pattern(n):

    for i in range(n):

        print(' ' * (n - i - 1), end='')

        print('*' + ' ' * (2 * i - 1) + '*' * (i > 0))


    for i in range(n - 2, -1, -1):

        print(' ' * (n - i - 1), end='')

        print('*' + ' ' * (2 * i - 1) + '*' * (i > 0))

if __name__ == "__main__":
    try:
        rows = int(input("Enter the number of rows for the diamond pattern: "))
        print_diamond_pattern(rows)
    except ValueError:
        print("Please enter a valid integer.")
