class Solution:
    def isValid(self, s: str) -> bool:
        
        stack_brackets = []
        dict_brackets = {")":"(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack_brackets.append(bracket)
            else:
                if stack_brackets:
                    last_open_bracket = stack_brackets.pop()
                else:
                    return False

                if dict_brackets[bracket] != last_open_bracket:
                    return False

        if stack_brackets:
            return False
        else:
            return True


        