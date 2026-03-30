class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #        l   r
        # [1,2,3,4,4]

        l,r = 0,1

        while l < len(nums) and r < len(nums):

            if nums[l] == nums[r]:

                while r < len(nums) and nums[r] == nums[l]:
                    r += 1

                if r >= len(nums):
                    break
            
                nums[l + 1] = nums[r]

                l += 1
            else:
                l += 1
                r += 1

        return l + 1

        