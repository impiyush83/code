import random
import string
import matplotlib.pyplot as plt

def find_brute(D, P):
    """
    Brute force string matching algorithm
    :param D: string
    :param P:  string
    :return: boolean
    """
    checks = 0
    n, m = len(D), len(P)
    for i in range(n - m + 1):
        k = 0
        checks += 1
        while k < m and D[i+k] == P[k]:
            k += 1
        if k == m:
            return i, checks
    return -1, checks


def find_boyer_moore(T, P):
    """
    Boyer moore
    :param T: string
    :param P: string
    :return: int
    """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    checks = 0
    i = m-1
    k = m-1
    while i < n:
        checks += 1
        if T[i] == P[k]:
            if k == 0:
                break
            else:
                i -= 1
                k -= 1
        # Not match , reset the positions
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m - 1
    return -1, checks


def compute_kmp_fail(P):
    """
    KMP Compute string function
    :param P: string
    :return: list
    """
    m = len(P)
    fail = [0]*m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j +=1
    return fail

def find_kmp(T, P):
    """
    KMP string matching algorithm
    :param T: string
    :param P:  string
    :return: boolean
    """
    checks = 0
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        checks += 1
        if T[j] == P[k]:
            if k == m-1:
                return j-m+1, checks
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1, checks


if __name__ == "__main__":
    N = 10
    brute_time = []
    boyer_time = []
    kmp_time = []
    algorithm_size = []
    while N < 1000000:
        hay = ''.join(random.choice(string.ascii_lowercase) for _ in range(N))
        key = hay[-5:-1]

        algorithm_size.append(N)

        _, checks = find_brute(hay, key)
        brute_time.append(checks)

        _, checks = find_boyer_moore(hay, key)
        boyer_time.append(checks)

        _, checks = find_kmp(hay, key)
        kmp_time.append(checks)
        N = N * 10

    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title('Algorithm runtime analysis')
    plt.loglog(algorithm_size, brute_time, label='brute')
    plt.loglog(algorithm_size, boyer_time, label='boyer')
    plt.loglog(algorithm_size, kmp_time, label='kmp')
    plt.legend(["brute", "boyer", "kmp"])
    plt.show()
