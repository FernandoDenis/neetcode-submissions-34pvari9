class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dictionary_courses = {}

        for after,before in prerequisites:
            if after in dictionary_courses:
                dictionary_courses[after].append(before)
            else:
                dictionary_courses[after] = [before]

        inLoop = set()

        def dfs(course):
            if course not in dictionary_courses or not dictionary_courses[course]:
                return True

            if course in inLoop:
                return False

            inLoop.add(course)

            for i in range(len(dictionary_courses[course]) - 1, - 1, -1):
                newCourse = dictionary_courses[course][i]
                if not dfs(newCourse):
                    return False
                dictionary_courses[course].pop()

            inLoop.remove(course)

            return True

        for c in prerequisites:
            if not dfs(c[0]):
                return False

        return True





        