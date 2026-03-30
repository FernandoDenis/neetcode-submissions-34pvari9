class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        ROW, COL = len(grid[0]), len(grid)
        q = deque([(0,0)])

        steps = 0
        moves = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
        visited = set([(0,0)])
        while q:
            for i in range(len(q)):
                y, x = q.popleft()

                if y == COL - 1 and x == ROW - 1:
                    return steps + 1

                for y1, x1 in moves:
                    nextYmove, nextXmove = y + y1, x + x1

                    if nextYmove >= COL or nextYmove < 0 or nextXmove >= ROW or nextXmove < 0 or (nextYmove, nextXmove) in visited or grid[nextYmove][nextXmove] == 1:
                        continue
                    
                    q.append((nextYmove, nextXmove))
                    visited.add((nextYmove, nextXmove))

            steps += 1

        return -1
        