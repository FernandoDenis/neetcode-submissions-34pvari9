class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        setNum = set(nums)
        longest_sub = 1
        for num in nums:
            i = num
            if num - 1 not in setNum:
                length = 0
                while i in setNum:
                    i += 1
                    length += 1
                longest_sub = max(longest_sub,length)

        return longest_sub


