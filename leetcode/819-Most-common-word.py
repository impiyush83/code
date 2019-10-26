import re
from operator import itemgetter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r"[^a-zA-Z]+", ' ', paragraph)
        print(paragraph)
        paragraph = paragraph.split(' ')
        dicto = dict()
        for i in paragraph:
            if not dicto.get(i):
                dicto[i] = 1
            else:
                dicto[i] += 1

        for word in banned:
            if dicto.get(word):
                dicto.pop(word)
        dicto = sorted(dicto.items(), key=itemgetter(1), reverse=True)
        ans = dicto[0]
        return ans[0]
