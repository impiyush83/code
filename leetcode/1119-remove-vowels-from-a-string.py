import re

def withoutRegex(s):
    v = {'a': True, 'e': True, 'i': True,'o': True,'u': True}
    swv = ""
    for c in s:
        if not v.get(c):
            swv += c
    return swv
    
def withRegex(s): 
    return re.sub("[aeiou]", "", s)

class Solution:
    def removeVowels(self, s: str) -> str:
        return withRegex(s)
        
