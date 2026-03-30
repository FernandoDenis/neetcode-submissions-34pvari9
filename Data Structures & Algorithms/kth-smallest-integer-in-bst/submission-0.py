# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = [] # [2,1]

        curr = root

        while curr:
            stack.append(curr)
            curr = curr.left

        smallest = 0 # 0
        while stack: # [5]
            for _ in range(len(stack)):
                
                root = stack.pop() # 5
                smallest += 1 # 4

                if smallest == k: 
                    return root.val

                if root.right:
                    curr = root.right

                    while curr:
                        stack.append(curr)
                        curr = curr.left

        return -1

                
                





        