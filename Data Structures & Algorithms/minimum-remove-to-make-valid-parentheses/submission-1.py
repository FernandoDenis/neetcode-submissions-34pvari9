class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        result = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                s[i] = 0
            elif s[i] == ")":
                if stack:
                    pos = stack.pop()
                    s[pos] = "("
                    continue
                else:
                    s[i] = 0

        for char in s:
            if char == 0:
                continue
            result.append(char)

        return "".join(result)





        