class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 9
        # 2,5,6,9
        # [9]]
        # 9
        # [[2,2,5]]
        nums.sort()
        result = []
        def dfs(idx, array, total):
            if total == target:
                result.append(array.copy())
                return

            for i in range(idx, len(nums)):
                addition = total + nums[i]

                if addition > target:
                    return

                array.append(nums[i])
                dfs(i, array, addition)
                array.pop()

            return

        dfs(0,[],0)
        return result

        
        