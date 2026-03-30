class Solution:
    def compress(self, chars: List[str]) -> int:
        #      l r
        # [1,2,2]
        # l 2
        # c 1
        if len(chars) == 1:
            return 1

        l, r = 0,0
        letter = ""
        counter = 0

        while l < len(chars) and r < len(chars):
            chars[l] = chars[r]
            
            letter = chars[r]
            counter = 1
            r += 1
                
            while r < len(chars) and chars[r] == letter:
                counter += 1
                r += 1
                
            if counter == 1:
                l += 1
            else:
                l += 1
                number = str(counter)

                for num in number:
                    chars[l] = num
                    l += 1

            letter = ""

        return l



        