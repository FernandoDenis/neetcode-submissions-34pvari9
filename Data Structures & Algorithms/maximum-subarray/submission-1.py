class Solution:
    #              num
    # [2,-3, 4,-2,2,1,-1,4]
    # total 8
    # largest_sum 4
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float("-inf")
        total = 0

        for num in nums:
            if total < 0:
                total = 0
            total += num
            largest_sum = max(largest_sum, total)

        return largest_sum
        