class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [1,5,10] # 12
        #          1
        #    2     6       11
        #  3 7 12 7 11, 16 12
        # {11:3,2:3}
        coins = sorted(coins, reverse= True)
        if amount == 0:
            return 0

        memo = {}

        def dfs(total):
            if total > amount:
                return float("inf")
            if total == amount:
                return 0

            if total in memo:
                return memo[total]

            minimum = float("inf")

            for coin in coins:
                minimum = min(minimum, dfs(coin + total))

            memo[total] = minimum + 1

            return memo[total]

        minimum = dfs(0)

        if minimum == float("inf"):
            return -1
        else:
            return minimum
        