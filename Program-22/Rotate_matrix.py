# rotate_matrix.py

def rotate_matrix(matrix):

    rotated = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            rotated[j][len(matrix) - 1 - i] = matrix[i][j]

    return rotated

if __name__ == "__main__":

    print("Enter a 3x3 matrix (row by row, space-separated):")
    matrix = []
    for _ in range(3):
        row = list(map(int, input().split()))
        while len(row) != 3:
            print("Please enter exactly 3 numbers for the row.")
            row = list(map(int, input().split()))
        matrix.append(row)


    rotated_matrix = rotate_matrix(matrix)

    print("Rotated Matrix:")
    for row in rotated_matrix:
        print(" ".join(map(str, row)))
