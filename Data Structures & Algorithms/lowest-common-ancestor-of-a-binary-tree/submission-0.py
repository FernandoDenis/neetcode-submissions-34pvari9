# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root,val):
            if not root:
                return 0                

            num1 = dfs(root.left, val)
            num2 = dfs(root.right, val)

            if num1 != 1 and num1 != 0:
                return num1

            if num2 != 1 and num2 != 0:
                return num2

            val = num1 + num2

            if root.val == q.val or root.val == p.val:
                val += 1
            
            if val == 2:
                return root
            else:
                return val

        return dfs(root, 0)

        # ver las variables dentro de un while {variable xd} existira afuera?


        