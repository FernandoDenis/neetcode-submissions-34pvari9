class Solution:
    def scoreOfString(self, s: str) -> int:
        # code
        #  i
        # result 24
        # susbtraction 1

        result = 0

        substraction = 0

        for i in range(1, len(s)):
            substraction = abs(ord(s[i]) - ord(s[i - 1]))
            result += substraction

        return result
        