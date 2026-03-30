class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        rotten_fruits = deque()
        fresh_fruits = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten_fruits.append((i,j))
                elif grid[i][j] == 1:
                    fresh_fruits += 1

        if not rotten_fruits and fresh_fruits > 0:
            return -1
        elif not rotten_fruits:
            return 0
        

        movements = [(-1,0),(0,1),(1,0),(0,-1)]
        time = 0
        while rotten_fruits:
            for _ in range(len(rotten_fruits)):
                y, x = rotten_fruits.popleft()

                for x1,y1 in movements:
                    next_X, next_Y = x + x1, y + y1

                    if next_X < 0 or next_X >= COL or next_Y < 0 or next_Y >= ROW or grid[next_Y][next_X] == 2 or grid[next_Y][next_X] == 0:
                        continue

                    grid[next_Y][next_X] = 2

                    rotten_fruits.append((next_Y, next_X))

            time += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return time - 1

        