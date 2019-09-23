from math import pow


def fib(precompute, n):
    precompute[0] = 0
    precompute[1] = 1
    for i in range(2, n):
        precompute[i] = (precompute[i - 1] + precompute[i - 2]) % 10
    return precompute


i = 1
results = [1, 2]
while results[i] < 10000000000000000000:
    results.append(results[i] * 2)
    i = i + 1


def closest_two_raise_to_n(n):
    for i in range(0, len(results)):
        if results[i] > n:
            break
    p = i - 1
    if i == 0:
        p = 0
    return int(pow(2, p)) % 60


if __name__ == "__main__":
    t = int(input())
    precomputed_fib = [0] * 60
    precomputed_fib = fib(precomputed_fib, 60)
    # print(precomputed_fib)
    while t:
        n = int(input())
        index = closest_two_raise_to_n(n)
        if index == 0:
            print(precomputed_fib[59])
        else:
            print(precomputed_fib[index - 1])
        t -= 1
