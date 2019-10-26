class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        ll = []
        for i in range(1, int(A ** 0.5) + 1):
            if A % i == 0:
                ll.append(i)
                if i != A ** 0.5:
                    ll.append(int(A / i))
        ll.sort()
        return ll