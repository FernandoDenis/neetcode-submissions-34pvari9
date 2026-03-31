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
            return node

        seen = dict()

        def dfs(graphNode):
            if not graphNode:
                return graphNode

            newNode = Node(graphNode.val)
            seen[newNode.val] = newNode

            for i in range(len(graphNode.neighbors)):
                if graphNode.neighbors[i].val in seen:
                    newNode.neighbors.append(seen[graphNode.neighbors[i].val])
                else:
                    newNode.neighbors.append(dfs(graphNode.neighbors[i]))

            return newNode

        return dfs(node)


        