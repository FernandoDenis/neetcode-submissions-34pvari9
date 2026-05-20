class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [-2,-1,0,2]
        # [0,4,0,-2]
        #    ^
        # [0,-5,0,2]

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                pos = abs(nums[i]) - 1

                if pos >= len(nums):
                    continue

                if nums[pos] == 0:
                    nums[pos] = -(len(nums) + 1)
                elif nums[pos] > 0:
                    nums[pos] *= -1                    

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return len(nums) + 1

        

        