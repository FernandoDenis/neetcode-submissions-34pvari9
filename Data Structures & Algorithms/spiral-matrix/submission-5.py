class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """[[1,2,3],
            [4,5,6],
            [7,8,9]]"""

        left = 0 # 0
        right = len(matrix[0]) # 1
        top = 0 # 1
        bottom = len(matrix) # 2

        result = [] # 1,2,4

        while left < right and top < bottom:

            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if left >= right or top >= bottom:
                break
            
            for i in range(right - 1, left - 1, -1):
                print(right,left,i)
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result

        