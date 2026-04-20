class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [9,3,4,5,3,3,7]
        #            ^ ^
        #  1 1 1 1 1 1 1
        # maxLenght 3
        # 

        length_of_subsequence = [1] * len(nums)

        for i in range(len(nums) - 1, -1, - 1):
            max_length = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_length = max(max_length, length_of_subsequence[j])
            length_of_subsequence[i] += max_length

        return max(length_of_subsequence)
                    

        