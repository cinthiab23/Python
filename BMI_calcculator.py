# Convert weight from pounds to kilograms
pound_to_kilograms = 0.453592
# Convert height from inches to meters
inches_to_meter = 0.0254


# Function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m * height_m)
    return bmi


# Function to categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# Main function
def main():
    while True:
        # Input: weight in pounds and height in inches
        weight_lbs = input("Enter your weight in pounds: ")
        height_inch = input("Enter your height in inches: ")

        if weight_lbs.isdigit() and height_inch.isdigit():
            weight_lbs = float(weight_lbs)
            height_inch = float(height_inch)
            break
        else:
            print("Please enter a valid number for both weight and height.")

    # Convert weight to kilograms and height to meters
    weight_kg = weight_lbs * pound_to_kilograms
    height_m = height_inch * inches_to_meter

    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)

    # Output  with two decimal places
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {bmi_category(bmi)}")


main()
