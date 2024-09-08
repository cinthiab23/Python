# Budget Application Assignment

# User to enter their total budget
total_budget = float(input("Enter your total budget: $"))

# User to enter amounts for different spending categories
housing = float(input("Enter amount spent on Housing: $"))
utilities = float(input("Enter amount spent on Utilities: $"))
groceries = float(input("Enter amount spent on Groceries: $"))
transportation = float(input("Enter amount spent on Transportation: $"))
health_care = float(input("Enter amount spent on Health Care: $"))
personal_care = float(input("Enter amount spent on Personal Care: $"))
clothing = float(input("Enter amount spend on Clothing: $"))
debt = float(input("Enter amount spent on Debt: $"))


# Calculate the percentage of the total budget spent in each category
def calculate_percentage(amount, total):
    return (amount / total) * 100


# Calculate percentages
housing_percentage = calculate_percentage(housing, total_budget)
utilities_percentage = calculate_percentage(utilities, total_budget)
groceries_percentage = calculate_percentage(groceries, total_budget)
transportation_percentage = calculate_percentage(transportation, total_budget)
health_care_percentage = calculate_percentage(health_care, total_budget)
personal_care_percentage = calculate_percentage(personal_care, total_budget)
clothing_percentage = calculate_percentage(clothing, total_budget)
debt_percentage = calculate_percentage(debt, total_budget)


# Output the results
print("\nBudget Breakdown:")
print(f"Housing:  ${housing:.2f}  ({housing_percentage:.2f} %)")
print(f"Utilities:  ${utilities:.2f}  ({utilities_percentage:.2f} %)")
print(f"Groceries:  ${groceries:.2f}  ({groceries_percentage:.2f} %)")
print(f"Transportation:  ${transportation:.2f}  ({transportation_percentage:.2f} %)")
print(f"Health Care:  ${health_care:.2f}  ({health_care_percentage:.2f} %)")
print(f"Personal Care:  ${personal_care:.2f}  ({personal_care_percentage:.2f} %)")
print(f"Clothing:  ${clothing:.2f}  ({clothing_percentage:.2f} %)")
print(f"Debt:  ${debt:.2f}  ({debt_percentage:.2f} %)")
