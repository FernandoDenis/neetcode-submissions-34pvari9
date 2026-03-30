class Solution:
    def romanToInt(self, s: str) -> int:
        # XLIX
        values_roman_numerals = {"I": 1, "V":5, "X": 10, "L":50,"C":100,"D":500,"M":1000}
        decimal_number = 0 # 49
        for idx, letter in enumerate(s): # 3 X
            if idx + 1 < len(s) and values_roman_numerals[s[idx + 1]] > values_roman_numerals[letter]:
                decimal_number -= values_roman_numerals[letter]
            else:
                decimal_number += values_roman_numerals[letter]

        return decimal_number

        