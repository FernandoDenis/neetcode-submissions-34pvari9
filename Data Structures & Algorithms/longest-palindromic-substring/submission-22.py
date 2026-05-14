class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longestPalindrome = ""
        lenLP = 0

        for i in range(len(s)):

            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:

                string = s[l:r + 1]
                
                if len(string) > lenLP:
                    longestPalindrome = string
                    lenLP = len(string)

                l -= 1
                r += 1

            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:

                string = s[l:r + 1]
                
                if len(string) > lenLP:
                    longestPalindrome = string
                    lenLP = len(string)

                l -= 1
                r += 1

        return longestPalindrome
