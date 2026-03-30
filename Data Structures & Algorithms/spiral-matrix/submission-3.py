class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 
        # [[1,2],
        #  [3,4]]

        top = 0 # 1
        right = len(matrix[0]) # 1
        bottom = len(matrix) # 2
        left = 0 # 0

        result = [] # 1,2,4

        while not(top >= bottom or left >= right): # 

            for i in range(left, right):  # 0  2
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom): # 1, 2
                result.append(matrix[i][right - 1])
            right -= 1

            if top >= bottom or left >= right:
                break

            for i in range(right - 1, left - 1, -1): # 0, -1
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result


        
        