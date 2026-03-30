class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = Counter(nums)

        res = []
        j = 0
        for i in sorted(countNums.items(), key = lambda x: -x[1] ):
            if j >= k:
                return res
            res.append(i[0])
            j += 1
        
        return res