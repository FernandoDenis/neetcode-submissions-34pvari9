class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights[0]), len(heights)

        pacific = [[False] * ROW for _ in range(COL)]
        atlantic = [[False] * ROW for _ in range(COL)]

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        def bfs(cells, ocean):

            q = deque(cells)

            while q:
                for _ in range(len(q)):
                    y, x = q.popleft()

                    ocean[y][x] = True

                    for y1, x1 in directions:

                        nextStepY, nextStepX = y + y1, x + x1
                        if (nextStepY < 0 or nextStepY >= COL or nextStepX < 0 or 
                            nextStepX >= ROW or ocean[nextStepY][nextStepX] == True or   
                            heights[nextStepY][nextStepX] < heights[y][x]):
                            continue
                        
                        q.append((nextStepY,nextStepX))                        

        pac = []
        atl = []

        for i in range(ROW):
            pac.append((0,i))
            atl.append((COL - 1, i))

        for i in range(COL):
            pac.append((i,0))
            atl.append((i,ROW - 1))

        bfs(pac, pacific)
        bfs(atl, atlantic)

        result = []

        for i in range(COL):
            for j in range(ROW):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])

        return result

        