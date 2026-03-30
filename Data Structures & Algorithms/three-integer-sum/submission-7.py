class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dic_num = Counter(nums)
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            dic_num[nums[i]] -= 1

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                dic_num[nums[j]] -= 1

                total = nums[i] + nums[j]
                diff = -total

                if diff in dic_num and dic_num[diff] > 0:
                    triplet = [nums[i], nums[j], diff]
                    triplet.sort()
                    result.append(tuple(triplet))

                dic_num[nums[j]] += 1

            dic_num[nums[i]] += 1

        result.sort()

        if not result:
            return []

        unique = [result[0]]

        for k in range(1, len(result)):
            if result[k] != result[k - 1]:
                unique.append(result[k])

        return [list(t) for t in unique]