class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,109,103,8,100] 109
        # [2,9,3,8,100] 16

        #   2
        #  3     8
        # 100,0 0,0

        # 9
        # 8 100
        # 0,0 
        
        for i in range(len(nums) - 1 - 2,-1,-1):
            nums[i] += max(nums[i + 2], nums[i + 3] if i + 3 < len(nums) else 0)

        return max(nums[0],nums[1] if len(nums) > 1 else 0)     


        