class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #        i          i
        # s = "egg", t = "add"
        dictionary_of_letters = {}
        letters_used = set()
        # {e:a,g:d}
        for i in range(len(s)):
            letter = s[i]
            if letter in dictionary_of_letters:
                if dictionary_of_letters[letter] != t[i]:
                    return False
            elif t[i] in letters_used:
                return False
            else:
                dictionary_of_letters[letter] = t[i]
                letters_used.add(t[i])

        return True
        