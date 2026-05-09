class Solution:
    def simplifyPath(self, path: str) -> str:
        # /neetcode/practice//...///../courses"
        # [neetcode, practice, ..., .., courses]
        # [neetcode, practice, courses]
        # /

        array_of_words = path.split("/")

        stack = []

        for word in array_of_words:
            if word:
                if word == "..":
                    if stack:
                        stack.pop()
                elif word == ".":
                    continue
                else:
                    stack.append(word)

        return "/" + "/".join(stack)
        