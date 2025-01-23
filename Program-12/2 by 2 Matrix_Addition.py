# matrix_sum.py

def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements of the matrix (space-separated):")
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) != cols:
                    print(f"Please enter exactly {cols} elements.")
                else:
                    matrix.append(row)
                    break
            except ValueError:
                print("Invalid input. Please enter integers only.")
    return matrix

def sum_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

if __name__ == "__main__":
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        print("Matrix 1:")
        matrix1 = input_matrix(rows, cols)

        print("Matrix 2:")
        matrix2 = input_matrix(rows, cols)

        result_matrix = sum_matrices(matrix1, matrix2)

        print("\nSum of the two matrices:")
        for row in result_matrix:
            print(" ".join(map(str, row)))

    except ValueError:
        print("Please enter valid integers for the number of rows and columns.")