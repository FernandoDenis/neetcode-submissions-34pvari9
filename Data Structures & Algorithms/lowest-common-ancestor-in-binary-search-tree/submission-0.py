# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
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