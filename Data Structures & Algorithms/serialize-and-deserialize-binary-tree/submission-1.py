# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# 1,2,3
# 1,2,null,null,3,4,5,null,null,null,null
# 1 * 2 l 
# 1 * 2 + 1 r
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string_ser = []

        def dfs(root):
            if not root:
                string_ser.append("null")
                string_ser.append("#")
                return
            
            string_ser.append(str(root.val))
            string_ser.append("#")

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return "".join(string_ser)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # [1,2,null,null,3,4,null,null,5,null,null]
        #                                     ^
        #  1
        # 2  3
        #   4 5
        data = data.split("#")
        curr = TreeNode()
        self.idx = 0

        def dfs(root):
            if self.idx >= len(data) or data[self.idx] == "null":
                self.idx += 1
                return None

            root = TreeNode(int(data[self.idx]))
            self.idx += 1
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            return root

        return dfs(curr)


