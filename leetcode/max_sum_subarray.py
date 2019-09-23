import sys

INT_MIN = -sys.maxsize


class Solution:
    def maxSubArray(self, nums):

        max_so_far = INT_MIN
        max_ending_here = 0

        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


if __name__ == "__main__":
    solution = Solution()
    input_num = list(map(int, input().split()))
    print(solution.maxSubArray(input_num))
