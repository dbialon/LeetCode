# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# You are given an array coordinates, coordinates[i] = [x, y],
# where [x, y] represents the coordinate of a point. Check if 
# these points make a straight line in the XY plane.

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 2 points always form a line
        if len(coordinates) == 2:
            return True
        # case when first 2 points form a line parallel to the Y axis
        # it's a special case when dx = 0 that would cause DivisionByZero error
        if coordinates[0][0] == coordinates[1][0]:
            for point in coordinates[2:]:
                if point[0] != coordinates[0][0]:
                    return False
            else:
                return True
        # a = dy / dx (first 2 points from the list)
        a = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        # b = y - a * x (of either point0 or point1)
        b = coordinates[0][1] - a * coordinates[0][0]
        # check if y = a*x + b for the rest of the list
        for point in coordinates[2:]:
            if point[1] != a * point[0] + b:
                return False
        else:
            return True


# coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates = [[2,1],[2,0],[2,-1]]

solution = Solution()
print(solution.checkStraightLine(coordinates))
