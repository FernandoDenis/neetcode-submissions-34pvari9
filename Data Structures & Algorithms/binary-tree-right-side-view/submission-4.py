# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def nodesInLevelsAndColumns(root,height):
            if not root:
                return 
            
            if len(result) == height:
                result.append(root.val)

            nodesInLevelsAndColumns(root.right, height + 1)
            nodesInLevelsAndColumns(root.left, height + 1)

        nodesInLevelsAndColumns(root,0)

        return result
        