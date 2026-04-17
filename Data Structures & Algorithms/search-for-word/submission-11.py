class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()

        # C, A

        def dfs(y,x,idx):

            if idx == len(word) - 1:
                return True

            visited.add((y,x))

            for y1,x1 in directions:
                
                nextStepY, nextStepX = y + y1, x + x1

                if nextStepY < 0 or nextStepY >= ROWS or nextStepX < 0 or nextStepX >= COLS or (nextStepY,nextStepX) in visited:
                    continue

                if board[nextStepY][nextStepX] == word[idx + 1]:
                    if dfs(nextStepY,nextStepX, idx + 1):
                        return True
                    
            visited.remove((y,x))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i,j, 0):
                        return True

        return False



                

                
        