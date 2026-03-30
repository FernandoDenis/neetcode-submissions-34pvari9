class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #   [1,5,10]
        #    1
        #  2
        # ..
        # 11
        # 12
        # {7:1}

        memo = {}

        def dfs(val):
            if val == amount:
                return 0
            elif val > amount:
                return float("inf")

            if val in memo:
                return memo[val]

            minimum = float("inf")
            for num in coins:
                minimum = min(minimum, dfs(val + num))

            memo[val] = minimum + 1

            return memo[val]

        num_coins = dfs(0)

        if num_coins >= float("inf"):
            return -1
        else:
            return num_coins

