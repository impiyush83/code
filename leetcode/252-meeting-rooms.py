from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        currentMeeting = []
        for interval in sorted(intervals, key=lambda x : x[0]):
            if currentMeeting and currentMeeting[1] > interval[0]:
                return False
            else:
                currentMeeting = interval
        return True




class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

