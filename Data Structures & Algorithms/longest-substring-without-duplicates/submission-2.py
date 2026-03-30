class Solution:
    #  l r
    # zxyzxyz
    # set x,y,z
    # res 3
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        set_substring = set()

        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in set_substring:
                set_substring.remove(s[left])
                left += 1
            
            set_substring.add(s[right])
            res = max(res, right - left + 1)

        return res
        