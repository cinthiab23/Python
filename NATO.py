# Step 3: main function
def main():
    spell_word()


# Step 1: create the NATO Phonetic alphabet Dictionary
nato_alphabet = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliette",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-Ray",
    "Y": "Yankee",
    "Z": "Zulu",
}


# Step 2: develop the spelling program
def spell_word():
    user_word = input("Enter a word to spell in NATO phonetic alphabet: ")

    for letter in user_word:
        uppercase_letter = letter.upper()
        if uppercase_letter in nato_alphabet:
            print(nato_alphabet[uppercase_letter])
        else:
            print(f"'{letter}' is not a valid letter")


main()
