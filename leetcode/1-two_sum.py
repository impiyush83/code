"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        dicto = dict()
        # create dictionary of value and index of list nums
        for i, num in enumerate(nums):
            dicto[num] = i

        for i, num in enumerate(nums):
            if target - num in dicto.keys():
                # indices cannot be same
                if dicto[target - num] == i:
                    continue
                return sorted([dicto[target - num], i])


if __name__ == "__main__":
    solution = Solution()
    input_array = list(map(int, input().split()))
    required_two_sum = int(input())
    print(solution.twoSum(input_array, required_two_sum))

