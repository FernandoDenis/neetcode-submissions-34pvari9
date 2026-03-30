class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        # GINO
        # ROW 1
        newString = []
        row = 0 # 1
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                idx = i
                while idx < len(s):
                    newString.append(s[idx])
                    idx += numRows + numRows - 2
            else:
                idx = i # 1
                middle = (row - 1) * 2 # 0
                even_od = True # True
                while idx < len(s): # 1 < x
                    if even_od: 
                        newString.append(s[idx])
                        idx += (numRows - (row + 1)) * 2 # (4 - (1 + 1)) * 2 #  (numRows + 1) - middle
                    elif idx < len(s):
                        newString.append(s[idx])
                        idx += middle + 2
                    else:
                        break
                    even_od = not even_od
            row += 1

        return "".join(newString)


        