class Solution:
    #   l   r
    # tab a cat
    #
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not (s[l].isalpha() or s[l].isdigit()):
                l += 1
                continue
            if not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

            
        