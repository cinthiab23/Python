# User names # used w3schools example didn't understand
# using bubble_sort function
# # Dont understand this part you didn't have it in the notes but w3schools has it.
def bubble_sort(names_list):
    n = len(names_list)
    for i in range(n):
        for j in range(
            0, n - i - 1
        ):  # I dont understand this, where did the "j" come from
            if names_list[j] > names_list[j + 1]:
                names_list[j], names_list[j + 1] = names_list[j + 1], names_list[j]


names = []
for i in range(5):
    name = input(f"Enter 5 names {i+1}:")
    names.append(name)

# bubble sort function
bubble_sort(names)

print("\nSorted list of names:")
print(names)

names.reverse()

print("\nReversed sorted list of names:")
print(names)

# it didn't run I have no ideas what the problem is
