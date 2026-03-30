class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lettersS = {}
        lettersT = {}

        for letter in s:
            lettersS[letter] = lettersS.get(letter, 0) + 1

        for letter in t:
            lettersT[letter] = lettersT.get(letter, 0) + 1

        if lettersS == lettersT:
            return True
        else:
            return False
        