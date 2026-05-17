class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #          i
        # [1,4,1,2,1,4,1,2]

        n = len(nums)

        for i in range(n):
            nums.append(nums[i])

        return nums
        
        