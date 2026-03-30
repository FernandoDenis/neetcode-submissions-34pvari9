# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #    5
        #  3   4
        # 2  1

        lowestAncestor = [None]

        def dfs(root):
            if not root:
                return False

            valRoot = False

            if root == p or root == q:
                valRoot = True

            left = dfs(root.left)
            right = dfs(root.right)

            if (left and right) or (left and valRoot) or (right and valRoot):
                lowestAncestor[0] = root

            return left or right or valRoot

        dfs(root)

        return lowestAncestor[0]



            


        