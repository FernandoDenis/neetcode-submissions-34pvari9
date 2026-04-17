# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if p and not q:
            return False
        elif q and not p:
            return False

        stack_p = [p] # 1
        stack_q = [q] # 1

        while stack_p and stack_q: 

            if not stack_p or not stack_q:
                return False

            for _ in range(len(stack_p)):
                
                root_p = stack_p.pop() # 3
                root_q = stack_q.pop() # 3

                if root_p.val != root_q.val:
                    return False

                if not root_p.left and root_q.left or (not root_q.left and root_p.left):
                    return False

                if not root_p.right and root_q.right or (not root_q.right and root_p.right):
                    return False

                if root_p.right and root_q.right:
                    stack_p.append(root_p.right)
                    stack_q.append(root_q.right)
                
                if root_p.left and root_q.left:
                    stack_p.append(root_p.left)
                    stack_q.append(root_q.left)

        return True
        