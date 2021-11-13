"""

The brute algorithm will run in O(DP) if P is found at the last substring of D

"""

def find_brute(D, P):
    """
    Brute force string matching algorithm
    :param D: string
    :param P:  string
    :return: boolean
    """

    n, m = len(D), len(P)
    for i in range(n - m + 1):
        k = 0
        while k < m and D[i+k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1


if __name__ == '__main__':
    H = "bbbabbbabbbabbbabbbabbbabbbc"
    N = "bbbc"
    print(find_brute(H, N))