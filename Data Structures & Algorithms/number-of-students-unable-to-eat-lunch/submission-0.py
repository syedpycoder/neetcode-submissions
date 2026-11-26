class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        uneaten = 0

        while students and uneaten < len(students):

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                uneaten = 0
            else:
                leftStudent = students.pop(0)
                students.append(leftStudent)
                uneaten += 1
        
        return uneaten            