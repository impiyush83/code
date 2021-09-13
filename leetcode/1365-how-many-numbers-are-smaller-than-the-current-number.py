from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        min_index = dict()
        for index, num in enumerate(sorted_nums):
            if min_index.get(num) == None:
                min_index[num] = index
        final = []
        for num in nums:
            final.append(min_index[num])
        return final

