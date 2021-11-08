def brute_force_string_matching(D, P):
    """
    Brute force string matching algorithm
    :param D: string
    :param P:  string
    :return: boolean
    """

    for i in range(0, len(D) - len(P) + 1):
        cnt = 0
        for j in range(0, len(P)):
            print(D[i+j], P[j])
            if D[i+j] == P[j]:
                cnt += 1
        if cnt == len(P):
            return True
    return False


print(brute_force_string_matching("accab", "ab"))