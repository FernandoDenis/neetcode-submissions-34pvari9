class Solution:
    def compress(self, chars: List[str]) -> int:
        #       l                                    r
        # ["a","a","a","a","a","a","a","a","a","a","a"]

        l, r = 0, 0
        character = None # None
        count_of_character = 1
        while r < len(chars):
            chars[l] = chars[r] 
            character = chars[r] # a

            l += 1
            count_of_character = 1 # 11

            while r + 1 < len(chars) and chars[r + 1] == character:
                r += 1
                count_of_character += 1
            
            # Move r to the start of the next group
            r += 1

            if count_of_character > 1:
                string_number = str(count_of_character)

                for num in string_number:
                    chars[l] = num
                    l += 1
        return l