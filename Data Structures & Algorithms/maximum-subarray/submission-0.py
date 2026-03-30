class Solution:
    #       ij
    # [2,-2,4]
    # largest_Sum = 4
    # larger_sum = 2
    # total 2
    def maxSubArray(self, nums: List[int]) -> int:

        largest_sum = float("-inf")

        for i in range(len(nums)):
            larger_sum = float("-inf")
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                larger_sum = max(larger_sum, total)
            largest_sum = max(largest_sum, larger_sum)

        return largest_sum

        