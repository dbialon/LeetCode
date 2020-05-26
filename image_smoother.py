# https://leetcode.com/problems/image-smoother/
# Given a 2D integer matrix M representing the gray scale of an image,
# you need to design a smoother to make the gray scale of each cell
# becomes the average gray scale (rounding down) of all the 8 surrounding
# cells and itself. If a cell has less than 8 surrounding cells, then use
# as many as you can.

from typing import List

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        ##  ----------------->
        ##  |      y (columns)
        ##  |
        ##  |
        ##  |
        ##  |
        ##  | x (rows)
        ##  |
        ##  v
                
        # 3 cases:
        ## corners where each pixel has 3 neighbours so we take avg of 4 pixels
        ## edges where each pixel has 5 neighbours so we take avg of 6 pixels
        ## inside where each pixel has 8 neighbours so we tale avg of 9 pixels

        # initialize N
        N = []

        # N = M[:] makes a copy of M but then each sublist of N is 
        # the same object as sublists of M

        # copy each sublist from M to N
        for idx, _ in enumerate(M):
            N.append([])
            N[idx] = M[idx][:]

        # define max_X and max_Y
        max_X, max_Y = len(M) - 1, len(M[0]) - 1

        # iterate over pixels in the original image
        for x, _ in enumerate(M):
            for y, _ in enumerate(M[x]):
                # maps of neighbour pixels for x and y
                map_x = (x - 1, x, x + 1)
                map_y = (y - 1, y, y + 1)
                # count valid pixels (not outside the image)
                # sum of pixel values
                count, pixel_sum = 0, 0
                # iterate over neighbours of each pixel
                for p in map_x:
                    for q in map_y:
                        # eliminate pixels 'outside' the image
                        if 0 <= p <= max_X and 0 <= q <= max_Y:
                            pixel_sum += M[p][q]
                            count += 1

                # apply average to current pixel
                N[x][y] = pixel_sum // count 

        return N


####################
### TESTING ONLY ###
####################

# M = [[1,1,1],[1,0,1],[1,1,1]]
# M = [[1]]
# M = [[1,2,3],[4,5,6]]
M = [[255,255,255],[255,0,255],[255,255,255]]

print("M:", M)

solution = Solution().imageSmoother(M)
print("N:", solution)
