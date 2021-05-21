class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        total_count = last_index = 0
        dicto = dict()
        for i in range(0, len(keyboard)):
            dicto[keyboard[i]] = i
        for i in word:
            total_count += abs(last_index - dicto[i])
            last_index = dicto[i]
        return total_count
            
