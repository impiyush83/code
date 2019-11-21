from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr, left, right, key):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                return binary_search(arr, mid + 1, right, key)
            else:
                return binary_search(arr, left, mid - 1, key)

        def find_pivot(num_list):
            if len(num_list) == 1:
                return 0
            left = 0
            right = len(num_list) - 1
            # if no inflection point
            if num_list[right] > num_list[0]:
                return 0
            while right >= left:
                mid = left + (right - left) // 2
                if num_list[mid] > num_list[mid + 1]:
                    return mid + 1
                if num_list[mid - 1] > num_list[mid]:
                    return mid
                if num_list[mid] > num_list[0]:
                    left = mid + 1
                else:
                    right = mid - 1

        if not nums:
            return -1
        pivot = find_pivot(nums)
        print(pivot)
        if pivot == 0:
            return binary_search(nums, 0, len(nums) - 1, target)
        else:
            left = binary_search(nums, 0, pivot - 1, target)
            right = binary_search(nums, pivot, len(nums) - 1, target)
            if right == left == -1:
                return -1
            if right != -1:
                return right
            else:
                return left