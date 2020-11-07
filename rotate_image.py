# https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note:
# You have to rotate the image in-place, which means you have to modify
# the input 2D matrix directly. DO NOT allocate another 2D matrix and
# do the rotation.

from typing import List

class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # size = height = width
        size = len(matrix)
        if size <= 1:
            return

        x = 0
        # firstly, flip it on the / diagonal (753) in 3x3 matrix
        while x < size - 1:
            y = size - 1
            while y > x: # stop when you get to the / diagonal 
                tmp = matrix[x][size-y-1]
                matrix[x][size-y-1] = matrix[y][size-x-1]
                matrix[y][size-x-1] = tmp
                y -= 1
            x += 1

        # secondly, flip it horizontally --
        x = 0
        while x < size / 2:
            tmp = matrix[x]
            matrix[x] = matrix[size-x-1]
            matrix[size-x-1] = tmp
            x += 1


    def rotate2(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        if size <= 1:
            return

        for x in range(int(size/2)):
            for y in range(size-x-1,x,-1):
                # print(f"[{x}{y}]<-[{size-y-1}{x}]<-[{size-x-1}{size-y-1}]<-[{y}{size-x-1}]")
                tmp = matrix[x][y]
                matrix[x][y] = matrix[size-y-1][x]
                matrix[size-y-1][x] = matrix[size-x-1][size-y-1]
                matrix[size-x-1][size-y-1] = matrix[y][size-x-1]
                matrix[y][size-x-1] = tmp


matrix = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]

    #[[1,2,3], # [0,0][0,2] [0,1][1,2] [0,2][2,2]   3x3    # [0,0][0,2][2,2][2,0]
    # [4,5,6], # [1,0][0,1] [1,1][1,1] [1,2][2,1] 3-cycles # [1,1][1,1][1,1][1,1]
    # [7,8,9]] # [2,0][0,0] [2,1][1,0] [2,2][2,0]          # [0,1][1,2][2,1][1,0]

    # 4x4 matrix
    # xzyx   4-cycles
    # yvvz   len(matrix) = 4
    # zvvy   x:00 03 33 30 z:01 13 32 20
    # xyzx   y:02 23 31 10 v:11 12 22 21

for row in matrix:
    print(row)
print()

solution = Solution()
solution.rotate1(matrix)

for row in matrix:
    print(row)
print()

solution.rotate2(matrix)
for row in matrix:
    print(row)
