class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # 2,-1,1,2 # 2
        # 0:1, 2:2, 1:1
        # 2

        prefix_sum = {0:1}

        subarray_k = 0
        total = 0
        res = 0
        for num in nums:
            total += num

            diff = total - k

            if diff in prefix_sum:
                res += prefix_sum[diff]
            
            if total in prefix_sum:
                prefix_sum[total] += 1
            else:
                prefix_sum[total] = 1

        return res