from professor import Professor
from enorll import Enroll

class Course:
    def __init__(self, name, min_part, max_part, professor):
        self.name = name
        self.min_part = min_part
        self.max_part = max_part
        self.professor = professor
        self.enrolments = []


    @property
    def professor(self):
        return self._professor

    @professor.setter
    def professor(self, professor):
        if isinstance(professor, Professor):
            self._professor = list()
            self._professor.append(professor)

        elif isinstance(professor, list):
            for enrty in professor:
                if not isinstance(enrty, Professor):
                    raise ValueError("Invalid Professor")
            self._professor = professor
        else:
            raise ValueError("Invalid Professor")


    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise ValueError("Invalid Professor")
        self._professor.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise ValueError("Invalid Enroll")
        if len(self.enrolments) == self.max_part:
            raise ValueError("Can not enroll course is full")
        self.enrolled.append(enroll)

    def is_canceled(self):
        return len(self.enrolments) < self.min_part