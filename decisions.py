# Ask the user for their age


def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age:"))
            return age
        except ValueError:
            print(
                "Invalid input. Please enter a valid number."
            )  # If it fails, inform the user and ask again


age = get_valid_age()

# Check if user is old enough to drive

if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

# Check if user can vote

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

# Check if user can legally buy alcohol

if age >= 21:
    print("You are legally allowed to buy alcohol. ")
else:
    print("You are not legally allowed to buy alcohol.")

# Check if user is eligible for senior discount

if age >= 65:
    print("You  are eligible for a senior discount.")
else:
    print("You are not eligible for a senior discount.")
