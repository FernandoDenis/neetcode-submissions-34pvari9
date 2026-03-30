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
        if not root:
            return False

        sum = targetSum - root.val

        if not root.left and not root.right:
            return sum == 0
        if self.hasPathSum(root.left, sum):
            return True
        if self.hasPathSum(root.right, sum):
            return True
        
        # Backtracking
        sum = targetSum + root.val
        
        return False

            
        