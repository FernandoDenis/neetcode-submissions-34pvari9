class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,6,1,2]  
        #          l r

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        if nums[l] == target:
            return l

        if nums[l] <= target <= nums[len(nums) - 1]:
            r = len(nums) - 1
        else:
            l, r = 0, l - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1 


        
                
        