class Solution:
    # dictNums {3:0}
    #   i
    # 3,4,5,6
    # 7
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}

        for i in range(len(nums)):
            if (target - nums[i]) in dictNums:
                return [dictNums[target - nums[i]], i]
            else:
                dictNums[nums[i]] = i
