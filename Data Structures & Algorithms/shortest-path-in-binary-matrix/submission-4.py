class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        grid = [
            [1,1,0],
            [1,1,1],
            [1,1,0]
        ]"""
        # steps 2
        # n 3
        # q (2,2)(0,2)(0,2)(2,2)
        #    y x
        n = len(grid)

        if grid[0][0] == 1:
            return -1

        q = deque([(0,0)])

        directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

        steps = 1

        while q:
            for _ in range(len(q)):
                y,x = q.popleft()
                grid[y][x] = 1

                if x == n - 1 and y == n - 1:
                    return steps

                for y1,x1 in directions:
                    nextStepY, nextStepX = y1 + y, x1 + x

                    if nextStepY < 0 or nextStepY >= n or nextStepX < 0 or nextStepX >= n or grid[nextStepY][nextStepX] == 1:
                        continue

                    q.append((nextStepY,nextStepX))
                    

            steps += 1

        return -1



        