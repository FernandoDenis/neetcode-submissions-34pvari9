class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 0,1,2,3,4
        # 2

        # 0,1,2

        # {0:[1],1:[0,2],2:[1]}

        graphs = {i:[] for i in range(n)}

        for node1,node2 in edges:
            graphs[node1].append(node2)
            graphs[node2].append(node1)

        visited = set()

        def dfs(node,prev):
            if node in visited:
                return 

            visited.add(node)

            for n in graphs[node]:
                if n == prev:
                    continue

                dfs(n,node)

            return 

        number_of_graphs = 0

        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                number_of_graphs += 1

        return number_of_graphs

        
        