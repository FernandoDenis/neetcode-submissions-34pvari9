class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0,len(matrix)

        while l < r:
            mid = (l + r) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break

            if target < matrix[mid][0]:
                r = mid
            else:
                l = mid + 1

        array = matrix[mid]

        l, r = 0,len(array)

        while l < r:
            mid = (l + r) // 2

            if target == array[mid]:
                return True

            if target < array[mid]:
                r = mid 
            else:
                l = mid + 1

        return False
        