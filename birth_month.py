import calendar
from datetime import datetime

# Main Function


def main():
    print("\n\n")  # Add some spacing
    try:
        # Get the current year
        current_year = datetime.now().year

        # Prompt the user for their birth month
        birth_month = int(input("Enter your birth month (1-12): "))

        # Prove the input
        if not (1 <= birth_month <= 12):
            print("Error: Please enter a number between 1 and 12.")
            return

        # Display the calendar for the specified month and current year
        cal = calendar.month(current_year, birth_month)
        print(f"\nHere is the calendar for {
              calendar.month_name[birth_month]} {current_year}:")
        print(cal)

    except ValueError:
        print("Error: Invalid input. Please enter a numeric value between 1 and 12.")


main()
