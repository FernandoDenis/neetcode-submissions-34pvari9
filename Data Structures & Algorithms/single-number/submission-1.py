class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # [3,2,3]
        #  2
        # 00011
        # 00011
        # 01
        res = 0
        for num in nums:
            res ^= num

        return res


        