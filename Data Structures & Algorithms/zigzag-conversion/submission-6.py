class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #              0     
        # GOOGLEISHIRING
        # firstPatter = idx + numRows + (numRows - 2)
        # secomPatter = idx + numRows + (numRows - 2) - row

        # G   I
        # O  ES
        # O L H
        # G

        if numRows == 1:
            return s

        result = [] # G,I,N

        for i in range(numRows):
            if i >= len(s):
                break
            if i == 0 or i == numRows - 1:
                for j in range(i, len(s), numRows + (numRows - 2)):
                    result.append(s[j])
            else:
                firstPattern = False # flase
                result.append(s[i]) # O 
                j = i # 1
                while j < len(s): 
                    if firstPattern:
                        nextPosition = j + numRows + (numRows - 2)
                        if nextPosition < len(s):
                            result.append(s[nextPosition])
                            firstPattern = not firstPattern
                            j = nextPosition
                        else:
                            break
                    else:
                        nextPosition = j + numRows + (numRows - 2) - (i * 2) # 1 + 4 +2 - 1
                        if nextPosition < len(s):
                            result.append(s[nextPosition])
                            firstPattern = not firstPattern
                        else:
                            break

        return "".join(result)



        