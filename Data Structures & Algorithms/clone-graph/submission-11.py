"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        nodesCreated = {}

        def copyGraph(graphNode):

            newNode = Node(graphNode.val)
            nodesCreated[newNode.val] = newNode

            for n in graphNode.neighbors:
                if n.val in nodesCreated:
                    newNode.neighbors.append(nodesCreated[n.val])
                    continue
                newNode.neighbors.append(copyGraph(n))

            return newNode

        return copyGraph(node)
