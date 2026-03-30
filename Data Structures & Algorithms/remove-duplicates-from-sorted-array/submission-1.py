class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #    l r     
        # [1,2,2,3,4]
        l, r = 0,1
        while r < len(nums) and l < len(nums):
            if nums[l] == nums[r]:
                while r < len(nums) and nums[l] == nums[r]:
                    print(r)
                    r += 1

                if r >= len(nums):
                    break

                nums[l + 1] = nums[r]
                l += 1
                print(nums)
            else:
                nums[l + 1] = nums[r]
                r += 1
                l += 1

        return l + 1
        