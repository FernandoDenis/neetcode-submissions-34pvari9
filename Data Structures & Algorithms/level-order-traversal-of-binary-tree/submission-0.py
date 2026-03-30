# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # [1,2,3,4,5,6,7]

        if not root:
            return []

        q = deque([root]) 

        result = [] # [[1],[2,3]]

        while q: # [4,5,6,7]
            array = [] # 

            for _ in range(len(q)):

                root = q.popleft() # 3

                array.append(root.val) 

                if root.left:
                    q.append(root.left)
                
                if root.right:
                    q.append(root.right)

            result.append(array.copy())

        return result




        