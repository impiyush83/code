def brute_non_overlapping_string_counter(D, P):
    """
    Brute force string matching algorithm
    :param D: string
    :param P:  string
    :return: boolean
    """

    n, m = len(D), len(P)
    counter = 0
    skip = 0

    for i in range(n - m + 1):

        if skip:
            skip -= 1
            continue

        k = 0

        while k < m and D[i+k] == P[k]:
            k += 1

        if k == m:
            counter += 1
            skip = m - 1

    return counter


if __name__ == '__main__':
    H = "bc" * pow(10, 5)
    H += "aaaa"
    N = "aa"
    print(brute_non_overlapping_string_counter(H, N))
