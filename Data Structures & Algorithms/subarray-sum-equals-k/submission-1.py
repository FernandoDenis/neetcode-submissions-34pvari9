class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [-1,2,2,1,1]
        #         i           
        # [2,-1,1,2]
        # {0:1,2:2:1:1}
        # res 4
        # curSum 4

        # 5 3

        total = 0
        subarrays_num = 0
        dictionary_sums = {0:1}

        for num in nums:
            total += num

            diff = total - k

            if diff in dictionary_sums:
                subarrays_num += dictionary_sums[diff]

            if total in dictionary_sums:
                dictionary_sums[total] += 1
            else:
                dictionary_sums[total] = 1

        return subarrays_num

        