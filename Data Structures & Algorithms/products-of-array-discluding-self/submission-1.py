class Solution:
    # 1,2,4,6
    # lA 1,1,2,8
    # rA 48,24,6,1
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArray = [1] * len(nums)
        rightArray = [1] * len(nums)

        total = 1
        for i in range(len(nums)):
            leftArray[i] = total
            total *= nums[i]

        total = 1

        for i in range(len(nums) - 1, -1, -1):
            rightArray[i] = total
            total *= nums[i]

        res = []

        for i in range(len(nums)):
            res.append(leftArray[i] * rightArray[i])

        return res