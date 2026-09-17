from course import Course
from student import Student
from datetime import datetime

class Enroll:
    def __init__(self, grade, course, student):
        self.date = datetime.now()
        self.grade = grade
        self.course = course
        self.student = student

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, student):
        if isinstance(student, Student) and self._student == []:
            self._student = list()
            self._student.append(student)
        elif isinstance(student, Student) and self._student != []:
            self._student.append(student)

    
        @property
        def course(self):
             return self._course
        
        @course.setter
        def course(self, course):
            if isinstance(course, Course) and self._course == []:
                self._student = list()
                self._student.append(student)
            elif isinstance(course, Course) and self._course != []:
                self._student.append(course)

        def set_grade(self, grade):
            self.grade = grade