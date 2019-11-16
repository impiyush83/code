from math import sqrt


def nth_fibonacci_formula(n):
    """
    Gives nth fibonacci number but cause overflow error if number larger

    :param n: integer
    :return: nth fibonacci number
    """
    phi = (1 + sqrt(5)) / 2
    return round(pow(phi, n) / sqrt(5))

