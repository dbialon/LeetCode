# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/

# Suppose you have a random list of people standing in a queue.
# Each person is described by a pair of integers (h, k),
# where h is the height of the person and k is the number of people
# in front of this person who have a height greater than or equal to h.
# Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = [None for _ in range(len(people))]
        taken = [0 for _ in range(len(queue))]

        for idx, person in enumerate(sorted(people)):
            n = person[1]
            if queue[n]:
                pass

        return queue
            

        # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        
        # 4 is the shortes
        # [[None],[None],[None],[None],[4,4],[None]]
        # [[7,0], [7,1], [5,0], [6,1], [5,2]]
        
        # 5 is the shortest
        # [[5,0],[None],[5,2][None],[4,4],[None]]
        # [[7,0], [7,1], [6,1]]
        
        # 6 is the shortest
        # [[5,0],[None],[5,2][6,1],[4,4],[None]]
        # [[7,0], [7,1]]
        
        # 7 is the shortest
        # [[5,0],[7,0],[5,2][6,1],[4,4],[7,1]]


####################
### TESTING ONLY ###
####################

# Input:
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

solution = Solution()
print(solution.reconstructQueue(people))