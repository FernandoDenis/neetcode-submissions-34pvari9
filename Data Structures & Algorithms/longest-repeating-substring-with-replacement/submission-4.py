class Solution:
    #  l   r
    # AAABABB
    def characterReplacement(self, s: str, k: int) -> int:

        count_of_letters = defaultdict(int) #{A:3, B: 2}

        maximum_frequency = 0 # 1

        l = 0 # 0

        longest_substring = 0 # 0

        for idx, letter in enumerate(s):
            count_of_letters[letter] += 1
            maximum_frequency = max(maximum_frequency, count_of_letters[letter]) # 4

            if (idx - l + 1) - maximum_frequency > k: # 
                count_of_letters[s[l]] -= 1 #
                l += 1

            longest_substring = max(longest_substring, idx - l + 1) # 5
        
        return longest_substring



        