# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #   -15
        # 10    20      35
        #     15   5
        #   0
        # 40
        maxSum = [float("-inf")]

        def dfs(root):
            if not root:
                return 0

            left = max(0,dfs(root.left)) 
            right = max(0,dfs(root.right))

            total = root.val + left + right

            maxSum[0] = max(maxSum[0], total)

            return root.val + max(left,right)

        addition = dfs(root)

        maxSum[0] = max(addition, maxSum[0])

        return maxSum[0]
        