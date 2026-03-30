# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #   1     r
        # 3   2   r1 
        def dfs(root, val):
            if not root:
                return False

            if not root.left and not root.right:
                return (val + root.val) == targetSum

            if dfs(root.left, val + root.val):
                return True
            
            if dfs(root.right, val + root.val):
                return True

            return False

        return dfs(root, 0)

            
        