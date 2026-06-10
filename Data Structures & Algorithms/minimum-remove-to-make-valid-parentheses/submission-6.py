class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # ))()((
        # 
        s = list(s) # [0,0,(),0,0]
        stack = [] # [4,5]

        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
                s[idx] = 0
            elif char == ")":
                if stack:
                    i = stack.pop()
                    s[i] = "("
                else:
                    s[idx] = 0

        res = []

        for char in s:
            if char == 0:
                continue
            res.append(char)

        return "".join(res)                
        