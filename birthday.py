from datetime import datetime


def main():
    print("\n\n")  # Add some spacing at the start for clarity
    try:
        # Get today's date
        today = datetime.today()

        # Prompt the user for their birth year, month, and day
        birth_year = int(input("What year were you born? "))
        birth_month = int(
            input("What month were you born (as a number, e.g., May = 5)? "))
        birth_day = int(input("What day of the month were you born? "))

        # Create a datetime object for the user's birthday
        birthday = datetime(birth_year, birth_month, birth_day)
        print("\nYour birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output)

        # Calculate the difference between today and the user's birthday
        delta = today - birthday
        total_days = delta.days
        print(f"\nDifference is {total_days:,} days")

        # Calculate age in years (approximately, accounting for leap years)
        # delta: delta = today-birthday
        delta_years = total_days / 365.2425
        print(f"You are approximately {delta_years:.1f} years old")

        # Calculate age in months (30.41 days per month)
        delta_months = total_days / 30.41
        print(f"You are approximately {delta_months:.1f} months old")

        # Calculate age in weeks (7 days per week)
        delta_weeks = total_days / 7
        print(f"You are approximately {delta_weeks:.1f} weeks old")

    except Exception as e:
        print(f"Oops! Something went wrong: {e}")
        main()  # Restart the program on error


main()
