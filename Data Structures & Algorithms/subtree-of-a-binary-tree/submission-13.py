# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return False

            if root.val == subRoot.val:
                if comparationTrees(root,subRoot):
                    return True
            
            return dfs(root.left) or dfs(root.right)
        
        def comparationTrees(root1,root2):
            if not root1 and not root2:
                return True
            elif not root1:
                return False
            elif not root2:
                return False
            elif root1.val != root2.val:
                return False
            
            return comparationTrees(root1.left, root2.left) and comparationTrees(root1.right,root2.right)

        return dfs(root)
