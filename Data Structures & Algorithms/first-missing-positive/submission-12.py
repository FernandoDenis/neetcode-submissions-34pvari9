class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #           i
        # [0,-2,7,0,2]
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            if abs(nums[i]) != 0:
                position = abs(nums[i]) # 2
                # [0,0, 1,-5]
                if position - 1 < len(nums) and nums[position - 1] > 0: #[-1,0,0,3]
                    nums[position - 1] = nums[position - 1] * -1
                elif position - 1 < len(nums) and nums[position - 1] == 0:
                    nums[position - 1] = (len(nums) + 1) * -1
                    
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1

        