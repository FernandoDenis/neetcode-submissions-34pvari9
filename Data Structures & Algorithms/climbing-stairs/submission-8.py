class Solution:
    def climbStairs(self, n: int) -> int:
        
        #     3
        #   2   1
        # 1  0 0  
        # 0    

        memo = {}

        def dfs(stair):
            if stair == 0:
                return 1
            elif stair < 0:
                return 0

            if stair in memo:
                return memo[stair]

            memo[stair] = dfs(stair - 1) + dfs(stair - 2)

            return memo[stair]

        return dfs(n)
        