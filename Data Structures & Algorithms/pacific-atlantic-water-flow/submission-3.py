class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights[0]), len(heights)

        notValid = set()
        valid = set()

        movements = [(-1,0),(0,1),(1,0),(0,-1)]

        def bfs(y,x):
            q = deque([(y,x)])

            moves = set()

            touchPacific = False
            touchAtlantic = False

            while q:
                for _ in range(len(q)):

                    y,x = q.popleft()

                    if x == 0 or y == 0:
                        touchPacific = True
                    
                    if x == ROW - 1 or y == COL - 1:
                        touchAtlantic = True

                    if touchPacific and touchAtlantic or (y,x) in valid:
                        return (True, None)

                    for y1,x1 in movements:

                        nextStepY, nextStepX = y + y1, x + x1

                        if nextStepY >= COL or nextStepY < 0 or nextStepX >= ROW or nextStepX < 0 or (nextStepY,nextStepX) in moves or heights[nextStepY][nextStepX] > heights[y][x]:
                            continue

                        q.append((nextStepY,nextStepX))
                        moves.add((nextStepY,nextStepX))

            return (False, moves)

        for i in range(COL):
            for j in range(ROW):
                isValid, path = bfs(i,j)
                if not isValid:
                    notValid.add((i,j))
                else:
                    valid.add((i,j))

        return list(valid)


        