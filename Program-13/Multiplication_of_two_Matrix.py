# matrix_multiplication.py

def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} elements.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")


    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

if __name__ == "__main__":
    try:
        rows1 = int(input("Enter the number of rows for the first matrix: "))
        cols1 = int(input("Enter the number of columns for the first matrix: "))

        print("Matrix 1:")
        matrix1 = input_matrix(rows1, cols1)

        rows2 = int(input("Enter the number of rows for the second matrix: "))
        cols2 = int(input("Enter the number of columns for the second matrix: "))

        print("Matrix 2:")
        matrix2 = input_matrix(rows2, cols2)

        result_matrix = multiply_matrices(matrix1, matrix2)

        print("Result of the multiplication:")
        for row in result_matrix:
            print(" ".join(map(str, row)))

    except ValueError as e:
        print(e)
