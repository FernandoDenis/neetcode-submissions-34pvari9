class Solution:
    def rob(self, nums: List[int]) -> int:
        #  4 4 3 3
        # [1,1,3,3]

        if len(nums) < 2:
            return max(nums)

        for i in range(len(nums) - 1, - 1, -1):
            if i + 3 < len(nums):
                nums[i] += max(nums[i + 2], nums[i + 3])
            elif i + 2 < len(nums):
                nums[i] += nums[i + 2]

        return max(nums[0],nums[1])
        