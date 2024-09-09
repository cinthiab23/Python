#  Grade from the user

def get_valid_grade():
    while True:
        try:
            #accep input and convert it to an integer
            grade = int(input("Enter your numeric grade (0-100): "))

            # Check if grade is range 
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100. ")

# valid grade

numeric_grade = get_valid_grade()

#Letter grade using if, elif  and else
if numeric_grade >= 90:
    letter_grade = 'A'
elif numeric_grade >= 80:
    letter_grade = 'B'
elif numeric_grade >= 70:
    letter_grade = 'C'
elif numeric_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Letter grade
print(f"Your letter grade is: {letter_grade}")