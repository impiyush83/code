class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix_sum_array = set()
        prefix_sum = 0
        for i in A:
            prefix_sum += i
            if prefix_sum == 0 or prefix_sum in prefix_sum_array:
                return 1
            prefix_sum_array.add(prefix_sum)
        return 0
