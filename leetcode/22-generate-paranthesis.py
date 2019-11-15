class Solution:
    def fun(self, n, noOpeningB, noClosingB, stringFormed):
        if noOpeningB == n and noClosingB == n:
            yield stringFormed
            return

        if stringFormed:
            if stringFormed[0] == '}':
                return

        if noOpeningB < noClosingB:
            return

        if noOpeningB != n:
            yield from self.fun(n, noOpeningB + 1, noClosingB,
                                stringFormed + '(')

        if noClosingB != n:
            yield from self.fun(n, noOpeningB, noClosingB + 1,
                                stringFormed + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        for i in self.fun(n, 0, 0, ''):
            ans.append(i)
        return ans


a = Solution()
print(a.generateParenthesis(2))
