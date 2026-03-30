class Solution:
    # set 91,1,24,2,25,26,6
    #      nu
    # 91,2,24,1,25,26,6 -> 24,25,26 
    # longest 3
    # subseq 3
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_of_numbers = set(nums)

        longest_subsequence = 0

        for num in nums:
            if num - 1 not in set_of_numbers:
                subsequence_length = 0
                while num in set_of_numbers:
                    subsequence_length += 1
                    num += 1
                longest_subsequence = max(subsequence_length, longest_subsequence)

        return longest_subsequence

        