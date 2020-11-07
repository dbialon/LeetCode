# https://leetcode.com/problems/minimum-time-visiting-all-points/
# On a plane there are n points with integer coordinates points[i] = [xi, yi].
# Your task is to find the minimum time in seconds to visit all points.
# You can move according to the next rules:
# In one second always you can either move vertically, horizontally
# by one unit or diagonally (it means to move one unit vertically
# and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        current = points[0]
        for point in points[1:]:
            hor_dist = abs(point[0] - current[0])
            vert_dist = abs(point[1] - current[1])
            time += min(hor_dist, vert_dist)
            time += abs(hor_dist - vert_dist)
            current = point
        return time


points = [[1,1],[3,4],[-1,0],[2,3],[0,0]]

solution = Solution()
print(solution.minTimeToVisitAllPoints(points))
