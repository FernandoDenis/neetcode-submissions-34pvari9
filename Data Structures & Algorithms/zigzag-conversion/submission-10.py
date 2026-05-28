class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #  idx + numRows + (numROws - 2)
        #  idx + (numRows - row)  *2

        """
        G     H
        O   S I
        O  I  R
        G E   I G
        L     N
        """
        #              x
        # GOOGLEISHIRING # 4

        if numRows >= len(s):
            return s

        res = [] # G,I,N,O,E,S,I,G

        for i in range(numRows): # 0

            idx = i # 2

            while (i == 0 or i == numRows - 1) and idx < len(s):
                res.append(s[idx])
                idx = idx + numRows + (numRows - 2)
            
            while (i != 0 and i != numRows - 1) and idx < len(s):
                res.append(s[idx])

                idx2 = idx + (numRows - (i + 1)) * 2 # 

                if idx2 < len(s):
                    res.append(s[idx2])

                idx = idx + numRows + (numRows - 2) # 7

        return "".join(res)



        