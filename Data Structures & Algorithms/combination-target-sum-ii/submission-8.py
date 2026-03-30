class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #  i
        # [1,2,2,4,5,6,9]
        # total 7
        # array [2,2,4]

        candidates.sort()
        result = []

        def dfs(idx, array,total):
            if total == target:
                result.append(array.copy())
            elif total > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                array.append(candidates[i])
                dfs(i + 1, array, total + candidates[i])
                array.pop()

            return 

        dfs(0,[],0)


        return result