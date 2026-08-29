class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # control access (Encapsulation)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise "Age cannot be negative"
        self._age = age

    @age.getter
    def age(self):
        return self._age

naif = Student("naif", 20)
print(naif.name)
print(naif.age)
