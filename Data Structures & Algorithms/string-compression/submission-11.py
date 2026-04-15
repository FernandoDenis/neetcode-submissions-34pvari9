class Solution:
    def compress(self, chars: List[str]) -> int:
        # ["A"]
        #      ^  ^                           
        # countere 1
        # ya acabe la exsplicacion

        l,r = 0,0

        while r < len(chars):
            chars[l] = chars[r]

            counter = 0

            while r < len(chars) and chars[r] == chars[l]:
                r += 1
                counter += 1

            if counter == 1:
                l += 1
            else:
                number_as_string = str(counter)

                for num in number_as_string:
                    l += 1
                    chars[l] = num

                l += 1

        return l



        