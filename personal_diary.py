# Main function
def main():

    # Prompt the user for the current date, time, and diary entry
    date = input("Enter the current date (e.g. Month-Day-Year):  ")
    time = input("Enter the current time: ")
    entry = input("Write your diary entry:")

    # open the diary.txt file in append mode
    diary_file = open("diary.txt", "a")

    # Write the date, time, and entry into the file, and separated by blank lines
    diary_file.write(f"Date: {date}, Time: {time}\n")
    diary_file.write(f"{entry}\n")
    diary_file.write("\n")

    # Close the file
    diary_file.close()

    print("Your entry has been saved to diary.txt.")


main()
