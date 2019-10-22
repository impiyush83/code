class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if len(s) > len(t):
            return False
        else:
            i = 0
            j = 0
            cnt = 0
            while i!=len(s) and j!= len(t):
                if s[i] == t[j]:
                    cnt += 1
                    i+=1
                    if cnt == len(s):
                        return True
                j+=1
            return False