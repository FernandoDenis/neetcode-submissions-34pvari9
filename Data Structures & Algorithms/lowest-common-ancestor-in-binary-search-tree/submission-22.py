# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val < q.val:
            smaller = p
            greater = q
        else: 
            smaller = q
            greater = p

        # smaller 3
        # grater 4

        curr = root

        while not (smaller.val <= curr.val <= greater.val):
            if curr.val > greater.val:
                curr = curr.left
            else:
                curr = curr.right

        return curr



        