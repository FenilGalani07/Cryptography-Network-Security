# square_hollow_pattern.py

def draw_square_hollow(size):
    for i in range(size):
        for j in range(size):
            # Print '*' for the border and ' ' for the hollow part
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  # Move to the next line

if __name__ == "__main__":
    try:
        size = int(input("Enter the size of the square: "))
        if size < 2:
            print("Size should be 2 or greater.")
        else:
            draw_square_hollow(size)
    except ValueError:
        print("Please enter a valid integer.")
