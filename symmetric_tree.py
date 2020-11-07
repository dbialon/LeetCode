# https://leetcode.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetricIter(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        q1 = [root]
        q2 = []
        empty = False
        
        while not empty:
            empty = True
            l = len(q1)
            for i in range(l):
                if q1[i]:
                    empty = False
                    q2.append(q1[i].left)
                    q2.append(q1[i].right)
                    q1[i] = q1[i].val
            if q1 != q1[::-1]:
                return False
            q1 = q2[:]
            q2 = []
            
        return True


    def isMirrorImage(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isMirrorImage(p.right, q.left) and self.isMirrorImage(p.left, q.right)


    def isSymmetricRec(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.isMirrorImage(root.left, root.right)


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
            TreeNode('B',
                TreeNode('D',
                    TreeNode('E'),
                    TreeNode('C')),
                TreeNode('A'))
                )

solution = Solution()
print(solution.isSymmetricIter(tree1))
print(solution.isSymmetricIter(tree2))
print(solution.isSymmetricRec(tree1))
print(solution.isSymmetricRec(tree2))
