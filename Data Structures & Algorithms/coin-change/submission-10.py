class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        if amount == 0:
            return 0

        memo = {}
        # 11:1, 12:2
        def dfs(val):
            if val == amount:
                return 0
            elif val > amount:
                return float("inf")

            if val in memo:
                return memo[val]

            minimum = float("inf")
            # 10
            # 11
            for num in coins:
                minimum = min(dfs(val + num), minimum)
            # 1
            memo[val] = minimum + 1

            return memo[val]

        num_coins = dfs(0)
        
        if num_coins >= float("inf"):
            return -1
        else:
            return num_coins

            
        