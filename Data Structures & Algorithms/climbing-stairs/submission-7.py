class Solution:
    def climbStairs(self, n: int) -> int:
        # 3 
        # 2: 1, 1: 2
        #  1 2
        # 2 3  3 4
        
        

        memo = {}

        def dfs(stair):
            if stair == n:
                return 1
            elif stair > n:
                return 0
            
            if stair in memo:
                return memo[stair]

            memo[stair] = dfs(stair + 1) + dfs(stair + 2)

            return memo[stair]

        return dfs(0)
         
        