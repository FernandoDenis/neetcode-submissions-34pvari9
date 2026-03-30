class Solution:
    # x i
    # 0,0,0
    # res
    # dict {0:[0,1,2]}
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dictionary_of_numbers = {}
        repeated_positions = set()
        repeated_triplets = set()
        res = []
        for idx, value in enumerate(nums):
            if value in dictionary_of_numbers:
                dictionary_of_numbers[value].append(idx)
            else:
                dictionary_of_numbers[value] = [idx]

        for idx, value in enumerate(nums):
            for i in range(idx + 1,len(nums)):
                if (0 - (nums[idx] + nums[i])) in dictionary_of_numbers: 
                    for num in dictionary_of_numbers[0 - (nums[idx] + nums[i])]:
                        if num != idx and num != i:
                            sorted_triplet = tuple(sorted([idx,i,num]))
                            triplet = [nums[sorted_triplet[0]],nums[sorted_triplet[1]], nums[sorted_triplet[2]]]
                            if sorted_triplet not in repeated_positions and tuple(sorted(triplet)) not in repeated_triplets:
                                repeated_triplets.add(tuple(sorted(triplet)))
                                repeated_positions.add(sorted_triplet)
                                res.append(triplet)
        print(repeated_positions)
        return res

                