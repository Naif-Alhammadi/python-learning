class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self.name

    def Hello(self):
        print("hello, world")


class student(Person):
    def __init__(self, name, age, tall):
        super().__init__(name, age)
        self.tall = tall

    def Hello(self):
        super().Hello()
        print("hello self")

class Person:
    def __init__(self, name, ph, email):
        self.name = name
        self.email = email
        self.ph = ph

    def purchase(self):
        pass

class Professor(Person):
    def __init__(self, name, ph, email, staff, years, number):
        super().__init__(name, ph, email)
        self.__years = years
        self.number = number
        self.staff = staff

    @property
    def salary(self):
        return self.__years * 1000



professor = Professor('naif', 774556789, "@gmail.com", 2, 1 , 1)
print(professor.salary)