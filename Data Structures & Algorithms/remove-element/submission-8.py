class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #                l r
        # [7]
        # 7
        if not nums or (len(nums) == 1 and nums[0] == val):
            return 0

        l, r = 0, 1
        seeing = False
        while l < len(nums) and r < len(nums):
            if nums[l] == val:
                seeing = True
                while r < len(nums) and nums[r] == val:
                    r += 1

                if r >= len(nums):
                    break

                nums[l],nums[r] = nums[r], nums[l]
            l += 1
            r += 1

        if not seeing:
            return l + 1

        return l

        