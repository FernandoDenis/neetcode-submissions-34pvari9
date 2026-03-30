class Solution:
    def romanToInt(self, s: str) -> int:
        romans_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        l, r = 0,0

        integer_numeral = 0

        while l < len(s) and r < len(s):
            if s[l] == s[r]:
                while r < len(s) and s[r] == s[l]:
                    r += 1
                
                if r >= len(s):
                    while l < len(s):
                        integer_numeral += romans_numerals[s[l]]
                        l += 1
                    return integer_numeral
            else:
                if romans_numerals[s[l]] > romans_numerals[s[r]]:
                    while s[l] != s[r]:
                        integer_numeral += romans_numerals[s[l]]
                        l += 1
                else:
                    substract = 0
                    while s[l] != s[r]:
                        substract += romans_numerals[s[l]]
                        l += 1
                    
                    integer_numeral += (romans_numerals[s[r]] - substract)
                    r += 1
                    l += 1

        return integer_numeral

        