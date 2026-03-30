class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        # is_Duplicate = set()

        # for i in nums:
        #     if i in is_Duplicate:
        #         return True

        #     is_Duplicate.add(i)

        # return False
        