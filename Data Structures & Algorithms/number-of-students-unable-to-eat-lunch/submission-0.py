class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter_students = Counter(students)

        sandwiches = deque(sandwiches)
        students = deque(students)

        while len(students) > 0:
            if counter_students[sandwiches[0]] <= 0:
                break

            if sandwiches[0] == students[0]:
                counter_students[sandwiches[0]] -= 1
                sandwiches.popleft()
                students.popleft()
            else:
                student = students.popleft()
                students.append(student)
        
        return len(students)
            

        