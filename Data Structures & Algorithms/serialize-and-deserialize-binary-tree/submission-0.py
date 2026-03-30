# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # 1#2#None#None#3#4#None#None#5#None#None
        # [1,2,None,None,3,4,None,None,5,None,None]
        string = []

        def dfs(root):
            if not root:
                string.append("None")
                return

            string.append(str(root.val))

            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)

        return " ".join(string)

        
    # Decodes your encoded data to tree.
    # [1,2,None,None,3,4,None,None,5,None,None]
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = data.split()

        q = deque(q)

        def dfs(root):
            if not q:
                return

            val = q.popleft()

            if val == "None":
                return

            root = TreeNode(int(val))

            dfs(root.left)
            dfs(root.right)

            return root

        return root
