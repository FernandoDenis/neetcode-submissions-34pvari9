class Solution:
    def simplifyPath(self, path: str) -> str:
        # "/neetcode/practice//...///../courses"
        # [neetcode/practice/courses]

        path = path.split("/")
        
        stack = []

        for file in path:
            if file != "." and file:
                if file == "..":
                    if stack:
                        stack.pop()
                    continue
                stack.append(file)
                
        return "/" + "/".join(stack)

        
