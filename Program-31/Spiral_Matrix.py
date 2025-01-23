# spiral_matrix.py

def generate_spiral_matrix(n):

    matrix = [[0] * n for _ in range(n)]

    left, right = 0, n - 1
    top, bottom = 0, n - 1
    num = 1

    while left <= right and top <= bottom:

        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1


        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1


        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1


        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    try:
        size = int(input("Enter the size of the spiral matrix (n x n): "))
        spiral_matrix = generate_spiral_matrix(size)
        print("Spiral Matrix:")
        print_matrix(spiral_matrix)
    except ValueError:
        print("Please enter a valid integer.")