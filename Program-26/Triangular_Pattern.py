# triangle_pattern.py

def print_triangle_pattern(n):
    current_number = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(current_number, end=' ')
            current_number += 1
        print()

if __name__ == "__main__":
    try:
        rows = int(input("Enter the number of rows for the triangle pattern: "))
        print_triangle_pattern(rows)
    except ValueError:
        print("Please enter a valid integer.")
