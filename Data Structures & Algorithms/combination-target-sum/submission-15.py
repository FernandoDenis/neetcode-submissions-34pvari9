class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #  0
        # [2,5,6,9]
        # array [2,2,2,2,2]
        # addition 4
        nums.sort()
        result = []
        cur = []

        def dfs(idx: int, addition: int) -> None:
            if addition == target:
                result.append(cur.copy())
                return

            for i in range(idx, len(nums)):
                num = nums[i]
                new_sum = addition + num

                if new_sum > target:
                    break  # poda por estar ordenado

                cur.append(num)
                dfs(i, new_sum)   # i (no i+1) porque se puede repetir
                cur.pop()

        dfs(0, 0)
        return result
        
        
        