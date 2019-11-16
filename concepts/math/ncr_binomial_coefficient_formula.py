def binomialCoeff(n, k):
    # default as 1
    res = 1
    # to reduce calculations
    if k > n - k:
        k = n - k

    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
