class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lettersS = {}
        lettersT = {}

        for letter in s:
            if letter in lettersS:
                lettersS[letter] += 1
            else:
                lettersS[letter] = 1

        for letter in t:
            if letter in lettersT:
                lettersT[letter] += 1
            else:
                lettersT[letter] = 1

        for key in lettersS:
            if key in lettersT:
                if lettersT[key] != lettersS[key]:
                    return False
            else:
                return False
        return True
        