
from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            hashmap = Counter(nums)
            for k in hashmap.keys():
                if hashmap[k] == 1:
                    return k




class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2

