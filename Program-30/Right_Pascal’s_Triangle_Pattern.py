# right_pascals_triangle.py

def print_right_pascals_triangle(n):

    for i in range(n):

        print(' ' * i, end='')
        print('* ' * (n - i))
    for i in range(1, n):

        print(' ' * (n - i - 1), end='')
        print('* ' * (i + 1))

if __name__ == "__main__":
    try:
        rows = int(input("Enter the number of rows for Right Pascal's Triangle: "))
        print_right_pascals_triangle(rows)
    except ValueError:
        print("Please enter a valid integer.")