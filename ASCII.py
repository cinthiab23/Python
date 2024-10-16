def main():
    # User input a character
    user_input = input("Enter a character: ")

    # loop until user enters one character
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")

    # convert to ascii value
    ascii_value = ord(user_input)

    # display the result
    print(f"The ASCII value of  {user_input}  is {ascii_value}")


main()
