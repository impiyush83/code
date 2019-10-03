class Solution:
    # @param A : integer
    # @return a list of integers
    # sieve implemented
    def sieve(self, A):
        primes = []
        for i in range(0, A + 1):
            primes.append(1)
        primes[0] = 0
        primes[1] = 0
        for i in range(2, int(A ** 0.5) + 1):
            if primes[i] == 1:
                j = 2
                while j:
                    if i * j > A:
                        break
                    primes[i * j] = 0
                    j += 1
        ans = []
        for i in range(0, A + 1):
            if primes[i] == 1:
                ans.append(i)

        return ans