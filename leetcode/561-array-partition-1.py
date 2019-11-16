from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arr = sorted(nums)
        return sum(arr[0::2])