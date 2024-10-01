def main():
    # tuple programing
    programing_classes = (
        "Intro to Python",
        "Advanced Python",
        "Database Essentials",
        "Web Development Basics",
        "Data Structures in Python",
        "Web Design Fundamentals",
    )

    # loop to print each class
    print("Programing Classes:")
    for course in programing_classes:
        print(course)
    # Use the len function to print how many classes are in the tuple
    total_classes = len(programing_classes)
    print(f"Total number of classes: {total_classes}")


main()
