import random
import sys

def get_matrix_dimension():
    """
    Accepts matrix dimensions
    :return: list
    """
    first_matrix = input("Enter the dimensions (p) of the matrices you want to"
                         " multiply (separated by space):\n")
    return [int(j) for j in first_matrix.split()]

def brute_matrix_multiplication(p, i, j):
    """
    Brute matrix multiplication
    :param p: list
    :param i: int
    :param j: int
    :return int
    """
    if i == j:
        return 0
    n = len(p)
    m = [[0 for __ in range(n)] for _ in range(n)]
    m[i][j] = sys.maxsize

    for k in range(i, j):
        q = brute_matrix_multiplication(p, i, k) \
             + brute_matrix_multiplication(p, k + 1, j) \
             + (p[i - 1] * p[k] * p[j])

        if q < m[i][j]:
            m[i][j] = q

    return m[i][j]


def inject_matrix(matrix_dimensions):
    """
    Sends a matrix for multiplication
    :param matrix_dimensions: list
    :return: None
    """
    print("\nMatrices' Dimensions:")
    for i in range(len(matrix_dimensions) - 1):
        print("\t[{}],[{}]".format(matrix_dimensions[i],
                                   matrix_dimensions[i + 1]))
    min_mul = brute_matrix_multiplication(matrix_dimensions, 1, len(matrix_dimensions) - 1)
    print(
        "Minimum number of multiplications to multiply {} matrices: {}".format(
            len(matrix_dimensions) - 1, min_mul))


dimension_array = [30, 35, 15, 5, 10, 20, 25]
inject_matrix(dimension_array)

for _ in range(10):  # Random Values
    dimension_array = random.sample(range(1, 25), 6)
    inject_matrix(dimension_array)