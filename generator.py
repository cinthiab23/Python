# Generator function to create two-letter combinations
def two_letter_combinations(characters):
    """
    Generator function takes a list of characters as input and yields all possible two-letter combinations from the list.
    """
    # Iterate over the list using nested loop to create combinations
    for char1 in characters:
        for char2 in characters:
            # Yield each two-letter combination
            yield char1 + char2

# Main function


def main():
    """
    Main function to call the generator function and print all combinations.
    """
    # Original 5-letter list of characters
    characters = ['a', 'b', 'c', 'e', 'g']
    print("Two-letter combinations from the given list: ")
    # Call the generator functions and iterate over it
    for combination in two_letter_combinations(characters):
        print(combination)


main()
