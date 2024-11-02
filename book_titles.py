def main():
    # empty list for book titles
    book_titles = []

    # Use a while loop to collect 10 book_titles
    count = 0
    while count < 10:
        title = input("Enter a book title:  ")
        book_titles.append(title.title())
        count += 1

    # Create a sorted list of book titles
    sorted_titles = sorted(book_titles)

    print("Here are the book titles in alphabetical order: ")
    for title in sorted_titles:
        print(title)


main()
