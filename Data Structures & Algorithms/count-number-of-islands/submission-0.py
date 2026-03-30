class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,-1],[1,0],[0,1],[-1,0]]
        ROW, COL = len(grid[0]), len(grid)
        num_islands = 0

        def bfs(c,r):
            q = deque([(c,r)])
            while q:
                for i in range(len(q)):
                    y,x = q.popleft()

                    for y1,x1 in directions:
                        nextStepY, nextStepX = y + y1, x + x1

                        if nextStepX < 0 or nextStepX >= ROW or nextStepY < 0 or nextStepY >= COL or grid[nextStepY][nextStepX] == "0":
                            continue

                        q.append((nextStepY,nextStepX))
                        
                    grid[y][x] = "0"

        for i in range(COL):
            for j in range(ROW):
                if grid[i][j] == "1":
                    bfs(i,j)
                    num_islands += 1

        return num_islands


                    
        