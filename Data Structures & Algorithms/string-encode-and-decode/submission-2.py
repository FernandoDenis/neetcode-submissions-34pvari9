class Solution:
    # ["Hello","World"]
    # 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        output_string = []
        for word in strs:
            output_string.append(str(len(word)))
            output_string.append("#")
            output_string.append(word)

        return "".join(output_string)
    
    # 5#Hello5#World
    #        i
    # res Hello,
    # l 5
    # Hello

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            length = ""
            while i < len(s) and s[i] != "#":
                length += s[i]
                i += 1

            word = ""
            i += 1
            length = int(length)

            for idx in range(i, i + length):
                word += s[idx]

            res.append(word)
            i += int(length)

        return res

