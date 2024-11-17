# Class pet definition
class Pet:
    def __init__(self, kind, breed, name):
        # instance attributes
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getting and setter  Methods
    def get_kind(self):
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Method print details
    def print_details(self):
        print(f"Pet Details: \n   Kind: {self.__kind}\n  Breed: {
              self.get_breed()}\n  Name: {self.__name}\n")
# Main functions


def main():
    pet1 = Pet("Dog", "Pitbull", "Bobby")
    pet2 = Pet("Cat", "Maine Coon", "Raven")
    pet3 = Pet("Geckos", "Leopard Geckos", "Bella")

    # print_details method for each pet
    print("Pet Information:")
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

    # Special methods or functions
    print("Special Methods and Functions: ")

    # __name__: Display class
    print(f"Class Name (using__name__): {Pet.__name__}")

    # type(): show the class
    print(f"Type of pet1 (using types()): {type(pet1)}")

    # __module__: Return the module name of Pet class is defined
    print(f"Module Name(using__module__): {Pet.__module__}")

    # __bases__: display the base classes of the pet class
    print(f"Base Classes of Pet (using__bases__): {Pet.__bases__}")

    # getattr(): Use it to access an attribute of a Pet instance
    print(f"Accessing 'breed' of pet2 using getattr(): {
          getattr(pet2, '_Pet__breed')}")

    # isinstance(): Check if an instance is of the Pet class
    print(f"Is Pet3 an instance of the Pet class (using isinstance()): {
          isinstance(pet3, Pet)}")


main()
