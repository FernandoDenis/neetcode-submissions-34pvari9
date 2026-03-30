class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        longest_substring = 0

        l, r = 0, 0
        distinct_characters = set()
        while r < len(s):
            while s[r] in distinct_characters:
                distinct_characters.remove(s[l])
                l += 1
            longest_substring = max(longest_substring,(r + 1) - l)
            
            distinct_characters.add(s[r])
            r += 1

        return longest_substring




        