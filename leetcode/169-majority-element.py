from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicto = dict()
        for i in nums:
            if not dicto.get(i):
                dicto[i] = 1
            else:
                dicto[i] += 1
        for i in dicto.keys():
            if dicto[i] > len(nums)//2:
                return i