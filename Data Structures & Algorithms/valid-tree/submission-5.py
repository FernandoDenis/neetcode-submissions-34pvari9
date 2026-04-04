class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # [0:0,1:1,2:1,3:1,1:2

        edges.sort()

        nodes = {0:0}

        for node1,node2 in edges:
            print(node1,node2)
            if node1 in nodes and node2 in nodes or node1 not in nodes and node2 not in nodes:
                return False
            elif node1 not in nodes:
                nodes[node1] = nodes[node2] + 1
            elif node2 not in nodes:
                nodes[node2] = nodes[node1] + 1

        return True

        
        

            
        