# Employee class
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Getters
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def __str__(self):
        return f"Employee Name: {self.__name}, Employee Number: {self.__number}"

# ProductionWorker subclass definition


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    # Getter
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    # Setters
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def __str__(self):
        shift = "Day" if self.__shift_number == 1 else "Night"
        return (
            f"{super().__str__()}, Shift: {shift}, Hourly Pay Rate: ${
                self.get_hourly_pay_rate():.2f}"
        )
# Main function and display a ProductionWorker instance


def main():
    print("Enter Employee Details:")
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number:  ")
    shift_number = int(
        input("Enter the shift number (1 for Day, 2 for Night):")
    )
    hourly_pay_rate = float(input("Enter the hourly pay rate:  "))

    # ProductionWorker instance
    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)

    # Display details
    print("\nStored Employee Details: ")
    print(worker)


main()
