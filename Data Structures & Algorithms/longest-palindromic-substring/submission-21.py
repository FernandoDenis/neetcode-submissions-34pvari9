class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubstring = ""

        def isPalindromic(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False, r
                l += 1
                r -= 1
            return True, r

        for i in range(len(s)):
            j = len(s) - 1

            while i <= j:
                if s[i] == s[j]:
                    pal, fail_r = isPalindromic(i, j)

                    if pal:
                        string = s[i:j + 1]

                        if len(string) > len(longestSubstring):
                            longestSubstring = string

                        break
                    else:
                        nuevo_j = fail_r + 1

                        if nuevo_j >= j:
                            j -= 1
                        else:
                            j = nuevo_j
                else:
                    j -= 1

        return longestSubstring