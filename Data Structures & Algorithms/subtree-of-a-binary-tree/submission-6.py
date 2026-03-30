# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def mainDfs(root,subRoot):# 1, 1 | 1, 1 | None, None
            if not root:
                return False

            left = mainDfs(root.left,subRoot) # true
            right = mainDfs(root.right,subRoot)# false

            if left or right:
                return True

            if root.val == subRoot.val:
                left = dfs(root.left, subRoot.left) # true
                right = dfs(root.right,subRoot.right) # true

                return left and right # true

            return False
        
        def dfs(root,subRoot): 
            if not root and not subRoot:
                return True
            elif not root:
                return False
            elif not subRoot:
                return False

            if root.val == subRoot.val:
                left = dfs(root.left, subRoot.left)
                right = dfs(root.right,subRoot.right)

                return left and right
            
            return False


        return mainDfs(root, subRoot)
        