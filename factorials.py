# function for factorial
def factorial(n):
    # Base case when n is 1 or 0 return is 1
    if n == 0 or n == 1:
        return 1
    # recursive step
    else:
        return n * factorial(n - 1)


# main function
def main():
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        # call the factorial function and print the result
        result = factorial(n)
        print(f"The factorial of {n} is {result}.")


# main function
main()
