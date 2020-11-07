# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def insert(self, val):
    #     if self.left > val:
    #         pass
    #     elif self.right > val:
    #         pass
    #     else:
    #         return True



class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        if not root.left and not root.right:
            return root.val
        p = root  # previous
        
        total = 0
        sum_so_far = 0
        
        while p.left or p.right:
            r = p
            sum_so_far = r.val

            while r.left or r.right:
                print(r.val)
                if r.left:
                    q = r.left
                    if not q.left and not q.right:
                        print(10 * sum_so_far + q.val)
                        total += 10 * sum_so_far + q.val
                        r.left = None
                        print(r.val)

                    elif q.left:
                        sum_so_far = 10 * sum_so_far + q.val
                        r = q
                        q = q.left
                        print(r.val)
                    else: # q.right
                        sum_so_far = 10 * sum_so_far + q.val
                        r = q
                        q = q.right
                        print(r.val)

                else: # r.right
                    q = r.right
                    if not q.left and not q.right:
                        print(10 * sum_so_far + q.val)
                        total += 10 * sum_so_far + q.val
                        r.right = None

                        print(r.val)
                    elif q.left:
                        sum_so_far = 10 * sum_so_far + q.val
                        #print(sum_so_far)
                        r = q
                        q = q.left
                        print(r.val)
                    else: # q.right
                        sum_so_far = 10 * sum_so_far + q.val
                        r = q
                        q = q.right
                        print(r.val)
            
        return total

bottom_left = TreeNode(5)
bottom_right = TreeNode(1)
left_node = TreeNode(9, left=bottom_left, right=bottom_right)
right_node = TreeNode(0)
my_tree = TreeNode(val=4, left=left_node, right=right_node)

solution = Solution()
print(solution.sumNumbers(my_tree))


# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026