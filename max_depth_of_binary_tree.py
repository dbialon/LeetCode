# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


tree = TreeNode('F',
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
print(solution.maxDepth(tree))
