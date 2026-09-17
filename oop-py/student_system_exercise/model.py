class Address:
    def __init__(self, country,  city, state, street, postal):
        self.country = country
        self.city = city
        self.state = state
        self.street = street
        self.postal = postal


class Person:
    def __init__(self, first_name, last_name, date_of_birth, phone_number):
        self.address = Address()
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number

class Student(Person):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, international):
        super().__init__(first_name, last_name, date_of_birth, phone_number)
        self.international = international



class Professor(Person):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, salary):
        super().__init__(first_name, last_name, date_of_birth, phone_number)
        self.salary = salary


class Course:
    def __init__(self, name, min_part, max_part):
        self.name = name
        self.min_part = min_part
        self.max_part = max_part

    def is_canceled(self):
        pass

class Enroll:
    def __init__(self, date, grade):
        self.date = date
        self.grade = grade
