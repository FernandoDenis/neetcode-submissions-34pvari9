class Solution:
    def compress(self, chars: List[str]) -> int:
        #               l                             r
        # ["a","1","1","a","a","a","a","a","a","a","a"]

        l, r = 0,0

        while l < len(chars) and r < len(chars):
            chars[l] = chars[r]
            character = chars[r]

            character_count = 0

            l += 1

            while r < len(chars) and chars[r] == character:
                character_count += 1
                r += 1

            if character_count > 1:

                string_number = str(character_count)

                for num in string_number:
                    chars[l] = num
                    l += 1

        return l

                
        