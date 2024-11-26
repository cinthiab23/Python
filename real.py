# Main function
def main():
    try:
        # Open the file in read mode
        with open('python\\sales_totals.txt', 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

        # Initialize variables for total and count
        total = 0
        count = 0

        print("Sales Totals: ")

        # loop through each line
        for line in lines:
            # Newline characters and convert to float
            sale = float(line.strip())

            # Add to total and increase count by 1
            total += sale
            count += 1

            # Print formatted number
            print(f"{sale: , .2f}")

        # Calculate and display total, count, and average
        average = total / count if count else 0
        print("\nSummary: ")
        print(f"Total: {total: , .2f}")
        print(f"Number of entries: {count}")
        print(f"Average:  {average: , .2f}")

    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found. ")
    except ValueError:
        print("Error: The file contains invalid data. Please try again. ")
    except IOError:
        print("An IOError has occurred. ")


main()
