class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1,2,1,1]
        # 
        n = len(nums)   

        if n <= 2:
            return max(nums)

        dict_memo = {}
        

        def memo(idx, cache):
            if idx >= n:
                return 0

            if idx in cache:
                return cache[idx]
            # cache[1] = 
                                            
            cache[idx] = max(memo(idx + 2, cache), memo(idx + 3, cache)) + nums[idx]

            return cache[idx]

        return max(memo(0,dict_memo), memo(1,dict_memo))
