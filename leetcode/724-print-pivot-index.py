from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        precompute = []
        for i in range(0, len(nums)):
            if not precompute:
                precompute.append(nums[i])
            else:
                current_sum = nums[i] + precompute[i - 1]
                precompute.append(current_sum)
        print(precompute)
        for i in range(0, len(nums)):
            left_sum = precompute[i] - nums[i]
            right_sum = precompute[-1] - precompute[i]

            if left_sum == right_sum:
                return i
        return -1