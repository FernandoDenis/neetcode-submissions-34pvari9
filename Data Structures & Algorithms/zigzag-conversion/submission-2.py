class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # GOOGLEISHIRING # row
        # patter (row - 1) * 2
        # pattern (row - actRow)* 2
        # G    I    N
        # O  E S  I G
        # O L  H R
        # G    I

        # GOOGLEISHIRING # numRows 4
        # result 
        # idx 
        if numRows == 1:
            return s

        result = [] # GINOESIGOHR

        for i in range(numRows): # 
            first_pattern = (numRows - 1) * 2 # 6
            idx = i # 3
            if i == 0 or i == numRows - 1:
                while idx < len(s): # 18 < 14
                    result.append(s[idx]) 
                    idx += first_pattern
            else:
                idx2 = i # 2
                switch = True # TRUE
                while idx < len(s) and idx2 < len(s): # 14 < 14 and 14 < 14
                    if switch:
                        print(f"row: {i + 1}: {idx2}")
                        result.append(s[idx2]) 
                        idx += (numRows - (i + 1)) * 2 # 2
                    else:
                        print(f"row: {i + 1}: {idx}")
                        result.append(s[idx])
                        idx2 += first_pattern # 6
                        idx = idx2
                    switch = not switch

        return "".join(result)

