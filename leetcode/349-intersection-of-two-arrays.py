from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        if not nums1 or not nums2:
            return []
        nums1 = list(nums1)
        nums1.sort()
        nums2 = list(nums2)
        nums2.sort()
        dicto = dict()
        for i in nums1:
            if not dicto.get(i):
                dicto[i] = 1
            else:
                dicto[i] += 1
        for i in nums2:
            if not dicto.get(i):
                dicto[i] = 1
            else:
                dicto[i] += 1
        ans = []
        for i in dicto.keys():
            if dicto[i] % 2 == 0:
                ans.append(i)
        return ans
