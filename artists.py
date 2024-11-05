def replace_artist(artists):
    try:
        # Asking user for index and new artist name
        index = int(
            input("Enter the number of the artist you want to replace (0-9):  "))
        new_artist = input("Enter the name of the new artist:   ")

        # replace artist at the specified index
        artists[index] = new_artist
        print(f"Artist at index {
              index} has been replaced with '{new_artist}'. ")
    except (ValueError, IndexError):
        print("Error occurred. Please check the index is a valid number and within range. ")
    except Exception as a:
        print(f"An unexpected error occurred: {a}")


def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    print("Top 10 performing Artist: ")
    for i, artist in enumerate(top_artists):
        print(f"{i}: {artist}")

    # function to replace an artist
    replace_artist(top_artists)

    # show the  modified list of artist
    print("\nUpdated List of Top Performing Artists: ")
    for i, artist in enumerate(top_artists):
        print(f"{i}: {artist}")


main()
