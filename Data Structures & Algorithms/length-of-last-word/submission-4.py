class Solution:
    # "   fly me   to   the moon  "
    #                      ^
    # lsl 4
    # True

    def lengthOfLastWord(self, s: str) -> int:
        last_string_length = 0
        theresChar = False
        for i in range(len(s) - 1, - 1, -1 ):
            if theresChar and s[i] != " ":
                last_string_length += 1
            elif s[i] != " ":
                theresChar = True
                last_string_length += 1
            elif theresChar and s[i] == " ":
                break

        return last_string_length




        