# pattern.py

def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

if __name__ == "__main__":
    try:
        rows = int(input("Enter the number of rows for the pattern: "))
        print_pattern(rows)
    except ValueError:
        print("Please enter a valid integer.")