class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) # 5

        if n <= 2:
            return max(nums)
        # [2,9,8,3,6]
        memo = {}

        def dfs(idx): 
            if idx >= n:
                return 0

            if idx in memo:
                return memo[idx]

            memo[idx] = max(dfs(idx + 2), dfs(idx + 3)) + nums[idx] 

            return memo[idx] 
        #           
        return max(dfs(0),dfs(1))