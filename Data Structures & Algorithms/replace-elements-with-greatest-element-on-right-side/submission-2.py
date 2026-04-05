class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #  5 5 3 2 2 2
        # [2,4,5,3,1,2]

        maxElement = arr[-1]

        for i in range(len(arr) - 1, - 1, - 1):
            temp = arr[i]
            arr[i] = maxElement
            maxElement = max(maxElement,temp)

        arr[-1] = -1

        return arr
            


        