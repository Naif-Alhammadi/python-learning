from address import Address

class Person:
    def __init__(self, first_name, last_name, date_of_birth, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.address = address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, Address):
            self._address = list()
            self._address.append(address)

        elif isinstance(address, list):
            for entry in address:
                if not isinstance(address, Address):
                    raise ValueError("Invalid Address")
            self._address = list(address)
        else:
            raise ValueError("Invalid Address")

    def add_address(self, address):
        if not isinstance(address, Address):
            raise ValueError("Invalid Address")

        self._address = address
        
def main():
    address = Address("Yemen", "Sana'a", "Amanh", "60 meter Rd", "000")
    person = Person("naif", "alhammadi", 2005, "+967 774 556 789", address)
    print(person.address)

if __name__ == "__main__":
    main()
