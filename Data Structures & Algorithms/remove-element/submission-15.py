class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 3,1,5,2,5,5,5  2
        #     ^ ^
        # 
        
        l, r = 0, len(nums) - 1

        while l < r:
            while l < r and nums[r] == val:
                r -= 1

            if not l < r:
                break

            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            else:
                l += 1

        if 0 <= l < len(nums) and nums[l] == val:
            return l

        return l + 1        