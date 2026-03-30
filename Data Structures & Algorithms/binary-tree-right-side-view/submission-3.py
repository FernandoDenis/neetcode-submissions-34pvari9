# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        levels_of_tree = dict()

        def nodesInLevelsAndColumns(root,height):
            if not root:
                return 
            
            if height not in levels_of_tree:
                levels_of_tree[height] = root.val

            nodesInLevelsAndColumns(root.right, height + 1)
            nodesInLevelsAndColumns(root.left, height + 1)

        nodesInLevelsAndColumns(root,0)

        result = []
        i = 0
        while i in levels_of_tree:
            result.append(levels_of_tree[i])
            i += 1

        return result
        