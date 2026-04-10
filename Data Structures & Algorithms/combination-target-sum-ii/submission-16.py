class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # [9,2,2,4,6,1,5]
        # [1,2,2,4,5,6,9]
        #  1,2,5
        #  [[1,2,5], ]

        candidates.sort()
        result = []

        def dfs(idx, array, total):
            if total == target:
                result.append(array.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i -1]:
                    continue
                if candidates[i] + total <= target:
                    array.append(candidates[i])
                    dfs(i + 1,array,total + candidates[i])
                    array.pop()
                else:
                    return
                
            return 

        dfs(0,[],0)

        return result
        