#  https://leetcode.com/problems/can-place-flowers/
#  Suppose you have a long flowerbed in which some of the plots are
#  planted and some are not. However, flowers cannot be planted in
#  adjacent plots - they would compete for water and both would die.

#  Given a flowerbed (represented as an array containing 0 and 1,
#  where 0 means empty and 1 means not empty), and a number n, return
#  if n new flowers can be planted in it without violating the
#  no-adjacent-flowers rule.
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed == [0]:
            return True
        if len(flowerbed) > 1:
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
        
        idx = 2
        while idx < len(flowerbed)- 1 and n > 0:
            if flowerbed[idx-1] == 0 and flowerbed[idx] == 0:
                if flowerbed[idx+1] == 0:
                    n -= 1
                    idx += 2
                else:
                    idx += 3
            else:
                idx += 1

        return n <= 0


####################
### TESTING ONLY ###
####################

flowerbed = [0,0,1,0,0]
n = 1

solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))

print(flowerbed)
