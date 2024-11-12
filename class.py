# class definition for a person
class Person:
    def __init__(self, name, address, age, phone_number):
        self._name = name
        self._address = address
        self._age = age
        self._phone_number = phone_number

    # Method to get person information
    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age

    def get_phone_number(self):
        return self._phone_number

    # Display data person information
    def display_info(self):
        print(self.get_info())
# return person information

    def get_info(self):
        return (
            f"Name: {self.get_name()}\n"
            f"Address: {self.get_address()}\n"
            f"Age: {self.get_age()}\n"
            f"Phone Number: {self.get_phone_number()}\n"
        )


# Creating 3 person Instances
person1 = Person("Selena", "123 Beach Rd", 23, "123-4567")
person2 = Person("Bobby", "456 Elm St", 25, "789-1234")
person3 = Person("May", "567 Lakewood Av", 30, "456-9874")

# Display data for each instance
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
