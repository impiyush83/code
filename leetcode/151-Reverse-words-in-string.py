class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        while "" in words:
            words.remove("")
        print(words)
        words = list(reversed(words))
        return ' '.join(words)