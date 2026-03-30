class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            if i + 3 < len(nums):
                nums[i] = max(nums[i + 2], nums[i + 3]) + nums[i]
            elif i + 2 < len(nums):
                nums[i] +=nums[i + 2]
            
        return max(nums[0], nums[1])
        