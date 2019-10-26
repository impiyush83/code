def fast_expo(a, n, mod):
    """
        This is a reursive solution
    :param a:
    :param n:
    :param mod:
    :return:
    """
    if n == 0:
        return 1
    x = fast_expo(a, int(n / 2), mod)
    if n % 2 == 0:
        return pow(x, 2) % mod
    else:
        return a * pow(x, 2) % mod


def fast_expo_iter(a, n, mod):
    """
        This is a iterative solution
    :param a:
    :param n:
    :param mod:
    :return:
    """
    ans = 1
    while n > 0:
        if n & 1:  # CHECKS IF ODD OR NOT GIVES RETURNS 1 IF ODD
            ans = (ans * a) % mod
        a = (a * a) % mod
        n = int(n / 2)
    return ans


num = int(input())
power = int(input())
MOD = 100000007
print("Recursive soln:")
print(fast_expo(num, power, MOD))
print()
print("Iterative soln:")
print(fast_expo_iter(num, power, MOD))
