class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4] # 
        #         ^     ^ 
        # {-1:1,0:1,1:0,:2:0,-4:1}
        # temp {-1:1,0:1,1:1,:2:1,-4:1}
        # [[1,0,-1]]
        # ((1,0,-1))

        nums.sort()
        dictionary_numbers = Counter(nums)
        result = []

        for i in range(len(nums)):
            dictionary_numbers[nums[i]] -= 1

            if i and nums[i] == nums[i - 1]:
                continue

            temp = dictionary_numbers.copy()


            for j in range(i + 1, len(nums)):
                dictionary_numbers[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                addition = nums[i] + nums[j]

                if 0 - addition in dictionary_numbers and dictionary_numbers[0 - addition] > 0:
                    result.append([nums[i],nums[j], 0 - addition])
            
            dictionary_numbers = temp

        return result

        


        