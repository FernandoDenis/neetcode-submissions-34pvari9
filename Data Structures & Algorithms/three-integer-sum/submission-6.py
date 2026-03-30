class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        dic_num = Counter(nums)

        def dfs(idx, array, total):
            if len(array) == 2:
                need = -total
                if dic_num[need] > 0:
                    triplet = tuple(sorted(array + [need]))
                    result.add(triplet)
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                dic_num[nums[i]] -= 1
                if dic_num[nums[i]] >= 0:
                    array.append(nums[i])
                    dfs(i + 1, array, total + nums[i])
                    array.pop()
                dic_num[nums[i]] += 1

        dfs(0, [], 0)
        return [list(x) for x in result]