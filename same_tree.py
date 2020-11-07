# https://leetcode.com/problems/same-tree/
# Given two binary trees, write a function to check if they are
# the same or not.
# Two binary trees are considered the same if they are structurally
# identical and the nodes have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        node_stack = [p, q]
        
        while node_stack:
            curr_q = node_stack.pop()
            curr_p = node_stack.pop()
            if curr_p and curr_q:
                if curr_p.val != curr_q.val:
                    return False
                node_stack.extend([curr_p.right, curr_q.right, curr_p.left, curr_q.left])
            elif (curr_p and not curr_q) or (not curr_p and curr_q):
                return False

        return True


tree1 = TreeNode('F',
            TreeNode('B',
                TreeNode('A'),
                TreeNode('D',
                    TreeNode('C'),
                    TreeNode('E'))),
            TreeNode('G',
                None,
                TreeNode('I',
                    TreeNode('H')))
               )

tree2 = TreeNode('F',
            TreeNode('B',
                TreeNode('A'),
                TreeNode('D',
                    TreeNode('C'),
                    TreeNode('E'))),
            TreeNode('G',
                None,
                TreeNode('I',
                    TreeNode('H')))
               )

solution = Solution()
print(solution.isSameTree(tree1, tree2))
