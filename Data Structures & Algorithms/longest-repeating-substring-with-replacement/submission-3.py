class Solution:
    # {A:2,B:2}
    #  l  r
    # AABABBA
    # res 4
    # letter max 3
    def characterReplacement(self, s: str, k: int) -> int:

        letters_frequency = defaultdict(int)

        left = 0

        letter_max_frequency = 0

        res = 0

        for right, letter in enumerate(s):
            letters_frequency[letter] += 1
            letter_max_frequency = max(letter_max_frequency, letters_frequency[letter])

            while (right - left + 1) - letter_max_frequency > k:
                letters_frequency[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res


        