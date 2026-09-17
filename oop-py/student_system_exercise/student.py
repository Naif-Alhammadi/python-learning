from person import Person
from enorll import Enroll
class Student(Person):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, international=False):
        super().__init__(first_name, last_name, date_of_birth, phone_number)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enrol):
        if not isinstance(enrol, Enroll):
            raise ValueError("Invalid Enroll")
        self.enrolled.append(enrol)

    def is_on_probation(self):
        pass

    def is_part_time(self):
        return self.enrolled <= 3