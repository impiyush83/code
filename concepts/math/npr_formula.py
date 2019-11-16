import math


def fact(n):
    if n <= 1:
        return 1

    return n * fact(n - 1)


def nPr(n, r):
    return math.floor(fact(n) / fact(n - r))
