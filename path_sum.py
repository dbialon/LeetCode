# https://leetcode.com/problems/path-sum/
# Given a binary tree and a sum, determine if the tree has
# a root-to-leaf path such that adding up all the values along
# the path equals the given sum.
# Note: A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        if not root:
            return False
        if root.val == total and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, total-root.val) or self.hasPathSum(root.right, total-root.val)


tree = TreeNode(1,
            TreeNode(2,
                TreeNode(3),
                TreeNode(4,
                    TreeNode(5),
                    TreeNode(8))),
            TreeNode(6,
                None,
                TreeNode(9,
                    TreeNode(7)))
               )

solution = Solution()
print(solution.hasPathSum(tree, 15))
