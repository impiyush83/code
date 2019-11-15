from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return self.pascals(numRows)

    def pascals(self, numRows):
        ans = []
        for line in range(0, numRows):
            temp = []
            for i in range(0, line + 1):
                temp.append(self.binomialCoeff(line, i))
            ans.append(temp)
        return ans

    def binomialCoeff(self, n, k):
        res = 1
        if k > n - k:
            k = n - k
        for i in range(0, k):
            res = res * (n - i)
            res = res // (i + 1)

        return res
