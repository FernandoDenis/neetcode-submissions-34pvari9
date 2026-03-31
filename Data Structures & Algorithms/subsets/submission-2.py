class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #    i
        # [7]
        # subsets [[],[7]]
        # arrya []

        subsets = [[]]

        def backtracking(idx,array):
            if idx >= len(nums):
                return

            for i in range(idx,len(nums)):
                array.append(nums[i])
                subsets.append(array.copy())
                backtracking(i + 1, array)
                array.pop()

            return 

        backtracking(0,[])

        return subsets 


        