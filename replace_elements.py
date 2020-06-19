#  https://leetcode.com/problems/replace-elements-with-greatest
#  -element-on-right-side/

#  Given an array arr, replace every element in that array with the
#  greatest element among the elements to its right, and replace
#  the last element with -1.
#  After doing so, return the array.
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        idx = 0
        length = len(arr)
        if length > 1:
            max_num = max(arr[idx+1:])
        while idx < length - 1:
            if arr[idx] == max_num:
                max_num = max(arr[idx+1:])
            arr[idx] = max_num
            idx += 1
        
        arr[-1] = -1
        
        return arr


####################
### TESTING ONLY ###
####################

#  arr = [17,18,5,4,6,1]
#  output: [18,6,6,6,1,-1]
arr = [1,1,1]

solution = Solution()
print(solution.replaceElements(arr))
