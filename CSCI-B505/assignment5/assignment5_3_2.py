import random
import sys

def print_optimal_parens(s, i, j):
    """
    Prints optimal parenthesis
    :param s: list
    :param i: int
    :param j: int
    :return: str
    """
    optimal_parens = ""
    if i == j:
        optimal_parens += "A[{}]".format(i)
    else:
        optimal_parens += "("
        optimal_parens += print_optimal_parens(s, i, s[i][j])
        optimal_parens += "."
        optimal_parens += print_optimal_parens(s, s[i][j] + 1, j)
        optimal_parens += ")"
    return optimal_parens


def matrix_chain_order(p):
    """
    Matrix chain order
    :param p: list
    :return: None
    """
    n = len(p)
    m = [[0 for __ in range(n)] for _ in range(n)]
    s = [[0 for __ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + (p[i - 1] * p[k] * p[j])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    print("\nM:")
    for i in range(n):
        print("{}".format(m[i][0:n]))

    print("\nS:")
    for i in range(n):
        print("{}".format(s[i][0:n]))

    print("Optimal Parenthesis: {}".format(print_optimal_parens(s, 1, n - 1)))
    print("Minimum number of multiplications to multiply {} matrices: {}"
          "".format(n - 1, m[1][n - 1]))


dimension_array = [30, 35, 15, 5, 10, 20, 25]
matrix_chain_order(dimension_array)

for i in range(10):  # Random Values
    dimension_array = random.sample(range(1, 25), 6)
    matrix_chain_order(dimension_array)