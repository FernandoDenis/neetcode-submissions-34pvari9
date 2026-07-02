class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        res = []

        i = 0
        for num in sorted(counter.items(), key = lambda x: -x[1]):
            if k == i:
                break

            res.append(num[0])
            i += 1

        return res
            