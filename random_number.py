import random  # Use the random module


def main():

    random_number = random.randint(1, 100)
    print("Guess the right number! Between (1-100)")

    # Random loop  for numbers
    while True:
        # input for a number
        try:
            guess = int(input("Enter your number between (1-100):  "))

            if guess < 1 or guess > 100:
                print("please enter a number between 1 and 100: ")
                continue

            difference = abs(guess - random_number)

            # Feedback for the user
            if difference == 0:
                print("You guessed the correct number!")
                break
            elif difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold!")

        except ValueError:
            print("Invalid number please try again.")


main()
# In my terminal im just getting COLD do dont know why?
