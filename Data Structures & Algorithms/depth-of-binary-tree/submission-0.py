# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def getHeight(root,height):
            if not root:
                return height - 1

            leftChild = getHeight(root.left, height + 1)
            rightChild = getHeight(root.right, height + 1)

            return max(leftChild, rightChild)

        return getHeight(root, 1)