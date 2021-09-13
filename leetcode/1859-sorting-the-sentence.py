
class Solution:
     def sortSentence(self, s: str) -> str:
        ans = dict()
        for i in s.split():
            ans[i[-1]] = i[:-1]
        return ' '.join(ans[a] for a in sorted(ans))
