from student_system.person import Person
from course import Course

class Professor(Person):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, salary, course):
        super().__init__(first_name, last_name, date_of_birth, phone_number)
        self.salary = salary
        self.courses = course
        self.got_raise = False

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, course):
        if isinstance(course, Course):
            self._course = list()
            self._course.append(course)
        elif isinstance(course, list):
            for entry in course:
                if not isinstance(entry, Course):
                    raise ValueError("Invalid Course")

            self._course = course
        else:
            raise ValueError("Invalid Course")

    def check_for_raise(self):
        if len(self._courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    def add_course(self, course):
        if not isinstance(course, Course):
            raise ValueError("Invalid Course")

        self._course.append(course)