class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #          l 
        # [3,4,5,6,1,2]

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid

        start = l
        l, r = 0, len(nums) - 1

        if target >= nums[start] and target <= nums[r]:
            l = start
        else:
            r = start - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        
        if nums[l] == target:
            return l

        return -1
        