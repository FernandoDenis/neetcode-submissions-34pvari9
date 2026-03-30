class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [9,1,4,2,3,3,7]#
        # {9:1, 1:4,4:2,2:3,3:2,7:1}
        #          1      
        #  4  2    3  3  7
        # 7 3 3 7  7  7   
        if not nums:
            return 0
        #  i         j
        # [0,3,1,3,2,3] 
        # [4,1,3,1,2,1]
        n = len(nums)
        num_consecutive = [0] * n 

        for i in range(n - 1, - 1, -1):
            consecutive = 0 # 3

            for j in range(i + 1,n):
                if nums[j] > nums[i]:
                    consecutive = max(consecutive, num_consecutive[j])

            num_consecutive[i] = consecutive + 1

        return max(num_consecutive)





        
        