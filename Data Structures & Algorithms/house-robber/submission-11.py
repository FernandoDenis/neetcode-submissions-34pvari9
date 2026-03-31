class Solution:
    def rob(self, nums: List[int]) -> int:
        #  
        # [1,1,3,3]
        # max

        if len(nums) == 1:
            return nums[0]

        maxAmount = 0
        memo = {}

        def dfs(idx):
            if idx >= len(nums):
                return 0

            if idx in memo:
                return memo[idx]

            maximum = max(dfs(idx + 2),dfs(idx + 3))

            memo[idx] = maximum + nums[idx]

            return memo[idx]     

        maxAmount = max(dfs(0),dfs(1))

        return maxAmount  