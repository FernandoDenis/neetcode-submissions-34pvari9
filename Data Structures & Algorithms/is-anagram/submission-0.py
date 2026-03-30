class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

        if len(lettersS) == len(lettersT):
            for key in lettersS:
                if key in lettersT:
                    if lettersT[key] != lettersS[key]:
                        return False
                else:
                    return False
            return True
        else:
            return False
        