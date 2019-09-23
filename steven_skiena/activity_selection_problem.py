"""
The Movie Star Scheduling Problem / Maximum Activity Selection problem
Input: A set I of n intervals on the line.
Output: What is the largest subset of mutually non-overlapping intervals which can be selected from I?
"""

from operator import itemgetter

start_time = list(map(int, input().split()))
end_time = list(map(int, input().split()))


time_series = []
for index in range(0, len(start_time)):
    time_series.append([start_time[index], end_time[index]])

time_series.sort(key=itemgetter(1))

cnt = 1

curr_end_time = time_series[0][1]
for i in range(1, len(time_series)):
    if time_series[i][0] >= curr_end_time:
        cnt += 1
        curr_end_time = time_series[i][1]

print("Max activities that can be done are : {count}".format(count=cnt))
