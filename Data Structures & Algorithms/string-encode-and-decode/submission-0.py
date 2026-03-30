class Solution:
    # ["Hello","World"]
    # s "5#Hello5#World"
    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            length = len(i)
            s += str(length) + "#" + i

        return s
    #  0123456789 
    #                i
    #           j
    # "5#Hello5#World"
    # length 5
    # word Hello
    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1
            i = j + length
            word = s[j:i]
            res.append(word)

        return res

