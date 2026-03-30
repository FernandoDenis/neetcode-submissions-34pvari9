# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        levels_of_tree = dict()

        def nodesInLevelsAndColumns(root,height,column):
            if not root:
                return 
            
            if height in levels_of_tree:
                if column >= levels_of_tree[height][0]:
                    levels_of_tree[height] = [column, root.val]
            else:
                levels_of_tree[height] = [column, root.val]

            nodesInLevelsAndColumns(root.left, height + 1, column - 1)
            nodesInLevelsAndColumns(root.right, height + 1, column + 1)

        nodesInLevelsAndColumns(root,0,0)

        result = []
        i = 0
        while i in levels_of_tree:
            result.append(levels_of_tree[i][1])
            i += 1

        return result
        