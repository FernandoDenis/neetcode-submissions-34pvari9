class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1 

        n = len(grid)
        q = deque([(0,0)])
        movements = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        steps = 0 # 1

        while q: # [(1,1)]
            for _ in range(len(q)):
                y,x = q.popleft()

                if x == n - 1 and y == n - 1:
                    return steps + 1

                for y1,x1 in movements:

                    nextStepY, nextStepX = y1 + y, x1 + x

                    if nextStepY < 0 or nextStepY >= n or nextStepX < 0 or nextStepX >= n or grid[nextStepY][nextStepX] == 1:
                        continue

                    q.append((nextStepY, nextStepX))
                    grid[nextStepY][nextStepX] = 1

            steps += 1

        return -1
                