class Solution:
    def isValid(self, s: str) -> bool:
        dicto = {']':'[', '}':'{', ')':'('}
        stk = []
        for i in s:
            if i in ['[', '{', '(']:
                stk.insert(0,i)
            if i in [']', '}', ')']:
                if not stk:
                    return False
                poped = stk.pop(0)
                if dicto[i] != poped:
                    return False
        if stk:
            return False
        else:
            return True