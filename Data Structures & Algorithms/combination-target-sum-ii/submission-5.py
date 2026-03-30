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
                if total + candidates[i] > target:
                    break
                array.append(candidates[i])
                dfs(i + 1, array, total + candidates[i])
                array.pop()

            return 

        dfs(0,[],0)
        result.sort()
        final_result = []
        print(result)

        for i in range(len(result)):
            if i != 0 and result[i] == result[i - 1]:
                continue
            final_result.append(result[i])

        return final_result