class Solution:
    # x i
    # 0,0,0
    # res
    # dict {0:[0,1,2]}
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result_triplets = []
        for idx, a in enumerate(nums):
            
            if a > 0:
                break

            if idx > 0 and a == nums[idx - 1]:
                continue

            l, r = idx + 1, len(nums) - 1

            while l < r:
                sum_triplet = a + nums[l] + nums[r]

                if sum_triplet > 0:
                    r -= 1
                elif sum_triplet < 0:
                    l += 1
                else:
                    result_triplets.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result_triplets

                