class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicateNumbers = set()

        for i in nums:
            if i in duplicateNumbers:
                return True
            duplicateNumbers.add(i)

        return False

        # return len(set(nums)) != len(nums)
