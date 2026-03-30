class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #        i
        # [-1,-2,4]
        # 

        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):
            pos = abs(nums[i])
            if pos > 0 and pos <= n:
                nums[pos - 1] = -(abs(nums[pos - 1])) if nums[pos - 1] != 0 else -pos

        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1


                



        