class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #      
        # [-4,-1,-1,0,1,2]
        # result [-4]
        # total -6
        # 
        nums.sort()

        result = []

        def dfs(idx, array, total):
            if total == 0 and len(array) == 3:
                result.append(array.copy())
                return
            elif len(array) >= 3:
                return 

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                if len(array) >= 3 or total + nums[i] > 0:
                    break
                array.append(nums[i])
                dfs(i + 1, array, total + nums[i])
                array.pop()

            return 

        dfs(0,[],0)

        return result

                


        