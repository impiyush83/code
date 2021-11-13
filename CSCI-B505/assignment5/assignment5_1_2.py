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

def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while i < n:
        # If match , decrease i,k
        if T[i] == P[k]:
            if k == 0:
                print(i)
                break
            else:
                i -= 1
                k -= 1
        # Not match , reset the positions
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m - 1
    return -1


if __name__ == '__main__':
    H = "bcaa"
    N = "aa"
    #print(brute_non_overlapping_string_counter(H, N))
    print(find_boyer_moore(H, N))
