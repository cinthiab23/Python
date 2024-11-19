# Define a custom exception
class NotNumericError(Exception):
    pass

# Main


def main():
    while True:
        try:
            # Prompt for user input
            user_input = input("Please enter a number: ")

            # Check if the input is numeric using the str.isnumeric() method
            if not user_input.isnumeric():
                # Raise the custom exception  not numeric
                raise NotNumericError(
                    "Invalid input. You must enter a number.")

            # convert to a float and break the loop
            number = float(user_input)

        except NotNumericError as e:
            #  invalid input
            print(f"Error: {e}")

        else:
            # Confirm valid input
            print(f"Thank you! You've entered a valid number: {number}")
            break

        finally:
            # To indicate the end of the iteration
        print("End of input validation process.\n")


main()
