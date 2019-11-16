class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A == 0 and B == 0:
            return 0
        if A and not B:
            return A
        if B and not A:
            return B
        mini = min(A, B)
        for i in range(mini, 0, -1):
            if A % i == 0 and B % i == 0:
                return i
