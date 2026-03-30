class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #              []
        #     [1],       [2], [3]
        # [1,2] [1,3] [2,3]
        # [1,2,3]
        result = [] #[[],[1],[1,2],[1,2,3]]

        def dfs(array, idx): # [1,2] 3
            if idx > len(nums):
                return 

            result.append(array)

            for i in range(idx, len(nums)): 
                print(array)
                copyArray = array.copy()
                copyArray.append(nums[i]) #[2]
                dfs(copyArray,i + 1) 

            return
        
        dfs([],0)
        return result
        