# Class definition
class Pet:
    # Class variable
    vet_name = "Pet Veterinary Clinic"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Private instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter methods
    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    # Setter methods
    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value

    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

    # Method to print pet details
    def print_pet_details(self):
        print("Pet Details:", vars(self))

    # Method to print basic info about the pet and owner
    def print_info(self):
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary Office: {Pet.vet_name}")


# main Function
def main():
    # Creating instances of Pet
    pet1 = Pet("Selena", "Janko", 111, "Raven", "Cat")
    pet2 = Pet("Bobby", "Smith", 123, "Bella")
    pet3 = Pet("May", "Flores", 456, "Autumn", "Rabbit")

    # Display information for each pet
    print("\nPet 1 Information:")
    pet1.print_pet_details()
    pet1.print_info()

    print("\nPet 2 Information:")
    pet2.print_pet_details()
    pet2.print_info()

    # Modify details of pet2 using setter methods
    pet2.set_pet_name("Bella")
    pet2.set_pet_type("Pitbulll")
    print("\nUpdated Pet 2 Information:")
    pet2.print_info()

    # Check for a property
    print("\nChecking if 'pet_type' exists in pet1:")
    print(hasattr(pet1, '_Pet__pet_type'))


main()
