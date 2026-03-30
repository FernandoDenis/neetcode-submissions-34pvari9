class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for idx, letter in enumerate(s):
            if letter == "(":
                stack.append((")",idx))
                s[idx] = "0"
            elif letter == ")" and stack and stack[-1][0] == ")":
                val, ix = stack.pop()
                s[ix] = "("
            elif letter.isalpha():
                continue
            else:
                s[idx] = "0"

        result = []
        print(s)
        for letter in s:
            if letter == "0":
                continue
            result.append(letter)

        return "".join(result)

        