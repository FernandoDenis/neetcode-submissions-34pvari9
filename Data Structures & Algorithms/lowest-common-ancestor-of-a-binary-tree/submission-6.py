# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        value_LCA = [None]

        def dfs(root):
            if not root:
                return False

            left = dfs(root.left)
            right = dfs(root.right)

            if (root == p or root == q) and (left or right):
                value_LCA[0] = root

            if left and right:
                value_LCA[0] = root

            if root == p or root == q:
                return True

            return left or right

        dfs(root)

        return value_LCA[0]

