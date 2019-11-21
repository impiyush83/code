from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        count = dict()
        for i in nums2:
            if count.get(i):
                count[i] += 1
            else:
                count[i] = 1
        ans = []
        for i in nums1:
            if i in nums2:
                if count[i]:
                    ans.append(i)
                    count[i] -= 1
        return ans