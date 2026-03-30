class Solution:
    #       i
    # zxyzxyz
    # heapLetter [(6,z)]
    # setLetter z
    # substring 1
    # longestSubstring 3
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_and_position = []
        heapq.heapify(letters_and_position)
        letters_in_substring = set()

        longest_substring = 0
        substring = 0
        for i, letter in enumerate(s):
            
            if letter not in letters_in_substring:
                letters_in_substring.add(letter)
                heapq.heappush(letters_and_position, (i, letter))
                substring += 1
            else:
                while letters_and_position[0][1] != letter:
                    popLetter = heapq.heappop(letters_and_position)
                    letters_in_substring.remove(popLetter[1])
                    substring -= 1

                popLetter = heapq.heappop(letters_and_position)
                letters_in_substring.remove(popLetter[1])
                substring -= 1

                letters_in_substring.add(letter)
                heapq.heappush(letters_and_position, (i, letter))
                substring += 1

            longest_substring = max(longest_substring, substring)

        return longest_substring
        