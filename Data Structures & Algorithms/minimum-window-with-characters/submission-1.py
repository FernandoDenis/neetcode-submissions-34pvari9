class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #      l  r
        # OUZODYXAZV
        # {X:1,Y:1,Z:1}
        # {0:2,U:1:,Z:2,D:1,Y:1,X:1:A:1,V:1}

        substring_to_search = Counter(t)

        actual_substring = defaultdict(int)

        substring = deque()

        l = 0

        minimum_substring = ""

        for idx, letter in enumerate(s):
            actual_substring[letter] += 1
            substring.append(letter)

            while l < idx and actual_substring[s[l]] > substring_to_search[s[l]]:
                substring.popleft()
                actual_substring[s[l]] -= 1
                l += 1

            for key in substring_to_search:
                if key not in actual_substring or substring_to_search[key] > actual_substring[key]:
                    break
            else:
                if minimum_substring == "" or len(substring) < len(minimum_substring):
                    minimum_substring = "".join(substring)

        return minimum_substring
        