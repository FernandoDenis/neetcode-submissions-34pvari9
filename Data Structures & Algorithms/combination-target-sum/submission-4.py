class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #  0
        # [2,5,6,9]
        # array [2,2,2,2,2]
        # addition 4

        result = []

        def dfs(idx, array, addition):
            if idx >= len(nums):
                return False

            for i in range(idx, len(nums)):
                num = nums[i]
                if addition + num == target:
                    print(array)
                    print(addition)
                    temp = array.copy()
                    temp.append(num)
                    result.append(temp)
                elif addition + num < target:
                    temp = array.copy()
                    temp.append(num)
                    dfs(i, temp, addition + num)

            return True

        dfs(0,[],0)

        return result
        
        
        