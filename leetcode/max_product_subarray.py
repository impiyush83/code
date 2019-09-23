import sys

INT_MIN = -sys.maxsize


class Solution:
    def maxProduct(self, nums):
        max_current = 1
        max_global = INT_MIN

        for i in nums:
            max_current *= i
            if max_global < max_current:
                max_global = max_current
        return max_global


if __name__ == "__main__":
    solution = Solution()
    input_num = list(map(int, input().split()))
    print(solution.maxProduct(input_num))
