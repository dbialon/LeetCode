# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Given the root of a Binary Search Tree and a target number k, return
# true if there exist two elements in the BST such that their sum is
# equal to the given target.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.visited = set()

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        
        if root.val in self.visited:
            return True
        
        self.visited.add(k - root.val)
        
        if root.left and root.right:
            return self.findTarget(root.left, k) or self.findTarget(root.right, k)
        elif root.left:
            return self.findTarget(root.left, k)
        else:
            return self.findTarget(root.right, k)
        
        return False
