class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = float("-inf")
        total = 0

        for num in nums:
            if total < 0:
                total = 0
            total += num
            maxSub = max(maxSub, total)

        return maxSub
        