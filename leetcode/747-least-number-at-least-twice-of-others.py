from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        maxi_index = -1
        maxi = max(nums)
        for i in range(0, len(nums)):
            if nums[i] == maxi:
                maxi_index = i
                break

        sl = -1

        for i in range(0, len(nums)):
            if i != maxi_index:
                if nums[i] > sl:
                    sl = nums[i]

        if maxi >= sl * 2:
            return maxi_index
        else:
            return -1