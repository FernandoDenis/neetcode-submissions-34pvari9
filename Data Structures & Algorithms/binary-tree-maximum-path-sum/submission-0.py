# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        larger_sum = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftNode = dfs(root.left) # larger left sum
            rightNode = dfs(root.right) # larger right sum

            leftNode = max(leftNode, 0)
            rightNode = max(rightNode, 0)

            larger_sum[0] = max(root.val + leftNode + rightNode, larger_sum[0])

            return root.val + max(leftNode,rightNode)

        dfs(root)

        return larger_sum[0]
