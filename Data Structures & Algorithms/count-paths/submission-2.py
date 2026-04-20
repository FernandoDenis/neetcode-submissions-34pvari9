class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 and n == 1:
            return 1

        dp = [[1] * n] * m

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

        