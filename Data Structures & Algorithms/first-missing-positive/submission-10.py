class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #  i
        # [-1,-2,4,-5,-6,-3,1]
        # position 1
        for i in range(len(nums)):
            if nums[i] < 0 :
                nums[i] = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                position = abs(nums[i])
                if position - 1 >= len(nums):
                    continue

                if nums[position - 1] == 0:
                    nums[position - 1] = (len(nums) + 1) * -1
                else:
                    if nums[position - 1] > 0:
                        nums[position - 1] = nums[position - 1] * -1
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1

        
                
        