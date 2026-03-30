class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = []
        triplets_used = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and (nums[i],nums[j],nums[k]) not in triplets_used:
                        triples.append([nums[i],nums[j],nums[k]])
                        triplets_used.add((nums[i],nums[j],nums[k]))
                    elif nums[i] + nums[j] + nums[k] > 0:
                        break
        
        return triples