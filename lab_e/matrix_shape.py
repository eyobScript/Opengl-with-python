def find_matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    return (rows, cols)
