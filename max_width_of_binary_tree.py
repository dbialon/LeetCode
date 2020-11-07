# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Given a binary tree, write a function to get the maximum width
# of the given tree. The width of a tree is the maximum width among
# all levels. The binary tree has the same structure as a full binary
# tree, but some nodes are null.
# The width of one level is defined as the length between the end-nodes
# (the leftmost and right most non-null nodes in the level, where
# the null nodes between the end-nodes are also counted into
# the length calculation.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        q1 = [root]
        q2 = []
        ans = 0
        
        while q1:
            for item in q1:
                if item:
                    q2.append(item.left)
                    q2.append(item.right)
                else:
                    q2.extend([None, None])
            i, j = 0, len(q1)-1
            while True:
                if not q1[i]:
                    i += 1
                if not q1[j]:
                    j -= 1
                if (q1[i] and q1[j]) or i >= j:
                    break
            ans = max(j-i+1, ans)
            m, n = 0, len(q2)-1
            while True:
                if not q2[m]:
                    m += 1
                if not q2[n]:
                    n -= 1
                if (q2[m] and q2[n]) or m >= n:
                    break
            q1 = q2[m:n+1]
            q2 = []

        return ans


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
print(solution.widthOfBinaryTree(tree))
