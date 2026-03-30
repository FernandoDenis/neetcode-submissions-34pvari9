class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        count_nums = Counter(nums)

        i = 1
        while i in count_nums:
            i += 1

        return i 
    
        