class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or len(nums) == 1:
            return 0
        #    l r
        # [0,1,3,2,2,0,4,2]
        # 2

        l, r = 0,1
        reapeated = False
        while r < len(nums):
            if nums[l] == val:
                reapeated = True
                while r < len(nums) and nums[r] == val:
                    r += 1

                if r >= len(nums):
                    break

                nums[l],nums[r] = nums[r],nums[l]

            r += 1
            l += 1

        if not reapeated:
            return l + 1

        return l



        