class Solution:
    def rob(self, nums: List[int]) -> int:
        #    i   i2
        # [1,1,3,3]
        # 
        if len(nums) <= 2:
            return max(nums)

        memo = {} # {2:3, 3:3, 1:4}

        def dfs(idx): # 1
            if idx >= len(nums):
                return 0

            if idx in memo:
                return memo[idx]

            memo[idx] = max(dfs(idx + 2), dfs(idx + 3)) + nums[idx]

            return memo[idx]
            #       4
        return max(dfs(0), dfs(1))
        