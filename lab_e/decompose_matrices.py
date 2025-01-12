import numpy as np

def decompose_matrices(array):
    U, S, V = np.linalg.svd(array)
    return U, S, V
#2, Write a python function named decompose_matrices that can an
# array as a parameter and returns 3 decomposed matrices using
# singular value decomposition technique.