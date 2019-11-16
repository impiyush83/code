class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        i = 5
        count = 0
        while A / i >= 1:
            count += int(A / i)
            i *= 5
        return int(count)
