# User enters 2 integers
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# Example the use of 'and' operator: if both numbers greater than 0
print(f" Both numbers greater than 0: {num1 > 0 and num2 > 0}")

# Logical example 'and: Both number greater than 100
print(f" Both number greater than 100: {num1 > 100 and num2 >100}")

# Example the use of 'not': num1 is not equal to num2
print(f"num1 is not equal to num2: {num1 != num2}")

# Logical example 'not: num1 is not 0
print(f" num1 is not 0: {num1 != 0}")

# Logical 'or': Either number is less than 100
print(f"Either number is less than 100? {num1 < 100 or num2 < 100 }")
