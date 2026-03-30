class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello","World"]
        # stirng 5#Hello5#World
        string = []

        for word in strs:
            string.append(f"{len(word)}#{word}")

        return "".join(string)

    def decode(self, s: str) -> List[str]:
        #        i
        # 5#Hello5#World
        # stirng[]
        string_list = []

        i = 0
        number = ""
        while i < len(s):
            char = s[i]
            if char.isdigit():
                number += char
            elif char == "#":
                number = int(number) # 5
                print(number)
                string_list.append(s[i + 1:i + number + 1])
                print(string_list)
                i = i + number
                number = ""

            i += 1

        return string_list
