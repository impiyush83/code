class Solution:
    def isPalindrome(self, A: str) -> bool:
        A = A.lower()
        LL = []
        for i in A:
            if i.isalnum():
                LL.append(i)
        LLR = list(reversed(LL))
        if LL != LLR:
            return False
        return True
