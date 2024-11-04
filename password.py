def is_between_8_and_20(password):
    length_of_password = len(password)
    if length_of_password < 8 or length_of_password > 20:
        return False
    else:
        return True


def has_one_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def has_one_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_one_number(password):
    for num in password:
        if num.isnumeric():
            return True
    return False


def has_one_symbol(password):
    symbols = "!@#$%&*"
    for char in password:
        if char in symbols:
            return True
    return False


def main():
    '''
    [x] Set up your program in a main() function
   [x] Create a Python program that asks the user to input a password.
   [x] Ensure the password meets the following criteria:
        Between 8 to 20 characters long.
        Contains at least one uppercase letter.
        Contains at least one lowercase letter.
        Includes at least one number.
        Includes at least one symbol from the set: !@#$%&*.
    [x]Use a while loop to keep asking for the password until all criteria are met.
    [x]Once a valid password is entered, prompt the user to enter it again for confirmation.
    [x]Use try-except blocks to handle any errors or exceptions that occur.
    If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.
    '''
    while True:
        try:
            user_input = input("Enter a password:  ")
            length = is_between_8_and_20(user_input)
            upper = has_one_uppercase(user_input)
            lower = has_one_lowercase(user_input)
            number = has_one_number(user_input)
            symbol = has_one_symbol(user_input)
            if not length and upper and lower and number and symbol:
                print("Try again")
            else:
                confirm_password = input("Re-enter you password to confirm:  ")
                if user_input == confirm_password:
                    print("Password successfully! ")
                    break
                else:
                    print("Password does not match. Please try again.  ")
        except Exception as e:
            print("An error occurred: ", e)


main()
