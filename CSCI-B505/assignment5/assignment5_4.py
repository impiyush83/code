def precompute(X, Y, m, n, dp):
    """
    Returns precompute count
    :param X: str
    :param Y: str
    :param m: int
    :param n: int
    :param dp: list
    :return: int
    """
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

def lcs(dp, m, n):
    """
    Returns lcs string
    :param dp: list
    :param m: int
    :param n: int
    :return: str
    """
    index = dp[m][n]
    lcs_string = [""] * (index +1)
    lcs_string[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print(lcs_string)
    return "".join(lcs_string)


if __name__ == "__main__":
    X = "fabcded"
    Y = "fefefabcdxe"
    m = len(X)
    n = len(Y)
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    print("Length of LCS:", precompute(X, Y, m, n, dp))
    print(dp)
    print("LCS String", lcs(dp, m, n))
