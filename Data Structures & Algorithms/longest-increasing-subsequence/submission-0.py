class Solution:
    #    i        j
    # [9,1,4,2,3,3,7]
    # [1,4,2,3,2,2,1]
    # val 1
    # longest_ number 3

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length_of_subsequence = [1] * n

        for i in range(n - 2, -1 , -1):
            val = nums[i]
            longest_number = 0
            for j in range(i + 1,n):
                if nums[j] > val:
                    longest_number = max(longest_number, length_of_subsequence[j])
            length_of_subsequence[i] += longest_number

        return max(length_of_subsequence)


        