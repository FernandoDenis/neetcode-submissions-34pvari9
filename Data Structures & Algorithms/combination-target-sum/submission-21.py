class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [2,5,6,9]
        #    2
        #  4   7  8 
        # 6 9 9

        nums.sort()

        result  = []

        def backtracking(idx, array, total):
            if total == target:
                result.append(array.copy())
                return
            elif idx >= len(nums):
                return

            for i in range(idx, len(nums)):
                num = nums[i]
                if total + num > target:
                    break
                array.append(num)
                backtracking(i, array, total + num)
                array.pop()

            return

        backtracking(0,[],0)

        return result

            