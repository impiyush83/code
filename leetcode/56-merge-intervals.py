from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        if len(intervals) == 0: return []
        merged_intervals = [intervals[0]]
        for interval in intervals[1:]:
            if merged_intervals[-1][1] >= interval[0] and merged_intervals[-1][1] <= interval[1]:
                  merged_intervals[-1][1] =  interval[1]
            elif merged_intervals[-1][1] >= interval[0] and merged_intervals[-1][1] > interval[1]:
                continue
            else:
                merged_intervals.append([interval[0], interval[1]])
        return merged_intervals