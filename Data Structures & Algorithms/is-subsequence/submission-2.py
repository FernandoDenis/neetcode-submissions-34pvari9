class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # "neetcode"
        #  ^
        # "node"
        #      ^

        if len(t) < len(s):
            return False

        letterS = 0
        letterT = 0

        while letterT < len(t):
            if letterS >= len(s):
                return True

            if t[letterT] == s[letterS]:
                letterS += 1
                letterT += 1
            else:
                letterT += 1

        if letterS >= len(s):
            return True
        
        return False