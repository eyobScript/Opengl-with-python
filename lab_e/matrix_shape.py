def find_matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    return (rows, cols)
#1, Write a python function named find_matrix_shape that can take
# an matrix as a parameter and returns the shape of a matrix.
# def find_matrix_shape(matrix):