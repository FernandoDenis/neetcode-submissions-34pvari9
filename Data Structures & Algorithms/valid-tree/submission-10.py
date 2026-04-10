class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # [[0, 1], [0, 2], [0, 3], [1, 4]]
        #     0 
        # 1   2       3
        #  \4/  
        # {0:[1,2,3],2:[0],1:[0,4],4:[1],3:[0]}

        # 0,1,4

        if not edges:
            return True

        dic_edges = {i:[] for i in range(n)}

        visited = set()

        for node1, node2 in edges:
            dic_edges[node1].append(node2)
            dic_edges[node2].append(node1)

        def dfs(node, prev):
            if not dic_edges[node]:
                return True

            if node in visited:
                return False

            visited.add(node)

            for n in dic_edges[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False

            return True

        return dfs(0,-1) and len(visited) == n

        
    